from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:customerId>/', views.customer, name='customer'),
    
    path('create_order/<str:pk>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    
    path('create_customer/', views.create_customer, name='create_customer'),
    
    
    path('account/', views.accountSettings, name='account'),
    
    path('user/', views.userPage, name='user'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
         name="reset_password"),
    
    path('reset_password_sent/)', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
         name="password_reset_sent"),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
         name="password_reset_confirm"),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), 
         name="password_reset_complete"),
]