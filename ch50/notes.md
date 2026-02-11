# Django Custom Model Manager – Complete README Notes



# 🧠 1️⃣ What is a Model Manager?

A **Model Manager** is the interface between your Django model and the database.

Whenever you write:

```python
Student.objects.all()
```

`objects` is the **default manager**.

Without a manager, you cannot query the database.

---

# 🔹 2️⃣ Why Do We Need a Custom Manager?

The default manager only provides basic querying:

* `.all()`
* `.filter()`
* `.get()`
* `.exclude()`

But in real projects, we often need:

* Custom reusable query logic
* Business-specific filters
* Cleaner code in views
* Structured query methods

Instead of repeating complex filters everywhere, we move that logic into a **custom manager**.

---

# 🔹 3️⃣ Your Model (models.py Explained)

```python
class Student(models.Model):
 name = models.CharField(max_length=70)
 roll = models.IntegerField(unique=True, null=False)
 city = models.CharField(max_length=70)
 marks = models.IntegerField()
 pass_date = models.DateField()
 admission_date=models.DateTimeField()

 objects = models.Manager()
```

### What this means:

* `objects` is the default manager
* It allows standard QuerySet operations

If you replace it with:

```python
objects = CustomStudentManager()
```

Then Django will use your custom logic instead.

---

# 🔹 4️⃣ Your Custom Manager (managers.py Explained)

```python
class CustomStudentManager(models.Manager):
  def get_stu_roll_range(self, r1, r2):
    return super().get_queryset().filter(roll__range=(r1, r2))
```

## What is happening here?

* We created a class that extends `models.Manager`
* We defined a custom method: `get_stu_roll_range()`
* It returns students whose roll numbers are between `r1` and `r2`

Internally it calls:

```python
super().get_queryset()
```

This gives the base QuerySet.

Then we apply filtering.

---

# 🔹 5️⃣ How It Is Used in Views

```python
student_data = Student.students.get_stu_roll_range(101, 105)
```

Instead of writing:

```python
Student.objects.filter(roll__range=(101, 105))
```

We now have a clean reusable method.

This improves:

* Code readability
* Maintainability
* Reusability

---

# 🔹 6️⃣ Different Ways to Attach Managers

You experimented with:

```python
objects = models.Manager()
# students = CustomStudentManager()
```

If you define:

```python
students = CustomStudentManager()
```

Then you access it as:

```python
Student.students.all()
```

Important rule:

> The first manager defined in the model becomes the **default manager**.

---

# 🔹 7️⃣ Proxy Model + Custom Manager

You also explored:

```python
class ProxyStudent(Student):
 students = CustomStudentManager()
 class Meta:
  proxy = True
  ordering = ['name']
```

Here:

* No new database table is created
* Only behavior changes
* Custom manager applies to proxy only

This is useful when you want:

* Different filtering behavior
* Different ordering
* Different admin representation

Without changing the original model.

---

# 🏪 Real-Life Use Case Examples

### Example 1: Passed Students

Instead of:

```python
Student.objects.filter(marks__gte=60)
```

Create:

```python
def passed(self):
    return self.get_queryset().filter(marks__gte=60)
```

Now:

```python
Student.objects.passed()
```

---

### Example 2: Active Records (Soft Delete)

```python
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
```

This automatically hides deleted records.

---

# 🔥 Why Custom Managers Are Important

In professional projects, managers are used for:

* Soft delete systems
* Role-based filtering
* Multi-tenant filtering
* Custom reusable business queries
* Cleaner API design

Especially important in DRF.

---

# 🎯 Interview-Ready Explanation

If asked:

### What is a Custom Model Manager?

A custom model manager in Django allows developers to define reusable database query logic and control how data is retrieved from the model.

---

### Why use Custom Managers?

To encapsulate business logic, avoid repetition in views, and make queries cleaner and reusable.

---

# 🧠 Final Summary

* Manager connects model to database
* Default manager is `objects`
* Custom managers allow custom query methods
* Improves code structure
* Frequently used in real backend systems

---

✅ This completes your session on **Django Custom Model Managers** with proper conceptual clarity and practical understanding.
