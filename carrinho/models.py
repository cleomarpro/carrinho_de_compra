from django.db import models
from produto.models import Produto
from django.db.models import Sum, F, FloatField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Carrinho(models.Model):
    frete = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    subtotal = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    total = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    cliente = models.CharField(
        max_length=100, blank=True, null=True)

    def carrinho_total(self):
        self.items = self.itemdopedido_set.all()
        total = self.items.aggregate(
            total = Sum((F(
                'quantidade_de_itens') * F(
                    'produto__price')), output_field=FloatField()))
        self.total = total['total'] or 0
        Carrinho.objects.filter(
            id=self.id).update(total = self.total)

    def carrinho_frete(self):
        if self.total < 250:
            valor_do_frete = 10
            itens = self.items.aggregate(
                items= Sum('quantidade_de_itens'))
            itens = itens['items'] or 0
            self.frete = valor_do_frete * itens
        else:
            self.frete = 0
        Carrinho.objects.filter(
            id=self.id).update(frete = self.frete)

    def carrinho_subtotal(self):
        subtotal = self.frete + self.total
        Carrinho.objects.filter(
            id=self.id).update(subtotal = subtotal)
    def __str__(self):
        return str(self.id) 

class ItemDoPedido(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE)
    quantidade_de_itens = models.IntegerField()

    def __str__(self):
        return  str(self.produto.name)

@receiver(post_save, sender=ItemDoPedido)
def update_carrinho_total(sender, instance, **kwargs):
    instance.carrinho.carrinho_total()

@receiver(post_save, sender=ItemDoPedido)
def update_carrinho_frete(sender, instance, **kwargs):
    instance.carrinho.carrinho_frete()

@receiver(post_save, sender=ItemDoPedido)
def update_carrinho_subtotal(sender, instance, **kwargs):
    instance.carrinho.carrinho_subtotal()
