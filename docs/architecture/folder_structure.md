# MORROW - Folder Structure Reference

## 1. Complete Directory Tree

```text
MORROW/
├── manage.py
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── .gitignore
├── README.md
├── pytest.ini
│
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── logging.py
│
├── apps/
│   ├── __init__.py
│   ├── core/
│   ├── accounts/
│   ├── organizers/
│   ├── events/
│   ├── venues/
│   ├── ticketing/
│   ├── bookings/
│   ├── payments/
│   ├── qr_verification/
│   ├── notifications/
│   ├── reviews/
│   └── analytics/
│
├── templates/
│   ├── base/
│   ├── components/
│   ├── partials/
│   ├── public/
│   ├── accounts/
│   ├── organizer/
│   ├── admin/
│   ├── events/
│   ├── bookings/
│   ├── payments/
│   ├── tickets/
│   └── errors/
│
├── static/
│   ├── css/
│   │   ├── base/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   └── themes/
│   ├── js/
│   │   ├── core/
│   │   ├── components/
│   │   ├── services/
│   │   ├── modules/
│   │   └── pages/
│   ├── images/
│   │   ├── branding/
│   │   ├── events/
│   │   ├── icons/
│   │   └── placeholders/
│   └── vendor/
│
├── media/
│   ├── event_banners/
│   ├── organizer_logos/
│   ├── user_profiles/
│   └── qr_codes/
│
├── integrations/
│   ├── __init__.py
│   ├── razorpay/
│   ├── email/
│   └── qr_code/
│
├── common/
│   ├── __init__.py
│   ├── constants/
│   ├── decorators/
│   ├── exceptions/
│   ├── middleware/
│   ├── permissions/
│   ├── validators/
│   ├── helpers/
│   └── pagination/
│
├── database/
│   ├── scripts/
│   ├── seeders/
│   └── backups/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── functional/
│   ├── security/
│   └── fixtures/
│
├── docs/
│   ├── architecture/
│   ├── database/
│   ├── api/
│   ├── modules/
│   ├── setup/
│   ├── deployment/
│   └── testing/
│
├── scripts/
│   ├── setup/
│   ├── maintenance/
│   └── deployment/
│
└── deployment/
    ├── nginx/
    ├── gunicorn/
    └── production/
```

---

## 2. Directory Taxonomy & Responsibilities

| Directory | Purpose |
|---|---|
| `config/` | Application bootstrapping, routing root (`urls.py`), ASGI/WSGI entrypoints, multi-stage settings split. |
| `apps/` | Domain-specific Django applications encapsulating business functionality via services and selectors. |
| `templates/` | Django DTL templates partitioned into atomic layouts, reusable partials, and view templates. |
| `static/` | Client-side vanilla CSS, modular ES6 JavaScript, icons, branding images, and third-party assets. |
| `media/` | User-uploaded files (event graphics, organizer verification docs, user avatars, generated QRs). |
| `integrations/` | Low-level adapters for third-party SDKs (Razorpay API client, QR builder, SMTP mailer). |
| `common/` | System-wide cross-cutting concerns: custom middleware, shared validators, pagination, exceptions. |
| `database/` | Database migration utilities, fixtures, seeding scripts, and point-in-time backup handlers. |
| `tests/` | Cross-app integration test suites, end-to-end booking scenarios, and security penetration checks. |
| `docs/` | Architecture specs, API contracts, ER diagrams, deployment manuals, and developer onboarding. |
| `scripts/` | Shell and Python automation scripts for environment provisioning, database resets, and cleanup. |
| `deployment/` | Production configurations for Nginx reverse proxy, Gunicorn systemd services, and Docker assets. |

