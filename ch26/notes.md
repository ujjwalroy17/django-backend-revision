# 📘 Django Forms – Built-in Validators & Custom Validators (ch24)

## 📌 Topic Covered

Using Django built-in validators and creating custom validators to validate form fields.

---

## 🔹 What are Validators in Django?

Validators are functions or classes used to check whether a field’s value meets certain conditions. They run automatically during form validation when `form.is_valid()` is called.

### Validators:
- Validate data before `cleaned_data` is created
- Raise `ValidationError` if input is invalid
- Are reusable and clean

---

## 🔹 Types of Validators in Django

- Built-in Validators
- Custom Validators

---

## 1️⃣ Built-in Validators

django provides many ready-made validators in [`django.core.validators`](https://docs.djangoproject.com/en/stable/ref/validators/).

### Common Built-in Validators:
- `MinLengthValidator`
- `MaxLengthValidator`
- `EmailValidator`
- `RegexValidator`
- `MinValueValidator`
- `MaxValueValidator`

---

## 📌 Example: Built-in Validators in Form 
```python
def registeration_form():
    from django import forms
    from django.core import validators  
    
    class Registration(forms.Form):
        name = forms.CharField(
            validators=[
                validators.MaxLengthValidator(10),
                validators.MinLengthValidator(3)
            ]
        )
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)
```
This ensures:
* Name length is between 3 and 10 characters

## 2️⃣ Custom Validators

Custom validators are used when:

- Built-in validators are not enough
- Business logic is specific
- You want reusable validation logic

### 📌 Creating a Custom Validator
```python
from django import forms

def start_with_u(value):
    if value[0].lower() != 'u':
        raise forms.ValidationError(
            "Emails should start with 'u'"
        )
```

### 📌 Using Custom Validator in Form
```python
class Registration(forms.Form):
    name = forms.CharField(
        validators=[
            validators.MaxLengthValidator(10),
            validators.MinLengthValidator(3)
        ]
    )
    email = forms.EmailField(validators=[start_with_u])
    password = forms.CharField(widget=forms.PasswordInput)
```

### 📌 The email field now:
- Must start with letter **u**
- Otherwise throws validation error

# View Logic (Same as Previous)

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

            print('Name:', name)
            print('Email:', email)
            print('Password:', password)

            return HttpResponseRedirect('/student/success/')
    else:
        form = Registeration()

    return render(request, 'student/register.html', {'form': form})

def reg_success(request):
    return render(request, 'student/sucess.html')
```

# Validation Execution Flow (Important)

- User submits form
- `form.is_valid()` is called
- Built-in validators run
- Custom validators run
- Errors collected (if any)
- `cleaned_data` created (only if valid)

# Validators vs `clean_<field>()` vs `clean()`
| Feature | Validators | `clean_<field>()` | `clean()` |
|---------|--------------|------------------|----------|
| Scope | Single field | Single field | Multiple fields |
| Reusable | ✅ Yes | ❌ No | ❌ No |
| Access other fields | ❌ No | ❌ No | ✅ Yes |
| Runs automatically | ✅ Yes | ✅ Yes | ✅ Yes |

# When to Use What?
| Scenario | Best Choice |
|----------|--------------|
| Simple length or format rule | Built-in validator |
| Reusable custom rule | Custom validator |
| Field-specific logic | `clean_<field>()` |
| Cross-field validation | `clean()` |

# 🔹 Example Validation Results

| Input | Result |
| --- | --- |
| name = ab | ❌ Error (min length) |
| name = abcdefghijk | ❌ Error (max length) |
| email = test@gmail.com | ❌ Error (must start with u) |
| email = ujjwal@gmail.com | ✅ Valid |

# 🔹 Advantages of Validators

- Clean and reusable code
- Separation of validation logic
- Easy to test
- Works for forms and models
- Django-recommended approach

# ✅ Summary

- Django provides powerful built-in validators
- Custom validators handle business rules
- Validators run before `cleaned_data`
- Validation errors prevent form submission
- `form.is_valid()` controls the flow