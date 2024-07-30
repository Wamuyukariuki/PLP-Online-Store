from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from .forms import CustomerSignUpForm


def login(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('accounts:dashboard')  # Redirect to dashboard after login
            else:
                return redirect('accounts:signup')  # Redirect to register if authentication fails
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            return redirect('accounts:login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    """Handle user logout."""
    django_logout(request)
    return redirect('home')  # Redirect to homepage after logout


@login_required
def dashboard_view(request):
    """Render the dashboard for authenticated users."""
    user = request.user
    customer = getattr(user, 'customer', None)
    context = {'customer': customer}
    return render(request, 'accounts/dashboard.html', context)
