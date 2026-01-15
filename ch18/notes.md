# 📘 Retrieve Data from Database Table in Django (ch18)

## 📌 Topic Covered

Retrieving data from a database table using Django ORM and displaying it in templates.

## 🔹 Model Used
**models.py**
```python
from django.db import models

class Profile(models.Model):
    Name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)
```

### This model represents a database table where:
- Each field is a column
- Each object is a row

## 🔹 Retrieving All Records from Database

To retrieve all rows from a table, Django ORM provides the `.all()` method.

**views.py**
```python
from django.shortcuts import render
from student.models import Profile

def all_data(request):
    all_students = Profile.objects.all()
    return render(request, 'student/all.html', {'students': all_students})
```

### `.all()` returns a QuerySet containing all records.

## 🔹 Displaying All Records in Template
**all.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>All Student Data</title>
</head>
<body>
<h1>All Students Data:</h1>
{% if students %}
    <h2>Student List:</h2>
    <ul>
        {% for student in students %}
            <li>{{ student.Name }} - {{ student.email }} - {{ student.city }}</li>
        {% endfor %}
    </ul>
{% else %}
    <h2>No Data Found</h2>
{% endif %}
</body>
html>
```

## 📌 Uses:
- `{% for %}` loop to iterate records 
- `{% if %}` to check if data exists

## Retrieving a Single Record from Database

To retrieve a single row, Django ORM provides `.get()`.

### views.py
```python
def single_data(request):
    student = Profile.objects.get(pk=1)
    return render(request, 'student/single.html', {'student': student})
```

### Other ways to retrieve a single object:
- `Profile.objects.get(id=1)`
- `Profile.objects.get(Name='Aman')`

> **Note:** `.get()` returns one object, not a QuerySet.

## Displaying a Single Record in Template

### single.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Single Student Data</title>
</head>
<body>
<h1>Student Data:</h1>
{% if student %}
    <ul>
        <li>{{ student.Name }} - {{ student.email }} - {{ student.city }}</li>
    </ul>
{% else %}
    <h2>No Data Found</h2>
{% endif %}
</body>
</html>
```

#W URL Configuration

**urls.py**
```python
from django.urls import path
from student.views import all_data, single_data

urlpatterns = [
    path('all/', all_data, name='all_data'),
    path('single/', single_data, name='single_data'),
]
```

## 📌 URLs:
- `/student/all/` → Display all records
- `/student/single/` → Display a single record

## 🔹 Important Notes
- `.all()` retrieves multiple records.
- `.get()` retrieves exactly one record.
- `.get()` raises an error if:
  - No record is found.
  - More than one record is found.
- QuerySets are iterable in templates.
- Django templates use dot notation to access model fields.

## 🔹 Key ORM Methods Used
| Method | Purpose |
|---------|---------|
| `.all()` | Retrieve all records |
| `.get()` | Retrieve a single record |
| `pk` | Primary key shortcut |
| `id` | Default primary key |

## 🔹 One-Line Interview Notes
- **QuerySet:** A collection of database objects returned by Django ORM.
- `.all()`: Returns all rows from a database table.
- `.get()`: Returns a single row matching the condition.

## ✅ Summary
- Data is retrieved using Django ORM.
- Views fetch data from the database.
- Templates display data dynamically.
- URLs connect user requests to views.