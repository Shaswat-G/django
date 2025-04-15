# ⚙️ Django Project Setup & Structure – The Practical Guide

## 📦 Step 1: Environment & Tools Setup

**Your Stack:**
- **OS**: Windows 11  
- **Package Manager**: [Miniconda](https://docs.conda.io/en/latest/miniconda.html)  
- **Editor**: VS Code (with extensions for Python, GitLens, Django Snippets, etc.)

**Installation Steps:**
```bash
conda create -n myenv python=3.11
conda activate myenv
pip install django
```

## 🔧 Step 2: Project Bootstrap

1. **Create a working directory**
   ```bash
   mkdir storefront
   cd storefront
   ```

2. **Initialize Git**
   ```bash
   git init
   echo "# Storefront" >> README.md
   echo "*.pyc\n__pycache__/" >> .gitignore
   touch LICENSE
   ```

3. **Create a GitHub repository and push**
   ```bash
   git remote add origin <your-repo-url>
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

4. **Start Django Project**
   ```bash
   django-admin startproject storefront .
   ```

   > The trailing `.` means: create files **in the current directory**, not a nested subfolder.

---

## 🧪 Essential Django Commands & Their Purpose

| Command                                | Purpose |
|----------------------------------------|---------|
| `django-admin startproject <name>`     | Creates a new Django project structure. Use only once. |
| `python manage.py runserver`           | Starts the development server. |
| `python manage.py startapp <appname>`  | Creates a new application within your project. |
| `python manage.py makemigrations`      | Generates migration scripts based on model changes. |
| `python manage.py migrate`             | Applies migrations to the database. |
| `python manage.py createsuperuser`     | Creates an admin user for the built-in Django Admin. |
| `python manage.py shell`               | Opens an interactive Python shell with Django context. |
| `python manage.py test`                | Runs unit tests. |

> From now on, we’ll use `manage.py` over `django-admin`, since it loads your project’s settings module automatically.

---

## 🧬 Breakdown of Core Project Files

Once you run `startproject`, Django generates this structure:

```
storefront/
│
├── manage.py
├── storefront/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

### File Purposes:

| File              | Purpose |
|-------------------|---------|
| `__init__.py`     | Marks the folder as a Python package. |
| `settings.py`     | Contains all configuration — installed apps, database, middleware, templates, etc. |
| `urls.py`         | URL routing: maps paths (e.g., `/about`) to views. |
| `asgi.py`         | Entry point for **asynchronous** web servers (e.g., for WebSockets). |
| `wsgi.py`         | Entry point for **WSGI-compatible** servers like Gunicorn or uWSGI — used in production deployments. |
| `manage.py`       | CLI utility to interact with the project (run server, migrations, shell, etc.). |

---

## 🌐 Running the Project

```bash
python manage.py runserver
```

- Visit `http://127.0.0.1:8000/` in your browser.
- You’ll see the default Django welcome page — confirming your setup works!

---

## 🧱 Every Django App Is Unique

Django is modular — meaning you create **apps** for isolated functionality:
- Each app has its own models, views, urls, and templates.
- You can reuse apps across projects (like plugins).

### 🎯 Popular Django Use Cases & Their Patterns

| Use Case                | Typical Features & Design Choices |
|-------------------------|------------------------------------|
| **E-Commerce Site**     | Products, Orders, Payments, Admin Panel, Inventory App, REST API for mobile apps |
| **Blog or CMS**         | Posts, Categories, Comments, Markdown/HTML Rendering, Rich Admin Customization |
| **Social Network**      | User Profiles, Posts, Likes, Follows, Notifications, Realtime updates (ASGI) |
| **Booking System**      | Calendars, Reservations, Time Slot Models, Email Notifications |
| **Internal Dashboards** | Auth, Role-based Access, Charts, Reports, DataTables, Custom Widgets |

> Each use case dictates architectural decisions: single-page vs multi-page rendering, sync vs async views, API-first design, use of external services, etc.

---

## ✅ Recap: Django's Strengths

- Kickstart projects quickly with powerful defaults.
- Rich, customizable admin interface.
- Robust ORM for database operations.
- Secure by default (CSRF protection, user auth, etc.).
- Ideal for both **monolithic apps** and **modular microservices**.