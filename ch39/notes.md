# Django Per-View Caching –

These notes cover **Per-View Caching (View-based & URL-based)** in Django. They are written for **quick future revision**, interviews, and practical project use.

---

## 📌 What is Per-View Caching?

**Per-view caching** means caching the response of **a specific view only**, instead of caching the entire website.

> Only selected views are cached, others work normally.

---

## 🧠 Why Per-View Caching is Needed

Real websites have:

* Some pages that are **heavy & slow** (course list, products)
* Some pages that are **dynamic** (profile, result, dashboard)

Per-view caching lets us:

* Cache **only expensive views**
* Keep dynamic views real-time

---

## 🔹 View-Based Caching (Decorator on View)

### Example

```python
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(30)
def course(request):
    return render(request, 'student/course.html')
```

### Meaning of `@cache_page(30)`

* Caches the **entire response of this view**
* Cache duration = **30 seconds**
* Stored using the configured cache backend

---

## 🔁 Flow: How View-Based Caching Works

### First Request (Cache MISS)

1. Request reaches `course` view
2. No cached response found
3. View executes
4. Template renders
5. Response stored in cache (30s)
6. Response sent to browser

### Second Request (Cache HIT)

1. Request reaches view
2. Cached response found
3. Response returned immediately
4. ❌ View not executed

---

## 🧩 Real-Life Example (View-Based)

### Online Course Website

* `/courses/` → cached (many users, same content)
* `/result/` → not cached (user-specific)

---

## 🔹 URL-Based Caching (Caching via urls.py)

### Example

```python
from django.views.decorators.cache import cache_page
from django.urls import path
from . import views

urlpatterns = [
    path('course/', cache_page(30)(views.course)),
]
```

### Meaning

* Cache is applied at **URL level**
* View code remains untouched
* Useful when you cannot modify view code

---

## 🧠 View-Based vs URL-Based Caching

| Feature       | View-Based     | URL-Based      |
| ------------- | -------------- | -------------- |
| Applied where | View function  | urls.py        |
| Cleaner for   | Small projects | Large projects |
| Modifies view | Yes            | No             |
| Common usage  | Very common    | Less common    |

---

## ⏱ Cache Timeout Behavior

```python
@cache_page(30)
```

* Cache valid for 30 seconds
* After expiry → cache invalidated
* Next request regenerates cache

---

## 🔑 Cache Key Generation

Django generates cache keys using:

* URL path
* Query parameters
* Headers

Example:

```
/course/?page=1
/course/?page=2
```

Cached separately.

---

## 🚫 When NOT to Use Per-View Caching

Do NOT cache:

* Result pages
* Profile pages
* Cart pages
* Authenticated dashboards

Reason:

> Data is user-specific and changes frequently

---

## ✅ When to Use Per-View Caching

Best for:

* Course listings
* Product listings
* Blog pages
* Public APIs

---

## 🎯 Interview-Ready Explanation

> “Per-view caching in Django allows caching the response of individual views using the `cache_page` decorator. Cached responses are served directly on subsequent requests, bypassing view execution and database access.”

---

## 🧠 Key Takeaways (Revision Fast)

* Per-view caching targets **specific views**
* Implemented using `@cache_page`
* Timeout controls freshness
* Safer than per-site caching
* Ideal for performance optimization

---

✅ These notes are optimized for **quick revision + interviews + real projects**
