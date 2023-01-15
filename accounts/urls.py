from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:customerId>/', views.customer, name='customer'),
    
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:orderId>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    
    path('create_customer/', views.create_customer, name='create_customer'),
]