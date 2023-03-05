from django.db import models

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
