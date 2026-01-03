from django.urls import path
from .views import learn_django


urlpatterns = [
    path('dj/', learn_django),
    path('py/', learn_django,{'status' :  "OK"}),
]