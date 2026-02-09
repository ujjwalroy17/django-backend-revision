# Django ORM Aggregation – Database Aggregate Functions 

## 📌 What We Studied Today (Aggregation)

* What aggregation means in Django ORM
* Difference between aggregation and normal QuerySets
* Using `aggregate()` method
* Common aggregate functions:

  * `Avg`
  * `Sum`
  * `Min`
  * `Max`
  * `Count`
* How aggregation hits the database
* Real-life use cases

---

## 🧠 What is Aggregation in Django?

> **Aggregation means performing calculations on a set of database records and returning a single summarized result.**

Instead of returning rows, aggregation returns **computed values**.

---

## 🔁 Normal QuerySet vs Aggregation

### Normal QuerySet

```python
Student.objects.all()
```

* Returns multiple rows (records)

### Aggregation Query

```python
Student.objects.aggregate(Avg('marks'))
```

* Returns a **single result**

---

## 🧩 Why Aggregation is Needed

Aggregation is used when you need:

* Average values
* Totals
* Minimum / maximum values
* Record counts

Without aggregation, these calculations would be slow and inefficient in Python.

---

## 🧠 Syntax of `aggregate()`

```python
QuerySet.aggregate(function('field_name'))
```

Example:

```python
Student.objects.aggregate(Avg('marks'))
```

---

## 🔢 Aggregate Functions You Used

---

## 1️⃣ `Avg()` – Average

```python
average = Student.objects.aggregate(Avg('marks'))
```

### Meaning

* Calculates average of `marks`

### Output

```python
{'marks__avg': 72.5}
```

### Real-Life Use

* Average student marks
* Average product rating

---

## 2️⃣ `Sum()` – Total

```python
total = Student.objects.aggregate(Sum('marks'))
```

### Meaning

* Calculates total sum

### Real-Life Use

* Total sales
* Total revenue

---

## 3️⃣ `Min()` – Minimum Value

```python
minimum = Student.objects.aggregate(Min('marks'))
```

### Meaning

* Finds lowest value

### Real-Life Use

* Lowest marks
* Cheapest product

---

## 4️⃣ `Max()` – Maximum Value

```python
maximum = Student.objects.aggregate(Max('marks'))
```

### Meaning

* Finds highest value

### Real-Life Use

* Top scorer
* Highest price

---

## 5️⃣ `Count()` – Count Records

```python
totalcount = Student.objects.aggregate(Count('marks'))
```

### Meaning

* Counts non-null values in a field

### Real-Life Use

* Total students
* Total orders

---

## 🔍 Understanding the Return Type

```python
average = Student.objects.aggregate(Avg('marks'))
```

* Always returns a **dictionary**
* Key format: `field__function`

Example:

```python
{'marks__avg': 72.5}
```

---

## 🧠 Multiple Aggregations Together

```python
Student.objects.aggregate(
    Avg('marks'),
    Sum('marks'),
    Min('marks'),
    Max('marks'),
    Count('marks')
)
```

* Executes in **single SQL query**
* Very efficient

---

## 🔄 ORM → SQL (Conceptual)

```python
Student.objects.aggregate(Avg('marks'))
```

Equivalent SQL:

```sql
SELECT AVG(marks) FROM student;
```

---

## ⚠️ Important Notes

* Aggregation hits the database immediately
* Does NOT return QuerySet
* Best for analytics & reports
* Use indexed fields for performance

---

## 🎯 Interview-Ready Definition

> “Aggregation in Django ORM allows developers to perform summary calculations like average, sum, minimum, maximum, and count directly at the database level using aggregate functions.”

---

## 🧠 Key Takeaways (Quick Revision)

* Aggregation returns computed results, not rows
* Uses database-level functions
* Always returns a dictionary
* Very efficient compared to Python loops

---

✅ These notes give you **complete clarity on Django ORM Database Aggregation**
