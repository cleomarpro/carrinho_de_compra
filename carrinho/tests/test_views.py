from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import requests
import json
class ItemDoPedidoCreateViewsTestCase(TestCase):
    def setUp(self):
        # criando usuário
        usuario = User.objects.create_user(
            password= "4455456",
            username= "admin"
            )
    
    def test_carrinho_e_items_de_carrinho(self):
        #Obtendo token do usuário
        user_data = {
            "username": "admin",
            "password": "4455456"
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, user_data)
        #print('código: ',response.json())
       # print(response.status_code)
        self.assertEqual(response.status_code, 200)

        # montando cabeçalho da requisição 
        response_deta = response.json()
        token = response_deta['access']
        headers = {"Authorization": f"Bearer {token}"}
        self.assertEqual(response.status_code, 200)

        # Adicionar produtos no carrinho
        url = 'http://127.0.0.1:8000/carrinho/item/'
        data = {
            "produto": 1,
            "quantidade_de_itens":1
        }
        response = requests.post(url = url, data=data, headers= headers)
        print('Inserir itens no pedido: ',response.json())
        self.assertEqual(response.status_code, 201)
        print()
        print()

        # Visualizar o carrinho que não fez o checkout, checkout = False
        url = 'http://127.0.0.1:8000/carrinho/pedido/false/'
        response = requests.get(url = url, headers= headers)
        print('Carrinho: ',response.json())
        carrinho_id = response.json()
        carrinho_id = carrinho_id[0]['id']      
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # Visualizar item do carrinho
        url = 'http://127.0.0.1:8000/carrinho/item/'
        response = requests.get(url = url, headers= headers)
        print('Item do carrinho: ',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # Deletar um item
        url = 'http://127.0.0.1:8000/carrinho/item-id/119/'
        response = requests.delete(url = url, headers= headers)
        print('Item Deletado: ',response)
        self.assertEqual(response.status_code, 200)
        print()
        print()

        #Fazer checkout em carrinho
        url = 'http://127.0.0.1:8000/carrinho/100/'
        data = { 
            'checkout': 'true'
            }
        response = requests.put(
            url = url, data = data, headers= headers)
        print('Carrinho_put: ',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # Visualizar o pedidos anteriores
        url = 'http://127.0.0.1:8000/carrinho/pedido/true/'
        response = requests.get(url = url, headers= headers)
        print('Pedidos anteriores: ',response.json())
        self.assertEqual(response.status_code, 200)