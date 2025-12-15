from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
from employees.forms import EmployeeRegistrationForm 
from employees.models import EmployeeProfile, Attendance 
import datetime 
 
# ===== HOME PAGE ===== 
def home(request): 
    return render(request, 'home.html') 
 
# ===== ADMIN REGISTRATION ===== 
def register(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            messages.success(request, 'Admin account created successfully! You can now login.') 
            return redirect('login') 
    else: 
        form = UserCreationForm() 
    return render(request, 'registration/register.html', { 
        'form': form, 
        'title': 'Admin Registration' 
    }) 
 
# ===== EMPLOYEE REGISTRATION ===== 
def employee_register(request): 
    if request.method == 'POST': 
        form = EmployeeRegistrationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            # Create employee profile 
            profile, created = EmployeeProfile.objects.get_or_create( 
                user=user, 
                defaults={ 
                    'employee_id': form.cleaned_data['employee_id'], 
                    'department': form.cleaned_data['department'], 
                    'position': form.cleaned_data['position'], 
                    'phone': form.cleaned_data['phone'], 
                    'address': form.cleaned_data['address'] 
                } 
            ) 
            if not created: 
                profile.employee_id = form.cleaned_data['employee_id'] 
                profile.department = form.cleaned_data['department'] 
                profile.position = form.cleaned_data['position'] 
                profile.phone = form.cleaned_data['phone'] 
                profile.address = form.cleaned_data['address'] 
                profile.save() 
 
            messages.success(request, 'Employee registration successful! Please login with your credentials.') 
            return redirect('login') 
    else: 
        form = EmployeeRegistrationForm() 
    return render(request, 'registration/employee_register.html', { 
        'form': form, 
        'title': 'Employee Registration' 
    }) 
 
# ===== DASHBOARD ===== 
@login_required 
def dashboard(request): 
    profile = None 
    attendances = [] 
    today_attendance = None 
 
    try: 
        profile = EmployeeProfile.objects.get(user=request.user) 
        attendances = Attendance.objects.filter(employee=profile).order_by('-date')[:10] 
        today_attendance = Attendance.objects.filter(employee=profile, date=datetime.date.today()).first() 
    except EmployeeProfile.DoesNotExist: 
        # If user doesn't have employee profile (e.g., admin) 
        pass 
 
    context = { 
        'profile': profile, 
        'attendances': attendances, 
        'today_attendance': today_attendance, 
        'today': datetime.date.today() 
    } 
    return render(request, 'dashboard.html', context) 
 
# ===== CLOCK IN ===== 
@login_required 
def clock_in(request): 
    try: 
        profile = EmployeeProfile.objects.get(user=request.user) 
    except EmployeeProfile.DoesNotExist: 
        messages.error(request, 'You need to complete your employee profile first.') 
        return redirect('dashboard') 
 
    today = datetime.date.today() 
 
    if not Attendance.objects.filter(employee=profile, date=today).exists(): 
        Attendance.objects.create( 
            employee=profile, 
            time_in=datetime.datetime.now().time() 
        ) 
        messages.success(request, 'Clocked in successfully!') 
    else: 
        messages.warning(request, 'You have already clocked in today.') 
 
    return redirect('dashboard') 
 
# ===== CLOCK OUT ===== 
@login_required 
def clock_out(request): 
    try: 
        profile = EmployeeProfile.objects.get(user=request.user) 
    except EmployeeProfile.DoesNotExist: 
        messages.error(request, 'You need to complete your employee profile first.') 
        return redirect('dashboard') 
 
    today = datetime.date.today() 
 
    attendance = Attendance.objects.filter(employee=profile, date=today).first() 
    if attendance and not attendance.time_out: 
        attendance.time_out = datetime.datetime.now().time() 
        # Calculate hours worked 
        time_in = datetime.datetime.combine(datetime.date.today(), attendance.time_in) 
        time_out = datetime.datetime.combine(datetime.date.today(), attendance.time_out) 
        hours = (time_out - time_in).seconds / 3600 
        attendance.hours_worked = round(hours, 2) 
        attendance.save() 
        messages.success(request, 'Clocked out successfully!') 
    else: 
        messages.warning(request, 'Please clock in first or already clocked out.') 
 
    return redirect('dashboard') 
