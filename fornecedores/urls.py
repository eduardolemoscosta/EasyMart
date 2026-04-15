from django.urls import path
from . import views

# URLs do app fornecedores
urlpatterns = [
    # Página de lista de fornecedores
    path('', views.lista_fornecedores, name='lista_fornecedores'),
    # Página de detalhes do fornecedor
    path('<int:fornecedor_id>/', views.detalhes_fornecedor, name='detalhes_fornecedor'),
]
