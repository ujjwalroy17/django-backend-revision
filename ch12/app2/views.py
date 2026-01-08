from django.shortcuts import render

# Create your views here.

# Create your views here.
def django_learn(request):
    return render(request,'app2/django.html')

def python_learn(req):
    return render(req,'app2/python.html')