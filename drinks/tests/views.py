from django.test import TestCase, Client
from django.urls import reverse
from drinks.models import Drink
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('drinks')
        self.details_url = reverse('drinks_details', args=(1, ))
        
        self.cerveja = Drink.objects.create(
            id = 1,
            name = 'Heineken',
            description = 'cerveja'
        )
                
    def testing_drinks_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
    
    def testing_drinks_details_GET(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, 200)
        
        
        

