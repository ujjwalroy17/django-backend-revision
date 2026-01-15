from django.urls import path
from app1.views import home,about
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
]
