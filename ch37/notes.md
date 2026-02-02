# Django Sessions – 
---

## 📌 What We Studied Today (Session Topic)

* What Django sessions are and why they are used
* How to **set, get, delete, flush** session data
* Session expiry handling
* Built-in session methods in views and templates
* Clearing expired sessions
* Test cookies (to check if browser supports cookies)
* Important session-related settings
* Complete **flow of how Django sessions work**

---

## 🧠 What is a Django Session?

A **session** is a way to store user-specific data on the **server-side** while keeping only a **session ID** in the browser cookie.

Django session data is stored in:

* Database (default)
* Cache
* File system
* Signed cookies (optional)

---

## 🔁 Session Working Flow (IMPORTANT)

### Step-by-step Session Flow

1. User sends a request to Django
2. Django checks for a **session ID** in browser cookies
3. If session ID exists:

   * Django fetches session data from session storage
4. If session ID does NOT exist:

   * Django creates a new session
   * Generates a new session ID
5. Session data is accessed or modified in views
6. Response is sent back to browser
7. Browser stores session ID in cookies

👉 **Only session ID is stored in browser, actual data stays on server**

---

## 🧪 Setting Session Data

```python
request.session['fname'] = 'Aman'
request.session['lname'] = 'Roy'
```

* Creates session if it does not exist
* Stores data as key-value pairs

---

## 📖 Getting Session Data

```python
first_name = request.session.get('fname')
last_name = request.session.get('lname')
```

✔ Safer than `request.session['key']`
✔ Prevents `KeyError`

Default value:

```python
request.session.get('fname', 'Guest')
```

---

## ❌ Deleting a Specific Session Key

```python
del request.session['lname']
```

* Removes **only one key**
* Session ID remains unchanged

Use case:

* Remove OTP
* Clear temporary values

---

## 🚨 Flushing Session (Logout / Security)

```python
request.session.flush()
```

* Deletes all session data
* Deletes session from database
* Generates **new session ID**

Use case:

* Logout
* Security-sensitive actions

---

## ⏳ Session Expiry

### Set Expiry in Seconds

```python
request.session.set_expiry(10)
```

### Expire When Browser Closes

```python
request.session.set_expiry(0)
```

---

## 🛠 Session Methods Used in Views

### Access Keys & Items

```python
request.session.keys()
request.session.items()
```

### Set Default Value

```python
request.session.setdefault('age', 31)
```

### Session Cookie Age

```python
request.session.get_session_cookie_age()
```

### Expiry Information

```python
request.session.get_expiry_age()
request.session.get_expiry_date()
request.session.get_expire_at_browser_close()
```

---

## 🧹 Clear Expired Sessions

```python
request.session.clear_expired()
```

* Deletes only **expired sessions**
* Does NOT affect current user session

Normally executed via:

```bash
python manage.py clearsessions
```

---

## 🧩 Session Data in Templates

You can access session data directly in templates:

```django
{{ request.session.fname }}
```

Or loop:

```django
{% for key, value in request.session.items %}
  {{ key }} : {{ value }}
{% endfor %}
```

---

## 🍪 Test Cookies

Used to check whether browser supports cookies.

### Set Test Cookie

```python
request.session.set_test_cookie()
```

### Check Test Cookie

```python
request.session.test_cookie_worked()
```

### Delete Test Cookie

```python
request.session.delete_test_cookie()
```

---

## ⚙️ Session Settings Used

```python
SESSION_COOKIE_AGE = 400
SESSION_COOKIE_NAME = 'sessionname'
```

* `SESSION_COOKIE_AGE`: Session lifetime (seconds)
* `SESSION_COOKIE_NAME`: Custom cookie name

---

## 🔥 Difference Summary (Interview Ready)

| Action               | Effect                        |
| -------------------- | ----------------------------- |
| `del session['key']` | Removes one key               |
| `session.flush()`    | Clears all data + new session |
| `clear_expired()`    | Removes expired sessions only |

---

## 🧠 Key Takeaways

* Sessions store data server-side
* Browser stores only session ID
* `flush()` is best for logout
* Use `.get()` to avoid errors
* Sessions improve security and personalization

---

✅ **This README can be used directly for revision, interviews, and project documentation**
