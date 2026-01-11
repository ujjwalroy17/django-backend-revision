# Chapter 14: Using URL Template Tag in Django (`{% url %}`)

## 1. Introduction

In this chapter, we learned how to create navigation links in Django templates and why using the `{% url %}` template tag is the recommended and best practice instead of hardcoding URLs.

Django provides the `{% url %}` tag to dynamically generate URLs based on URL names, making applications more maintainable and scalable.

## 2. Problem with Hardcoded URLs

Hardcoded URLs are written directly as paths in templates.

**Example (Not Recommended)**
```html
<nav>
    <ul>
        <li><a href="/app1/">Home</a></li>
        <li><a href="/app1/about">About</a></li>
        <li><a href="/app2/dj">Django</a></li>
        <li><a href="/app2/py">Python</a></li>
    </ul>
</nav>
```

### Issues with Hardcoded URLs:
- If URL patterns change, templates must be updated manually
- Difficult to maintain in large projects
- Error-prone and not scalable
- Breaks DRY (Don’t Repeat Yourself) principle

## 3. Recommended Approach: `{% url %}` Template Tag

Django provides the `{% url %}` template tag to generate URLs dynamically using URL names defined in `urls.py`.

This approach ensures:
- Loose coupling between templates and URL structure
- Automatic updates if URLs change
- Cleaner and safer code

## 4. Using `{% url %}` in Templates

**Example (Recommended)**
```html
<nav>
    <ul>
        <li><a href="{% url "home" %}">Home</a></li>
        <li><a href="{% url "about" %}">About</a></li>
        <li><a href="{% url "django" %}">Django</a></li>
        <li><a href="{% url "python" %}">Python</a></li>
    </ul>
</nav>
```
Here:
- "home", "about", "django", "python" are URL names.
- Django resolves them to correct paths automatically.

## 5. Defining URL Names in `urls.py`

To use `{% url %}`, URL patterns must have a `name` attribute.

### Example: `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dj/', views.django_page, name='django'),
    path('py/', views.python_page, name='python'),
]
```

## 6. Why `{% url %}` is Recommended
- Decouples templates from URL paths
- Prevents broken links
- Improves maintainability
- Supports refactoring easily
- Industry-standard Django practice

## 7. `{% comment %}` Tag Usage
Django also provides the `{% comment %}` tag to write template-level comments.

### Example:
```django
{% comment %} Recommended {% endcomment %}
```
This comment:
- Is ignored during rendering
- Does not appear in HTML source
- Useful for documentation inside templates

## 8. Complete Example: Base Template with Navigation
```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
    <link rel="stylesheet" href="{% static "app1/css/style.css" %}">
</head>
<body>

    <!-- Hardcoded URLs (Not Recommended) -->
    <nav>
        <ul>
            <li><a href="/app1/">Home</a></li>
            <li><a href="/app1/about">About</a></li>
            <li><a href="/app2/dj">Django</a></li>
            <li><a href="/app2/py">Python</a></li>
        </ul>
    </nav>

    <hr>

    <!-- Recommended Django URL Template Tag -->
    <nav>
        <ul>
            <li><a href="{% url "home" %}">Home</a></li>
            <li><a href="{% url "about" %}">About</a></li>
            <li><a href="{% url "django" %}">Django</a></li>
            <li><a href="{% url "python" %}">Python</a></li>
        </ul>
    </nav>

    {% block content %}{% endblock content %}
    {% block footer %}this is a footer{% endblock footer %}

</body>
</html>
```

## 9. Common Mistakes to Avoid

- Forgetting to define `name` in `urls.py`
- Using hardcoded URLs in templates
- Typos in URL names
- Mixing hardcoded paths with `{% url %}`

## 10. Summary

- Hardcoded URLs are not scalable
- `{% url %}` template tag is the recommended approach
- URL names must be defined in `urls.py`
- `{% url %}` improves maintainability and safety
- Essential concept for real-world Django projects