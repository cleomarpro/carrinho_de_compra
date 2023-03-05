from django.test import TestCase
from carrinho.models.carrinho import(Carrinho)
from carrinho.models.item_do_pedido import(ItemDoPedido)
from produto.models.produto import Produto

class CarrinhoModelTestCase(TestCase):
    def setUp(self):
        # criando produtos
        Produto.objects.create(
            name = "Super Mario Odyssey", 
            price =100,
            score = 100,
            image = "super-mario-odyssey.png"
        )
        Produto.objects.create(
            name = "Call Of Duty Infinite Warfare",
            price =60,
            score = 80,
            image = "call-of-duty-infinite-warfare.png"
        )
        
        # criando carrinho
        Carrinho.objects.create(checkout='false', cliente = 1)
        Carrinho.objects.create(checkout='false', cliente = 2)

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
    def test_calcular_carrinho_frete(self):
        print()
        print('carrinho: \n')
        carrinho = Carrinho.objects.get(id=1)
        print('frete: ', carrinho.frete)
        assert carrinho.frete == 0

    def test_calcular_carrinho_total(self):
        carrinho = Carrinho.objects.get(id=1)
        print('Total: ', carrinho.total)
        assert float(carrinho.total) == 260
    
    def test_calcular_carrinho_subtotal(self):
        carrinho = Carrinho.objects.get(id=1)
        print('Subtotal: ', carrinho.subtotal)
        assert float(carrinho.subtotal) == 260

    

    def test_deletar_itens_do_carrinho(self):
        # deletando um item do carrinho
        itens = ItemDoPedido.objects.get(id = 1)
        itens.delete()

        carrinho = Carrinho.objects.get(id=1)

        # carrinho atualizado
        print()
        print("carrinho atualizado depois de deletar um item: \n")
        print('Carrinho cliente:', carrinho.cliente)
        print('frete:', carrinho.frete)
        print('Total: ', carrinho.total)
        print('Subtotal: ', carrinho.subtotal)
        print(ItemDoPedido.objects.filter(carrinho_id=1))
        assert carrinho.frete == 10
        assert float(carrinho.total) == 60
        assert float(carrinho.subtotal) == 70