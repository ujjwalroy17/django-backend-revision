# Save, Update & Delete Form Data to Database in Django 5 (ch26)

## 📌 Topic Covered

- Performing CRUD operations (Create, Update, Delete) using Django Forms and Models.

## 🔹 What is CRUD in Django?

CRUD stands for:

- **Create** → Save data to database
- **Read** → Fetch data from database
- **Update** → Modify existing records
- **Delete** → Remove records from database

In this chapter, we focus on:
- Create (Save)
- Update
- Delete

to perform these operations using Django Form + Model.

## 🔹 Model Definition (`models.py`)
```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
```

> This model represents a database table named: `student_profile`

## 🔹 Django Form (`forms.py`)
```python
from django import forms

class Registeration(forms.Form):
    name = forms.CharField(error_messages={'required':'Name is required'})
    email = forms.EmailField(error_messages={'required':'Email is required'})
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required':'Password is required'}
    )
```
> The form collects user input and validates it before database operations.

## 🔹 View Logic (`views.py`)
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
```

## Data Operations in Django

### 1️⃣ Save Data to Database (Create)
```python
user = Profile(name=name, email=email, password=password)
user.save()
```

> **This creates a new record in the database.**

### 2️⃣ Update Data in Database
```python
user = Profile(id=1, name=name, email=email, password=password)
user.save()
```

> **Explanation:**
>
> - Django checks `id`
> - If record exists → UPDATE
> - If record does not exist → INSERT

### 3️⃣ Delete Data from Database
```python
user = Profile(id=3)
user.delete()
```

> **This deletes the record with `id = 3` from the database.**

### 🔁 Complete View Example
```python
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # SAVE
            # user = Profile(name=name, email=email, password=password)
            # user.save()

            # UPDATE
            # user = Profile(id=1, name=name, email=email, password=password)
            # user.save()

            # DELETE
            user = Profile(id=3)
            user.delete()

            return HttpResponseRedirect('/student/success/')
    else:
        form = Registration()
    
    return render(request, 'student/register.html', {'form': form})
```
## 🔹 Important Notes

- `save()` → Inserts or updates data
- `delete()` → Removes data permanently
- `cleaned_data` → Always use validated form data
- `id` → Used to identify records uniquely

**Always validate form before database operations**

## 🔹 Recommended Alternative (Best Practice)

Instead of:

```python
Profile(id=1).delete()
```

Use:

```python
Profile.objects.get(id=1).delete()
```

This ensures the object exists before deletion.

# 🔹 CRUD Summary Table
| Operation | Code |
| --- | --- |
| Create | `Profile(...).save()` |
| Update | `Profile(id=1,...).save()` |
| Delete | `Profile(id=1).delete()` |

# ✅ Summary
- Django forms collect and validate user input
- Models handle database operations
- `save()` is used for create & update
- `delete()` removes records
- Django ORM makes CRUD operations easy and secure