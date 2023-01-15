from django.contrib import admin

from .models import *

# Register your models here

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'email']
    list_display = ['name', 'phone', 'email', 'date_created']
    list_filter = ['date_created']
    
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category', 'price', 'description']
    list_display = ['name', 'category', 'price', 'description','date_created']
    list_filter = ['category', 'price','date_created']
    

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']    
    list_filter = ['name']

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['product', 'customer']
    list_display = ['product', 'customer', 'status', 'date_created']
    list_filter = ['status', 'product', 'date_created']
    

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)