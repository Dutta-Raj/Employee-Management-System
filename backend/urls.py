from django.contrib import admin 
from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'), 
    path('employee/register/', views.employee_register, name='employee_register'), 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    # Change logout to use POST properly 
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('clock-in/', views.clock_in, name='clock_in'), 
    path('clock-out/', views.clock_out, name='clock_out'), 
] 
 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
