from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, blank=True,  null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='logo.png', null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
 
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField()
    date_created =  models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.name
    
    