from django.shortcuts import render
from datetime import datetime

# Example 1.1 - Variable

# Create your views here.

# def  learn_django(request):
#     return render(request,'app1/django.html', context={'name': 'django'})

# Example 1.2 - Variable

# def  learn_django(request):
#     name = 'Django'
#     duration = '4 months'
#     seats = 10
#     data = {'name' : name, 'duration' : duration, 'seats' : seats}
#     return render(request,'app1/django.html', context=data)


# # Example 2 - Filter

# def  learn_django(request):
#     return render(request,'app1/django.html', context={'name': 'django','desc' : 'Django is an awesome Web framework'})

# Example 3 - Date and time

# def  learn_django(request):
#     d = datetime.now()
#     return render(request,'app1/django.html', context={'date': d})


# # Example 4 - Float Format

# def  learn_django(request):
#     d = datetime.now()
#     return render(request,'app1/django.html', context={'p1':56.24321,'p2':56.000,'p3':56.37000})


# Example 5.1 -  If Tag

# def  learn_django(request):
#     d = datetime.now()
#     return render(request,'app1/django.html', context={'nm':True})

# # Example 5.2 -  If Tag

# def  learn_django(request):
#     return render(request,'app1/django.html', context={'nm':'Django','st' : 5})

# Example 6 -  For Loop

def  learn_django(request):
    student = {'names': ['Rahul','ujjwal','Aman','Raj']}
    return render(request,'app1/django.html', context=student)