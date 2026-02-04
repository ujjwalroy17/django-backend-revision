# Django Low-Level Caching – Complete README Notes

These notes cover **Low-Level Caching in Django**, which is the **most preferred caching method in real-world applications**. This document is designed for **future revision, interviews, and practical backend understanding**.

---

## 📌 What We Studied Today (Low-Level Caching)

* What low-level caching is
* Difference between automatic caching and low-level caching
* Cache-as-a key–value store concept
* Common cache operations (`get`, `set`, `get_or_set`, etc.)
* Cache versioning
* Increment / decrement operations
* Cache clearing and expiry handling
* Real-life use cases of each cache method
* Internal working flow (cache hit & miss)

---

## 🧠 What is Low-Level Caching?

**Low-level caching** means manually storing and retrieving **Python data** in cache using keys.

> It gives developers full control over **what to cache, when to cache, and how long to cache**.

Unlike:

* Per-site caching → caches whole site
* Per-view caching → caches whole view
* Template fragment caching → caches HTML blocks

👉 **Low-level caching caches data, not pages.**

---

## 🔑 Core Idea: Cache as a Key–Value Store

```
KEY  →  VALUE  (with expiry time)
```

Just like a dictionary, but:

* Stored in memory / file / Redis
* Shared across requests
* Automatically expires

---

## 🔄 Flow: How Low-Level Caching Works

### First Request (CACHE MISS)

1. Request reaches view
2. Django checks cache for a key
3. Cache not found
4. Data is computed / fetched from DB
5. Data stored in cache with timeout
6. Response sent to client

---

### Second Request (CACHE HIT)

1. Request reaches view
2. Django finds cached value
3. Cached data returned
4. ❌ No DB query
5. ❌ No recomputation
6. Faster response

---

## 🔹 Common Cache Commands (Explained with Real-Life Examples)

---

### 1️⃣ `cache.set(key, value, timeout)`

```python
cache.set('movie', 'RRR', 60)
```

**Meaning**:

* Forcefully stores data in cache
* Overwrites existing value if present

**Real-life example**:

* Writing today’s special dish on a board (overwrite allowed)

---

### 2️⃣ `cache.get(key, default)`

```python
cache.get('movie', 'expired')
```

**Meaning**:

* Fetch cached value
* Returns default if not found

**Real-life example**:

* Checking notice board before asking staff

---

### 3️⃣ `cache.add(key, value, timeout)`

```python
cache.add('offer', '10% OFF', 60)
```

**Meaning**:

* Stores value **only if key does not exist**

**Real-life example**:

* Posting a notice only if it’s not already posted

---

### 4️⃣ ⭐ `cache.get_or_set(key, value, timeout)` (MOST USED)

```python
cache.get_or_set('movie', 'The One', 60)
```

**Meaning**:

* Gets cached value if exists
* Otherwise sets and returns value

**Internal logic**:

```python
if not cache.get(key):
    cache.set(key, value)
```

**Real-life example**:

* If food is ready → serve
* Else → cook and serve

---

### 5️⃣ `cache.set_many(dict, timeout)`

```python
cache.set_many({'name':'Sonam', 'roll':101}, 30)
```

**Meaning**:

* Stores multiple values in one call

**Real-life example**:

* Uploading multiple products at once

---

### 6️⃣ `cache.get_many(keys)`

```python
cache.get_many(['name', 'roll'])
```

**Meaning**:

* Retrieves multiple cached values

**Real-life example**:

* Asking for multiple items in one request

---

### 7️⃣ `cache.delete(key)`

```python
cache.delete('movie')
```

**Meaning**:

* Deletes a specific cache entry

**Real-life example**:

* Removing outdated notice from board

---

### 8️⃣ `cache.delete_many(keys)`

```python
cache.delete_many(['movie', 'roll'])
```

**Meaning**:

* Deletes multiple cache entries

---

### 9️⃣ `cache.clear()` 🚨

```python
cache.clear()
```

**Meaning**:

* Clears entire cache

**Real-life example**:

* Cleaning entire notice board

---

### 🔟 `cache.touch(key, timeout)`

```python
cache.touch('movie', 120)
```

**Meaning**:

