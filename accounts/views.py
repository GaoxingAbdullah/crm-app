from django.shortcuts import redirect, render
from accounts.form import OrderForm, CustomerForm, UserCreateForm
from django.forms import inlineformset_factory
from accounts.models import Customer, Order, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users, admin_only

from .filter import OrderFilter

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Account OR Password is incorrect.")
            
    context ={}      
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerUser(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user =  form.save()
            username = form.cleaned_data.get("username")
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            Customer.objects.create(user=user)
            
            messages.success(request, "Account created for " + username)
            return redirect('login')
    
    context = {"form":form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    pending = orders.filter(status = 'Pending').count()
    delivered = orders.filter(status = 'Delivered').count()
    
    context =  {"orders": orders,
                   "total_orders":total_orders,
                   "pending":pending,
                   'delivered':delivered }
    return render(request, "accounts/user.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == "POST":
       form = CustomerForm(request.POST, request.FILES, instance=customer) 
       if form.is_valid():
           form.save()
           
    context = {"form": form}
    return render(request, 'accounts/account_settings.html', context)



@login_required(login_url="login")
@admin_only
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

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def customer(request, customerId):
    customer = Customer.objects.get(id=customerId)
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context =  {"customer": customer, "orders":orders, "orders_count":orders_count , "myFilter": myFilter}
    
    return render(request, 'accounts/customer.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={"customer": customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        #form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        
    context = {"formset": formset}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
        
    context = {"item":order}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
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