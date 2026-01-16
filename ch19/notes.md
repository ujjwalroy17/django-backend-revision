# 📘 Django Built-in Admin Panel & Superuser (ch19)

## 📌 Topic Covered

Understanding Django’s built-in Admin Panel and creating a superuser to manage the application.

---

## 🔹 What is Django Admin Panel?

The Django Admin Panel is a built-in web-based interface provided by Django that allows developers and administrators to:

- Manage database records
- Perform CRUD operations
- Manage users and permissions
- Control application data without writing custom views

> 📌 It is automatically available when a Django project is created.

---

## 🔹 Why Django Admin Panel is Important?

- Saves development time
- Provides ready-made UI for data management
- Secure authentication system
- Useful for internal tools and admin dashboards
- Highly customizable

---

## 🔹 Creating a Django Project 
```bash
django-admin startproject ch19 
```
This creates:
- Project configuration files
- Default Django apps (admin, auth, sessions, etc.)

---

## 🔹 Running Initial Migrations 
Before using the admin panel, Django’s default database tables must be created.
Commands:
```bash
def manage.py makemigrations
def manage.py migrate
```
This creates tables for:
| Purpose | Description |
|---------|--------------|
| Authentication | Handles user authentication |
| Admin | Manages admin interface |
| Sessions | Manages user sessions |
| Permissions | Handles permissions |
| Content types | Manages content types |

----
## Creating a Superuser

A superuser is an admin-level user who has full access to the Django Admin Panel.

### Command:
```bash
python manage.py createsuperuser
```

### Example Input:
- **Username:** user
- **Email:** user@example.com
- **Password:** ********

### If Django shows a password warning:
> The password is too similar to the username.
>
> You can bypass it by typing:
> `y`

📌 **Superuser is created successfully.**

---

## Starting the Development Server
```bash
python manage.py runserver
```

Server runs at:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Accessing Django Admin Panel
Open your browser and go to:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Login using:
- Superuser username
- Superuser password

---

## What You Can Do in Admin Panel

- View users and groups
- Add, update, delete records 
- Manage permissions 
- Monitor admin actions 
- Control application data securely 

---

## Default Apps Used by Admin Panel  
table:
| App Name   | Purpose                     |
|------------|------------------------------|
| admin      | Admin interface              |
| auth       | Authentication system        |
| contenttypes | Model metadata             |
| sessions   | Session management           |
