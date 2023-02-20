from django.test import TestCase
from carrinho.models import Carrinho, ItemDoPedido
from produto.models import Produto
from django.db.models import Sum, F, FloatField

class CarrinhoModelTestCase(TestCase):
    def setUp(self):
        # criando produtos
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
        
        # criando carrinho
        Carrinho.objects.create()
        Carrinho.objects.create()

        # inserindo itens no carrinho de 1
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
     # inserindo itens no carrinho de 2
        ItemDoPedido.objects.create(
            quantidade_de_itens = 2, 
            produto_id = 2,
            carrinho_id = 2
            )

        ItemDoPedido.objects.create(
            quantidade_de_itens = 2, 
            produto_id = 2,
            carrinho_id = 2
            )
    
    def test_calcular_carrinho_total(self):
        carrinho = Carrinho.objects.get(id=1)
        print('Total: ', carrinho.total)
        assert float(carrinho.total) == 445.75
    
    def test_calcular_carrinho_subtotal(self):
        carrinho = Carrinho.objects.get(id=1)
        print('Subtotal: ', carrinho.subtotal)
        assert float(carrinho.subtotal) == 445.75

    def test_calcular_carrinho_frete(self):
        carrinho = Carrinho.objects.get(id=1)
        print('frete: ', carrinho.frete)
        assert carrinho.frete == 0

    def test_deletar_itens_do_carrinho(self):
        # deletando um item do carrinho
        itens = ItemDoPedido.objects.get(id=1)
        itens.delete()

        # atualizado o carrinho
        itens = ItemDoPedido.objects.filter(carrinho_id=1)
        carrinho = Carrinho.objects.get(id=1)
        total = itens.aggregate(
            total = Sum((F(
                'quantidade_de_itens') * F(
                'produto__price')), output_field=FloatField()))
        total = total['total'] or 0
        if total < 250:
            valor_do_frete = 10
            itens = itens.aggregate(
                total_item= Sum('quantidade_de_itens'))
            itens = itens['total_item'] or 0
            frete = valor_do_frete * itens
        else:
            frete = 0 
        carrinho.total = total
        carrinho.frete =frete
        carrinho.subtotal = frete + total
        carrinho.save()

        # carrinho atualizado
        print("Depois de um item deletado")
        print('frete:', carrinho.frete)
        print('Total: ', carrinho.total)
        print('Subtotal: ', carrinho.subtotal)
        assert carrinho.frete == 10
        assert float(carrinho.total) == 49.99
        assert float(carrinho.subtotal) == 59.99