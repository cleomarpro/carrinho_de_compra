
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
class ProdutoCreateViewsTestCase(TestCase):
    def setUp(self):
        # criando usuário
        User.objects.create_user(
            password= "4455456",
            username= "admin"
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

        # Novo usuario
        url = reverse('novo_usuario')
        data = {
            "email":"cleomar@emais.te",
            "username": "admin01",
            "password": "4455456"
        }
        response = self.client.post(url, data= data)
        print('Usuario criado: \n',response.json())
        self.assertEqual(response.status_code, 201)
        print(response) 
        print()
        print()
        
        #buscar o usuario logado
        url = '/usuario/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION = f'Bearer {token}')
        print('Usuario: \n',response.json())
        self.assertEqual(response.status_code, 200)
        usuario = response.json()[0]["id"]
        print("usuario id: ", usuario)
        print()

        # alterar dados do usuario
        url = reverse('usuario')
        data = {
            "id":1,
            "email":"cleomar@emais.te55",
            "username": "admin55",
            "password": "4455456"
        }
        response = self.client.put(
            url, data=data, HTTP_AUTHORIZATION = f'Bearer {token}', content_type='application/json')
        print('Usuario alterado: \n', response.json())
        self.assertEqual(response.status_code, 200)
        print(response) 
        print()
        print()
