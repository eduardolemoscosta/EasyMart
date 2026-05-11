from django.db import models

# Modelo para representar um fornecedor
class Fornecedor(models.Model):
    # Nome do fornecedor
    nome = models.CharField(max_length=150)
    
    # Email de contato
    email = models.EmailField(blank=True, null=True)
    
    # Telefone de contato
    telefone = models.CharField(max_length=15, blank=True, null=True)
    
    # Endereço detalhado
    rua = models.CharField(max_length=200, blank=True, null=True, verbose_name="Rua")
    numero = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número")
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    
    # Data de cadastro
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
