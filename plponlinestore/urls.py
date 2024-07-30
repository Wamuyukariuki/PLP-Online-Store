"""
URL configuration for plponlinestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', RedirectView.as_view(url='/home/', permanent=False)),  # Redirect root URL to home page
    path('home/', include('home.urls')),  # Home app URLs
    path('accounts/', include('accounts.urls')),  # Accounts app URLs
    path('category/', include('category.urls')),  # Category app URLs
    path('store/', include('store.urls')),  # Store app URLs
]