* Extends expiry time without changing value

**Real-life example**:

* Renewing expiry date of poster

---

### 1️⃣1️⃣ `cache.incr(key, delta)`

```python
cache.incr('views', delta=1)
```

**Meaning**:

* Atomically increments numeric value

**Real-life example**:

* Visitor counter

---

### 1️⃣2️⃣ `cache.decr(key, delta)`

**Meaning**:

* Decreases numeric value atomically

---

### 1️⃣3️⃣ `cache.close()`

```python
cache.close()
```

**Meaning**:

* Closes cache connection
* Used in cleanup or scripts

---

## 🧠 Cache Versioning (Advanced Concept)

```python
cache.get_or_set('movie', 'Harry', 60, version=2)
```

Creates:

```
movie:v1 → The One
movie:v2 → Harry
```

**Real-life use**:

* API versioning
* Feature rollout
* A/B testing

---

## 🎯 Why Low-Level Caching is Most Preferred

* Fine-grained control
* Safe for dynamic applications
* Works with APIs
* Scales with Redis
* Production-friendly

---

## 🎤 Interview-Ready Explanation

> “Low-level caching allows manual caching of Python objects using Django’s cache framework. It is widely used to optimize database queries, expensive computations, and frequently accessed data, especially with Redis as backend.”

---

## 🧠 Key Takeaways (Quick Revision)

* Low-level caching caches **data**, not pages
* Provides maximum control
* `get_or_set()` is most commonly used
* Atomic operations support counters
* Redis is used in production

---

✅ These notes complete your **Django Caching Journey**:

* Per-site caching
* Per-view caching
* Template fragment caching
* ⭐ Low-level caching

---

## 🔍 Difference Between All Django Caching Methods (Complete Comparison)

This section compares **all caching methods you studied** so you can revise quickly and choose the right one in real projects.

---

### 📊 Caching Methods Comparison Table

| Caching Method                | What is Cached                         | Level of Control | Typical Usage               | Risk Level | Preferred In       |
| ----------------------------- | -------------------------------------- | ---------------- | --------------------------- | ---------- | ------------------ |
| **Per-Site Caching**          | Entire HTTP response (whole site/page) | ❌ Very Low       | Fully static websites       | 🔴 High    | Rare cases only    |
| **Per-View Caching**          | Entire response of one view            | ⚠️ Medium        | Public pages (blogs, lists) | 🟡 Medium  | Some real projects |
| **Template Fragment Caching** | Part of a template (HTML block)        | ✅ High           | Sidebar, footer, lists      | 🟢 Low     | Very common        |
| **Low-Level Caching** ⭐       | Python data (querysets, values)        | ✅✅ Very High     | APIs, DB optimization       | 🟢 Lowest  | MOST preferred     |

---

## 🧠 Conceptual Difference (Easy to Remember)

* **Per-site caching** → Cache everything
* **Per-view caching** → Cache one page
* **Template fragment caching** → Cache part of page
* **Low-level caching** → Cache only data ⭐

---

## 🏪 Real-Life Analogy Comparison

| Django Cache | Real-Life Example                         |
| ------------ | ----------------------------------------- |
| Per-site     | Serving the same meal to every customer ❌ |
| Per-view     | Preparing one popular dish in advance     |
| Fragment     | Pre-cut vegetables for cooking            |
| Low-level    | Keeping ingredients ready ⭐               |

---

## 🚀 Which One is MOST Preferred (Final Verdict)

> **Low-level caching is the most preferred caching method** because it provides fine-grained control, is safe for dynamic applications, and works perfectly with Redis in production.

In real projects:

* HTML optimization → Fragment caching
* API / DB optimization → Low-level caching

---

## 🎤 Interview-Ready One-Liner

> “Django provides multiple caching levels, but low-level caching is most preferred in production because it allows developers to cache only expensive data with full control and minimal risk.”

---

## 🧠 Final Revision Rule (Golden Rule)

```
Static page      → Per-view cache
Partial HTML     → Fragment cache
Dynamic data/API → Low-level cache ⭐
```

---

✅ This comparison completes your **Django Caching Master Notes** and makes the README fully revision + interview ready.
