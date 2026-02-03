# Django Caching – Complete README Notes

This document contains **clean, revision‑ready notes** for **Django Caching**, focused on **Per‑Site Caching**, cache backends, commands, and real‑life intuition. These notes are meant for **exam prep, interviews, and project revision**.

---

## 📌 What We Studied Today (Caching Topic)

* What caching is and why it is needed
* Django cache framework basics
* Per‑site caching using middleware
* Cache expiry (`CACHE_MIDDLEWARE_SECONDS`)
* Cache backends:

  * Database cache
  * File‑based cache
  * Local memory cache
* Cache table creation command
* How per‑site caching works internally (flow)

---

## 🧠 What is Caching?

**Caching** means storing **temporary copies of expensive data** so that future requests can be served **faster** without recomputing or reloading the same data again.

In Django:

* Cache data is **server‑side**
* Cache data is **temporary**
* Cache data can be safely regenerated

---

## 🎯 Why Caching is Needed (Real‑Life Analogy)

### Without cache:

A restaurant cooks the same dish from scratch every time → slow service.

### With cache:

Popular dishes are kept ready → faster service.

➡️ Django cache works the same way for web pages.

---

## 🔁 Per‑Site Caching (Whole Website Caching)

Per‑site caching means:

> Django caches the **entire HTTP response** of a page and serves it directly on future requests.

### Key Benefit

* View is **not executed**
* Database is **not hit**
* Page loads **very fast**

---

## 🔄 Flow: How Per‑Site Caching Works (IMPORTANT)

### First Request (Cache MISS)

1. Browser sends request to Django
2. `FetchFromCacheMiddleware` checks cache
3. Cache not found (MISS)
4. View executes
5. Database queries run
6. Template renders
7. Response is created
8. `UpdateCacheMiddleware` stores response in cache
9. Response sent to browser

---

### Second Request (Cache HIT – within expiry time)

1. Browser sends same request
2. `FetchFromCacheMiddleware` finds cached response
3. Cached response returned immediately
4. ❌ View not executed
5. ❌ Database not queried

---

### After Cache Expiry

* Cache entry expires
* Next request becomes a MISS
* View runs again
* Cache is refreshed

---

## ⏱ `CACHE_MIDDLEWARE_SECONDS = 30`

### Meaning

* Cached response lives for **30 seconds**
* After 30 seconds → cache expires automatically

### Real‑Life Example

News website:

* Headlines cached for 30 seconds
* Reduces server load
* Content still remains fresh

---

## 🧱 Cache Backends (Where Cache Data is Stored)

Django allows multiple cache storage options.

---

## 1️⃣ Database Cache

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'student_cache',
    }
}
```

### Meaning

* Cache data stored in **database table**
* Managed entirely by Django

### Required Command

```bash
python manage.py createcachetable student_cache
```

### Real‑Life Use

* Simple shared storage
* Learning purposes

⚠️ Not recommended for high‑traffic production apps

---

## 2️⃣ File‑Based Cache

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'student_cache',
    }
}
```

### Meaning

* Cache stored as **files on disk**
* Each cache entry → file

### Real‑Life Use

* Local development
* Debugging cache behavior

⚠️ Slower than memory‑based caching

---

## 3️⃣ Local Memory Cache (LocMemCache)

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'student_cache',
    }
}
```

### Meaning

* Cache stored in **RAM (process memory)**
* Fastest built‑in cache backend

### Important Characteristics

* Cache cleared on server restart
* Not shared across processes

### Real‑Life Use

* Development
* Single‑server testing

---

## ⚖️ Cache Backend Comparison

| Backend     | Storage  | Speed     | Persistence | Best For    |
| ----------- | -------- | --------- | ----------- | ----------- |
| LocMemCache | RAM      | Very Fast | ❌           | Development |
| File Cache  | Disk     | Medium    | ✅           | Learning    |
| DB Cache    | Database | Slow      | ✅           | Practice    |

---

## 🧠 Cache Key Generation (Internal Concept)

Django generates cache keys using:

* URL path
* Query parameters
* Headers

Example:

```
/products/?page=1
/products/?page=2
```

Cached separately.

---

## 🚫 What Should NOT Be Cached (Per‑Site)

* User dashboards
* Cart pages
* Profile pages
* Authenticated user data

Reason:

> Same cached response may be shown to multiple users

---

## 🎯 Interview‑Ready Explanation

> “Django per‑site caching stores full HTTP responses using cache middleware. Cached responses are served directly on subsequent requests, bypassing view execution and database access. Cache expiry is controlled using `CACHE_MIDDLEWARE_SECONDS`.”

---

## 🧠 Key Takeaways

* Cache improves performance, not correctness
* Cache stores temporary, regeneratable data
* Per‑site caching is middleware‑based
* Cache backend decides where data is stored
* Redis is used later for production‑grade caching

---

✅ These notes are **revision‑ready**, **project‑friendly**, and **interview‑safe**
