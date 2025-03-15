"""
URL configuration for Employee_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name = 'home'),
    path("employee_list",employee_list,name = 'employee_list'),
    path("add_employee",add_employee,name = 'add_employee'),
    path('delete_employee/<int:emp_id>/', delete_employee, name='delete_employee'),
    path('edit_employee/<int:emp_id>/', edit_employee, name='edit_employee'),
    
]
