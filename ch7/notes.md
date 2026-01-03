# Chapter 6: Templates in Django

## 1. What are Templates in Django?

Templates in Django are used to define the presentation layer of a web application. They allow us to separate HTML (UI) from Python logic (views).

Django templates are mainly used to:
- Render HTML pages
- Display dynamic content
- Keep views clean and readable

## 2. Why Use Templates?

**Without templates:**
- HTML is written directly inside views
- Code becomes hard to read and maintain

**With templates:**
- Views handle logic
- Templates handle UI
- Better structure and scalability

## 3. Two Ways to Return HTML in Django Views

In Django, HTML can be returned in two ways:
1. Writing HTML directly inside views (not recommended)
2. Using Django templates with `render()` (recommended)

### Method 1: Writing HTML Directly Inside Views
**Description**
In this approach, HTML code is written directly inside the view and returned using `HttpResponse`.

**Example:**
```python
def learn_django(request):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hello Django</title>
        </head>
        <body>
            <h1>Hello Django from App1</h1>
        </body>
    </html>
    """
    return HttpResponse(html)
```
### Drawbacks of This Method:
- HTML and Python logic are mixed 
- Difficult to manage large HTML 
- Not reusable 
- Not suitable for real-world projects 
This method is useful only for learning or quick testing.

### Method 2: Using Templates with render() (Recommended)
**Description**

In this approach:
- HTML is written in a separate `.html` file.
- Views use Django’s `render()` function to load templates.

This is the standard and professional approach in Django.

## 4. Template Directory Structure

For app-level templates, Django follows this structure:

```
app1/
├── templates/
│   └── app1/
│       ├── django.html
│       └── drf.html
```

Using an `app-name` folder inside `templates` avoids name conflicts between apps.

## 5. Creating Templates

`django.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello Django</title>
</head>
<body>
    <h1>Hello Django 5.1 from App1</h1>
</body>
</html>
```

`drf.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello DRF</title>
</head>
<body>
    <h1>Hello DRF from App1</h1>
</body>
</html>
```

## 6. Rendering Templates from Views

views.py:
```python
from django.shortcuts import render

def learn_django(request):
    return render(request, 'app1/django.html')

def learn_drf(request):
    return render(request, 'app1/drf.html')
```
### How `render()` Works

- Loads the template
- Combines it with request data
- Returns an `HttpResponse` automatically

## 7. Advantages of Using Templates

- Clean separation of logic and UI
- Easier maintenance
- Reusable HTML files
- Scalable for large applications
- Industry-standard practice

## 8. Best Practices for Templates

- Always use templates instead of inline HTML
- Follow app-level template structure
- Keep views lightweight
- Avoid writing business logic inside templates

## 9. Summary

templates handle the presentation layer in Django.
HTML can be returned directly or via templates.
Writing HTML inside views is not recommended.
`render()` with templates is the preferred approach.
Proper template structure avoids conflicts and improves scalability.