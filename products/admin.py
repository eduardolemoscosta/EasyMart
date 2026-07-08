from django.contrib import admin
from .models import Produto, HistoricoPedido

class HistoricoPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'fornecedor', 'quantidade', 'data_pedido', 'status')
    list_filter = ('status', 'data_pedido', 'fornecedor', 'produto')
    search_fields = ('produto__nome', 'fornecedor__nome')
    readonly_fields = ('data_pedido',)
    ordering = ('-data_pedido',)
    
    fieldsets = (
        ('Informações do Pedido', {
            'fields': ('produto', 'fornecedor', 'quantidade', 'data_pedido')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
    )

# Registrando os modelos no painel admin
admin.site.register(Produto)
admin.site.register(HistoricoPedido, HistoricoPedidoAdmin)
