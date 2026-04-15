from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Produto

# View para listar todos os produtos na página inicial
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

# View para exibir formulário de pedido ao fornecedor e enviar e-mail
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
                f'Olá {fornecedor.nome},\n\n'
                f'Por favor, envie reposição do produto "{produto.nome}".\n'
                f'Quantidade atual em estoque: {produto.quantidade}.\n\n'
                'Atenciosamente,\nEquipe EasyMart'
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
