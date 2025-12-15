from django.urls import path 
from . import views 
ECHO is on.
urlpatterns = [ 
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'), 
    path('dashboard/', views.dashboard_view, name='dashboard'), 
    path('logout/', views.logout_view, name='logout'), 
    path('logout-page/', views.logout_page, name='logout_page'), 
] 
