from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto

# View para listar todos os produtos na página inicial
def index(request):
    # Busca todos os produtos do banco de dados
    produtos = Produto.objects.all()
    # Renderiza o template 'index.html' passando os produtos
    return render(request, 'index.html', {'produtos': produtos})

# View para vender uma unidade de um produto
def vender(request, produto_id):
    # Busca o produto pelo ID, ou retorna 404 se não encontrar
    produto = get_object_or_404(Produto, id=produto_id)
    # Verifica se há estoque suficiente
    if produto.quantidade > 0:
        # Diminui a quantidade em 1
        produto.quantidade -= 1
        # Salva a alteração no banco
        produto.save()
    # Redireciona de volta para a página inicial
    return redirect('index')
