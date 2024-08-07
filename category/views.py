from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from decimal import Decimal
from store.models import Products
from .models import Category


def filter_products(request):
    try:
        min_price = Decimal(request.GET.get('min_price', '0'))
        max_price = Decimal(request.GET.get('max_price', '9999999'))
    except:
        return HttpResponseBadRequest("Invalid price range.")

    brand = request.GET.get('brand')
    size = request.GET.get('size')
    color = request.GET.get('color')

    filtered_products = Products.objects.all()
    filtered_products = filtered_products.filter(price__gte=min_price, price__lte=max_price)

    if brand:
        filtered_products = filtered_products.filter(brand=brand)
    if size:
        filtered_products = filtered_products.filter(size=size)
    if color:
        filtered_products = filtered_products.filter(color=color)

    return render(request, 'category/filter_results.html', {'products': filtered_products})


def search(request):
    query = request.GET.get('q')
    results = Products.objects.filter(title__icontains=query)
    return render(request, 'category/search_results.html', {'results': results, 'query': query})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category/category_detail.html', {'category': category})
