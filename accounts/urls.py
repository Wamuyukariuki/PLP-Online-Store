from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/vendor/', views.register_vendor, name='register_vendor'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('order/place/<int:product_id>/', views.place_order, name='place_order'),
    path('some-default/', views.some_default_view, name='some_default_view'),
]
