from django.contrib import admin

from .models import(
    Carrinho, 
    ItemDoPedido, 
)

admin.site.register(Carrinho)
admin.site.register(ItemDoPedido)