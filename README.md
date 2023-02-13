DESCRIÇÃO

pseudo e-commerce de games

REQUISITOS FUNCIONÁIS
- O usuário deverá fazer login
- O usuário poderá adicionar e remover produtos do carrinho.
- O usuário poderá ordenar os produtos por preço, popularidade (score) e ordem alfabética
- Os valores exibidos no checkout (frete, subtotal e total) são calculados dinamicamente conforme o usuário seleciona ou remove produtos.
- A cada produto adicionado, deve-se somar R$ 10,00 ao frete.
- Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.
- O usuário pode realizar checkout de seu carrinho de compras.
- O usuário pode consultar os pedidos feitos.



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

- dominio/carrinho/id/ "Visualizar o carrinho de id especificado"
- dominio/carrinho/item_do_pedido/id/ "visualizar item de carrinho especifico"
- dominio/carrinho/item/ "Visualizar todos os itens"
- dominio//carrinho/item-id/id/ "Excluir ou editar item"
- dominio/ "Lista de produtos" 
- dominio/carrinho/True/ "Realizar o checkou"
- dominio/filtro/score/ "Ordenar os produtos por popularidade"
- dominio/filtro/price/ "Ordenar os produtos por preço"
- dominio/filtro/name/ "Ordenar os produtos por odem alfabetica"
- dominio/1/ "Celecionar o produto para delettar ou editar"