# Chapter 10: Using Static Files in Django (CSS & JavaScript)

## 1. What are Static Files in Django?

Static files are files that do not change dynamically during runtime.
They are used to improve the UI and interactivity of a web application.

**Common static files include:**
- CSS files (styling)
- JavaScript files (client-side logic)
- Images
- Fonts

Django provides a built-in system to manage static files efficiently.

## 2. Why Use Static Files?

**Without static files:**
- HTML pages look plain
- No styling or interactivity

**With static files:**
- Clean and responsive UI
- Better user experience
- Separation of frontend assets from backend logic

## 3. Static Files Directory Structure (App-Level)

Django recommends keeping static files inside each app.
Your structure follows the best practice:
```
app1/
├── static/
│   └── app1/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── scripts.js
├── templates/
│   └── app1/
│       └── django.html
```
Using the app name inside the static folder avoids conflicts when multiple apps use static files.

## 4. Enabling Static Files in Django

django enables static files by default.
Important settings in `settings.py`:
```python
STATIC_URL = '/static/'
```
during development, Django automatically serves static files when `DEBUG = True`.

## 5. Loading Static Files in Templates

Before using static files in any template, you must load the static template tag:
```django
t{% load static %}
```

This allows Django to locate static files correctly.

## 6. Linking CSS Files in Templates
**Example:** `django.html`

```html
<link rel="stylesheet" href="{% static "app1/css/style.css" %}">
```

**Explanation:**
- `{% static %}` generates the correct URL.
- `app1/css/style.css` matches the static folder structure.

## 7. Linking JavaScript Files in Templates
**Example:** `django.html`

```html
<script src="{% static "app1/js/scripts.js" %}"></script>
```

This loads the JavaScript file and enables client-side functionality.

## 8. Example Complete Template with Static Files
```html
document class="no-js" lang="en"
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static "app1/css/style.css" %}">
    <title>Django</title>
</head>
<body>
    <h1>Django with static files</h1>
    <form>
        <input type="button" value="Click me" onclick="disp()" />
    </form>
    <script src="{% static "app1/js/scripts.js" %}"></script>
</body>
document>
```

## 9. Key Points to Remember
- Always use `{% load static %}` in templates.
- Never hardcode static file paths.
- Follow app-level static folder structure.
- Use app name inside the static directory.
- Static files improve UI and interactivity.

## 10. Common Mistakes to Avoid
- Forgetting `{% load static %}`.
- Incorrect static file path.
- Missing app name inside the static folder.
- Writing inline CSS/JS instead of using static files.


# 11. Summary
- Static files handle CSS, JavaScript, and images in Django.
- Django provides `{% static %}` template tag to load assets.
- App-level static structure is recommended for organized asset management.
- Static files are essential for real-world Django applications.