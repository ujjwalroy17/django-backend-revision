# 📘 Django Forms – Field-wise & Form-wide Validation (ch22)

This module explains how Django validates form data using the Form API, covering:

- **Field-specific validation** using `clean_<fieldname>()`
- **Form-wide validation** using `clean()`
- **Difference between both approaches**
- **Error handling and flow of `is_valid()`**

## 🔹 What is Django Form Validation?

Django Form Validation ensures that:

- User input is correct
- Data follows business rules
- Invalid data is rejected before processing

Validation runs automatically when:

```python
form.is_valid()
```

## 1️⃣ Field-Specific Validation (`clean_<fieldname>()`)

Used when:
- Validation applies to one field only
- Example: minimum length of name, email format check, etc.

### 📌 Example: Validate name and email separately
```python
from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        name_value = self.cleaned_data['name']
        if len(name_value) < 4:
            raise forms.ValidationError(
                'Enter more than or equal to 4 characters'
            )
        return name_value

    def clean_email(self):
        email_value = self.cleaned_data['email']
        if len(email_value) < 20:
            raise forms.ValidationError(
                'Enter more than or equal to 20 characters'
            )
        return email_value
```

### 🔍 Key Points for `clean_<fieldname>()`
- Method name must be `clean_<fieldname>`
- Must raise `ValidationError`, not return it.
- Runs after individual field cleaning.
- Error automatically appears below that field.

## 2️⃣ Form-Wide Validation (`clean()`)

Used when:
- Validation depends on multiple fields.
- Rules involve cross-field checks.

### 📌 Example: Validate all fields at once 
```python
from django import forms

class Registeration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')

        if name_value and len(name_value) < 4:
            self.add_error(
                'name',
                'Enter more than or equal to 4 characters'
            )

        if email_value and len(email_value) < 10:
            self.add_error(
                'email',
                'Enter more than or equal to 10 characters'
            )

        return cleaned_data
```

### Key Points

- `clean()` validates all fields together.
- Use `self.add_error(field, message)` to attach errors.
- Do not raise `ValidationError` unless it's a non-field error.
- Runs after field-level cleaning.

## 3️⃣ View Logic (Same for Both Methods)
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

## 4️⃣ Template (Error Display is Automatic)
```html
<form method="post" novalidate>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>
```

## 📌 Notes
- `{{ form.as_p }}` automatically shows field errors.
- `novalidate` disables browser validation (Django still works).

## 🔁 Validation Execution Flow
1. `form = Registeration(request.POST)`
2. `form.is_valid()` is called.
3. Field validation (`clean_<fieldname>`) runs.
4. Form-wide validation (`clean`) runs.
5. If errors exist → `is_valid()` returns ❌ False.
6. If no errors → `is_valid()` returns ✅ True.

## 🧠 When to Use What?
| Use Case | Method |
| --- | --- |
| Single field rule | `clean_<field>()` |
Multiple fields rule| `clean()` |
Cross-field dependency| `clean()` |
Simple length check| Field argument (`min_length`) |
## Summary
does the following:
- `clean_<field>()` for individual fields,
- `clean()` for entire form,
- `raise ValidationError` for field-level errors,
- `add_error()` for form-level errors,
- `form.is_valid()` controls submission flow.
