"""
URL configuration for interview project.

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
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('teacher_students',teacher_students,name='teacher_students'),
    path('student_teachers',student_teachers,name='student_teachers'),
    path('generate_certificate/<int:student_id>/<int:teacher_id>/', generate_certificate, name='generate_certificate'),
    path('verify_certificate/', verify_certificate, name='verify_certificate'),

]
