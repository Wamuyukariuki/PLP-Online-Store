from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from store.forms import ProductForm
from store.models import Products, Order
from .forms import CustomerSignUpForm, VendorSignUpForm
from .models import Customer, Vendor


def login(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)

                # Redirect based on user role
                if user.is_superuser:
                    return redirect('admin:index')  # Redirect to Django admin
                elif user.groups.filter(name='Vendor').exists():
                    return redirect('accounts:vendor_dashboard')
                elif user.groups.filter(name='Customer').exists():
                    return redirect('accounts:customer_dashboard')

                # Fallback if no specific role found
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def register_customer(request):
    """Handle customer registration."""
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                Customer.objects.get_or_create(user=user)
                customer_group, _ = Group.objects.get_or_create(name='Customer')
                customer_group.user_set.add(user)
                return redirect('accounts:login')
            except IntegrityError:
                form.add_error(None, 'A customer with this username already exists.')
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/register_customer.html', {'form': form})


def register_vendor(request):
    """Handle vendor registration."""
    if request.method == 'POST':
        form = VendorSignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                Vendor.objects.get_or_create(user=user)
                return redirect('accounts:login')
            except IntegrityError:
                form.add_error(None, 'A vendor with this username already exists.')
    else:
        form = VendorSignUpForm()
    return render(request, 'registration/register_vendor.html', {'form': form})


def logout(request):
    """Handle user logout."""
    django_logout(request)
    return redirect('home')


@login_required
def customer_dashboard(request):
    """View for the customer dashboard."""
    products = Products.objects.all()
    return render(request, 'accounts/customer_dashboard.html', {'products': products})


@login_required
def place_order(request, product_id):
    """View for placing an order."""
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        if request.user.customer:
            order = Order.objects.create(customer=request.user.customer, product=product)
            return redirect('accounts:order_success', order_id=order.id)
        else:
            return redirect('accounts:login')  # Redirect to login if not a customer
    return render(request, 'store/place_order.html', {'product': product})


def some_default_view(request):
    return render(request, 'some_default_template.html')


@login_required
def vendor_dashboard(request):
    """View for the vendor dashboard."""
    vendor = get_object_or_404(Vendor, user=request.user)
    products = Products.objects.filter(vendor=vendor)
    orders = Order.objects.filter(product__vendor=vendor)
    return render(request, 'accounts/vendor_dashboard.html', {'products': products, 'orders': orders})

@login_required
def add_product(request):
    """View for adding a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.save()
            return redirect('vendor:vendor_dashboard')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    """View for editing an existing product."""
    product = get_object_or_404(Products, id=product_id, vendor=request.user.vendor)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('vendor:vendor_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    """View for deleting a product."""
    product = get_object_or_404(Products, id=product_id, vendor=request.user.vendor)
    if request.method == 'POST':
        product.delete()
        return redirect('vendor:vendor_dashboard')
    return render(request, 'store/delete_product.html', {'product': product})
