# MORROW - Event Management & Ticket Booking System

MORROW is a modern, enterprise-grade Event Management & Ticket Booking web application engineered for high-throughput ticketing, real-time seat reservation, secure payment workflows via Razorpay, tamper-proof QR code admission verification, and comprehensive event lifecycle analytics.

---

## 1. Project Overview & Tech Stack

- **Backend:** Python 3.11+, Django 5.0 (Clean Modular Architecture / Selector-Service Pattern)
- **Frontend:** Semantic HTML5, Modular CSS3, Vanilla JavaScript (ES6+ modular, no heavy framework dependencies)
- **Database:** PostgreSQL (production), SQLite (local quick-boot/testing)
- **Payment Processing:** Razorpay Gateway (Test & Live Mode with Webhook verification)
- **Verification:** Secure Python `qrcode` generation with HMAC signature and duplicate-scan prevention
- **Communications:** SMTP / Django Email Backend with async event hooks
- **Version Control:** Git

---

## 2. Architecture & Design Principles

MORROW is designed adhering to proven software architecture principles:
1. **Separation of Concerns:** Business logic lives strictly in `services/`, database reads/queries in `selectors/`, request orchestration in `views/`, and data contracts in `models/` and `forms/`.
2. **Modular Django Apps:** Functionality is distributed across 12 domain-specific apps (`apps/accounts`, `apps/events`, `apps/ticketing`, `apps/bookings`, etc.) avoiding monolithic anti-patterns.
3. **Robust Security:** Zero hardcoded credentials, full environment separation (`config/settings/`), CSRF protection, role-based access control, cryptographic webhook validation, and timing-attack-safe QR scanning.
4. **Maintainability & Testability:** Dedicated unit, integration, and security test harnesses with pre-configured `pytest` suite.

---

## 3. Directory Layout Overview

```text
MORROW/
├── manage.py                   # Django CLI entrypoint
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development and testing dependencies
├── .env.example                # Canonical environment variable template
├── .gitignore                  # Git exclusions for secrets, media, cache
├── pytest.ini                  # Pytest test runner configuration
│
├── config/                     # Application configurations & settings split
├── apps/                       # 12 Modular Django domain applications
├── templates/                  # Layered HTML templates (base, components, roles)
├── static/                     # Modular CSS, ES6 JS, images, and vendors
├── media/                      # Uploaded assets (banners, avatars, generated QRs)
├── integrations/               # External client wrappers (Razorpay, QR, SMTP)
├── common/                     # Cross-cutting middleware, permissions, helpers
├── database/                   # DB seeders, SQL migrations, scripts, backups
├── tests/                      # Global integration, functional, security tests
├── docs/                       # In-depth architectural & operational documentation
├── scripts/                    # Setup, maintenance, and deployment utilities
└── deployment/                 # Nginx, Gunicorn, systemd production setups
```

---

## 4. Documentation Index

Detailed architectural documentation is organized under [`docs/`](file:///run/media/jevin/Box%20A/The-Social-Club/docs):

- **System Architecture:** [`docs/architecture/system_architecture.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/architecture/system_architecture.md)
- **Folder Structure Reference:** [`docs/architecture/folder_structure.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/architecture/folder_structure.md)
- **Database Architecture & Schema:** [`docs/database/database_design.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/database/database_design.md)
- **Entity Relationship Model (ERD):** [`docs/database/erd.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/database/erd.md)
- **Domain Modules Overview:** [`docs/modules/module_overview.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/modules/module_overview.md)
- **API & Endpoint Specifications:** [`docs/api/api_structure.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/api/api_structure.md)
- **Local Development Setup:** [`docs/setup/local_setup.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/setup/local_setup.md)
- **Deployment & Production Hardening:** [`docs/deployment/deployment_guide.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/deployment/deployment_guide.md)
- **Testing & Quality Assurance:** [`docs/testing/testing_strategy.md`](file:///run/media/jevin/Box%20A/The-Social-Club/docs/testing/testing_strategy.md)

---

## 5. Development Status

> [!NOTE]
> **Current Phase: Phase 1 (Project Architecture & Foundational Organization)**  
> The structural skeleton, configuration environments, package initializations, and design specifications have been established. Feature implementation, model migrations, and views will be executed in Phase 2 upon architectural sign-off.
