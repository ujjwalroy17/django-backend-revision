# ModelForm in Django 5 (ch27)

## 📌 Topic Covered

Using Django ModelForm to create forms directly from models with less code and built-in database integration.

## 🔹 What is ModelForm in Django?

A **ModelForm** is a Django form that is directly linked to a database model.
It automatically creates form fields based on model fields.

👉 **ModelForm = Form + Model**

## 🔹 Why Use ModelForm?

### Without ModelForm:
- You write form fields manually
- You manually save data to database

### With ModelForm:
- Django auto-generates fields
- Validation matches model fields
- Easy saving to database using `form.save()`

## 🔹 Model Definition (`models.py`)
```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
```
> This model maps directly to a database table.

## 🔹 Creating ModelForm (`forms.py`)
```python
from django import forms
from student.models import Profile

class Registration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Enter Name',
            'email': 'Enter Email',
            'password': 'Enter Password'
        }
        error_messages = {
            'email': {'required': 'Email is required'}
        }
        widgets = {
            'password': forms.PasswordInput()
        }
```
# Explanation of ModelForm Components

## Meta Class
| Option | Purpose |
|---------|---------|
| `model` | Connects form to model |
| `fields` | Fields to include |
| `labels` | Custom field labels |
| `error_messages` | Custom validation messages |
| `widgets` | Customize HTML input |

## Extra Fields in ModelForm
```python
confirm_password = forms.CharField(widget=forms.PasswordInput)
```

### Fields not in `fields`
- Are not saved to database
- Used for validation only

# Using ModelForm in View (`views.py`)
```python
from django.shortcuts import render
from student.forms import Registeration
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = Registeration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Password: {password}")

            return HttpResponseRedirect('/student/success/')
    else:
        form = Registeration()

    return render(request, 'student/register.html', {'form': form})
```

# Best Practice: Saving Data Using ModelForm
Instead of manually extracting fields, use:
```python
form.save()
```
Example:
```python
if form.is_valid():
    form.save()
```
django automatically:
- Creates model instance
- Saves data to database

# Difference: Form vs ModelForm 
| Feature | Form | ModelForm |
|---------|-------|-----------|
| Linked to model | ❌ No | ✅ Yes |
| Manual fields | ✅ Required | ❌ Optional |
| Auto DB save | ❌ No | ✅ Yes |
eValidation | Manual | Automatic |

# 🔹 Common Use Cases for ModelForm

- **Registration forms**
- **CRUD operations**
- **Admin-like forms**
- **Rapid development**

# 🔹 Important Notes

- `confirm_password` is not stored in DB
- `ModelForm` respects model field constraints
- Use `form.save(commit=False)` for custom logic
- Validation can be added using `clean()` or `clean_<field>()`

# ✅ Summary

- **ModelForm connects forms and models**
- **Reduces boilerplate code**
- **Auto-handles validation**
- **Simplifies database operations**
- **Best choice for CRUD applications**