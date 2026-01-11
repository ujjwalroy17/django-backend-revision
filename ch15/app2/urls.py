from django.urls import path
from app2.views import django_learn,python_learn

urlpatterns = [
    path('dj/',django_learn, name='django'),
    path('py/',python_learn, name='python'),

]
