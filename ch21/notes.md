# Django Model Admin – Display Database Data in Admin Panel (ch21)

## 📌 Topic Covered

- Customizing Django Admin Panel to display database data using `ModelAdmin` and `list_display`.

## 🔹 Why Customize Django Admin Display?

By default, the Django Admin Panel:

- Displays only one column (`__str__()` value)
- Does not show detailed fields in the list view

To display multiple fields (columns) from a database table, we use Django `ModelAdmin` customization.

## 🔹 Models Used

**models.py**
```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)

class Result(models.Model):
    subject = models.CharField(max_length=70)
    roll = models.IntegerField()
    marks = models.IntegerField()
```

## 📌 In this topic, __str__() is not required because we are displaying fields explicitly using `list_display`.

## 🔹 What is ModelAdmin?

`ModelAdmin` is a Django class that allows us to customize how a model is displayed and managed in the admin panel.

Using `ModelAdmin`, we can control:
- Which fields are displayed
- Filters, search, ordering
- Editable fields
- Admin layout

## 🔹 Displaying Multiple Fields Using `list_display`
### Syntax:
```python
def class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
def```

📌 `list_display` defines the columns shown in the admin list view.

# Admin Customization for Profile and Result Models

## Profile Model Customization
**File:** `admin.py`
```python
from django.contrib import admin
from student.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'email', 'city')

admin.site.register(Profile, ProfileAdmin)
```

### This displays:
- **ID**
- **Name**
- **Roll**
- **Email**
- **City**
as columns in the admin panel.

## Result Model Customization (Decorator Method)
### An alternative way to register models with admin customization:
```python
@admin.register(Result)
def result_admin():
    class ResultAdmin(admin.ModelAdmin):
        list_display = ('id', 'subject', 'marks')
```

### Benefits:
- Cleaner registration method.
- Same functionality as traditional registration.

## Two Ways to Register Models in Admin
1. **Normal Registration:**
admin.site.register(Profile, ProfileAdmin)
2. **Decorator-Based Registration:**
```python
@admin.register(Result)
def result_admin(): ... \
the same as above.
```

### Both methods work the same.

## Result in Django Admin Panel
After starting the server and logging into admin:
- Each model appears as a table.
- Fields appear as columns.
- Data is clearly visible and readable.

## Important Notes
- Field names in `list_display` must exist in the model.
- `id` is Django’s default primary key.
- `__str__()` method is optional when using `list_display`.
- Restart server after making admin changes.

## One-Line Interview Notes
### ModelAdmin:
- a Django class used to customize how models are displayed in the admin panel.
### list_display:
- defined by `list_display`, which specifies fields shown as columns.
