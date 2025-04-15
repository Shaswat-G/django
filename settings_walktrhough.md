## 🌐 **Project Structure**
```python
BASE_DIR = Path(__file__).resolve().parent.parent
```
- This sets the base directory of your project. It's useful for defining file paths relative to your project root—so your code works no matter where it's deployed.

---

## ⚠️ **Security Settings**
```python
SECRET_KEY = 'django-insecure-...'
DEBUG = True
ALLOWED_HOSTS = []
```
- `SECRET_KEY`: Unique key used for cryptographic operations. Keep it secret in production.
- `DEBUG`: Set to `True` during development to see detailed errors. Set to `False` in production!
- `ALLOWED_HOSTS`: List of domain names/IPs allowed to access your app. Use `['*']` for dev testing, or set it properly for deployment (e.g. `['myapp.com']`).

---

## ⚙️ **Installed Applications**
```python
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Handles content types of models
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Flash messages framework
    'django.contrib.staticfiles',  # Static files handling
]
```
- These are Django apps you’re using. You’ll later add your own apps here, like `'store'` or `'blog'`.
- The servcice you are building is functionally composed of smaller apps like orders, shipping, customer service, etc.
- These are functionally separated to contain very similar functionalities together for ease of use, maintaneability and modular use (can be reused in other projects).

---

## 🧱 **Middleware Stack**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ...
]
```
- Middleware are hooks that process requests and responses. Think of them as filters that run *before* your view logic.
- Example: CSRF protection, session handling, security headers, etc.

---

## 🔗 **Routing / URLs**
```python
ROOT_URLCONF = 'storefront.urls'
```
- This tells Django where your top-level URL routes live.

---

## 🎨 **Templates (Frontend)**
```python
TEMPLATES = [...]
```
- This configures how Django processes HTML templates.
- `APP_DIRS=True` means Django will look for a `templates/` folder inside each app.
- `context_processors`: Inject helpful variables into templates (e.g., logged-in user info, request data).

---

## 🔌 **WSGI Application**
```python
WSGI_APPLICATION = 'storefront.wsgi.application'
```
- WSGI is the entry point for serving your app. You don’t mess with this much—used in deployment setups like Gunicorn or uWSGI.

---

## 🗃️ **Database Configuration**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
- Uses SQLite by default (file-based database, great for dev/testing).
- You’ll switch to PostgreSQL or MySQL in production.

---

## 🔐 **Password Validators**
```python
AUTH_PASSWORD_VALIDATORS = [...]
```
- Built-in validators to improve password strength and security.

---

## 🌍 **Internationalization**
```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```
- Language and time zone settings.
- `USE_I18N` enables translation/internationalization.
- `USE_TZ` ensures timezone-aware datetimes (important for APIs & logging).

---

## 📁 **Static Files**
```python
STATIC_URL = 'static/'
```
- URL to access static files like CSS, JS, and images.
- During development: Django serves static files automatically.
- In production: You'll use something like Nginx to serve them.

---

## 🧾 **Default Primary Key Type**
```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
- Sets the default type of primary key for models (uses a big integer instead of a regular one—future-proofing).

---

## ✅ How to Use These Settings
1. **Add your own apps** in `INSTALLED_APPS`:
   ```python
   'store',
   'blog',
   ```
2. **Change `DEBUG = False` and set `ALLOWED_HOSTS`** before deploying.
3. **Switch the database** to PostgreSQL if needed:
   ```python
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'mydb',
   'USER': 'myuser',
   'PASSWORD': 'secret',
   'HOST': 'localhost',
   'PORT': '5432',
   ```
4. **Put your templates and static files** in organized folders (`templates/`, `static/`).

---