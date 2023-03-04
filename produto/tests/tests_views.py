
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import json
from produto.models import Produto
class ProdutoCreateViewsTestCase(TestCase):
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
            score = 30,
            image = "super-mario-odyssey.png"
        )
        Produto.objects.create(
            name = "Call Of Duty Infinite Warfare",
            price =60,
            score = 80,
            image = "call-of-duty-infinite-warfare.png"
        )
        
        Produto.objects.create(
            name = "free fier",
            price =80,
            score = 90,
            image = "call-of-duty-infinite-warfare.png"
        )
        
    def test_produto_put_delete_update_filtros(self):
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

         # Criar produtos
        url = '/produto/'
        data = {
            "name": "free frier", 
            "price": 100,
            "score": 100
        }
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Produto criado: \n',response.json())
        self.assertEqual(response.status_code, 201)
        print(response) 
        produto = response.json()
        produto = produto['id']
        print()
        print()

        print()
        print()

         # Editar produto
        url = f'/produto/{produto}/'
        data = {
            "name": "free frier",
            "price": "197",
            "score": 200
        }
        response = self.client.put(
            url, data=data, HTTP_AUTHORIZATION = f'Bearer {token}', content_type='application/json')
        print('Produto alterado: \n', response.json())
        self.assertEqual(response.status_code, 200)
        print(response) 
        produto = response.json()
        produto = produto['id']
        print()
        print()
    
      
        # Visualizar produto
        url = reverse('produto')
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Produtos: \n',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()

        #deletar produto
        url = f'/produto/{produto}/'
        response = self.client.delete(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Produto Deletado: \n',response)
        self.assertEqual(response.status_code, 200)
        print()
        print()
        
        # filtro por ordem score
        url = f'/produto/filtro/score/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Filtro por ordem score: \n',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()

        # filtro por ordem alfabetica
        url = f'/produto/filtro/name/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Filtro por ordem alfabetica: \n',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()


        # filtro por ordem preço
        url = f'/produto/filtro/price/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Filtro por ordem preço: \n',response.json())
        self.assertEqual(response.status_code, 200)
        print()
        print()