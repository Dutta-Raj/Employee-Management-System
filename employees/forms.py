from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmployeeProfile

class EmployeeRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=10,
        min_length=8,
        help_text="Required. 8-10 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    email = forms.EmailField(required=True)
    employee_id = forms.CharField(max_length=20, required=True)
    department = forms.CharField(max_length=100, required=True)
    position = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                 'employee_id', 'department', 'position', 'phone', 'address']

class AdminRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=10,
        min_length=8,
        help_text="Required. 8-10 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']