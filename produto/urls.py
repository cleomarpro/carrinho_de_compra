from .views import (
    ProdutoCreate, 
    ProdutoDetailChangeDelete, ProdutoFiltro
)
from django.urls import path

urlpatterns = [
    path('produto/filtro/<str:filtro>/', ProdutoFiltro.as_view()),
    path('produto/', ProdutoCreate.as_view()),
    path('produto/<int:pk>/', ProdutoDetailChangeDelete.as_view()),
]