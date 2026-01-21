# 📘 Dynamic URL in Django (ch30)

## 📌 Topic Covered

Creating and using dynamic URLs in Django to pass parameters from URL to views and templates.

## 🔹 What is a Dynamic URL in Django?

A Dynamic URL is a URL that contains variable parts instead of fixed values. These variable parts are captured and passed to the view function.

## 📌 Dynamic URLs help in:
- Creating user profile pages
- Displaying record-specific data
- Reducing hardcoded URLs
- Building scalable web applications

## 🔹 URL Converters in Django

Django provides path converters to capture dynamic values.

| Converter | Description |
| --- | --- |
| `int` | Integer value |
| `str` | String without `/` |
| `slug` | Slug format (a-z, 0-9, -) |
| `path` | Full path |

## 🔹 URL Configuration (`urls.py`)
```python
from django.urls import path
from student.views import Home, Profile

urlpatterns = [
    path('home/', Home, name="Home"),
    path(
        'template/<int:my_class>/<int:my_id>',Profile,
        name="Profile")
]
```
- 📌 This URL expects two dynamic parameters:
   - `my_class`
   - `my_id`

## 🔹 View Functions (`views.py`)
```python
from django.shortcuts import render

def Home(request):
    return render(request, 'student/home.html')

def Profile(request, my_class, my_id):
    student = {
        'class': my_class,
        'id': my_id
    }
    return render(request, 'student/profile.html', student)
```
- 📌 The captured URL values are received as function arguments.

## Home Template (`home.html`)

## Home Page

```html
<h1>Home Page</h1>
<ul>
    <li><a href="{% url 'Profile' 1 101 %}">Student 1</a></li>
    <li><a href="{% url 'Profile' 2 102 %}">Student 2</a></li>
    <li><a href="{% url 'Profile' 3 103 %}">Student 3</a></li>
    <li><a href="{% url 'Profile' 4 104 %}">Student 4</a></li>
    <li><a href="{% url 'Profile' 5 105 %}">Student 5</a></li>
</ul>
```

**📌 `{% url %}` Tag:**
- Dynamically generates URLs using:
  - URL name
- Parameters in correct order

---

## Profile Template (`profile.html`)

```html
<h1>Profile Page</h1>
<h2>Student {{ id }}</h2>
<h2>Class {{ class }}</h2>
```

**📌 Values passed from the URL are displayed dynamically.**

---

## How Dynamic URL Works (Flow)
- User clicks a dynamic link.
- Django matches URL pattern.
- Captured values are passed to the view.
- View processes data.
- Template renders dynamic content.

---

## Common Dynamic URL Variations
- `path('profile/<int:my_id>', Profile)`
- `path('profile/<str:title>', Profile)`
- `path('profile/<slug:title>', Profile)`

---

## Common Errors & Fixes
| Error | Reason |
| --- | --- |
| **404 Page Not Found** | Missing required URL parameter |
| **TypeError** | View signature mismatch |
eWrong URL generated | Incorrect `{% url %}` arguments |