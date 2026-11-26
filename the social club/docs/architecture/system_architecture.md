# MORROW - System Architecture Design

## 1. Architectural Philosophy

MORROW is architected as a modular, scalable, and resilient Event Management and Ticketing platform. The design prioritizes:
- **High Concurrency & Seat Locking Safety:** Protection against overbooking and double-allocation through atomic transactions and status-based expiring reservations.
- **Service-Selector Pattern:** Clear decoupling of business workflows from Django's HTTP request-response cycle and ORM access.
- **Fail-Safe Third-Party Integrations:** Payment gateway hooks, email dispatchers, and QR generation isolated within dedicated integration boundaries.

```
+-------------------------------------------------------------------------------+
|                                CLIENT LAYER                                   |
|   Web Browsers (Desktop / Tablet / Mobile) - Semantic HTML5, CSS3, ES6 JS     |
+-------------------------------------------------------------------------------+
                                       |
                                       | HTTPS / WSS
                                       v
+-------------------------------------------------------------------------------+
|                       REVERSE PROXY & STATIC EDGE (Nginx)                     |
|   SSL Termination, Rate Limiting, Static/Media Asset Caching, Gzip/Brotli     |
+-------------------------------------------------------------------------------+
                                       |
                                       | Unix Domain Socket / HTTP
                                       v
+-------------------------------------------------------------------------------+
|                         WSGI / ASGI RUNTIME (Gunicorn)                        |
|   Process Management, Worker Pooling, Request Buffering                       |
+-------------------------------------------------------------------------------+
                                       |
                                       v
+-------------------------------------------------------------------------------+
|                               DJANGO APPLICATION                              |
|                                                                               |
|   [ Middleware Layer ]                                                        |
|   Security, Session, Auth, Role Enforcement, Exception Handling               |
|                                                                               |
|   [ Presentation / Routing Layer (urls.py & views/) ]                         |
|   Public Views, Organizer Views, Admin Views                                  |
|                                                                               |
|   [ Domain Logic Layer (services/) ] <--------------------+                   |
|   Booking Engine, Seat Allocation, Payment Verification   |                   |
|                                                           |                   |
|   [ Query & Read Layer (selectors/) ]                     |                   |
|   Optimized reads, aggregations, filtered QuerySets       |                   |
|                                                           |                   |
|   [ Integrations Layer ]                                  |                   |
|   - Razorpay API Client (Orders, Signatures, Webhooks)    |                   |
|   - QR Code Engine (HMAC Signatures, Vector/Raster gen)   |                   |
|   - SMTP Mailer (Templated HTML tickets & receipts)       |                   |
+-----------------------------------------------------------+-------------------+
                                       |
                                       v
+-------------------------------------------------------------------------------+
|                               PERSISTENCE LAYER                               |
|   PostgreSQL Relational DB (ACID, Row-Level Locking, JSONB, Spatial Indexes)  |
+-------------------------------------------------------------------------------+
```

---

## 2. Layered Responsibilities

### 2.1 Presentation Layer (`views/` & `templates/`)
- Views are thin controllers responsible only for HTTP protocol concerns: extracting input, validating form syntax, invoking the appropriate service/selector, and returning rendered HTML or JSON.
- Views do not write raw database update queries or orchestrate multiple models directly.

### 2.2 Service Layer (`services/`)
- Pure business operations (e.g., `create_booking_reservation`, `verify_payment_and_issue_tickets`, `invalidate_qr_admission`).
- Wraps complex mutations inside `django.db.transaction.atomic()`.
- Raises domain-specific exceptions defined in `common/exceptions/`.

### 2.3 Selector Layer (`selectors/`)
- Pure read queries and aggregations (e.g., `get_active_events_by_city`, `get_organizer_revenue_breakdown`, `get_available_seats_for_event`).
- Applies caching and eager loading (`select_related`, `prefetch_related`) to prevent N+1 query bottlenecks.

### 2.4 Domain Model Layer (`models/`)
- Encapsulates schema definitions, table constraints, indices, foreign keys, and minimal model-level validations.

### 2.5 Integration Layer (`integrations/`)
- Isolates external SDKs and protocols (`razorpay`, `qrcode`, `smtplib`) from core models.
- Standardizes error handling and retries for third-party failures.

