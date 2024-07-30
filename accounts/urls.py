from django.urls import path
from .views import login, register, logout, dashboard_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
