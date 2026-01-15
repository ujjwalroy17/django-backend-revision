from django.urls import path,include
from main.views import home

urlpatterns = [
    path('home/',home, name='home')
]