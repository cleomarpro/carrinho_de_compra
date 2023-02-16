DESCRIÇÃO
Pseudo e-commerce de games

REQUISITOS FUNCIONÁIS
1 - O usuário deverá fazer login
2 - O usuário poderá adicionar e remover produtos do carrinho.
3 - O usuário poderá ordenar os produtos por preço, popularidade (score) e ordem alfabética
4 - Os valores exibidos no checkout (frete, subtotal e total) são calculados dinamicamente conforme o usuário seleciona ou remove produtos.
5 - A cada produto adicionado, deve-se somar R$ 10,00 ao frete.
6 - Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.
7 - O usuário pode realizar checkout de seu carrinho de compras.
8 - O usuário pode consultar os pedidos feitos.



INSTRUÇÕES PARA O DEPLOY
1 - Baixar o repositório do GitHaub (git remote add origin URLdeOrigem)
2 - Entrar em uma branch (git checkout nome_da_branch)
3 - Criar uma virtualenv (Linux:  python3 -m  venv  nome da venv.   Windous: python -m venv myvenv (criar virtula enve na mesma pasta do projeto)
4 - Ativar a virtualenv (Linux: source NomeDaVenv/bin/activate.)
5 - Atualizar o pip (python -m pip install --upgrade pip)
6 - Instalar os requirements.txt(pip install -r requirements.txt)
7 - Fazer as migrações {python manage.py migrate}
8 - Criar um super usuario(python manage.py createsuperuser)
9 - Ligar o servidor (python manage.py runserver)
9.1 Acesse no seu navegador http://127.0.0.1:8000/admin 

INSTRUÇÕES Da USO DA API
1 - Tipo de autenticação: JWT
2 - Usando o CURL para testar os end-point:
2.1 - Gerat togin de autenticação:
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}' \
  http://localhost:8000/token/

2.2 - Fazer um GET em todos os produtos:
    curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/carrinho/

2.3 E segue esse padrão 2.2 para todas as outras solicitações utilizado as URLS a baixa

3 - dominio/carrinho/+id "Visualizar o carrinho de id especificado"
4 - dominio/carrinho/item_do_pedido/id/ "visualizar item de carrinho especifico"
5 - dominio/carrinho/item/ "Visualizar todos os itens"
6 - dominio/carrinho/item-id/+id "Excluir ou editar item"
7 - dominio/ "Lista de produtos" 
8 - dominio/+id"Celecionar o produto para delettar ou editar"
9 - dominio/carrinho/True/ "Realizar o checkou"
10 - dominio/filtro/score/ "Ordenar os produtos por popularidade"
11 - dominio/filtro/price/ "Ordenar os produtos por preço"
12 - dominio/filtro/name/ "Ordenar os produtos por ordem alfabetica"
13 - Metodos utilizados: post: criar um novo arquivo, put: editar, get: buscar: delete: excluir