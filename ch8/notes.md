# Chapter 7: Rendering Dynamic Templates in Django

## 1. What are Dynamic Templates?

Dynamic templates in Django are templates that display data sent from views at runtime.
Instead of showing fixed (static) content, dynamic templates use variables and context data provided by views.

This allows Django applications to:
- Display dynamic values
- Render user-specific content
- Show database-driven data

## 2. Role of render() in Dynamic Templates

The `render()` function is used to:
- Load an HTML template
- Pass data (context) from views to templates
- Return an `HttpResponse` automatically

**Basic syntax:**
```python
def render(request, template_name, context)
```
where:
- `request` → HTTP request object
- `template_name` → HTML file path
- `context` → dictionary containing dynamic data

## 3. Passing Data from Views to Templates

Data is passed from views to templates using a dictionary, commonly called *context*.

### Example: View with Dynamic Data:
```python
from django.shortcuts import render
def learn_django(request):
    data = {
        'course_name': 'Django'
    }
    return render(request, 'app1/django.html', data)
```
Here:
- `course_name` is the key
- `'Django'` is the value
This data becomes available inside the template.

## 4. Using Template Variables in HTML

django.html uses double curly braces to display variables.

### Example: django.html:
```html
<h1>Hello {{ course_name }} 5.1 from App1</h1>
```
### how it works:
- {{ course_name }} fetches value from context

- The value is rendered dynamically in the browser

## 5. Different Ways to Pass Context Data

**Type 1: Using a Separate Dictionary Variable**
```python
data = {'course_name': 'Django'}
return render(request, 'app1/django.html', context=data)
```

**Type 2: Passing Dictionary Directly**
```python
return render(request, 'app1/django.html', {'course_name': 'django'})
```

**Type 3: Passing Dictionary Without `context` Keyword**
```python
data = {'course_name': 'Django'}
return render(request, 'app1/django.html', data)
```

*All three approaches are valid in Django.*

---

## 6. Passing Multiple Values to Templates

Views can pass multiple variables at once.

### Example: View
```python
def learn_drf(request):
    seat = 10
    data = {
        'course_name': 'DRF',
        'version': 5,
        'sts': seat
    }
    return render(request, 'app1/drf.html', data)
```

### Example: drf.html
```html
<h1>Hello {{ course_name }} {{ version }} from App1</h1>
<h2>No of seats available: {{ sts }}</h2>
```

*Each variable is accessed using its key name inside `{{ }}`.*

---

## 7. Benefits of Dynamic Templates
- Clean separation of logic and UI
- Reusable templates
- Easy to update content
- Essential for database-driven applications
- Industry-standard Django practice 
 
--- 
 
## 8. Best Practices for Dynamic Templates 
- Always pass data using context dictionaries
- Keep logic inside views, not templates
- Use meaningful variable names
- Follow app-level template structure
- Avoid hardcoding dynamic values in HTML

--- 

## 9. Common Mistakes to Avoid 
- Forgetting to forget to pass context data.
- Typo mismatch between context key and template variable.
- Writting Python logic inside HTML.
- Using inline HTML inside views for dynamic content.

--- 

## 10. Summary 
- Dynamic templates render data at runtime.
- Views send data using context dictionaries.
- Templates access data using {{ variable_name }}.
- Renders() simplifies template rendering.
- Dynamic templates are essential for real-world Django applications.