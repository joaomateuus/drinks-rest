from django.test import TestCase
from drinks.models import Drink

class DrinkTest(TestCase):
    def setUp(self):
        self.first_drink = Drink.objects.create(
            name = 'caipirinha',
            description = 'limao'
        )
        self.second_drink = Drink.objects.create(
            name = 'heineken',
            description = 'cerveja'
        )
        
    def testing_title(self):
        self.assertEqual(self.first_drink.name, 'caipirinha')
        self.assertEqual(self.second_drink.name, 'heineken')
    
    def testing_description(self):
        self.assertEqual(self.first_drink.description, 'limao')
        self.assertEqual(self.second_drink.description, 'cerveja')
        