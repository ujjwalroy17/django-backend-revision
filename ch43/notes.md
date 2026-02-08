# Django Middleware –



## 📌 What We Studied Today (Middleware Topic)

* What middleware is in Django
* Why middleware is important
* Middleware request–response flow
* Function-based middleware
* Class-based middleware
* Multiple middleware execution order
* One-time initialization concept
* `process_view`, `process_exception`, `process_template_response`
* How middleware interacts with views

---

## 🧠 What is Middleware in Django?

**Middleware** is a layer that sits **between the request and the response** in Django.

> It allows you to process, modify, allow, or block requests and responses **globally**, before they reach the view and before they are returned to the client.

---

## 🎯 Core Definition (Interview-Ready)

> “Middleware in Django is a framework of hooks into Django’s request/response processing. It allows global processing of requests and responses.”

---

## 🔁 Middleware Flow (Request → Response Lifecycle)

```
Browser Request
      ↓
Middleware 1  (before view)
      ↓
Middleware 2  (before view)
      ↓
Middleware 3  (before view)
      ↓
View
      ↓
Middleware 3  (after view)
      ↑
Middleware 2  (after view)
      ↑
Middleware 1  (after view)
      ↑
Browser Response
```

Middleware works like **stack / onion layers**.

---

## 🏪 Real-Life Analogy

### 🏢 Office Building Security

* Entry gate checks ID → middleware before view
* Office work happens → view
* Exit gate logs exit → middleware after view

You don’t repeat security checks inside each office.

---

## ⚙️ Why Middleware is Important

Middleware is used for:

* Authentication (`request.user`)
* Sessions (`request.session`)
* Caching
* CSRF protection
* Security headers
* Logging & monitoring
* Error handling

Without middleware, this logic would be repeated in every view ❌

---

## 🧩 Types of Custom Middleware You Implemented

---

## 1️⃣ Function-Based Middleware

```python
def my_fun_middleware(get_response):
    print("One Time Initialization")

    def my_func(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response

    return my_func
```

### Explanation

* `get_response` → next middleware or view
* Outer function → runs **once** at server startup
* Inner function → runs on **every request**

### Flow

1. Django loads middleware → prints *One Time Initialization*
2. Request arrives → before-view code runs
3. View executes
4. After-view code runs

---

## 2️⃣ Short-Circuiting a View (Returning Response Early)

```python
# response = HttpResponse("Response from middleware")
# response = render(request, 'blog/uc.html')
```

### Meaning

* Middleware can **stop request from reaching view**
* Useful for:

  * Maintenance mode
  * Permission denial
  * Feature blocking

---

## 3️⃣ Class-Based Middleware

```python
class MyClMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response
```

### Explanation

* `__init__` → runs once
* `__call__` → runs per request
* Preferred for complex logic

---

## 4️⃣ Multiple Middleware Execution Order

```python
class MyMiddleware1:
class MyMiddleware2:
class MyMiddleware3:
```

### Execution Order

**Before View (top → bottom):**

* MyMiddleware1
* MyMiddleware2
* MyMiddleware3

**After View (bottom → top):**

* MyMiddleware3
* MyMiddleware2
* MyMiddleware1

This explains your printed output order.

---

## 🧠 One-Time Initialization Concept

```python
print("One Time Initialization")
```

* Runs when server starts
* Not per request
* Used for:

  * Setup
  * Configuration
  * Logging startup

---

## 🧩 Advanced Middleware Hooks (Conceptual)

### 1️⃣ `process_view`

```python
def process_view(request, view_func, view_args, view_kwargs):
```

* Runs **just before the view**
* Can return `HttpResponse` to skip view

---

### 2️⃣ `process_exception`

```python
def process_exception(self, request, exception):
```

* Runs when exception occurs in view
* Used for global error handling

Your example:

* Captures `ZeroDivisionError`
* Returns custom error response

---

### 3️⃣ `process_template_response`

```python
def process_template_response(self, request, response):
```

* Runs when view returns `TemplateResponse`
* Can modify context before rendering

Your use case:

* Inject extra context (`name = 'Sonam'`)

---

## 🔗 Middleware Configuration (`settings.py`)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middlewares.my_fun_middleware',
]
```

### Important Points

* Order matters
* Custom middleware usually comes **after Django core middleware**

---

## 🧠 How Middleware Interacts with Your Views

### Example: `home` view

```python
def home(request):
    print("I am home view")
    return render(request, 'blog/home.html')
```

Execution order:

1. Middleware before-view prints
2. View executes
3. Middleware after-view prints

---

### Example: Exception Handling (`my_math`)

```python
a = 10 / 0
```

* Exception raised
* `process_exception` middleware catches it
* Custom error response returned

---

### Example: TemplateResponse (`user_info`)

```python
return TemplateResponse(request, 'blog/user.html', context)
```

* Middleware modifies context
* Template rendered later

---

## ⚠️ Best Practices

✅ Use middleware for **cross-cutting concerns**

❌ Do NOT:

* Put business logic
* Perform heavy DB operations
* Overuse middleware

---

## 🧠 Key Takeaways (Fast Revision)

* Middleware wraps around views
* Runs on every request
* Order is extremely important
* Can block or modify requests/responses
* Essential for Django’s architecture

---

## 🎯 Final Interview Answer

> “Middleware in Django is a mechanism that processes requests and responses globally before and after views. It is used for authentication, sessions, caching, security, and other cross-cutting concerns.”

---

✅ These notes give you **complete clarity on Django Middleware**, both conceptually and practically.
