from .views import ProdutoCreate, ProdutoDetailChangeDelete
from django.urls import path

urlpatterns = [
    path('', ProdutoCreate.as_view()),
    path('<int:pk>/', ProdutoDetailChangeDelete.as_view()),
]