# MORROW - Local Development Setup Guide

## 1. Prerequisites

- **Python:** Version 3.11 or higher
- **PostgreSQL:** Version 14+ (or local SQLite for zero-configuration testing)
- **Git:** Version 2.30+
- **Virtual Environment:** `venv` or `virtualenv`

---

## 2. Step-by-Step Installation

### Step 1: Clone Repository
```bash
git clone <repository_url> morrow
cd morrow
```

### Step 2: Initialize Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Production dependencies:
pip install -r requirements.txt

# Development & testing dependencies:
pip install -r requirements-dev.txt
```

### Step 4: Environment Configuration
Copy the template configuration file:
```bash
cp .env.example .env
```
Edit `.env` to configure your PostgreSQL credentials and Razorpay test credentials. (If `DB_NAME` is left empty in development, MORROW automatically falls back to SQLite for convenience).

### Step 5: Database Setup & Migration (When Implemented)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 7: Launch Development Server
```bash
python manage.py runserver 127.0.0.1:8000
```
Visit `http://127.0.0.1:8000` in your web browser.

---

## 3. Running Test Suites

Execute all tests using `pytest`:
```bash
pytest
```
Run coverage analysis:
```bash
pytest --cov=apps --cov-report=term-missing
```

