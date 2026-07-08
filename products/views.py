from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from .models import Produto, HistoricoPedido
from fornecedores.models import Fornecedor

def index(request):
    q = request.GET.get('q', '').strip()
    produtos = Produto.objects.select_related('fornecedor')
    if q:
        produtos = produtos.filter(Q(nome__icontains=q) | Q(fornecedor__nome__icontains=q))
    alertas_estoque = Produto.objects.filter(quantidade__lt=5).select_related('fornecedor')
    
    # Cálculo de resumos para dashboard
    total_produtos = Produto.objects.count()
    produtos_estoque_baixo = Produto.objects.filter(quantidade__lte=5).count()
    total_fornecedores = Fornecedor.objects.count()
    
    return render(request, 'index.html', {
        'produtos': produtos,
        'alertas_estoque': alertas_estoque,
        'busca_q': q,
        'total_produtos': total_produtos,
        'produtos_estoque_baixo': produtos_estoque_baixo,
        'total_fornecedores': total_fornecedores,
    })

def finalizar_venda(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method != 'POST':
        return redirect('products:index')
    quantidade = request.POST.get('quantidade', '0')
    try:
        quantidade = int(quantidade)
        produto.baixa_estoque(quantidade)
        messages.success(request, f'Venda concluída: {quantidade} unidades de {produto.nome}.')
    except ValueError as error:
        messages.error(request, str(error))
    except Exception:
        messages.error(request, 'Erro ao finalizar a venda.')
    return redirect('products:index')

def pedir_fornecedor(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    fornecedor = produto.fornecedor

    if not fornecedor or not fornecedor.email:
        return render(request, 'produto_sem_fornecedor.html', {'produto': produto})

    if request.method == 'POST':
        subject = request.POST.get('subject', f'Pedido de Reposição: {produto.nome}')
        message = request.POST.get('message', '').strip()
        quantidade = request.POST.get('quantidade', '1')
        
        if not message:
            message = (
                f'Olá {fornecedor.nome}, '
                f'Por favor, envie reposição do produto "{produto.nome}" o estoque atual em estoque: {produto.quantidade}. '
                'Atenciosamente,Equipe EasyMart'
            )

        try:
            quantidade = int(quantidade) if quantidade else 1
            if quantidade <= 0:
                quantidade = 1
        except ValueError:
            quantidade = 1

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'no-reply@easymart.local')
        recipient_list = [fornecedor.email]
        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            produto.ultimo_pedido = timezone.now()
            produto.save()
            
            # Salvar no histórico de pedidos
            HistoricoPedido.objects.create(
                produto=produto,
                fornecedor=fornecedor,
                quantidade=quantidade,
                status='enviado'
            )
            
            return render(request, 'email_enviado.html', {'produto': produto, 'fornecedor': fornecedor})
        except Exception as error:
            return render(request, 'email_form.html', {
                'produto': produto,
                'fornecedor': fornecedor,
                'error': str(error),
                'subject': subject,
                'message': message,
                'quantidade': quantidade,
            })

    return render(request, 'email_form.html', {'produto': produto, 'fornecedor': fornecedor})

def relatorio_estoque_baixo(request):
    """Gera PDF com produtos em estoque crítico (quantidade <= 5)"""
    produtos = Produto.objects.filter(quantidade__lte=5).select_related('fornecedor').order_by('quantidade')
    return gerar_pdf_estoque_critico(produtos)

def gerar_pdf_estoque_critico(produtos):
    """Gera PDF com formatação limpa para estoque crítico"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="estoque_critico.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    # Título
    title_style = styles['Title']
    title_style.textColor = '#ef4444'  # Vermelho
    elements.append(Paragraph('RELATÓRIO DE ESTOQUE CRÍTICO', title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Informações gerais
    info_text = f'<b>Data:</b> {timezone.now().strftime("%d/%m/%Y %H:%M")}<br/><b>Produtos em Crítico:</b> {len(produtos)}'
    elements.append(Paragraph(info_text, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Dados da tabela
    data = [[
        Paragraph('<b>Produto</b>', styles['Normal']),
        Paragraph('<b>Quantidade</b>', styles['Normal']),
        Paragraph('<b>Fornecedor</b>', styles['Normal'])
    ]]
    
    for produto in produtos:
        fornecedor_nome = produto.fornecedor.nome if produto.fornecedor else 'Sem Fornecedor'
        data.append([
            Paragraph(produto.nome, styles['Normal']),
            Paragraph(str(produto.quantidade), styles['Normal']),
            Paragraph(fornecedor_nome, styles['Normal'])
        ])
    
    # Criar tabela
    table = Table(data, colWidths=[3*inch, 1.5*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#ef4444'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#ffffff'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), '#ffffff'),
        ('GRID', (0, 0), (-1, -1), 1, '#cccccc'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), ['#ffffff', '#f9fafb']),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    
    elements.append(table)
    doc.build(elements)
    return response

def gerar_pdf_estoque_baixo(request):
    threshold = request.GET.get('threshold', '5')
    try:
        threshold = int(threshold)
    except ValueError:
        threshold = 5
    produtos = Produto.objects.filter(quantidade__lt=threshold).select_related('fornecedor')
    return gerar_pdf_produtos(produtos, f'Produtos com Estoque Baixo (menos de {threshold})')

def gerar_pdf_todos_produtos(request):
    produtos = Produto.objects.all().select_related('fornecedor')
    return gerar_pdf_produtos(produtos, 'Lista Completa de Produtos')

def gerar_pdf_produtos(produtos, titulo):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{titulo}.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Título
    elements.append(Paragraph(titulo, styles['Title']))
    elements.append(Paragraph('', styles['Normal']))  # Espaço
    
    # Dados da tabela
    data = [['Nome', 'Preço', 'Quantidade', 'Fornecedor']]
    for produto in produtos:
        fornecedor_nome = produto.fornecedor.nome if produto.fornecedor else 'N/A'
        data.append([
            produto.nome,
            f'R$ {produto.preco:.2f}',
            str(produto.quantidade),
            fornecedor_nome
        ])
    
    # Criar tabela
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#f0f0f0'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), '#ffffff'),
        ('GRID', (0, 0), (-1, -1), 1, '#000000'),
    ]))
    
    elements.append(table)
    doc.build(elements)
    return response
