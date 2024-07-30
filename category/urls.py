from django.urls import path
from .views import filter_products, search, category_list, category_detail

app_name = 'category'

urlpatterns = [
    path('', category_list, name='category_list'),
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('search/', search, name='search'),
    path('filter/', filter_products, name='filter_products'),
]
