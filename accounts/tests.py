from django.test import TestCase

from .models import Customer, Tag, Product

# Create your tests here.

class ModelTesting(TestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(
           name="Hari", phone="123456", email="hari@zms.com" )
        
        self.tag = Tag.objects.create(name="food")
        
        self.product = Product.objects.create(
            name="BBQ Pizza", price=20.5, category="Indoor",  description="Something", 
        )
        
    def test_customer_model(self):
        data = self.customer
        self.assertTrue(isinstance(data, Customer))
        self.assertEqual(str(data), 'Hari')
        
    def test_tag_model(self):
        data = self.tag 
        self.assertTrue(isinstance(data, Tag))
        self.assertEqual(str(data), 'food')
        
    def test_product_model(self):
        data = self.product
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'BBQ Pizza')