from .views import (
    NovoUsuario, 
    NovaSenha
)
from django.urls import path

urlpatterns = [
    path('novo_usuario', NovoUsuario.as_view(), name = 'novo_usuario'),
    path('', NovaSenha.as_view(), name= 'usuario')
]