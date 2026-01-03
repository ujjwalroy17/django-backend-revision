"""
URL configuration for ch4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1 import views as ap1
from app2 import views as ap2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap1.home, name='home'),
    path('app1/', ap1.myapp1, name='myapp1'),
    path('app12/', ap2.myapp12, name='myapp12'),
    path('app2_me/', ap2.myapp2_me, name='myapp2_me'),
]
