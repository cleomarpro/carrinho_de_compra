from django.test import TestCase
from carrinho.models import Carrinho, ItemDoPedido
from produto.models import Produto
from django.db.models import Sum, F, FloatField

class CarrinhoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(
            name = "Super Mario Odyssey", 
            price = 197.88,
            score = 100,
            image = "super-mario-odyssey.png"
        )
        Produto.objects.create(
            name = "Call Of Duty Infinite Warfare",
            price = 49.99,
            score = 80,
            image = "call-of-duty-infinite-warfare.png"
        )

        Carrinho.objects.create()

        ItemDoPedido.objects.create(
            quantidade_de_itens = 2, 
            produto_id = 1,
            carrinho_id = 1
            )

        ItemDoPedido.objects.create(
            quantidade_de_itens = 1, 
            produto_id = 2,
            carrinho_id = 1
            )
    
    def test_calcular_carrinho_total(self):
        carrinho = Carrinho.objects.get(id=1)
        print(carrinho.total)
        assert float(carrinho.total) == 445.75
    
    def test_calcular_carrinho_subtotal(self):
        carrinho = Carrinho.objects.get(id=1)
        print(carrinho.subtotal)
        assert float(carrinho.subtotal) == 445.75

    def test_calcular_carrinho_frete(self):
        carrinho = Carrinho.objects.get(id=1)
        print(carrinho.frete)
        assert carrinho.frete == 0
"""
    def test_deletar_itens_do_carrinho(self):
        itens = ItemDoPedido.objects.get(id=1)
        itens.delete()
      
        carrinho = Carrinho.objects.get(id=1)
        
        print(carrinho.frete)
        print(carrinho.total)
        print(carrinho.subtotal)
        assert carrinho.frete == 30
"""