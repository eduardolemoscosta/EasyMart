from django.contrib import admin
from .models import Fornecedor

# Registrar modelo Fornecedor no admin
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')
    list_filter = ('data_cadastro',)
    readonly_fields = ('data_cadastro',)
