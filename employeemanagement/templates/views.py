from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.contrib.auth.models import User 
from .models import Employee 
ECHO is on.
def home(request): 
    return render(request, 'home.html') 
ECHO is on.
def register_view(request): 
    if request.method == 'POST': 
        # Handle registration logic here 
        pass 
    return render(request, 'register.html') 
ECHO is on.
def login_view(request): 
    if request.method == 'POST': 
        username = request.POST.get('email') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            login(request, user) 
            return redirect('dashboard') 
        else: 
            messages.error(request, 'Invalid credentials') 
    return render(request, 'login.html') 
ECHO is on.
@login_required 
def dashboard_view(request): 
    return render(request, 'dashboard.html') 
ECHO is on.
def logout_view(request): 
    logout(request) 
    return redirect('logout_page') 
ECHO is on.
def logout_page(request): 
    return render(request, 'logout.html') 
