from carrinho.models import  ItemDoPedido, Carrinho
from rest_framework import serializers


class ItemDoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDoPedido
        fields = ['id', 'produto', 'quantidade_de_itens']

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ['id', 'total', 'frete', 'subtotal', 'cliente', 'checkout']