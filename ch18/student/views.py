from django.shortcuts import render
from student.models import Profile

# Create your views here.
def all_data(req):
    all_students = Profile.objects.all()
    print(all_students)
    return render(req,'student/all.html',{'students' : all_students})

def single_data(req):
    student = Profile.objects.get(pk=1)
    # student = Profile.objects.get(id=1)
    # student = Profile.objects.get(Name='Aman')
    print(student)
    return render(req,'student/single.html',{'student' : student})