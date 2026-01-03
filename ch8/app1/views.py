from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    # type 1-->
    data = {'course_name' : 'Django'}
    # return render(request,'app1/django.html',context=data)
    
    #type 2--> 
    # return render(request,'app1/django.html',{'course_name' : 'django'})
    
    #type 3-->
    return render(request,'app1/django.html',data)


def learn_drf(request):
    seat = 10
    data = {
        'course_name' : 'DRF',
        'version' : 5,
        'sts' : seat
    }
    return render(request,'app1/drf.html',data)