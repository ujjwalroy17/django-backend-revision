from django import forms
from django.core import validators
from student.models import Profile

# class Registeration(forms.Form):
#     name = forms.CharField(error_messages={'required':'Name is required'})
#     email = forms.EmailField(error_messages={'required':'Email is required'})
#     password =  forms.CharField(error_messages={'required':'Password is required'},widget=forms.PasswordInput)
    
class Registeration(forms.ModelForm):
    name = forms.CharField(max_length=50,required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['name','email','password']
        labels = {'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
        error_messages={'email' : {'required':'Email is required'}}
        widgets = {'password':forms.PasswordInput}