
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import json
from carrinho.models import Carrinho, ItemDoPedido
from produto.models import Produto
class ItemDoPedidoCreateViewsTestCase(TestCase):
    def setUp(self):
        # criando usuário
        usuario = User.objects.create_user(
            password= "4455456",
            username= "admin"
            )

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
            carrinho_id = 1
            )

        ItemDoPedido.objects.create(
            quantidade_de_itens = 2, 
            produto_id = 2,
            carrinho_id = 1
            )
    
    def test_carrinho_e_items_de_carrinho(self):
        #Obtendo token do usuário
        user_data = {
            "username": "admin",
            "password": "4455456"
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 200)
        response_deta = response.json()
        token = response_deta['access']
    
        print()
        print()

        # Visualizar o carrinho que não fez o checkout, checkout = False
        estado='false'
        url = '/carrinho/pedido/false/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Carrinho: \n',response.json())
        carrinhoid = response.json()
        carrinhoid = carrinhoid[0]['id']      
        self.assertEqual(response.status_code, 200)
        print()

        # Adicionar produtos no carrinho
        url = '/carrinho/item/'
        data = {
            "produto": 1,
            "quantidade_de_itens":1
        }
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Itens inserido no carrinho: \n',response.json())
        self.assertEqual(response.status_code, 201)
        itens = response.json()
        itemid = itens['id']
        print()
        print()

        # Visualizar o carrinho que não fez o checkout, checkout = False
        url = '/carrinho/pedido/false/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Carrinho atualizado: \n',response.json())     
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # Visualizar item do carrinho
        url = reverse('item')
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Item do carrinho: \n',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # Deletar um item
        url = f'/carrinho/item-id/{itemid}/'
        response = self.client.delete(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Item Deletado: \n',response)
        self.assertEqual(response.status_code, 200)
        print()
        print()
        
        #carrinho atualizado
        url = '/carrinho/pedido/false/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Carrinho atualizado: \n',response.json())   
        self.assertEqual(response.status_code, 200)
        print()
        print()

        #Fazer checkout em carrinho
        url = f'/carrinho/{carrinhoid}/'
        response = self.client.put(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Carrinho checkout: \n',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # Visualizar os pedidos anteriores
        url = '/carrinho/pedido/true/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Pedidos anteriores: \n',  response.json())
        self.assertEqual(response.status_code, 200)
       
