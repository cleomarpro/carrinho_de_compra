from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=30, null=False)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0)
    score = models.IntegerField()
    image = models.ImageField( null =True, blank=True)

def __str__(self): 
        return str(self.name)+ ' - ' +str(self.price)