from _decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from .forms import OrderForm, ProductForm
from .models import Products, Order


def store_view(request):
    """Render the store main page."""
    return render(request, 'store/store.html')


@login_required(login_url='/login/')
def product_list(request):
    """Render a list of all products."""
    products = Products.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_list_by_category(request, category_slug):
    """Render a list of products filtered by category."""
    category = get_object_or_404(Category, slug=category_slug)
    products = Products.objects.filter(category=category)
    return render(request, 'store/product_list_by_category.html', {'products': products, 'category': category})


def product_details(request, category_slug, product_slug):
    """Render the details of a specific product."""
    product = get_object_or_404(Products, slug=product_slug, category__slug=category_slug)
    return render(request, 'store/product_details.html', {'product': product})


@login_required
def place_order(request, product_id):
    """View for placing an order."""
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, product=product)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.customer  # Associate the order with the logged-in customer
            order.save()
            return redirect('accounts:customer_dashboard')  # Redirect to a success page
    else:
        form = OrderForm(product=product)

    return render(request, 'store/place_order.html', {'form': form, 'product': product})


@login_required
def add_product(request):
    """View for adding a new product by the vendor."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor  # Associate the product with the logged-in vendor
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('accounts:vendor_dashboard')  # Redirect to the vendor's dashboard after adding
        else:
            messages.error(request, 'Please correct the errors below.')
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
            return redirect('accounts:vendor_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, product_id):
    """View for deleting a product."""
    product = get_object_or_404(Products, id=product_id, vendor=request.user.vendor)
    if request.method == 'POST':
        product.delete()
        return redirect('accounts:vendor_dashboard')
    return render(request, 'store/delete_product.html', {'product': product})
