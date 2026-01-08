# Chapter 11: Django Template Inheritance

## 1. What is Template Inheritance in Django?

Template inheritance is a feature of Django Template Language (DTL) that allows us to:

- Define a base layout once
- Reuse it across multiple HTML pages
- Override only specific sections when needed

It helps in maintaining a consistent UI and avoids code duplication.

## 2. Why Use Template Inheritance?

**Without template inheritance:**
- HTML code is repeated across multiple files
- Hard to maintain navigation bars, headers, and footers

**With template inheritance:**
- Common layout is written once
- Child templates only define page-specific content
- Easy to update global UI changes

## 3. Base Template (`base.html`)

The base template defines the common structure of the website.

### Example: `base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
</head>
<body>

    <ul>
        <li>Home</li>
        <li>Django</li>
        <li>Python</li>
    </ul>

    {% block content %}{% endblock content %}

    {% block footer %}
        this is a footer
    {% endblock footer %}

</body>
</html>
```

### Explanation:
- **block title** → Page title section
- **block content** → Main content area
- **block footer** → Footer section with default content

## 4. Child Templates Using `{% extends %}`
Child templates inherit the structure of `base.html` using the `{% extends %}` tag.

⚠️ **Important rule:**

{% extends %} must be the first line of the template.

## 5. Home Page Template (`home.html`)
```django
{% extends "app1/base.html" %}

{% block title %} Home {% endblock title %}

{% block content %}
<h1>Home Page</h1>
{% endblock content %}

{% block footer %}
this is a home footer
{% endblock footer %}
```

**Explanation:**
- Overrides `title`, `content`, and `footer` blocks.
- Reuses navigation and layout from `base.html`.

---

## 6. Django Page Template (`django.html`)
```django
{% extends "app1/base.html" %}

{% block title %} Django {% endblock title %}

{% block content %}
<h1>Django Page</h1>
{% endblock content %}

{% block footer %}
{{ block.super }} this is Django footer
{% endblock footer %}
```

**What is `{{ block.super }}`?**
- Includes the parent block content.
- Allows extending instead of replacing content.

**Output example:**
the combined footer:
> this is a footer this is Django footer

---

## 7. Python Page Template (`python.html`)
```django
{% extends "app1/base.html" %}

{% block title %}
python
{% endblock title %}

{% block content %}
<h1>Python Page</h1>
{% endblock content %}
```

**Explanation:**
- Inherits footer from base template.
- Overrides only `title` and `content` blocks.

---

## 8. Template Folder Structure (Best Practice)

```plaintext
app1/
├── templates/
│   └── app1/
│       ├── base.html
│       ├── home.html
│       └── django.html
│
app2/
├── templates/
│   └── app2/
│       └── python.html

``` 
Using app-name folders avoids template name conflicts.

---

## 9. Rules of Template Inheritance

- `{% extends %}` must be the first tag
- Block names must match exactly
- Child templates can override any block
- `block.super` is optional but useful
- Parent template must define blocks

## 10. Common Mistakes to Avoid

- Extra spaces in `{% block %}` tags
- Mismatched block names
- Forgetting `{% extends %}`
- Writing full HTML structure in child templates

## 11. Summary

- Template inheritance avoids code duplication
- `base.html` defines common layout
- Child templates override blocks as needed
- `block.super` helps extend parent content
- Template inheritance is essential for scalable Django projects