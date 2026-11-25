# MORROW: Project Architecture & Folder Structure Report

**Phase:** Phase 1 - Project Architecture & Foundational Structure  
**Status:** Completed & Verified  
**Date:** 2026-11-25  

---

## 1. Executive Summary

As Senior Software Architect and Full-Stack Project Architect, Phase 1 has been executed strictly within scope:
- Full directory architecture organized according to clean modular Django standards.
- Clear separation of concerns between business services, selectors, views, integrations, and static assets.
- Foundational configurations created without implementing premature business features or mock database operations.
- Foundational architectural documentation prepared.

---

## 2. Complete Folder Tree

```text
MORROW/
├── manage.py                                 # Django CLI entrypoint
├── requirements.txt                          # Production dependencies
├── requirements-dev.txt                      # Development & QA dependencies
├── .env.example                              # Environment configuration template
├── .gitignore                                # Git ignore rules (credentials, media, cache)
├── README.md                                 # Project overview & documentation index
├── pytest.ini                                # Test runner configuration
│
├── config/                                   # Project Configuration Root
│   ├── __init__.py
│   ├── settings/                             # Environment-split settings
│   │   ├── __init__.py                       # Environment dynamic selector
│   │   ├── base.py                           # Core settings & app declarations
│   │   ├── development.py                    # Local debug settings & sqlite fallback
│   │   ├── production.py                     # Hardened security & postgres settings
│   │   └── testing.py                        # In-memory fast test settings
│   ├── urls.py                               # Top-level URL routing table
│   ├── asgi.py                               # ASGI entrypoint
│   ├── wsgi.py                               # WSGI entrypoint
│   └── logging.py                            # Structured logging configuration
│
├── apps/                                     # 12 Modular Domain Applications
│   ├── __init__.py
│   ├── core/                                 # Shared base models, health check views
│   ├── accounts/                             # Custom user model, auth, profiles, RBAC
│   ├── organizers/                           # Organizer profile, KYC, verification
│   ├── events/                               # Event catalog, schedules, categories
│   ├── venues/                               # Venues, seating geometry, section layouts
│   ├── ticketing/                            # Ticket types, pricing, inventory
│   ├── bookings/                             # Cart checkout, seat hold locks, expiration
│   ├── payments/                             # Razorpay orders, webhook signature verification
│   ├── qr_verification/                      # QR code crypto generation, gate admission scan
│   ├── notifications/                        # Transactional email & booking confirmation
│   ├── reviews/                              # Verified attendee feedback & ratings
│   └── analytics/                            # Organizer revenue & platform sales reports
│   │   └── [Each app contains]:
│   │       ├── admin.py                      # Django admin integration
│   │       ├── apps.py                       # AppConfig declaration
│   │       ├── permissions.py                # Role-based permissions
│   │       ├── signals.py                    # Domain signal dispatchers
│   │       ├── tasks.py                      # Asynchronous tasks
│   │       ├── urls.py                       # Domain route definitions
│   │       ├── validators.py                 # Custom data validators
│   │       ├── forms/                        # Django Forms
│   │       ├── migrations/                   # Schema migrations
│   │       ├── models/                       # Entity schemas
│   │       ├── selectors/                    # Optimized read queries
│   │       ├── services/                     # Business logic mutations
│   │       ├── tests/                        # App-specific unit tests
│   │       └── views/                        # View controllers
│
├── templates/                                # Layered HTML Templates
│   ├── base/                                 # Base layouts & head boilerplate
│   ├── components/                           # Navbar, footer, buttons, cards, modals
│   ├── partials/                             # Dynamic HTML snippets
│   ├── public/                               # Landing, search, discovery views
│   ├── accounts/                             # Login, register, profile views
│   ├── organizer/                            # Organizer dashboard & event management
│   ├── admin/                                # Platform administration views
│   ├── events/                               # Event detail & schedules
│   ├── bookings/                             # Seat picker & cart checkout
│   ├── payments/                             # Payment redirect & summary
│   ├── tickets/                              # Customer digital ticket & PDF view
│   └── errors/                               # 400, 403, 404, 500 error pages
│
├── static/                                   # Static Assets (Vanilla HTML/CSS/JS)
│   ├── css/                                  # Modular styles (base, components, layouts, pages, themes)
│   ├── js/                                   # Modular ES6 scripts (core, components, services, modules, pages)
│   ├── images/                               # Branding, icons, placeholders, events
│   └── vendor/                               # External client libraries
│
├── media/                                    # Uploaded & Generated Media
│   ├── event_banners/                        # Event artwork uploads
│   ├── organizer_logos/                      # Organizer branding
│   ├── user_profiles/                        # User avatars
│   └── qr_codes/                             # Generated admission QR images
│
├── integrations/                             # Isolated Third-Party Integrations
│   ├── __init__.py
│   ├── razorpay/                             # Razorpay client & signature helper
│   ├── email/                                # SMTP email dispatcher & HTML builder
│   └── qr_code/                              # QR code cryptographic generator
│
├── common/                                   # Cross-Cutting Concerns
│   ├── __init__.py
│   ├── constants/                            # Enums, statuses, error codes
│   ├── decorators/                           # View & function decorators
│   ├── exceptions/                           # Domain-level exceptions
│   ├── middleware/                           # Request/response security middleware
│   ├── permissions/                          # Role validation logic
│   ├── validators/                           # Common regex & format validators
│   ├── helpers/                              # Currency, date, formatting utilities
│   └── pagination/                           # Standard pagination classes
│
├── database/                                 # Database Scripts & Seeders
│   ├── scripts/                              # Custom maintenance scripts
│   ├── seeders/                              # Development database seeders
│   └── backups/                              # Backup utility placeholders
│
├── tests/                                    # System-Wide Integration Tests
│   ├── unit/                                 # Cross-cutting unit tests
│   ├── integration/                          # Multi-app workflow tests
│   ├── functional/                           # User scenario flows
│   ├── security/                             # Authorization & signature tests
│   └── fixtures/                             # Shared test data & factory objects
│
├── docs/                                     # Comprehensive Documentation
│   ├── architecture/                         # System architecture & structure docs
│   ├── database/                             # Database design & ERD diagrams
│   ├── api/                                  # API routing specifications
│   ├── modules/                              # Module responsibility catalogs
│   ├── setup/                                # Local development setup guide
│   ├── deployment/                           # Production hardening manual
│   └── testing/                              # Testing & QA strategy
│
├── scripts/                                  # Operational Automation Scripts
│   ├── setup/                                # Provisioning scripts
│   ├── maintenance/                          # Cleanup & stale lock releases
│   └── deployment/                           # Build & deploy scripts
│
└── deployment/                               # Production Server Configuration
    ├── nginx/                                # Reverse proxy configs
    ├── gunicorn/                             # WSGI process configs
    └── production/                           # Environment orchestration templates
```

