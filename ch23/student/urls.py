from django.contrib import admin
from django.urls import path
from student.views import register

urlpatterns = [
    path('register/', register, name='register' ),
]