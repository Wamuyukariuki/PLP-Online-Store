from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from category.models import Category
from .forms import OrderForm, ProductForm
from .models import Products, Order  # Ensure this matches the model name used in your project


def store_view(request):
    """Render the store main page."""
    return render(request, 'store/store.html')


@login_required(login_url='/login/')  # Adjust the login URL as needed
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
    context = {'product': product}
    return render(request, 'store/product_details.html', context)


def store_home(request):
    """Render the store home page."""
    return render(request, 'store/store_home.html')  # Adjust the template name accordingly


# views.py in your store app


@login_required
def place_order(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, product=product)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('accounts:customer_dashboard')  # Redirect to a success page

    else:
        form = OrderForm(product=product)

    return render(request, 'store/place_order.html', {'form': form, 'product': product})


@login_required
def customer_orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'accounts/customer_orders.html', {'orders': orders})


@login_required
def vendor_orders(request):
    orders = Order.objects.filter(product__vendor=request.user.vendor)
    return render(request, 'accounts/vendor_orders.html', {'orders': orders})


@login_required
def add_product(request):
    """View for adding a new product by the vendor."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle both form data and files
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor  # Associate the product with the logged-in vendor
            product.save()
            return redirect('vendor:product_list')  # Redirect to the vendor's product list after adding
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})
