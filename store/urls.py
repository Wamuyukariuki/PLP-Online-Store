from django.urls import path
from . import views

app_name = 'store'  # Ensure this is correctly set

urlpatterns = [
    path('', views.store_home, name='store_home'),  # This is the correct name
    path('products/', views.product_list, name='product_list'),
    path('products/category/<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('product/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
    path('customer-orders/', views.customer_orders, name='customer_orders'),
    path('vendor-orders/', views.vendor_orders, name='vendor_orders'),
]
