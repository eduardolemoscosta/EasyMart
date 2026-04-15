from django.db import models

# Modelo para representar um fornecedor
class Fornecedor(models.Model):
    # Nome do fornecedor
    nome = models.CharField(max_length=150)
    
    # Email de contato
    email = models.EmailField(blank=True, null=True)
    
    # Telefone de contato
    telefone = models.CharField(max_length=15, blank=True, null=True)
    
    # Endereço
    endereco = models.CharField(max_length=250, blank=True, null=True)
    
    # Data de cadastro
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
