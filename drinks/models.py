from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    class DrinkCategory(models.TextChoices):
        SOFT_DRINKS = 1, _('Soft Drinks')
        BEERS = 2, _('Beers')
        DESTILATE = 3, _('Destilate')
        WINES = 4, _('Wines')
        
    category = models.CharField(max_length = 40, choices = DrinkCategory.choices)
    
    def __str__(self):
        return self.category 

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantidade_liquido_bebida = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class CalculoLitros(models.Model):
    unidades = models.IntegerField()
    quantidade_liquido = models.FloatField
    total_litros = models.FloatField()
    
    def calculando_litros(self):
        self.total_litros = self.unidades * self.quantidade_liquido
        return self.total_litros
        
    
    