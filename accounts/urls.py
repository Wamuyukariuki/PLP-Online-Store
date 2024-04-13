from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Customer-login"),
    path('register', views.register, name="Customer-signup"),
    path('login', views.login, name="Customer-signin"),

]
