from django.db import models 
from django.contrib.auth.models import User 
 
class EmployeeProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    employee_id = models.CharField(max_length=20, unique=True) 
    department = models.CharField(max_length=100) 
    position = models.CharField(max_length=100) 
    phone = models.CharField(max_length=15) 
    address = models.TextField() 
    join_date = models.DateField(auto_now_add=True) 
    profile_picture = models.ImageField(upload_to='profiles/', blank=True) 
 
    def __str__(self): 
        return f'{self.user.username} - {self.employee_id}' 
 
class Attendance(models.Model): 
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True) 
    time_in = models.TimeField() 
    time_out = models.TimeField(null=True, blank=True) 
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, default=0) 
 
    def __str__(self): 
        return f'{self.employee} - {self.date}' 
