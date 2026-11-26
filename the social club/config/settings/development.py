import os
from .base import *

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key-placeholder-morrow-2026")

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database configuration: defaults to SQLite for quick setup if PostgreSQL credentials are unset
DB_NAME = os.getenv("DB_NAME")
if DB_NAME:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_NAME,
            "USER": os.getenv("DB_USER", "postgres"),
            "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Development Email Backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Internal IPs for debug toolbar if enabled
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

