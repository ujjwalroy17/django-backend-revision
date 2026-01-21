from django import forms
from student.models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']