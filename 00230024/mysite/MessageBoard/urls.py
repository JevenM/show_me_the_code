# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'MessageBoard'
urlpatterns = [
    path('', views.index, name='index'),
    path('postmsgs/', views.postmessages, name='postmessages'),
]