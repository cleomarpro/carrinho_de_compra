from produto.models.produto import  Produto
from rest_framework import serializers


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'name', 'price', 'score', 'image']