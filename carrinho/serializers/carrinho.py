from carrinho.models.carrinho import Carrinho
from rest_framework import serializers

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ['id', 'total', 'frete', 'subtotal', 'cliente', 'checkout']