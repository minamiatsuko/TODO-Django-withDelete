from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'TodoList'


urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
]

