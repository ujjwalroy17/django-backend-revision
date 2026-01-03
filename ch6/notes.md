# Chapter 5: URL Configuration in Django (URLs)

## 1. What are URLs in Django?

In Django, URLs define how incoming HTTP requests are mapped to views. The URL configuration system decides which view should handle a given request.

Django uses a file called `urls.py` to define these mappings.

## 2. Two Ways to Configure URLs in Django

Django provides two common approaches for handling URLs:

- Defining all URLs in the root (project-level) `urls.py`
- Defining app-level `urls.py` and including them in root URLs (recommended)

Both methods are valid, but they are used in different scenarios.

### Method 1: Defining All URLs in Root `urls.py`

#### Description

In this approach, all views from all apps are directly connected in the project’s main `urls.py` file.

This method is mostly used for:
- Learning
- Small projects
- Quick testing

#### Example: Root `urls.py`
```python
from django.contrib import admin
from django.urls import path
from app1.views import learn_django
from app2.views import myapp2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj/', learn_django),
    path('py/', learn_django, {'status': 'OK'}),
    path('app2/', myapp2),
]
```

#### Key Points (Method 1)
- All URL patterns are written in one file.
- Views are imported directly from apps.
- Easy to understand for beginners.
- Becomes hard to manage as the project grows.

#### Limitations of Method 1:
- Root `urls.py` becomes very large.
- Difficult to maintain in multi-app projects.
- Higher chance of naming conflicts.
- Not scalable for real-world applications.

### Method 2: App-Level URLs with include() (Best Practice)


#### Description

In this approach:

- Each app has its own `urls.py`
- The root `urls.py` includes app URLs using `include()`

This is the recommended and professional approach.

####  Step 1: Create `urls.py` Inside Each App

#### `app1/urls.py`
```python
from django.urls import path
from .views import learn_django

urlpatterns = [
    path('dj/', learn_django),
    path('py/', learn_django, {'status': 'OK'}),
]
```

#### `app2/urls.py`
```python
from django.urls import path
from .views import myapp2

urlpatterns = [
    path('app2/', myapp2),
]
```

#### Step 2: Include App URLs in Root `urls.py`

#### Project `urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),  # Include app1 URLs at root level
    path('', include('app2.urls')),  # Include app2 URLs at root level
]
```

#### How URL Resolution Works (Method 2)
1. Request comes to root `urls.py`
2. Django forwards request to app-level `urls.py`
3. Matching view is executed
4. Response is returned 
 
#### Advantages of Method 2 
- Clean and modular URL structure 
- Easy to scale and maintain 
- Each app controls its own URLs 
- Avoids clutter in root `urls.py` 
- Preferred in interviews and production projects 
 
## 3. Passing Extra Data Through URLs 
Django allows passing extra data to views via URL patterns.
Example:
```python
path('py/', learn_django, {'status': 'OK'}),
```
the data is available inside the view as a parameter.
 
## 4.best practices for URL configuration:
a. Use app-level urls.py for large projects.
b. Keep root urls.py minimal.
c. Use meaningful and readable URL paths.
d. Avoid hardcoding logic in URLs.
e. Use include() to maintain modularity.										# 5. Comparison Summary

| Aspect | Method 1 (Root Only) | Method 2 (Include) |
|---|---|---|
| **Complexity** | Simple | Slightly advanced |
| **Scalability** | Low | High |
| **Maintenance** | Difficult | Easy |
| **Recommended** | ❌ | ✅ |

## 6. Summary
- Django URLs map requests to views.
- URLs can be defined directly or via `include()`.
- Small projects can use root-only URLs.
- Real-world projects should use app-level URLs.
- `include()` is the industry-standard approach..