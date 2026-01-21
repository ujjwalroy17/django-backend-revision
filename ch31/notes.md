# Django Messages Framework (Flash Messages) (ch29)

## 📌 Topic Covered

Using Django Messages Framework to display one-time notification messages (success, info, warning, error, debug) to users.

## 🔹 What is Django Messages Framework?

The Django Messages Framework allows you to store messages temporarily and display them to users after an action such as:

- Form submission
- Registration
- Login / Logout
- Errors or warnings

📌 These messages are also called flash messages because they appear once and disappear automatically.

## 🔹 Why Use Django Messages?

- Provides user feedback
- Improves user experience
- Avoids hardcoding messages in templates
- Works well with redirects
- Built-in and secure

## 🔹 Message Levels in Django

django provides five message levels:
| Level | Purpose |
|---|---|
| DEBUG | Debugging messages |
| INFO | Informational messages |
| SUCCESS | Successful operations |
| WARNING | Warning messages |
| ERROR | Error messages |

## 🔹 Adding Messages in Views (`views.py`)
```python
def Home(request):
    from django.contrib import messages  
    # Add different types of messages 
    messages.add_message(request, messages.SUCCESS, 'Your account has been created')
    messages.add_message(request, messages.INFO, 'This is info')
    messages.add_message(request, messages.WARNING, 'This is warning')
    messages.add_message(request, messages.ERROR, 'This is error')
    messages.add_message(request, messages.DEBUG, 'This is Debug')
  
    # Get current message level 
    print(messages.get_level(request))
    # Set message level to DEBUG 
    messages.set_level(request, messages.DEBUG)
    # Add a debug message 
    messages.add_message(request, messages.DEBUG, 'This is Debug')
    # Verify the level set 
    print(messages.get_level(request))
  
    return render(request, 'student/home.html')
```
# Shortcut Methods for Messages

Instead of `add_message()`, Django provides shortcuts:

- `messages.success(request, 'Success message')`
- `messages.info(request, 'Info message')`
- `messages.warning(request, 'Warning message')`
- `messages.error(request, 'Error message')`
- `messages.debug(request, 'Debug message')`

## Displaying Messages in Template (`home.html`)
```django
{% if messages %}
    {% for message in messages %}
        <span class="{{ message.tags }}">{{ message }}</span>
    {% endfor %}
{% endif %}
```

## Explanation

- `messages` → iterable message storage
- `message.tags` → CSS class based on message level
- `message` → actual text message

## Using Messages After Form Submission
**views.py**
```python
def registeration(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registration Success!!')
    else:
        fm = StudentRegisteration()

    return render(request, 'student/registeration.html', {'form': fm})
```

**Message is displayed after successful registration.**

## Registration Template (registeration.html)

```html
<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>

{% if messages %}
    {% for message in messages %}
        <span class="{{ message.tags }}">{{ message }}</span>
    {% endfor %}
{% endif %}
```

## Model Used (models.py)

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
```

## ModelForm Used (forms.py)

```python
from django import forms
from student.models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
```

## Message Storage Behavior
- Messages are stored in session or cookies.
- Automatically removed after being displayed.
- Persist across redirects.

## Common Use Cases
- Registration success message.
- Login failure message.
- Form validation feedback.
- Warning alerts.
- Debugging during development.