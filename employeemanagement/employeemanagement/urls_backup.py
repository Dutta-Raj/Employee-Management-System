from django.contrib import admin 
from django.urls import path, include 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', include('employee_portal.urls')), 
] 
from django.contrib import admin 
from django.urls import path, include 
from employee.views import home 
ECHO is on.
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('employee/', include('employee.urls')), 
    path('', home, name='home'),  # Main landing page 
] 
