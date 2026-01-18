from django import forms

class Registeration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password =  forms.CharField(widget=forms.PasswordInput)