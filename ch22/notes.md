# Django Form API – Create Django Form (ch22)

## 📌 What is Django Form API?

The Django Form API provides a high-level way to create HTML forms using Python classes. It handles:

- **Form field generation**
- **Data validation**
- **Rendering HTML automatically**
- **Security against invalid input**

Instead of writing raw HTML forms, Django forms allow us to define forms in Python.

## 📌 Types of Django Forms

- `forms.Form` → Used when data is not directly linked to a database table
- `forms.ModelForm` → Used when form is directly connected to a Django model

👉 In this chapter, we used `forms.Form`

## 📌 Creating Django Forms (`forms.py`)
```python
from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
```

## 🔹 Key Points

- Each form field maps to an HTML input field.
- Underscore (`first_name`) becomes space (`First name`) in the label.
- `EmailField` provides built-in email validation.

## 📌 Using Forms in Views (`views.py`)
```python
from django.shortcuts import render
from student.forms import Registration, Login  

def register(req):
    fm = Registration(field_order=['email', 'city'])
    return render(req, 'student/registration.html', {'form': fm})
def login(req):
    fm = Login(initial={
        'email': 'user@example.com',
        'password': '12345678'
    })
    return render(req, 'student/login.html', {'form': fm})
```
## 🔹concepts_used:
- field_order → controls order of fields

- initial → pre-fills form fields

- Form object is passed to template as context

## 📌 Rendering Forms in Template

### 🔹 Render Entire Form
{{ form }}

### 🔹 Other Rendering Options
- `{{ form.as_p }}`
- `{{ form.as_table }}`
- `{{ form.as_ul }}`

## 📌 Registration Template (registeration.html)
```html
<form action="">
    {{ form }}
    <input type="submit" value="submit">
</form>
```

## 📌 Login Template (login.html)
```html
<h1>Login :</h1>
{{ form }}
```

## 📌 Important Form Features Used
| Feature | Description |
|---------|--------------|
| forms.Form | Create form using Python |
| CharField | Text input |
| EmailField | Email validation |
| initial | Default values |
| field_order | Custom field sequence |
| `{{ form }}` | Auto HTML rendering |

## 📌 Advantages of Django Form API
- Automatic HTML generation
- Built-in validation
- Clean separation of logic and UI
- Secure and reusable
- Less boilerplate code