from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
 
def home(request): 
    return render(request, 'home.html') 
 
def register_view(request): 
    return render(request, 'register.html') 
 
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
 
@login_required 
def dashboard_view(request): 
    return render(request, 'dashboard.html') 
 
def logout_view(request): 
    logout(request) 
    return redirect('logout_page') 
 
def logout_page(request): 
    return render(request, 'logout.html') 
