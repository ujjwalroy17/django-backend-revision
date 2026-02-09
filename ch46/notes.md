# Django ORM Database Field Lookups – Complete README Notes

These notes cover **Database Field Lookups in Django ORM**, which are used inside `filter()`, `exclude()`, and `get()` to build **powerful WHERE conditions** in queries. This document is designed for **clear understanding, future revision, and interview preparation**.

---

## 📌 What We Studied Today

* What database field lookups are
* Why field lookups are needed
* Syntax of field lookups (`field__lookup=value`)
* Commonly used lookup types
* String, numeric, date, and NULL lookups
* Range and comparison lookups
* Real-life use cases for each lookup

---

## 🧠 What are Database Field Lookups?

> **Database field lookups are special query expressions used to filter data based on conditions applied to model fields.**

They extend Django ORM’s filtering power beyond simple equality checks.

---

## 🧩 Basic Syntax

```python
Model.objects.filter(field_name__lookup=value)
```

Examples:

```python
Student.objects.filter(city__exact='Delhi')
Student.objects.filter(marks__gte=60)
```

---

## 🎯 Why Field Lookups are Important

Without field lookups:

```python
Student.objects.filter(marks=60)
```

With field lookups:

```python
Student.objects.filter(marks__gte=60)
```

Field lookups allow:

* Comparisons
* Partial matching
* Case-insensitive queries
* Range queries

---

## 🔹 Common Database Field Lookups

---

## 1️⃣ `exact` – Exact Match

```python
Student.objects.filter(city__exact='Bokaro')
```

* Same as `city='Bokaro'`
* Case-sensitive (depends on DB)

**Real-life use:** Find students from an exact city.

---

## 2️⃣ `iexact` – Case-Insensitive Exact Match

```python
Student.objects.filter(name__iexact='rahul')
```

**Real-life use:** Username matching without case issues.

---

## 3️⃣ `contains` – Substring Match

```python
Student.objects.filter(name__contains='ra')
```

* Case-sensitive

**Real-life use:** Search feature.

---

## 4️⃣ `icontains` – Case-Insensitive Substring Match ⭐

```python
Student.objects.filter(name__icontains='ra')
```

**Real-life use:** Search bars (most common).

---

## 5️⃣ `startswith` / `istartswith`

```python
Student.objects.filter(name__startswith='Ra')
Student.objects.filter(name__istartswith='ra')
```

**Real-life use:** Auto-suggestions.

---

## 6️⃣ `endswith` / `iendswith`

```python
Student.objects.filter(email__endswith='@gmail.com')
```

**Real-life use:** Filter users by email domain.

---

## 7️⃣ `in` – Match Any Value in List

```python
Student.objects.filter(city__in=['Delhi', 'Mumbai'])
```

**Real-life use:** Multi-select filters.

---

## 8️⃣ `gt`, `gte`, `lt`, `lte` – Comparisons

```python
Student.objects.filter(marks__gt=60)
Student.objects.filter(marks__gte=60)
Student.objects.filter(marks__lt=90)
Student.objects.filter(marks__lte=90)
```

**Real-life use:** Marks, price, age filters.

---

## 9️⃣ `range` – Between Two Values

```python
Student.objects.filter(marks__range=(50, 80))
```

**Real-life use:** Price range sliders.

---

## 🔟 `isnull` – NULL Check

```python
Student.objects.filter(pass_date__isnull=True)
```

**Real-life use:** Find incomplete records.

---

## 1️⃣1️⃣ Date Lookups

```python
Student.objects.filter(pass_date__year=2024)
Student.objects.filter(pass_date__month=5)
Student.objects.filter(pass_date__day=10)
```

**Real-life use:** Reports by year/month/day.

---

## 1️⃣2️⃣ `regex` / `iregex`

```python
Student.objects.filter(name__regex=r'^R')
```

**Real-life use:** Advanced pattern matching.

⚠️ Use carefully (performance-heavy).

---

## 🧠 Combining Field Lookups

```python
Student.objects.filter(
    name__icontains='ra',
    marks__gte=60,
    city__in=['Delhi', 'Mumbai']
)
```

This creates a powerful SQL WHERE clause.

---

## 🔍 ORM → SQL (Concept)

```python
Student.objects.filter(marks__gte=60)
```

