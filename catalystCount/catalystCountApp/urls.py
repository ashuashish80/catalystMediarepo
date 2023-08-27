from django.contrib import admin
from django.urls import path
from catalystCountApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_view, name='login_view'),
    path('registration/', views.Registration, name='Registration'),
    path('logout/', views.logoutpage, name='logout'),
]