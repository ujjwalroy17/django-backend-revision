from django.shortcuts import render
from student.form import Registeration,Login
# Create your tests here.
def register(req):
    # fm = Registeration()
    fm = Registeration(field_order=['email','city'])
    return render(req,'student/registeration.html',{'form' : fm})

def login(req):
    # fm = Login()
    # fm = Login(auto_id='user_%s')
    # fm = Login(auto_id=True)
    # fm = Login(auto_id=False)
    
    fm = Login(initial={'email':'user@example.com','password':'12345678'})
    return render(req,'student/login.html',{'form' : fm})