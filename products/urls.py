from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vender/<int:produto_id>/', views.finalizar_venda, name='finalizar_venda'),
    path('pedir-fornecedor/<int:produto_id>/', views.pedir_fornecedor, name='pedir_fornecedor'),
]
            