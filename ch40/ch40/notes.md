# Django Template Fragment Caching – 
---

## 📌 What is Template Fragment Caching?

**Template Fragment Caching** means caching **only a specific portion of a template**, instead of caching the whole page or the entire view.

> Useful when a page contains both **static/expensive** and **dynamic** content.

---

## 🧠 Why Template Fragment Caching is Needed

Many web pages contain:

* A **dynamic section** (user name, result, profile)
* A **static or heavy section** (course list, sidebar, recommendations)

Caching the entire page is risky, but caching **only the heavy part** is safe and efficient.

---

## 🔹 Syntax Used in Template Fragment Caching

```django
{% load cache %}

{% cache 30 mycourse %}
   ... template content ...
{% endcache mycourse %}
```

---

## 🧩 Explanation of Each Term (Line by Line)

### `{% load cache %}`

* Loads Django’s cache template tag library
* Required before using `{% cache %}`

---

### `{% cache 30 mycourse %}`

| Part       | Meaning                 |
| ---------- | ----------------------- |
| `cache`    | Cache template tag      |
| `30`       | Cache timeout (seconds) |
| `mycourse` | Cache key name          |

This tells Django:

> Cache this template block for 30 seconds using key `mycourse`.

---

### `{% endcache mycourse %}`

* Ends the cached block
* Must match the cache key name

---

## 🔁 Flow: How Template Fragment Caching Works

### First Request (Cache MISS)

1. Template rendering starts
2. Django checks cache for key `mycourse`
3. Cache not found
4. HTML inside block is rendered
5. Rendered HTML stored in cache (30s)
6. Full page sent to browser

---

### Second Request (Cache HIT)

1. Template rendering starts
2. Django finds cached fragment
3. Cached HTML fragment is inserted
4. ❌ Fragment not re-rendered
5. Page loads faster

---

### After Cache Expiry

* Cached fragment expires after 30s
* Next request regenerates fragment

---

## 🧩 Real-Life Example (Very Important)

### Online Learning Website

| Page Section       | Behavior               |
| ------------------ | ---------------------- |
| Header (user name) | Dynamic – NOT cached   |
| Course list        | Heavy – cached         |
| Footer             | Mostly static – cached |

This improves performance **without breaking personalization**.

---

## 🔐 Using Dynamic Cache Keys (Advanced Concept)

```django
{% cache 30 mycourse request.user.id %}
```

This creates **separate cache per user**.

Use case:

* User-specific recommendations
* Personalized dashboards

---

## ⚖️ Comparison with Other Caching Levels

| Caching Type              | Scope            |
| ------------------------- | ---------------- |
| Per-site caching          | Entire site      |
| Per-view caching          | Single view      |
| Template fragment caching | Part of template |

Template fragment caching is the **most precise and safest**.

---

## 🚫 When NOT to Use Fragment Caching

Do NOT cache fragments that:

* Show live data (marks, balance)
* Are highly user-specific
* Change every request

---

## 🎯 Interview-Ready Explanation

> “Template fragment caching allows caching specific parts of a Django template using the `{% cache %}` tag. It improves performance by avoiding repeated rendering of expensive template blocks while keeping dynamic content fresh.”

---

## 🧠 Key Takeaways (Quick Revision)

* Caches **only part of a page**
* Used inside templates
* Controlled using timeout
* Safer than per-site caching
* Very common in real projects

---

✅ These notes complete your **Django Caching trilogy**:

* Per-site caching
* Per-view caching
* Template fragment caching
