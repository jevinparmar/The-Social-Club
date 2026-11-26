# MORROW - Deployment & Production Hardening Guide

## 1. Production Architecture Overview

In production, MORROW operates behind an Nginx reverse proxy communicating via Unix domain sockets to Gunicorn WSGI workers. PostgreSQL handles transactional persistence.

```
[ Internet ]
      │
      ▼ (Port 80/443 HTTPS)
  [ Nginx ]  ──(Static Files)──> [/var/www/morrow/static/]
      │      ──(Media Files)───> [/var/www/morrow/media/]
      ▼ (Unix Socket: /run/gunicorn.sock)
 [ Gunicorn ] (4 Workers: (2 x CPUs) + 1)
      │
      ▼
 [ Django 5.0 (MORROW) ]
      │
      ▼ (Port 5432)
 [ PostgreSQL 15+ ]
```

---

## 2. Security Hardening Checklist

1. **Environment Secrets:**
   - Store all passwords, secret keys, and Razorpay secrets exclusively in environment variables or vault secret managers.
   - Enforce `DEBUG=False` in `config/settings/production.py`.
2. **SSL/TLS & Transport Security:**
   - Enforce `SECURE_SSL_REDIRECT=True`.
   - Enable HTTP Strict Transport Security (HSTS): `SECURE_HSTS_SECONDS=31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`, `SECURE_HSTS_PRELOAD=True`.
   - Protect session and CSRF cookies: `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`, `SESSION_COOKIE_HTTPONLY=True`.
3. **Web Security Headers:**
   - `X_FRAME_OPTIONS = "DENY"` (Prevents clickjacking).
   - `SECURE_CONTENT_TYPE_NOSNIFF = True` (Prevents MIME sniffing).
   - Content Security Policy (CSP) headers configured in Nginx.
4. **Payment Gateway Security:**
   - Validate Razorpay webhook signatures using `hmac.new(..., hashlib.sha256)` against the raw payload before accepting payment capture events.
5. **QR Code Admission Security:**
   - QR code payloads contain salted HMAC-SHA256 tokens rather than plain database IDs. Scanners verify cryptographic validity before recording gate admission.

---

## 3. Server Configuration Templates

Foundational server configurations are located in:
- `deployment/nginx/morrow.conf`: Nginx reverse proxy and static file routing template.
- `deployment/gunicorn/gunicorn.service`: Systemd service unit definition for Gunicorn worker management.
- `deployment/gunicorn/gunicorn_conf.py`: Runtime Gunicorn configuration (worker counts, timeout, access logging).

