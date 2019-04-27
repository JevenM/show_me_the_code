"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 相当于确定了所有的URL前都要有“polls”，具体的后面的内容在polls.urls里面定义
    # 比如："/polls/34/"，它切掉了匹配的文本（"polls/"），将剩余文本——"34/"，发送至 'polls.urls' URLconf 做进一步处理。
    path('polls/', include('polls.urls')),
    path('mb/', include('MessageBoard.urls')),
    path('todo/', include('todo.urls')),
]
