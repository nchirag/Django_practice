"""
URL configuration for Student_management project.

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
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name = 'home'),
    path('student_list/',student_list,name = 'student_list'),
    path('add_student/',add_student,name = 'add_student'),
    path('delete_student/<int:id>',delete_student,name = 'delete_student'),
    path('edit_student/<int:id>',edit_student,name = 'edit_student'),

]
