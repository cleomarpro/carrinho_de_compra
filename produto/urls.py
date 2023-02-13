from .views import (
    ProdutoCreate, 
    ProdutoDetailChangeDelete, ProdutoFiltro
)
from django.urls import path

urlpatterns = [
    path('filtro/<str:filtro>/', ProdutoFiltro.as_view()),
    path('', ProdutoCreate.as_view()),
    path('<int:pk>/', ProdutoDetailChangeDelete.as_view()),
]