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

3 - Criar uma virtualenv na mesma pasta do projeto

3.1 - Linux:  python3 -m  venv  nome da venv


3,2 - Windous: python -m venv myvenv 

4 - Ativar a virtualenv (Linux: source NomeDaVenv/bin/activate.)

5 - Atualizar o pip (python -m pip install --upgrade pip)

6 - Instalar os requirements.txt(pip install -r requirements.txt)

7 - Fazer as migrações {python manage.py migrate}

8 - Criar um super usuario(python manage.py createsuperuser)

9 - Ligar o servidor (python manage.py runserver)

9.1 Acesse no seu navegador http://127.0.0.1:8000/admin 

DEPLOY UTILIZANDO DOCKER

1 - Sertifique-se de ter o docke e o docker-compose estão instalodo na sua maquina
2 - Navegue até a pasta raiz do projeto onde está o arquivo docker-compose.py
3 - Pra criar o container do sistema e do banco de dados insere: docker-compose up

INSTRUÇÕES DE USO DA API

MESSAGEM DE ERROR:

Sucesso: Response: 200 ou 201

Objeto não encontrado GET: Response: 404

Não criado POST Response: 404

Não alterado: PUT Response: 404

Erro de servidor Response: 500

1 - Tipo de autenticação: JWT
1.1 - dominio/usuario/novo_usuario/: Criar novo usuário, metodo POST
Exemplo_de_data = {"email":"cleomar@emais.te", "username": "admin", "password": "44@58fdsfr"}

1.2 - dominio/usuario/ : Busacar usuário logado, metodo GET

1.3 - dominio/usuario/ : Alterar dados do usuário, metodo PUT

2 - Usando o CURL para testar os end-point:

2.1 - dominio/token/:  Gerar token de autenticação: 
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

3 - dominio/carrinho/pedido/true/ "Visualizar carrinhos de compra anterior, metodo GET"

4 - dominio/carrinho/pedido/false/ "Visualizar carrinho,  metodo GET"

5 - dominio/carrinho/item/ "Visualizar os itens do carrinho, e adicionar um novo item, 
metodo GET/POST"
Exemplo_de_data = { "produto": 1," quantidade_de_itens":1}

6 - dominio/carrinho/item-id/+id "Buscar um item para visualizar, excluir ou editar, metodo GET, PUT e DELETE"

7 - dominio/carrinho/+id "Realizar o checkou, metodo PUT"

8 - dominio/produto/ "Lista de produtos, metodo GET e Criar produto POST"
Exemplo_de_data = {"name": "free frier", "price": 100, "score": 100 }

9 - dominio/produto/+id" Buscar produto por id, motodo GET, DELETE e PUT"

10 - dominio/produto/filtro/score/ "Ordenar os produtos por popularidade, metodo GET"

11 - dominio/produto/filtro/price/ "Ordenar os produtos por preço, metodo GET"

12 - dominio/produto/filtro/name/ "Ordenar os produtos por ordem alfabetica, metodo GET"

13 - Metodos utilizados: post: criar um novo arquivo, put: editar, get: buscar: delete: excluir

14 - Para mais detalhes consulter a documentação PELO swagger

14.1 - Redoc: http://127.0.0.1:8000/api/redoc/

14.2 - swagger: http://127.0.0.1:8000/api/swagger/

