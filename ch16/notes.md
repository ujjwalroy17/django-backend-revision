# Django Templates: Template Inside Template (Using `{% include %}` Tag)

## 1. What is `{% include %}` in Django?

The `{% include %}` tag allows you to embed one template inside another template.
It is mainly used to create reusable UI components such as:

- Navbar
- Hero section
- Footer
- Course list
- Cards / sections

This helps follow the DRY (Don’t Repeat Yourself) principle.

## 2. Why Use `{% include %}`?

- Improves code reusability
- Keeps templates clean and modular
- Makes UI easier to maintain
- Supports passing data dynamically
- Works well with template inheritance

## 3. Recommended Folder Structure
```text
app1/
├── templates/
│   └── app1/
│       ├── base.html
│       ├── home.html
│       └── components/
│           ├── nav.html
│           ├── hero.html
│           └── about.html


def app2/
├── templates/
│   └── app2/
│       ├── django.html
│       ├── python.html
│       └── components/
│           └── course.html
```
**Best Practice:**
Always place reusable templates inside a `components/` folder.

## 4. Base Template (`base.html`)
The base template defines the overall layout and includes reusable components.
```html
t{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}{% endblock title %}</title>
    <link rel="stylesheet" href="{% static 'app1/css/style.css' %}">
</head>
<body>
    {% include "app1/components/nav.html" %}
    {% block Hero %}
        {% include "app1/components/hero.html" %}
    {% endblock Hero %}
    {% block content %}{% endblock content %}
    {% block footer %}
        this is a footer
    {% endblock footer %}
</body>
<html>
```


## 5. Creating a Component (Example: `nav.html`)
```html
<nav>
    <ul>
        <li><a href="{% url 'home' %}">Home</a></li>
        <li><a href="{% url 'about' %}">About</a></li>
        <li><a href="{% url 'django' %}">Django</a></li>
        <li><a href="{% url 'python' %}">Python</a></li>
    </ul>
</nav>
```

## 6. Including a Template Without Data
**Example: `django.html`**
```django
{% extends "app1/base.html" %}

{% block title %} Django {% endblock title %}

{% block content %}
<h1>Django Page</h1>
{% include "app2/components/course.html" %}
{% endblock content %}
```

## 7. Passing Data to Included Templates (IMPORTANT)
Django allows passing data to included templates using the `with` keyword.

### View (`views.py`)
def django_learn(request):
    return render(request, 'app2/django.html', {'name': 'Django 5.X'})

### Child Template (`django.html`)
```django
{% extends "app1/base.html" %}

{% block title %} Django {% endblock title %}

{% block content %}
<h1>Django Page</h1>
{% include "app2/components/course.html" %}
{% endblock content %}
```

### Passing Data Using `with` (Another Method)
**File: `python.html`**
django html file:
```django
{% extends "app1/base.html" %}

{% block title %} Python {% endblock title %}

{% block content %}
h1>Python Page</h1>
{% include "app2/components/course.html" with name='Rust' %}
{% endblock content %}
django html component (`course.html`):
h2>Top Courses</h2>
<ul>
    <li>{{ name }}</li>
    l<li>Python</li>
    <li>JavaScript</li>
    <li>Java</li>
</ul>
```
# 8. Two Ways to Pass Data to Included Templates
| Method | Description |
|---------|--------------|
| From views.py | Data passed using `render()` |
| Using with | Data passed directly in `{% include %}` |

# 9. Difference Between `{% include %}` and `{% extends %}`
| `{% extends %}` | `{% include %}` |
|------------------|-------------------|
| Used for layout inheritance | Used for reusable components |
| Only one parent template | Multiple components allowed |
| Defines page structure | Injects partial UI |

# 10. Best Practices
- Use `{% extends %}` for layouts
- Use `{% include %}` for components
- Keep components logic-free
- Always namespace template paths
- Use `with` only for small, reusable data

# 11. Summary
- `{% include %}` allows template inside template
- Components make UI reusable and clean
- Data can be passed via `views.py` or `with`
- Works seamlessly with template inheritance