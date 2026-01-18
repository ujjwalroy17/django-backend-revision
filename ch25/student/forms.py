from django import forms

# clean and validate field specific 
# class Registeration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password =  forms.CharField(widget=forms.PasswordInput)
    
#     def clean_name(self):
#         name_value = self.cleaned_data['name']
#         if len(name_value) < 4:
#             raise forms.ValidationError('Enter more than  or equal to 4 charcaters')
#         return name_value
#     def clean_email(self):
#         email_value = self.cleaned_data['email']
#         if len(email_value) < 20:
#             raise forms.ValidationError('Enter more than  or equal to 20 charcaters')
#         return email_value
    
# clean and validate django form all at once
class Registeration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password =  forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')
        
        if name_value and len(name_value)<4:
            self.add_error('name','Enter more than  or equal to 4 charcaters')
        if email_value and len(email_value)<10:
            self.add_error('email','Enter more than  or equal to 10 charcaters')
            
        return cleaned_data