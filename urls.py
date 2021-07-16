from django.urls import path
from django.contrib import admin
from.import views

urlpatterns = [

path('',views.home, name='home'),
 path('signup',views.handleSignup, name='handleSignup'),
 path('login',views.handleLogin, name='handleLogin'),
 path('logout',views.handleLogout, name='handleLogout'),
 path('editprofile',views.editprofile, name='editprofile'),
 path('profile',views.profile, name='profile'),
 
]