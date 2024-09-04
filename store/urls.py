from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Store main page
    path('', views.store_view, name='store_view'),

    # List of all products
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_details, name='product_detail'),


    # List of products by category
    path('products/category/<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),

    # Product details
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),

    # Place an order
    path('products/order/<int:product_id>/', views.place_order, name='place_order'),

    # Customer orders
    path('orders/customer/', views.customer_orders, name='customer_orders'),

    # Vendor orders
    path('orders/vendor/', views.vendor_orders, name='vendor_orders'),

    # Add a product (vendor only)
    path('products/add/', views.add_product, name='add_product'),

    # Edit a product (vendor only)
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),

    # Delete a product (vendor only)
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
