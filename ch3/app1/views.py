from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def  learn_django(request):
    return HttpResponse('Hello Django')

def  learn_python(request):
    return HttpResponse('<h1>Hello Python<h1>')