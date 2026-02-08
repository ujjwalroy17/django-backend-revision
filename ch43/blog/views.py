from django.shortcuts import render
from django.template.response import TemplateResponse

def home(request):
  print("i am home view")
  return render(request, 'blog/home.html')

def my_math(request):
 print("I am my_math View")
 a = 10/0
 return render(request, 'blog/math.html', {'a': a})

def user_info(request):
 print("I am user_info View")
 context = {'name':'Rahul'}
 return TemplateResponse(request, 'blog/user.html', context)
