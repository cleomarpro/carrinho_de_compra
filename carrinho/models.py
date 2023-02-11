from django.db import models
from produto.models import Produto

class Carrinho(models.Model):
    frete = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    subtotal = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    total = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    cliente = models.CharField(
        max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.id) + ' - ' + str(self.valor)



class ItemDoPedido(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE)
    quantidade_de_itens = models.IntegerField()

    def __str__(self):
        return str(self.carrinho.id) + ' - ' + str(self.produto.name)
