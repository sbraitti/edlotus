from django.contrib import admin
from django.urls import path,include
from reservas import views

urlpatterns = [
    path('', views.login, name='login'),
]