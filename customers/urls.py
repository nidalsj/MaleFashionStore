from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signupuser, name='user_signup'),
    path('login', views.loginuser, name='user_login'),
]
