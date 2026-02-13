# 📘 One-to-One Relationship in Django Models


# 🔹 What is a One-to-One Relationship?

A **One-to-One relationship** means:

> One object of Model A is linked to exactly one object of Model B — and vice versa.

In Django, this is implemented using:

```python
models.OneToOneField()
```

It creates a **unique relationship** between two models.

---

# 🧠 Real-Life Understanding

Examples:

* One User → One Profile
* One Profile → One Page
* One Page → One Like record

Each object strictly maps to only one related object.

Most common use case:

👉 Extending Django's built-in `User` model

```python
from django.contrib.auth.models import User
```

---

# 🛠 Basic Syntax

```python
models.OneToOneField(to, on_delete, **options)
```

### Important Parameters

| Parameter          | Meaning                                   |
| ------------------ | ----------------------------------------- |
| `to`               | Model to connect with                     |
| `on_delete`        | What happens if related object is deleted |
| `limit_choices_to` | Restrict selectable objects (admin level) |

---

# 🧾 Cleaned & Correct Model Structure

## ✅ Profile Model (Correct Version)

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
```

### Meaning

* One `User` → One `Profile`
* If `User` is deleted → `Profile` is deleted (CASCADE)

---

# 🔹 Understanding `on_delete` Options

| Option       | Meaning                             |
| ------------ | ----------------------------------- |
| `CASCADE`    | Delete related object automatically |
| `PROTECT`    | Prevent deletion if related exists  |
| `DO_NOTHING` | Do nothing (may cause DB error)     |

### Example

```python
user = models.OneToOneField(User, on_delete=models.PROTECT)
```

If you try to delete User → Django will raise an error.

---

# 🔹 Using `limit_choices_to`

```python
user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True}
)
```

Meaning:

Only staff users can be selected in admin panel.

---

# 🧩 Page Model (Corrected)

Your earlier version connected `profile` field to `User`. That naming was confusing.

Better structure:

```python
class Page(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=255)
```

Meaning:

* One Profile → One Page
* One Page → One Profile

---

# 🧬 Like Model (Multi-Table Inheritance Case)

If you write:

```python
class Like(Page):
    likes = models.IntegerField()
```

Django automatically creates:

```
page_ptr = OneToOneField(Page)
```

internally.

⚠ Therefore, writing this again is redundant:

```python
page = models.OneToOneField(Page, on_delete=models.CASCADE)
```

Because inheritance already creates that OneToOne relation.

---

# 🗄 Database-Level Understanding

`OneToOneField` works like:

```
ForeignKey(unique=True)
```

It creates:

* A foreign key column
* With a UNIQUE constraint

Example table structure:

| id | user_id (unique) | name |

`user_id` must be unique.

---

# 🔄 Relationship Comparison

| Field Type        | Relationship Type |
| ----------------- | ----------------- |
| `ForeignKey`      | One-to-Many       |
| `ManyToManyField` | Many-to-Many      |
| `OneToOneField`   | One-to-One        |

---

# 🎯 When Should You Use OneToOne?

Use it when:

✅ Extending User model
✅ Splitting a large model into logical parts
✅ Strict 1:1 data mapping
✅ Multi-table inheritance

---

# 🏗 Example Real-World Structure

```
User
  ↓
Profile
  ↓
Page
  ↓
Like
```

Each layer strictly has only one related object.

---

# 💡 Accessing Related Data

Django automatically creates reverse relations.

```python
user.profile
profile.page
page.like
```

No extra configuration needed.

---

# 🚀 Interview-Ready Definition

> A OneToOneField in Django creates a unique relationship between two models where one instance of a model is linked to exactly one instance of another model. It is commonly used to extend the User model or implement multi-table inheritance.

---

# ⚠ Common Mistakes

❌ Using OneToOneField and inheritance together unnecessarily
❌ Forgetting to define `on_delete`
❌ Confusing `ForeignKey` with `OneToOneField`
❌ Naming fields incorrectly (causing confusion)

---

# 🧠 Final Concept Clarity

Think of `OneToOneField` as:

> ForeignKey + UNIQUE constraint + strict 1:1 semantic meaning

.
