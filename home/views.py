from django.shortcuts import render
from category.models import Category


def home(request):
    categories = Category.objects.all()  # Fetch categories or other data as needed
    return render(request, 'home/home.html', {'categories': categories})
