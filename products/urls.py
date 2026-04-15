from django.urls import path
from . import views

# URLs do app products
urlpatterns = [
    # Página inicial: lista produtos
    path('', views.index, name='index'),
    # URL para pedir ao fornecedor: /pedir/<id>/
    path('pedir-fornecedor/<int:produto_id>/', views.pedir_fornecedor, name='pedir_fornecedor'),
]