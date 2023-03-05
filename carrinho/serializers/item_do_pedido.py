from carrinho.models.item_do_pedido import(ItemDoPedido)
from rest_framework import serializers


class ItemDoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDoPedido
        fields = ['id', 'produto', 'quantidade_de_itens']
