from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from fornecedores.models import Fornecedor

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantidade = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    ultimo_pedido = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.preco < 0:
            raise ValidationError({'preco': 'Preço não pode ser negativo.'})
        if self.quantidade < 0:
            raise ValidationError({'quantidade': 'Quantidade não pode ser negativa.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def baixa_estoque(self, quantidade_vendida):
        if quantidade_vendida <= 0:
            raise ValueError('Quantidade de venda deve ser maior que zero.')
        if self.quantidade < quantidade_vendida:
            raise ValueError('Estoque insuficiente para finalizar a venda.')
        self.quantidade -= quantidade_vendida
        self.save(update_fields=['quantidade'])
        return self.quantidade

    def __str__(self):
        return self.nome


class HistoricoPedido(models.Model):
    STATUS_CHOICES = [
        ('enviado', 'Enviado'),
        ('confirmado', 'Confirmado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    # Relacionamentos
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='historico_pedidos')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='historico_pedidos')
    
    # Dados do pedido
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enviado')
    
    # Observações opcionais
    observacoes = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Histórico de Pedido'
        verbose_name_plural = 'Históricos de Pedidos'
        ordering = ['-data_pedido']
    
    def __str__(self):
        return f"Pedido {self.id} - {self.produto.nome} - {self.data_pedido.strftime('%d/%m/%Y %H:%M')}"
