from django.db import models
from produto.models import Produto
from django.db.models import Sum,Count, F, FloatField
from django.db.models.signals import post_save, post_delete
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
    checkout = models.CharField(max_length=10, null=True, blank=True)
   
    def __str__(self):
        return str(self.id) 

class ItemDoPedido(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE)
    quantidade_de_itens = models.IntegerField()
    
    def carrinho_total(self):
        self.items = ItemDoPedido.objects.filter(
            carrinho_id = self.carrinho.id)
        total = self.items.aggregate(
            total = Sum((F(
                'quantidade_de_itens') * F(
                    'produto__price')), output_field=FloatField()))
        self.total = total['total'] or 0
        Carrinho.objects.filter(
            id=self.carrinho.id).update(total = self.total)

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
            id=self.carrinho.id).update(frete = self.frete)

    def carrinho_subtotal(self):
        subtotal = self.frete + self.total
        Carrinho.objects.filter(
            id=self.carrinho.id).update(subtotal = subtotal)

    def __str__(self):
        return  str(self.produto.name)

@receiver(post_delete, sender=ItemDoPedido)
def update_carrinho_total(sender, instance, **kwargs):
    instance.carrinho_total()
    instance.carrinho_frete()
    instance.carrinho_subtotal()

@receiver(post_save, sender=ItemDoPedido)
def update_carrinho_total(sender, instance, **kwargs):
    instance.carrinho_total()
    instance.carrinho_frete()
    instance.carrinho_subtotal()

