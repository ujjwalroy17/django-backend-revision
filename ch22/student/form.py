from django import forms

class Registeration(forms.Form):
    first_name = forms.CharField() #<-- underscore means space
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    
class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    