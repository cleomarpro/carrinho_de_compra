from .views import ItemDoPedidoCreate, ItemDoPedidoDetailChangeDelete, CarrinhoCompras, CarrinhoDetailChangeDelete
from django.urls import path

urlpatterns = [
    path('itens/', ItemDoPedidoCreate.as_view()),
    path('itens/<int:pk>/', ItemDoPedidoDetailChangeDelete.as_view()),
    path('<int:pk>/', CarrinhoDetailChangeDelete.as_view()),
    path('', CarrinhoCompras.as_view())
]