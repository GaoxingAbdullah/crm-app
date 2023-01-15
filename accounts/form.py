from django.forms import ModelForm

from .models import Order, Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = {'customer', 'product', 'status'}
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = {'name', 'email', 'phone'}
        