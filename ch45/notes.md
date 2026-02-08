# Django ORM Manager Methods – Non‑QuerySet Operations 

## 📌 What We Studied Today (Non‑QuerySet ORM Methods)

* Fetching single objects (`get`, `first`, `last`, `latest`, `earliest`)
* Existence checks (`exists`, `count`)
* Creating objects (`create`, `get_or_create`)
* Updating objects (`update`, `update_or_create`)
* Bulk operations (`bulk_create`, `bulk_update`, `in_bulk`)
* Deleting records (`delete`)

These methods usually **return a model instance, tuple, integer, or dictionary** — not a QuerySet.

---

## 🧠 Important Concept: Manager vs QuerySet

* `Student.objects` → **Manager**
* Manager provides:

  * QuerySet-returning methods (`filter`, `exclude`, `all`)
  * **Non‑QuerySet shortcut methods** (today’s topic)

---

## 1️⃣ `get()` – Fetch a Single Object

```python
Student.objects.get(pk=1)
```

### Meaning

* Returns **exactly one object**
* Raises exception if:

  * No record found (`DoesNotExist`)
  * More than one record found (`MultipleObjectsReturned`)

### Real‑Life Use

* Fetch user by ID
* Fetch order by order ID

---

## 2️⃣ `first()` and `last()`

```python
Student.objects.first()
Student.objects.last()
```

### Meaning

* Returns first or last record
* Returns `None` if table is empty

### Ordered Variants

```python
Student.objects.order_by('name').first()
Student.objects.order_by('name').last()
```

### Real‑Life Use

* Show newest or oldest record

---

## 3️⃣ `latest()` and `earliest()`

```python
Student.objects.latest('pass_date')
Student.objects.earliest('pass_date')
```

### Meaning

* Fetch record based on **date or field ordering**
* Requires a field name

### Real‑Life Use

* Latest transaction
* Earliest registration

---

## 4️⃣ `exists()` – Check if Data Exists

```python
Student.objects.filter(pk=2).exists()
```

### Meaning

* Returns `True` or `False`
* Efficient (uses `SELECT 1`)

### Real‑Life Use

* Check if username already exists

---

## 5️⃣ `count()` – Count Records

```python
Student.objects.all().count()
```

### Meaning

* Returns number of rows
* Uses SQL `COUNT()`

### Real‑Life Use

* Total users
* Total orders

---

## 6️⃣ `create()` – Create & Save Object

```python
Student.objects.create(name='Sameer', roll=114, city='Bokaro', marks=60)
```

### Meaning

* Creates and saves object in **one step**

### Real‑Life Use

* Quick inserts

---

## 7️⃣ `get_or_create()`

```python
obj, created = Student.objects.get_or_create(name='Anisa', roll=115)
```

### Meaning

* Gets object if exists
* Otherwise creates new

### Returns

* `obj` → instance
* `created` → boolean

### Real‑Life Use

* Avoid duplicate users

---

## 8️⃣ `update()` – Bulk Update

```python
Student.objects.filter(id=4).update(name='Kabir', marks=80)
```

### Meaning

* Updates records **without calling save()**
* Returns number of updated rows

### Real‑Life Use

* Bulk status update

---

## 9️⃣ `update_or_create()`

```python
obj, created = Student.objects.update_or_create(
    id=10,
    defaults={'name':'Kohli', 'roll':156}
)
```

### Meaning

* Updates if exists
* Creates if not

### Real‑Life Use

* Sync external data

---

## 🔟 `bulk_create()` – Insert Multiple Objects

```python
Student.objects.bulk_create(objs)
```

### Meaning

* Inserts many objects in one query
* Very fast

⚠️ Does NOT call `save()` or signals

---

## 1️⃣1️⃣ `bulk_update()` – Update Multiple Objects

```python
Student.objects.bulk_update(all_student_data, ['city'])
```

### Meaning

* Updates many objects efficiently

⚠️ Does NOT call `save()` or signals

---

## 1️⃣2️⃣ `in_bulk()` – Fetch Multiple Objects by IDs

```python
Student.objects.in_bulk([1, 3])
```

### Meaning

* Returns dictionary: `{id: object}`

### Real‑Life Use

* Fetch multiple known IDs quickly

---

## 1️⃣3️⃣ `delete()` – Remove Records

```python
Student.objects.get(pk=2).delete()
Student.objects.filter(marks=60).delete()
Student.objects.all().delete()
```

### Meaning

* Deletes records
* Returns `(count, details)`

---

## ⚠️ Important Differences (Quick Table)

| Method            | Returns        | Raises Error |
| ----------------- | -------------- | ------------ |
| `get()`           | Object         | ✅ Yes        |
| `first()`         | Object / None  | ❌ No         |
| `latest()`        | Object         | ✅ Yes        |
| `create()`        | Object         | ❌ No         |
| `get_or_create()` | (Object, Bool) | ❌ No         |
| `update()`        | Integer        | ❌ No         |
| `bulk_create()`   | List           | ❌ No         |

---

## 🎯 Interview‑Ready Summary

> “Django ORM provides Manager methods that perform single‑object operations, bulk inserts, updates, and deletes. These methods often return model instances or simple values instead of QuerySets and are optimized for specific use cases.”

---

## 🧠 Key Takeaways (Fast Revision)

* These methods are part of **Manager**, not pure QuerySet chaining
* Used for **CRUD shortcuts and performance**
* Bulk methods skip signals
* Use carefully in real projects

---

✅ These notes complete your understanding of **Django ORM beyond QuerySets**
