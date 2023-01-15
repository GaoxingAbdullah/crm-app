from itertools import count
from struct import pack_into
from django.shortcuts import redirect, render
from django.http import HttpResponse
from accounts.form import OrderForm, CustomerForm

from accounts.models import Customer, Order, Product

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.filter()
    
    total_orders = orders.count()
    pending = orders.filter(status = 'Pending').count()
    delivered = orders.filter(status = 'Delivered').count()
    
    context =  {"customers": customers, "orders": orders,
                   "total_orders":total_orders,
                   "pending":pending,
                   'delivered':delivered }
    
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, customerId):
    customer = Customer.objects.get(id=customerId)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context =  {"customer": customer, "orders":orders, "orders_count":orders_count }
    return render(request, 'accounts/customer.html', context)


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'accounts/order_form.html', context)


def update_order(request, orderId):
    order = Order.objects.get(id=orderId)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'accounts/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        redirect('/')
        
    context = {"item":order}
    return render(request, 'accounts/delete.html', context)

def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            pass
    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)