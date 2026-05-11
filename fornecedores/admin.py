from django.contrib import admin
from .models import Fornecedor

# Registrar modelo Fornecedor no admin
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')
    list_filter = ('data_cadastro',)
    readonly_fields = ('data_cadastro',)
    
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('nome', 'email', 'telefone')
        }),
        ('Endereço', {
            'fields': ('rua', 'numero', 'bairro', 'cidade'),
            'classes': ('collapse',),  # Makes it collapsible like a tab
        }),
        ('Datas', {
            'fields': ('data_cadastro',),
            'classes': ('collapse',),
        }),
    )