---

## 3. Django App Responsibilities

1. **`core`**: Base models (`TimeStampedModel`), system-wide context processors, and health check endpoints.
2. **`accounts`**: Custom user model, login/logout, registration, profile updates, and role-based permissions.
3. **`organizers`**: Organizer business profiles, verification documents, and organizer dashboard interfaces.
4. **`events`**: Event creation, categorization, schedule definitions, and city/geo discovery.
5. **`venues`**: Venue directory, seating layouts, sections, and row/seat numbering.
6. **`ticketing`**: Ticket tier definitions (VIP, Early Bird, GA), pricing structures, and inventory caps.
7. **`bookings`**: Checkout workflow, atomic 10-minute seat locking, and booking histories.
8. **`payments`**: Razorpay payment order initialization, webhook listener, HMAC signature validation, and refund tracking.
9. **`qr_verification`**: Cryptographic QR code generation and gatekeeper admission scanning with duplicate scan detection.
10. **`notifications`**: Transactional email notifications (order receipts, QR delivery, event reminders).
11. **`reviews`**: Verified purchaser event ratings and feedback management.
12. **`analytics`**: Organizer ticket sales analytics, platform revenue reports, and data exports.

---

## 4. Frontend Architecture

- **HTML5:** Modular Django Template Language (DTL) layout: `base/` contains boilerplate, `components/` provides reusable elements (nav, footer, cards, modals), and role-specific folders (`organizer/`, `admin/`, `public/`) isolate UI views.
- **CSS3:** Atomic architecture separating CSS into `base/` (reset, typography, CSS variables), `components/` (buttons, forms, cards), `layouts/` (grid, flexbox, dashboards), `pages/` (page-specific styling), and `themes/`.
- **Vanilla JavaScript:** ES6+ modular architecture cleanly split into:
  - `core/`: HTTP client wrappers, CSRF token extractors.
  - `services/`: Razorpay checkout handler, QR camera scanner wrapper.
  - `components/`: Seat selection grid, countdown timer for seat locking.
  - `pages/`: Page-specific view orchestrators.

