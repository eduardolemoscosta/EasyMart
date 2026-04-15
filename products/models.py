from django.db import models
from django.utils import timezone
from fornecedores.models import Fornecedor

# Modelo para representar um produto no supermercado
class Produto(models.Model):
    # Nome do produto, campo de texto obrigatório
    nome = models.CharField(max_length=100)
    
    # Preço do produto, campo decimal com 2 casas decimais
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Quantidade em estoque, campo inteiro
    quantidade = models.IntegerField(default=0)
    
    # Fornecedor do produto
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    
    # Data do último pedido ao fornecedor
    ultimo_pedido = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        # Método para representar o produto como string (usado no admin)
        return self.nome
