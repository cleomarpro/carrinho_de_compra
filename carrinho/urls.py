from .views import (
    ItemDoPedidoCreate, 
    CarrinhoItem, ItemDoPedidoDetailChangeDelete, 
    CarrinhoCompras
)
from django.urls import path

urlpatterns = [
    path('item/', ItemDoPedidoCreate.as_view()),
    path('item-id/<int:pk>/', ItemDoPedidoDetailChangeDelete.as_view()),
    path('<checkout>/', CarrinhoCompras.as_view()),
    path('item_do_pedido/<int:pk>/', CarrinhoItem.as_view())
]