---

## 5. Database Architecture & Concurrency Preparation

- **Primary Database:** PostgreSQL 15+.
- **Concurrency Protection (Seat Overbooking Prevention):**
  - Distinct `seat_reservations` holding table.
  - Atomic transactions using `django.db.transaction.atomic()` combined with `SELECT ... FOR UPDATE` row-level locks.
  - Expirable lock timestamps (`expires_at = NOW() + INTERVAL '10 minutes'`) automatically checked prior to payment capture.
- **Data Integrity:** Strict foreign keys, composite indexes (`events(city, status, start_time)`), unique constraints on gateway order IDs, and immutable admission logs.

---

## 6. Integrations & Security Preparation

- **Razorpay Integration:** Isolated in `integrations/razorpay/` with signature verification logic (`hmac.new(secret, payload, sha256)`).
- **QR Code Verification:** Cryptographically signed tokens preventing forged tickets or brute-force scanning.
- **Security Posture:**
  - Zero committed credentials (`.env.example` template provided; `.env` strictly gitignored).
  - Production settings configure `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `X_FRAME_OPTIONS = "DENY"`, and HSTS.

---

## 7. Files Created

1. **Foundational Configurations:**
   - [`manage.py`](file:///run/media/jevin/Box%20A/The-Social-Club/manage.py)
   - [`requirements.txt`](file:///run/media/jevin/Box%20A/The-Social-Club/requirements.txt)
   - [`requirements-dev.txt`](file:///run/media/jevin/Box%20A/The-Social-Club/requirements-dev.txt)
   - [`.env.example`](file:///run/media/jevin/Box%20A/The-Social-Club/.env.example)
   - [`.gitignore`](file:///run/media/jevin/Box%20A/The-Social-Club/.gitignore)
   - [`pytest.ini`](file:///run/media/jevin/Box%20A/The-Social-Club/pytest.ini)
   - [`config/settings/__init__.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/settings/__init__.py)
   - [`config/settings/base.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/settings/base.py)
   - [`config/settings/development.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/settings/development.py)
   - [`config/settings/production.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/settings/production.py)
   - [`config/settings/testing.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/settings/testing.py)
   - [`config/urls.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/urls.py)
   - [`config/wsgi.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/wsgi.py)
   - [`config/asgi.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/asgi.py)
   - [`config/logging.py`](file:///run/media/jevin/Box%20A/The-Social-Club/config/logging.py)

2. **Documentation Suite:**
   - [`README.md`](file:///run/media/jevin/Box%20A/The-Social-Club/README.md)
   - [`docs/architecture/system_architecture.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/architecture/system_architecture.md)
   - [`docs/architecture/folder_structure.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/architecture/folder_structure.md)
   - [`docs/database/database_design.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/database/database_design.md)
   - [`docs/database/erd.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/database/erd.md)
   - [`docs/modules/module_overview.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/modules/module_overview.md)
   - [`docs/api/api_structure.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/api/api_structure.md)
   - [`docs/setup/local_setup.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/setup/local_setup.md)
   - [`docs/deployment/deployment_guide.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/deployment/deployment_guide.md)
   - [`docs/testing/testing_strategy.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/testing/testing_strategy.md)
   - [`apps/core/views/health.py`](file:///run/media/jevin/Box%20A/The-Social-Club/apps/core/views/health.py)

3. **Application Skeleton:**
   - Standard modular packages across all 12 apps (`admin.py`, `apps.py`, `urls.py`, `permissions.py`, `validators.py`, `signals.py`, `tasks.py`, `models/`, `views/`, `services/`, `selectors/`, `forms/`, `migrations/`, `tests/`).

---

## 8. Pending Architectural Decisions for Phase 2

1. **Background Task Runner:** Choosing between Celery (with Redis) vs. Django-Q2 for asynchronous email dispatch and expired seat lock reclamation.
2. **Real-Time Seat Updates:** Evaluating WebSocket support via Django Channels vs. light client polling (SSE or HTTP GET every 10s) for live seat map updates.
3. **Storage Backend for Media:** Selecting local file storage with Nginx caching vs. AWS S3 / Cloudflare R2 bucket for production event banner uploads.

---
*Phase 1 is complete. Awaiting user review and authorization to proceed to Phase 2.*

