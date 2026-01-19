from django.shortcuts import render,redirect
from student.forms import Registeration
from django.http import HttpResponseRedirect
from student.models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registeration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Name:{name}")
            print(f"Email:{email}")
            print(f"password:{password}")
            return HttpResponseRedirect('/student/success/')
            # return redirect(reg_success)

    else:
        form = Registeration()
    return render(request,'student/register.html',{'form':form})

def reg_success(request):
    return render(request,'student/sucess.html')
