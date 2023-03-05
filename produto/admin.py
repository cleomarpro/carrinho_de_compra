from django.contrib import admin

from produto.models.produto import(
    Produto,  
)

admin.site.register(Produto)