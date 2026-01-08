# Chapter 12: Django Template Inheritance with Static Files

## 1. What is Template Inheritance with Static Files?

Django template inheritance allows us to create a base template that contains common HTML structure and then extend it in child templates.
When combined with static files (CSS/JS), it helps manage styles efficiently across multiple pages and apps.

This approach ensures:
- **Consistent layout**
- **Reusable design**
- **Controlled CSS loading per page**

## 2. Why Combine Template Inheritance with Static Files?

Without this approach:
- CSS may be duplicated across templates
- Hard to manage shared and page-specific styles
- Layout changes require updates in many files

With inheritance + static files:
- Base template handles structure
- Child templates decide which CSS to load
- Cleaner and scalable frontend architecture

## 3. Base Template (`base.html`)

The base template defines:
- Common HTML layout
- Navigation
- Template blocks for title, CSS, content, and footer

### Example: `base.html`
```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
    
    {% block corecss %}
    <link rel="stylesheet" href="{% static "app1/css/style.css" %}">
    {% endblock corecss %}
</head>ody>
    
    <ul>
        <li>Home</li>
        <li>Django</li>
        <li>Python</li>
    </ul>
    														   	   	   	   	   	   	   	   	   	   {% block content %}{% endblock content %}
dd     {% block footer %}
        this is a footer
    {% endblock footer %}
</body>
html>
```

**Explanation:**
- corecss block controls CSS loading.
- default CSS (app1) is provided by the base template.
- either blocks can be overridden by child templates.


## 4. Child Template with Additional CSS (django.html)

Child templates extend the base template and can:

- Override blocks
- Add their own CSS
- Extend base CSS using `block.super`

### Example: django.html
```django
{% extends "app1/base.html" %}
{% load static %}

{% block title %} Django {% endblock title %}

{% block corecss %}
{{ block.super }}
<link rel="stylesheet" href="{% static "app2/css/style.css" %}">
{% endblock corecss %}

{% block content %}
<h1>Django Page</h1>
{% endblock content %}

{% block footer %}
{{ block.super }} this is Django footer
{% endblock footer %}
```

## 5. What is `block.super`?

`block.super` is used to include the parent block’s content inside the child block.

**In this case:**
- Base CSS is loaded first
- Child CSS is loaded after
- Browser applies CSS using cascade rules

## 6. CSS Cascade Behavior (Important)

CSS is handled by the browser, not Django.

**Example behavior:**
- `body` background from base CSS remains
- `h1` color from child CSS overrides base CSS
- Last loaded CSS has higher priority
- This is normal and expected.

## 7. Alternative Approach: Page-Specific CSS Only
If you want only child CSS and no base CSS:

### `base.html`
```django
{% block corecss %}{% endblock corecss %}
```
### `child template`
```django
{% block corecss %}
<link rel="stylesheet" href="{% static "app2/css/style.css" %}">
{% endblock corecss %}
```


This completely disables base-level CSS

## 8. Static Files Folder Structure (Best Practice)

```
ch12/
├── app1/
│   ├── static/
│   │   └── app1/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── app1/
│   │       ├── base.html
│   │       └── home.html
│
├── app2/
│   ├── static/
│   │   └── app2/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── app2/
│   │       └── django.html
└── manage.py
```

**Using app-name folders avoids conflicts between static files.**

## 9. Common Mistakes to Avoid
- Loading CSS outside a block in `base.html`
- Expecting Django to remove inherited CSS automatically
- Misusing `block.super`
- Forgetting `{% load static %}`
- Hardcoding static file paths

## 10. Summary
- Template inheritance controls HTML, not CSS behavior.
- Static files must be loaded inside overridable blocks.
- `block.super` includes base styles intentionally.
- CSS cascade decides final appearance.
- Proper structure ensures clean and scalable projects.