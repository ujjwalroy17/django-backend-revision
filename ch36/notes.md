# 🍪 Django Cookies – Complete Notes (chXX)

## 📌 Topic: Working with Cookies in Django

## 📌 Goal: Understand how cookies work, how Django handles them, and where to use them safely.

---

### 1️⃣ What is a Cookie?

A cookie is a small piece of data that:
- Is stored in the user’s browser
- Exists as a key–value pair
- Is automatically sent with every HTTP request
- Helps maintain state in stateless HTTP

> **Cookies are client-side storage.**

---

### 2️⃣ Setting a Cookie in Django

Cookies are always set on the response object.

#### 🔹 Basic Cookie (Session Cookie)
```python
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('pay_id', 'ppp123')
    return response
```
* Stored in browser.
* Deleted when browser closes.
* No expiry set.

#### 🔹 Cookie with max_age
```python
esponse.set_cookie('pay_id', 'ppp123', max_age=3600)
```
* Expires after 3600 seconds (1 hour).
* Countdown-based expiry.

#### 🔹 Cookie with expires (Recommended)
```python
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie(
        'pay_id',
        'ppp123',
        expires=datetime.now(timezone.utc) + timedelta(days=2)
    )
    return response
```
- Absolute expiry time.
- Clear and predictable.
- Browser deletes cookie after given date.



#### Code Used to Set a Cookie
```python
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie(
        'pay_id',
        'ppp123',
        expires=datetime.now(timezone.utc) + timedelta(days=2)
    )
    return response
```

### 3️⃣ Reading a Cookie
### Direct Access (Unsafe ❌)
> pay_id = request.COOKIES['pay_id']
> 
> **Raises KeyError if cookie doesn’t exist**

### Safe Access (Recommended ✅)
> pay_id = request.COOKIES.get('pay_id')

### With Default Value
> pay_id = request.COOKIES.get('pay_id', 'default_pay_id123')

**Advantages:**
- Prevents error
- Useful when cookie may not exist

#### Code Used to Read a Cookie
```python
def getcookie(request):
    pay_id = request.COOKIES.get('pay_id', 'default_pay_id123')
    return render(request, 'student/getcookie.html', {'pay_id': pay_id})
```

### 4️⃣ Deleting a Cookie
```python
def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('pay_id')
    return response
```

**Outcome:**
- Browser removes the cookie
- Cookie is not sent in future requests

### 5️⃣ Signed Cookies (Secure Cookies)

#### 🔐 What is a Signed Cookie?

A signed cookie:

- Is tamper-proof
- Uses Django’s `SECRET_KEY`
- Raises an error if the user modifies the value

#### 🔹 Setting a Signed Cookie
```python
response.set_signed_cookie('token', 't123456', salt='tk')
```

#### 🔹 Getting a Signed Cookie
```python
token = request.get_signed_cookie('token', salt='tk')
```

#### 🔹 With Default Value
```python
token = request.get_signed_cookie(
    'token',
    default='guest_token123',
    salt='tk'
)
```

#### ✔ Benefits:
- Prevents crash if cookie is missing
- Prevents tampering

#### ✅ Code Used:
```python
def setsignedcookie(request):
    response = render(request, 'student/setsignedcookie.html')
    response.set_signed_cookie('token', 't123456', salt='tk')
    return response

def getsignedcookie(request):
    token = request.get_signed_cookie(
        'token',
        default="guest_token123",
        salt='tk'
    )
    return render(request, 'student/getsignedcookie.html', {'token': token})
```

### 6️⃣ Normal vs Signed Cookies

| Feature | Normal Cookie | Signed Cookie |
| --- | --- | --- |
| Editable by user | ✅ Yes | ❌ No |
| Tamper-proof | ❌ | ✅ |
| Uses SECRET_KEY | ❌ | ✅ |
| Security | Low | High |

### 7️⃣ Important Cookie Parameters

```python
response.set_cookie(
    key='pay_id',
    value='ppp123',
    max_age=None,
    expires=None,
    path='/',
    domain=None,
    secure=False,
    httponly=False,
    samesite=None
)
```

## 🔑 Meaning of Cookie Attributes
- **secure** → HTTPS only
- **httponly** → JavaScript cannot access the cookie
- **samesite** → Protects against CSRF attacks
- **path/domain** → Scope of the cookie (which URLs or domains it applies to)

### 8️⃣ Where Cookies Should NOT Be Used ❌
Never store:
- Passwords
- Authentication tokens
- Roles / permissions
- Sensitive user data
> 👉 Use Sessions or JWT instead.

### 9️⃣ Cookies vs Sessions (Quick Revision)
| Cookies | Sessions |
| --- | --- |
| Stored in browser | Stored on server |
| Less secure | More secure |
| User editable | Not editable |
| Small data | Large data |

> 📌 Django authentication uses sessions, not cookies directly.
### 🔄 Flow of Working of Cookies in Django (MOST IMPORTANT 🔥)

#### Step-by-Step Flow

1. **Client sends request**
2. **Django creates response**
3. **Cookie attached using `set_cookie()`**
4. **Response sent to browser**
5. **Browser stores cookie**
6. **Browser sends cookie automatically on next request**
7. **Django reads via `request.COOKIES`**

#### 🧠 Flow Diagram

```mermaid
flowchart TD
    Browser -->|Request| DjangoView
    DjangoView -->|set_cookie()| HTTPResponse[HTTP Response (Set-Cookie)]
    HTTPResponse -->|Stores cookie| Browser
    Browser -->|Next Request: sends Cookie header| DjangoView2[Django reads request.COOKIES]
```

### 🔟 Interview One-Liner 🎯

Django cookies store data on the client side, while signed cookies ensure integrity using Django’s `SECRET_KEY` to prevent tampering.