Equivalent SQL:

```sql
SELECT * FROM student WHERE marks >= 60;
```

---

## ⚠️ Important Notes

* Field lookups are **database-agnostic**
* Chaining lookups is safe
* Avoid regex in large datasets
* Prefer indexed fields for performance

---

## 🎯 Interview-Ready Definition

> “Database field lookups in Django ORM allow developers to apply conditional logic to model fields while querying the database, enabling comparisons, partial matches, and advanced filtering.”

---

## 🔹 Additional Field Lookups (Practiced Examples – Merged Notes)

This section merges the **exact queries you practiced** with the earlier field lookup concepts, so you can revise from **real code examples**.

---

## 🔤 String-Based Lookups (Text Fields)

```python
Student.objects.filter(name__exact="Sonam")
```

* Exact match (case-sensitive depending on DB)

```python
Student.objects.filter(name__iexact="Sonam")
```

* Case-insensitive exact match

```python
Student.objects.filter(name__contains="S")
Student.objects.filter(name__icontains="i")
```

* Substring search (search functionality)

```python
Student.objects.filter(name__startswith='S')
Student.objects.filter(name__istartswith='S')
Student.objects.filter(name__endswith='t')
Student.objects.filter(name__iendswith='t')
```

* Prefix / suffix matching (auto-suggest, filtering)

---

## 🔢 Numeric Lookups (Integer / Float Fields)

```python
Student.objects.filter(id__in=[1, 3, 7])
```

* Match values from a list (checkbox filters)

```python
Student.objects.filter(marks__gt=200)
Student.objects.filter(marks__gte=200)
Student.objects.filter(marks__lte=200)
```

* Greater than / equal / less than comparisons

---

## 📅 Date Lookups (DateField / DateTimeField)

```python
Student.objects.filter(pass_date__range=('2024-01-01', '2024-12-24'))
```

* Date range filtering (reports, analytics)

```python
Student.objects.filter(pass_date__year=2023)
Student.objects.filter(pass_date__year__gt=2023)
```

* Year-based filtering

```python
Student.objects.filter(pass_date__month=12)
Student.objects.filter(pass_date__month__gt=5)
```

* Month-based filtering

```python
Student.objects.filter(pass_date__day=4)
Student.objects.filter(pass_date__day__gt=4)
```

* Day-based filtering

```python
Student.objects.filter(pass_date__week=15)
Student.objects.filter(pass_date__week__gt=15)
```

* Week-based filtering

```python
Student.objects.filter(pass_date__week_day=4)
Student.objects.filter(pass_date__week_day__gt=4)
```

* Weekday-based filtering (Mon–Sun)

```python
Student.objects.filter(pass_date__quarter=1)
Student.objects.filter(pass_date__quarter__gt=2)
```

* Quarter-based filtering (Q1–Q4)

---

## ⏰ Time Lookups (DateTimeField)

```python
Student.objects.filter(admission_date__date=date(2023, 8, 15))
Student.objects.filter(admission_date__date__gt=date(2022, 8, 15))
```

* Exact date extraction from DateTimeField

```python
Student.objects.filter(admission_date__time=time(6, 0))
Student.objects.filter(admission_date__time__gt=time(10, 0))
```

* Time-based filtering

```python
Student.objects.filter(admission_date__hour=6)
Student.objects.filter(admission_date__hour__gt=5)
```

* Hour-level filtering

```python
Student.objects.filter(admission_date__minute=40)
Student.objects.filter(admission_date__minute__gt=40)
```

* Minute-level filtering

```python
Student.objects.filter(admission_date__second=40)
Student.objects.filter(admission_date__second__gt=40)
```

* Second-level filtering

---

## ❓ NULL Check Lookup

```python
Student.objects.filter(roll__isnull=False)
```

* Checks whether field has NULL value
* Common in data-cleanup and validation

---

## 🧠 Final Key Takeaways (Quick Revision)

* Field lookups extend Django ORM filtering power
* Syntax: `field__lookup=value`
* String, numeric, date, and time lookups are all supported
* Extremely useful for **search, filters, reports, dashboards**
* Database-agnostic and optimized

---

✅ This merged section now makes the README a **complete, practical reference** for Django ORM Database Field Lookups.
