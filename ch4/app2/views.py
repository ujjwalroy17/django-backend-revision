from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myapp12(request):
    return HttpResponse("My App 2 Page")

def myapp2_me(request):
    return HttpResponse("My App 2  me Page")