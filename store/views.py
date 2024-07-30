from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Products


def store_view(request):
    # You can add any context you need here
    return render(request, 'store/store.html')


@login_required  # This decorator ensures that only logged-in users can access this view
def product_list(request):
    # Fetch the products from your database
    products = Products.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def store_home(request):
    return render(request, 'store/store_home.html')  # Adjust the template name accordingly
