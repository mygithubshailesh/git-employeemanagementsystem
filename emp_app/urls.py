"""emp_maneg_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('all_employee', views.all_employee, name ='all_employee'),
    path('add_employee', views.add_employee, name ='add_employee'),
    path('remove_employee', views.remove_employee, name ='remove_employee'),
    path('filter_employee', views.filter_employee, name ='filter_employee'),
]
