from django.shortcuts import render, get_object_or_404
from .models import Fornecedor

# View para listar todos os fornecedores
def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

# View para exibir detalhes de um fornecedor e seus produtos
def detalhes_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    produtos = fornecedor.produtos.all()
    return render(request, 'fornecedores/detalhes_fornecedor.html', {'fornecedor': fornecedor, 'produtos': produtos})
