from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('filter/', views.filter_products, name='filter_products'),
    path('search/', views.search, name='search'),
    path('list/', views.category_list, name='category_list'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),

]
