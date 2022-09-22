from django.db import models
"""
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    class DrinkCategory(models.TextChoices):
        SOFT_DRINKS = 1, _('Soft Drinks')
        BEERS = 2, _('Beers')
        DESTILATE = 3, _('Destilate')
        WINES = 4, _('Wines')
        
    category = models.CharField(
        choices = DrinkCategory.choices(max_lenght = 50)
    )
    
    def __str__(self):
        return self.category 
"""
        

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    # category = models.ForeignKey(Category)

    def __str__(self):
        return self.name