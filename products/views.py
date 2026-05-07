from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Produto

def index(request):
    q = request.GET.get('q', '').strip()
    produtos = Produto.objects.select_related('fornecedor')
    if q:
        produtos = produtos.filter(Q(nome__icontains=q) | Q(fornecedor__nome__icontains=q))
    alertas_estoque = Produto.objects.filter(quantidade__lt=5).select_related('fornecedor')
    return render(request, 'index.html', {
        'produtos': produtos,
        'alertas_estoque': alertas_estoque,
        'busca_q': q,
    })

def finalizar_venda(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method != 'POST':
        return redirect('index')
    quantidade = request.POST.get('quantidade', '0')
    try:
        quantidade = int(quantidade)
        produto.baixa_estoque(quantidade)
        messages.success(request, f'Venda concluída: {quantidade} unidades de {produto.nome}.')
    except ValueError as error:
        messages.error(request, str(error))
    except Exception:
        messages.error(request, 'Erro ao finalizar a venda.')
    return redirect('index')

def pedir_fornecedor(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    fornecedor = produto.fornecedor

    if not fornecedor or not fornecedor.email:
        return render(request, 'produto_sem_fornecedor.html', {'produto': produto})

    if request.method == 'POST':
        subject = request.POST.get('subject', f'Pedido de Reposição: {produto.nome}')
        message = request.POST.get('message', '').strip()
        if not message:
            message = (
                f'Olá {fornecedor.nome}, '
                f'Por favor, envie reposição do produto "{produto.nome}" o estoque atual em estoque: {produto.quantidade}. '
                'Atenciosamente,Equipe EasyMart'
            )

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'no-reply@easymart.local')
        recipient_list = [fornecedor.email]
        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            produto.ultimo_pedido = timezone.now()
            produto.save()
            return render(request, 'email_enviado.html', {'produto': produto, 'fornecedor': fornecedor})
        except Exception as error:
            return render(request, 'email_form.html', {
                'produto': produto,
                'fornecedor': fornecedor,
                'error': str(error),
                'subject': subject,
                'message': message,
            })

    return render(request, 'email_form.html', {'produto': produto, 'fornecedor': fornecedor})
