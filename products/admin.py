from django.contrib import admin
from .models import Produto

# Registrando o modelo Produto no painel admin
admin.site.register(Produto)
