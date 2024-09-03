from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store_view, name='store_home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
]
