# MORROW - API & URL Routing Architecture

## 1. Routing Strategy

MORROW employs a hybrid routing architecture:
1. **Server-Rendered Views (Django Templates):** Full-page views for public discovery, account authentication, customer dashboard, and organizer console.
2. **REST-Compliant Internal Endpoints (JSON APIs):** Interactive AJAX operations for seat reservation locking, cart updates, payment verification, gate scanning, and chart metrics.

All endpoints adhere to clean URL namespaces configured in `config/urls.py`.

---

## 2. API Endpoint Structure

### 2.1 Public & Event Discovery Endpoints
| HTTP Method | Route | Description | Response Type |
|---|---|---|---|
| `GET` | `/` | Platform landing page & trending events | HTML |
| `GET` | `/events/` | Filterable event catalog (city, category, date) | HTML |
| `GET` | `/events/<slug:slug>/` | Event detail, ticket tiers, venue overview | HTML |
| `GET` | `/api/v1/events/<int:event_id>/seats/` | Real-time seat layout & availability status | JSON |

### 2.2 Accounts & Authentication Endpoints
| HTTP Method | Route | Description | Response Type |
|---|---|---|---|
| `GET`, `POST` | `/accounts/login/` | User authentication | HTML / Redirect |
| `GET`, `POST` | `/accounts/register/` | User registration | HTML / Redirect |
| `POST` | `/accounts/logout/` | Terminate session | Redirect |
| `GET`, `POST` | `/accounts/profile/` | Customer profile management | HTML |

### 2.3 Booking & Reservation Endpoints
| HTTP Method | Route | Description | Response Type |
|---|---|---|---|
| `POST` | `/bookings/reserve-seats/` | Temporarily lock selected seats (10-min hold) | JSON |
| `DELETE` | `/bookings/release-seats/` | Release held seat locks | JSON |
| `GET` | `/bookings/checkout/<uuid:booking_ref>/` | Checkout summary page | HTML |
| `GET` | `/bookings/history/` | Customer booking records | HTML |

### 2.4 Payment & Gateway Endpoints
| HTTP Method | Route | Description | Response Type |
|---|---|---|---|
| `POST` | `/payments/razorpay/create-order/` | Initialize Razorpay order with server amount | JSON |
| `POST` | `/payments/razorpay/verify/` | Verify payment signature and finalize booking | JSON |
| `POST` | `/payments/webhooks/razorpay/` | Async gateway webhook listener | JSON |

### 2.5 QR Gate Verification Endpoints
| HTTP Method | Route | Description | Response Type |
|---|---|---|---|
| `GET` | `/verify/scanner/` | Gatekeeper camera scanning view | HTML |
| `POST` | `/verify/scan-ticket/` | Verify scanned QR payload, validate admission | JSON |

### 2.6 System & Health Endpoints
| HTTP Method | Route | Description | Response Type |
|---|---|---|---|
| `GET` | `/health/` | Service liveness and readiness probe | JSON |

