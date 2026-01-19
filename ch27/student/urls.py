from django.urls import path
from student.views import register,reg_success

urlpatterns = [
    path('register/',register, name='register'),
    path('success/',reg_success, name='reg_success'),

]