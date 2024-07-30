from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store_view, name='store_view'),
    path('products/', views.product_list, name='product_list'),

    # Add other store URLs here
]
