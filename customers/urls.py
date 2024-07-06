from django.urls import path
from . import views

urlpatterns = [
    path('user_signup', views.signupuser, name='user_signup'),
    path('user_login', views.loginuser, name='user_login'),
    path('user_logout', views.logoutuser, name='user_logout'),
    path('user_profile', views.user_profile, name='user_profile'),
    
]
