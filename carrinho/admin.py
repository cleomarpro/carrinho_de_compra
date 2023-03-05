from django.contrib import admin
from carrinho.models.carrinho import(Carrinho)
from carrinho.models.item_do_pedido import(ItemDoPedido)

admin.site.register(Carrinho)
admin.site.register(ItemDoPedido)