from django.urls import path
from . import views

# URLs do app products
urlpatterns = [
    # Página inicial: lista produtos
    path('', views.index, name='index'),
    # URL para vender um produto: /vender/<id>/
    path('vender/<int:produto_id>/', views.vender, name='vender'),
]