from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Order
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return render(request, 'product_not_found.html')  # Handle product not found

    context = {'product': product}
    return render(request, 'product_detail.html', context)


@login_required  # Restricts access to logged-in users
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'order_list.html', context)
