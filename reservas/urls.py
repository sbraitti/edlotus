from django.contrib import admin
from django.urls import path,include
from reservas import views
from django.conf.urls import url

urlpatterns = [
    path('', views.lotus_login, name='lotus_login'),
    path('logout/', views.lotus_logout, name='lotus_logout'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
]