from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'student/home.html')
# def Profile(request,my_id):
#     student = {'id':my_id}
#     return render(request,'student/profile.html',student)

def Profile(request,my_class,my_id):
    student = {'class':my_class,'id':my_id}
    return render(request,'student/profile.html',student)