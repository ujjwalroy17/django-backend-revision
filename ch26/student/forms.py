from django import forms
from django.core import validators

# Custom validation
def start_with_u(value):
    if value[0].lower() != 'u':
        raise forms.ValidationError("Emails should starts with 'u'")
    
    
# Built-in validators
class Registeration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(3)])
    email = forms.EmailField(validators=[start_with_u])
    password =  forms.CharField(widget=forms.PasswordInput)
    