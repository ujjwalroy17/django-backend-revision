# 📘 Customize Django Form Error Fields (ch25)

## 📌 Topic Covered

Customizing Django form error messages and controlling how errors are displayed in templates.

## 🔹 Why Customize Form Error Messages?

By default, Django shows generic error messages like:

- This field is required.
- Enter a valid email address.

Customizing error messages helps:

- Improve user experience
- Show meaningful, user-friendly messages
- Match business or UI requirements

## 🔹 Customizing Error Messages in Django Forms

Django allows us to customize error messages using the `error_messages` argument in form fields.

## 🔹 Form Definition (`forms.py`)
```python
def registeration(forms.Form):
    name = forms.CharField(
        error_messages={'required': 'Name is required'}
    )
    email = forms.EmailField(
        error_messages={'required': 'Email is required'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required'}
    )
```

## 🔍 Key Points
- `error_messages` accepts a dictionary.
- `'required'` overrides the default required-field error.
- Works for both built-in and custom fields.

## 🔹 Common Error Message Keys |
p | Purpose |
rquired | Field is empty |
invalid | Invalid input format |
mmax_length | Value exceeds max length |
mmin_length | Value below min length |

# Displaying Errors in Template (Custom Rendering)

Instead of using `{{ form.as_p }}`, we manually loop through fields to fully control layout.

## Template (`register.html`)
```html
<form action="" method="post" novalidate>
    {{ form.non_field_errors }}
    {% csrf_token %}

    {% for field in form %}
        <div>
            {{ field.label_tag }}
            {{ field }}
            {{ field.errors }}
        </div>
    {% endfor %}
</form>
```

## Explanation
- `{{ field.errors }}` → displays field-specific errors
- `{{ form.non_field_errors }}` → displays form-wide errors
- `{% for field in form %}` → loops through each form field
- `novalidate` → disables browser validation (Django validation still works)

## Difference Between `field.errors` and `non_field_errors`
| Type | Description |
| --- | --- |
| `field.errors` | Errors related to a specific field |
| `non_field_errors` | Errors from `clean()` method |

## When to Use Manual Form Rendering?
Use manual rendering when:
- You want full control over form layout
- You need to style error messages
- You want to place errors beside fields
- You are building a custom UI

## Advantages of Custom Error Handling
- Better UX
- Cleaner UI
- Clear feedback to users
- Professional form behavior

## ✅ Summary
- Django allows custom error messages using `error_messages`
- Default messages can be overridden easily
- Manual rendering gives full control over error display
- `field.errors` and `non_field_errors` serve different purposes
- `novalidate` disables browser validation but keeps Django validation active