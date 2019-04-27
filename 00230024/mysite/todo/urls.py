# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
]
