# Django Model Inheritance – Abstract, Multi-Table & Proxy Models


# 🧠 1️⃣ What is Model Inheritance in Django?

Model inheritance allows one Django model to inherit fields and behavior from another model.

It helps in:

* Code reusability
* Avoiding duplication
* Clean database design
* Structuring large applications

Django supports three types:

1. Abstract Base Class
2. Multi-Table Inheritance
3. Proxy Model

---

# 🔹 2️⃣ Abstract Model Inheritance

## 📌 Definition

An **abstract model** is a base model that provides fields to child models but does NOT create its own database table.

It is only used for sharing common fields and logic.

---

## ✅ Your Example

```python
class BaseModel(models.Model):
  name = models.CharField(max_length=255)
  age = models.IntegerField()
  join_date = models.DateField()

  class Meta:
    abstract = True
```

This means:

* No table will be created for `BaseModel`
* Its fields will be copied into child models

---

## Child Models

```python
class Student(BaseModel):
  fees = models.IntegerField()
  join_date = None
```

Here:

* `Student` inherits `name` and `age`
* `join_date` is removed by setting it to `None`
* Adds new field `fees`

---

```python
class Teacher(BaseModel):
  salary = models.IntegerField()
```

```python
class Contractor(BaseModel):
  payment = models.IntegerField()
  join_date = models.DateTimeField()
```

In `Contractor`:

* `join_date` is overridden with a new type (`DateTimeField`)

---

## 🗄 What Happens in Database?

Tables created:

* student → name, age, fees
* teacher → name, age, join_date, salary
* contractor → name, age, join_date (DateTime), payment

❌ No basemodel table is created.

---

## 🏪 Real-Life Example

Think of `BaseModel` as:

"Common properties every employee has"

But there is no separate "BaseModel" person in real life.

---

## ✅ When to Use Abstract Models

* For reusable fields like:

  * created_at
  * updated_at
  * is_active
* When parent is NOT a real database entity
* For performance (no joins required)

---

# 🔹 3️⃣ Multi-Table Inheritance

## 📌 Definition

In multi-table inheritance:

* Each model creates its own database table
* Child model has a OneToOne relationship with parent model

---

## ✅ Your Example

```python
class ExamCenter(models.Model):
  center_name = models.CharField(max_length=255)
  center_city = models.CharField(max_length=255)
```

```python
class Candidate(ExamCenter):
  name = models.CharField(max_length=255)
  roll = models.IntegerField()
```

---

## 🗄 What Happens in Database?

Two tables are created:

1. examcenter
2. candidate

Candidate table contains:

* id (primary key)
* examcenter_ptr_id (OneToOneField automatically created)
* name
* roll

So data is split across two tables.

---

## 🔁 How Query Works

When you fetch a Candidate:

Django performs a JOIN between:

* examcenter
* candidate

So it is slightly slower than abstract inheritance.

---

## 🏪 Real-Life Example

ExamCenter is a real entity.
Candidate is a special type related to an exam center.

You want both:

* Exam center to exist independently
* Candidate to extend it

---

## ✅ When to Use Multi-Table Inheritance

* When parent model is meaningful
* When you need separate tables
* When polymorphism is required

⚠️ Used less frequently than abstract models.

---

# 🔹 4️⃣ Proxy Model

## 📌 Definition

A proxy model:

* Does NOT create a new database table
* Does NOT add new fields
* Only changes Python-level behavior

---

## ✅ Your Example

```python
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  stock = models.IntegerField()
```

```python
class DiscountedProduct(Product):
  class Meta:
    proxy = True
    ordering = ['id']
```

---

## 🗄 What Happens in Database?

Only ONE table:

* product

No new table for `DiscountedProduct`.

---

## 🧠 What Proxy Model Changes

* Default ordering
* Managers
* Methods
* Admin behavior

But NOT fields.

---

## 🏪 Real-Life Example

You have one product table.

But you want:

* A special view for discounted products
* Different ordering
* Different admin representation

Proxy model solves this.

---

# 🔥 Full Comparison Table

| Feature          | Abstract | Multi-Table | Proxy |
| ---------------- | -------- | ----------- | ----- |
| Creates DB table | ❌ No     | ✅ Yes       | ❌ No  |
| Shares fields    | ✅ Yes    | ✅ Yes       | ❌ No  |
| Adds new fields  | ❌ No     | ✅ Yes       | ❌ No  |
| Requires JOIN    | ❌ No     | ✅ Yes       | ❌ No  |
| Changes behavior | ✅ Yes    | ✅ Yes       | ✅ Yes |
| Performance      | Fast     | Slower      | Fast  |

---

# 🎯 Interview-Ready Answers

### What is an Abstract Model?

An abstract model provides common fields to child models but does not create a database table.

---

### What is Multi-Table Inheritance?

Each model creates its own table, and Django links them using an automatic OneToOneField.

---

### What is a Proxy Model?

A proxy model changes the behavior of an existing model without creating a new database table.

---

# 🧠 Final Summary

* Use **Abstract** for shared fields
* Use **Multi-Table** when parent is real entity
* Use **Proxy** to change behavior only

---

✅ This completes your session on Django Model Inheritance with proper conceptual clarity and practical understanding.
