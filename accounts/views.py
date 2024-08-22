from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
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
                # Check if the user is a customer or vendor and redirect accordingly
                if hasattr(user, 'customer'):
                    return redirect('accounts:customer_dashboard')
                elif hasattr(user, 'vendor'):
                    return redirect('accounts:vendor_dashboard')
                else:
                    return redirect('some_default_view')  # Add a fallback view if needed
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
                vendor_group, _ = Group.objects.get_or_create(name='Vendor')
                vendor_group.user_set.add(user)
                return redirect('accounts:login')  # Ensure this is the correct redirect
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
        # Implement order creation logic here
        order = Order.objects.create(customer=request.user.customer, product=product)
        return redirect('accounts:order_success', order_id=order.id)
    return render(request, 'store/place_order.html', {'product': product})


@login_required
def vendor_dashboard(request):
    """View for the vendor dashboard."""
    vendor = request.user.vendor
    products = Products.objects.filter(vendor=vendor)
    orders = Order.objects.filter(product__vendor=vendor)
    return render(request, 'accounts/vendor_dashboard.html', {'products': products, 'orders': orders})


@login_required
def add_product(request):
    """View for adding a new product."""
    if request.method == 'POST':
        # Handle product addition logic here
        # e.g., use a form to gather product details
        return redirect('vendor:product_list')
    return render(request, 'vendor/add_product.html')
