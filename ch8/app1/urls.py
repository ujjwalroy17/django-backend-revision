from django.urls import path
from .views import learn_django,learn_drf

urlpatterns = [
    path('dj/', learn_django),
    path('drf/',learn_drf)
]
