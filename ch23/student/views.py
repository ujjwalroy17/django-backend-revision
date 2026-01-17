from django.shortcuts import render
from student.form import Registeration
# Create your tests here.
def register(req):
    fm = Registeration()
    return render(req,'student/registeration.html',{'form' : fm})
