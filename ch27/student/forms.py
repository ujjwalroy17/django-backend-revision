from django import forms
from django.core import validators

class Registeration(forms.Form):
    name = forms.CharField(error_messages={'required':'Name is required'})
    email = forms.EmailField(error_messages={'required':'Email is required'})
    password =  forms.CharField(error_messages={'required':'Password is required'},widget=forms.PasswordInput)
    