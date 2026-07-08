from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('vender/<int:produto_id>/', views.finalizar_venda, name='finalizar_venda'),
    path('pedir-fornecedor/<int:produto_id>/', views.pedir_fornecedor, name='pedir_fornecedor'),
    path('relatorio-pdf/', views.relatorio_estoque_baixo, name='relatorio_estoque_baixo'),
    path('pdf/estoque-baixo/', views.gerar_pdf_estoque_baixo, name='pdf_estoque_baixo'),
    path('pdf/todos/', views.gerar_pdf_todos_produtos, name='pdf_todos_produtos'),
]
            