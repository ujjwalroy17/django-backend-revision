# Chapter 13: Using Bootstrap with Django (Static Files & Template Inheritance)

## 1. Introduction

In this chapter, we learned how to integrate Bootstrap into a Django project using:

- Django static files
- Template inheritance
- Proper use of block tags for CSS and JavaScript

This approach allows us to use Bootstrap globally while still keeping templates clean and reusable.

## 2. Why Use Bootstrap in Django?

Bootstrap helps in:

- Creating responsive UI quickly
- Using ready-made components (buttons, navbars, forms, etc.)
- Maintaining consistency across pages

When combined with Django template inheritance:

- Bootstrap can be loaded once in a base template
- Child templates can reuse it without duplication

## 3. Static Files Structure for Bootstrap (App-Level)

Following Django best practices, Bootstrap files are kept inside the app’s static directory.

```
app1/
├── static/
│   └── app1/
│       ├── css/
│       │   ├── bootstrap.css
│       │   └── style.css
│       └── js/
│           └── bootstrap.js
├── templates/
│   └── app1/
│       ├── base.html
      	└── home.html"
``` 
Using the app name inside static avoids conflicts when multiple apps exist.

## 4. Loading Static Files in Templates
Before using any static file, Django requires loading the static template tag:
```django {% load static %}```
This enables the `{% static %}` tag to correctly resolve file paths.

## 5. Base Template with Bootstrap (`base.html`)
The base template defines:
- Common HTML layout 
- Bootstrap CSS and JS blocks 
- Custom CSS block 
- Content and footer blocks

Example: `base.html`
```django
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}{% endblock title %}</title>

    {% block bootstrap_css %}
    <link rel="stylesheet" href="{% static "app1/css/bootstrap.css" %}">
    {% endblock bootstrap_css %}

    {% block corecss %}
    <link rel="stylesheet" href="{% static "app1/css/style.css" %}">
    {% endblock corecss %}
</head>
<body>

    <ul>
        <li>Home</li>
        <li>Django</li>
        <li>Python</li>
    </ul>

    <!-- Bootstrap Buttons -->
    <button type="button" class="btn btn-primary">Primary</button>
    <button type="button" class="btn btn-secondary">Secondary</button>
    <button type="button" class="btn btn-success">Success</button>
    <button type="button" class="btn btn-danger">Danger</button>
    <button type="button" class="btn btn-warning">Warning</button>
    <button type="button" class="btn btn-info">Info</button>
    <button type="button" class="btn btn-light">Light</button>
    <button type="button" class="btn btn-dark">Dark</button>
    <button type="button" class="btn btn-link">Link</button>

    {% block content %}{% endblock content %}

    {% block footer %}
    this is a footer
    {% endblock footer %}

    {% block bootstrap_js %}
    <script src="{% static "app1/js/bootstrap.js" %}"></script>
    {% endblock bootstrap_js %}

</body>
</html>
```

# 6. Purpose of Each Block

- **title** → Page title
- **bootstrap_css** → Loads Bootstrap CSS
- **corecss** → Loads custom app CSS
- **content** → Page-specific content
- **footer** → Footer section
- **bootstrap_js** → Loads Bootstrap JavaScript

Blocks allow child templates to override or extend behavior when needed.

# 7. Advantages of This Approach

- Bootstrap loaded only once
- Clean separation of layout and content
- Reusable base template
- Easy maintenance
- Scalable for large Django projects

# 8. Common Mistakes to Avoid

- Using `{% block %}` without a name
- Loading JS files using `<link>` instead of `<script>`
- Forgetting `{% load static %}`
- Placing static files outside the `static/app_name/` directory
- Writing Bootstrap links directly in every template

# 9. Summary

- Bootstrap can be integrated using Django static files.
- Template inheritance helps reuse layout and assets.
- CSS and JS should be loaded inside named blocks.
- App-level static structure is the best practice.
- This setup is production-ready and interview-safe.