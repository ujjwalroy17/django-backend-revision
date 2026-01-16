# Register Models in Django Admin Panel (ch20)

## 📌 Topic Covered

Registering model classes in the Django Admin Panel to manage database records.

## 🔹 Why Register Models in Admin Panel?

- By default, models do not appear in the Django Admin Panel.
- To manage model data (add, update, delete records), we must explicitly register models with the admin site.

Registering models allows:
- Viewing database records
- Performing CRUD operations
- Managing application data via UI

## 🔹 Models Used
```python
# models.py
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.name  # return str(self.roll)  → alternative representation

class Result(models.Model):
    subject = models.CharField(max_length=70)
    marks = models.IntegerField()

    def __str__(self):
        return self.subject
```

## 📌 The `__str__()` Method 

defines how objects are displayed in the admin panel.

## 🔹 What is `__str__()` Used For?
- Controls how model instances appear in admin lists.
- Improves readability in dropdowns and foreign keys.

### Example:
def __str__(self):
    return self.name  

### Without `__str__()`:
*Profile object (1)*
*Profile object (2)*

### With `__str__()`:
*Aman*
*Rahul*


## Registering Models in Admin Panel

To make models visible in admin, register them in `admin.py`.

```python
### admin.py
from django.contrib import admin
from student.models import Profile, Result

admin.site.register(Profile)
admin.site.register(Result)
```

📌 **This tells Django:**

> "These models should appear in the Admin Panel."

## Accessing Registered Models

Start the server:

```bash
python manage.py runserver
```

Open the Admin Panel:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Login using superuser credentials.
You will see:
- Profile model
- Result model

## What You Can Do After Registration
- Add new Profile and Result records.
- Edit existing records.
- Delete records.
- View data stored in database.

## Important Notes
- Every model must be registered to appear in admin.
- `__str__()` is strongly recommended.
- Registration is done only once.
- Changes reflect immediately after server restart.

## One-Line Interview Notes
### Admin Registration:
Registering models allows them to be managed via Django’s admin interface.
### `__str__()` Method:
Defines the human-readable representation of a model object.