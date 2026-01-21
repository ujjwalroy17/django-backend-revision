from django.shortcuts import render
from django.contrib import messages
from student.models import User
from student.forms import StudentRegisteration

# Create your views here.
def Home(request):
    messages.add_message(request,messages.SUCCESS,'Your account has been created')
    messages.add_message(request,messages.INFO,'THis is info')
    messages.add_message(request,messages.WARNING,'this is warning')
    messages.add_message(request,messages.ERROR,'This is error')
    messages.add_message(request,messages.DEBUG,'This is Debug')
    print(messages.get_level(request))
    messages.set_level(request, messages.DEBUG)
    messages.add_message(request,messages.DEBUG,'This is Debug')
    print(messages.get_level(request))

    return render(request,'student/home.html')

def registeration(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Registeration Success!!')
    else:
        fm = StudentRegisteration()
    return render(request,'student/registeration.html',{'form':fm})