# Chapter 15: Using Bootstrap in Django with django-bootstrap5

## 1. Introduction

In this chapter, we learned an alternative and cleaner method to integrate Bootstrap into a Django project using the `django-bootstrap5` package.

Instead of manually managing Bootstrap CSS and JS files in the static directory, this approach uses template tags provided by the package to load Bootstrap automatically.

## 2. Why Use django-bootstrap5?

Using `django-bootstrap5`:
- Removes the need to manually download Bootstrap files
- Automatically handles correct Bootstrap versions
- Reduces boilerplate HTML
- Keeps templates clean and readable
- Is widely used in real-world Django projects

This method is especially useful when working with forms, alerts, and messages.

## 3. Installing django-bootstrap5

Install the package using pip:
```bash
pip install django-bootstrap5
```

Add it to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'django_bootstrap5',
]
```

## 4. Loading Bootstrap Template Tags
To use Bootstrap template tags, load them in your template:
```django
template{% load django_bootstrap5 %}
```
This makes Bootstrap-related template tags available.

## 5. Base Template Using django-bootstrap5 (Example: base.html)
```html
document type html>
{% load static %}
{% load django_bootstrap5 %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <link rel="stylesheet" href="{% static "app1/css/style.css" %}">
</head>
body>
    <ul>
        <li>Home</li>
        <li>Django</li>
        <li>Python</li>
    </ul>
    {% bootstrap_messages %}

    {% block content %}{% endblock content %}

    {% block footer %}
    this is a footer
    {% endblock footer %}
/body>
/html>
```

## 6. Explanation of Bootstrap Template Tags

- `{% bootstrap_css %}`
  - Loads Bootstrap CSS automatically.

- `{% bootstrap_javascript %}`
  - Loads Bootstrap JavaScript bundle (including Popper).

- `{% bootstrap_messages %}`
  - Displays Django messages using Bootstrap alert styling.

> These tags replace manual `<link>` and `<script>` tags.

## 7. Comparing Bootstrap Integration Methods

### Method 1: Manual Static Files
- Bootstrap files stored in `static/`
- Requires manual updates
- More control over files

### Method 2: django-bootstrap5 (This Method)
- No static Bootstrap files needed
- Faster setup
- Cleaner templates
- Ideal for forms and messages

> Both methods are valid; choice depends on project needs.

## 8. Advantages of django-bootstrap5
- Simple and clean integration
- Automatic Bootstrap handling
- Less configuration
- Better readability of templates
- Commonly used in production projects

## 9. Common Mistakes to Avoid
- Forgetting to install django-bootstrap5
- Not adding it to `INSTALLED_APPS`
- Forgetting `{% load django_bootstrap5 %}`
- Mixing manual Bootstrap CSS with package tags unnecessarily 
 
## 10. Summary 

- django-bootstrap5 provides a clean way to use Bootstrap in Django.
- Bootstrap CSS and JS are loaded via template tags.
- No need to manage Bootstrap files manually.
- Ideal for rapid development and form-heavy applications.
- Industry-accepted and interview-safe approach.