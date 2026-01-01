# DJANGO BACKEND REVISION NOTES

## What is Django?

Django is a high-level web framework written in Python that helps in building web applications quickly and cleanly.

Django follows these core ideas:
- Rapid development
- Clean and maintainable code
- Reusability of components
- DRY principle (Don’t Repeat Yourself)

Django follows the MVT (Model–View–Template) architectural pattern:
- **Model:** Handles database structure and data logic
- **View:** Contains business logic and handles requests
- **Template:** Responsible for presentation (HTML)

Django was created in 2003 at the Lawrence Journal-World newspaper.
It was released publicly in July 2005 under the BSD license and is maintained by the Django Software Foundation.

## Features and Advantages of Django

- **Built-in Admin Interface:**
  Django provides an automatic admin panel to manage application data easily.
- **ORM (Object Relational Mapper):**
  Allows interaction with the database using Python code instead of writing raw SQL queries.
- **Authentication System:**
  Provides built-in support for user login, logout, permissions, and sessions.
- **Rapid Development:**
  Django reduces boilerplate code and speeds up development.
- **Versatility:**
  Used for blogs, APIs, dashboards, e-commerce platforms, and enterprise applications.
- **Security:**
  Provides built-in protection against common security threats like SQL injection, CSRF, and XSS.

## Installation of Django

### Step 1: Create a virtual environment (recommended)
This keeps project dependencies isolated.
```bash
python -m venv venv
```
Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

### Step 2: Install Django
```bash
pip install django
```
Check installation:
```bash
django-admin --version
```
### Step 3: Create a Django project
```bash
django-admin startproject project_name
```

## Django Project Directory Structure 
After creating a project, Django creates the following structure:
```
prefix{project_name} (Outer project folder / Root directory)
prefix{|}
prefix{├── {project_name} (Inner project folder)}
prefix{| ├── init.py}
prefix{| ├── settings.py}
prefix{| ├── urls.py}
prefix{| ├── asgi.py}
prefix{| └── wsgi.py}
prefix{|}
prefix└── manage.py

```
## Explanation of Project Files

## Outer Project Folder (Root Directory)
This is the main container folder. It holds the inner project folder and `manage.py`. Used to manage and run the project.

## Inner Project Folder
This folder is the actual Python package for the Django project. It contains all the core configuration files.

### `__init__.py`
- This file marks the folder as a Python package.
- It allows Python to import modules from this directory.
- Usually kept empty.

### `wsgi.py` (Web Server Gateway Interface)
- This file helps Django communicate with the web server.
- It is used for synchronous applications.
- Commonly used with servers like Gunicorn and uWSGI.
- Acts as the entry point for deploying Django applications.

### `asgi.py` (Asynchronous Server Gateway Interface)
- This file allows Django to handle both synchronous and asynchronous requests.
- Used for WebSockets, async views, and real-time features.
- Commonly used with servers like Uvicorn and Daphne.
- Supports both synchronous and asynchronous communication.

### `settings.py`
- The main configuration file of the Django project. Contains:
  - Installed applications
  - Middleware
  - Database configuration
  - Static and media files settings
  - Security and environment settings
- Every Django project depends heavily on this file.

### `urls.py`
- Handles URL routing.
- Maps URLs to their corresponding views.
- Acts as the entry point for HTTP requests.

### `manage.py`
- Command-line utility file. Used to perform administrative tasks such as:
  - Running the development server
  - Creating apps
  - Applying migrations
  - Accessing Django shell
> Example: `python manage.py runserver`

## Conclusion
Django provides a structured and secure way to build backend applications. Understanding the project structure and configuration files is essential for:
- Backend development
- Debugging
- Deployment
- Interviews
These notes are part of my Django backend revision process.