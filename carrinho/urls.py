from carrinho.views.carrinho import (
    CarrinhoItem, 
    CarrinhoDetailChangeDeleteGet
)
from carrinho.views.item_do_pedido import (
    ItemDoPedidoCreate, 
    ItemDoPedidoDetailChangeDelete, 
)
from django.urls import path

urlpatterns = [
    path('item/', ItemDoPedidoCreate.as_view(), name = 'item'),
    path('item-id/<int:pk>/', ItemDoPedidoDetailChangeDelete.as_view(), name = 'item_id'),
    path('<int:pk>/', CarrinhoDetailChangeDeleteGet.as_view(), name = 'carrinho'),
    path('pedido/<str:all>/', CarrinhoItem.as_view(), name = 'pedidos_anteriores'),
]