from django.urls import path
from student.views import Home,registeration

urlpatterns = [
    path('home/',Home, name="home"),
    path('register/',registeration, name='register')
]