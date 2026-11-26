# MORROW - Testing & Quality Assurance Strategy

## 1. Testing Philosophy

MORROW adopts a test pyramid strategy with comprehensive coverage across unit, integration, and security layers:

```
          / \
         /   \       End-to-End & Security Checks (Top)
        /-----\
       /       \     Integration & Workflow Tests (Middle)
      /---------\
     /           \   Unit Tests: Services, Selectors, Models (Base)
    /-------------\
```

---

## 2. Test Classification

### 2.1 Unit Tests (`apps/<app_name>/tests/`)
- **`test_models.py`:** Field validation, string representations, default values, and model constraint checks.
- **`test_services.py`:** Pure business logic execution (seat reservation expiry, booking total calculation, payment status transitions).
- **`test_views.py`:** View response status codes, template rendering, and context data presence.

### 2.2 Integration Tests (`tests/integration/`)
- End-to-end booking flow: Seat selection -> Locking hold -> Razorpay order creation -> Webhook verification -> Ticket & QR generation -> Email notification dispatch.
- Gatekeeper validation flow: Scanned QR ticket verification -> Database status transition -> Repeated scan attempt rejection.

### 2.3 Security Tests (`tests/security/`)
- Authorization bypass tests: Customer attempting to access organizer dashboards or event management mutations.
- CSRF protection validation on state-modifying requests.
- Razorpay webhook signature spoofing prevention tests.
- Replay attack checks on QR tickets.

---

## 3. Test Fixtures & Factories

- Shared factory classes using `factory-boy` and `faker` will reside in `tests/fixtures/` to produce realistic event dates, ticket batches, user roles, and payment payloads without database pollution.

