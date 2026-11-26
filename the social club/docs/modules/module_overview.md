# MORROW - Domain Module Responsibilities

The MORROW system is partitioned into 12 distinct, decoupled Django applications under `apps/`. Each application adheres to a strict single-responsibility boundary.

---

## 1. Core (`apps/core`)
- **Mission:** Shared foundation, health checks, system-wide base models (e.g., `TimeStampedModel`, `UUIDModel`), and custom context processors.
- **Dependencies:** None (root foundational app).

## 2. Accounts (`apps/accounts`)
- **Mission:** User lifecycle, authentication, profile management, password resets, and Role-Based Access Control (RBAC: Customer, Organizer, Admin/Staff, Gate Scanner).
- **Key Responsibilities:**
  - Custom User model (`AbstractUser` with verified email login).
  - Customer profile attributes.
  - Role validation & permission decorators.

## 3. Organizers (`apps/organizers`)
- **Mission:** Organizer onboarding, identity verification documents, organization branding, and administrative approval workflows.
- **Key Responsibilities:**
  - Business KYC / tax / registration handling.
  - Multi-tenant event organizer isolation.
  - Organizer settings and payout profile.

## 4. Events (`apps/events`)
- **Mission:** Event lifecycle management, categorization, multi-day scheduling, and public discovery.
- **Key Responsibilities:**
  - Event CRUD and publishing workflow (`Draft` -> `Under Review` -> `Published` -> `Completed` -> `Cancelled`).
  - Category taxonomies and tag filtering.
  - Geo/city-based event search and filtering selectors.

## 5. Venues (`apps/venues`)
- **Mission:** Venue specifications, location mapping, and seating geometry.
- **Key Responsibilities:**
  - Venue directory and capacity configuration.
  - Seating layout structures (Sections, Rows, Seat Numbers, GA zones).
  - Stage orientation and floor plan representations.

## 6. Ticketing (`apps/ticketing`)
- **Mission:** Ticket types, pricing policies, inventory limits, and availability state.
- **Key Responsibilities:**
  - Tiered ticket inventory (VIP, Early Bird, Regular).
  - Dynamic pricing parameters and discount codes.
  - Inventory balance calculations.

## 7. Bookings (`apps/bookings`)
- **Mission:** Order lifecycle, seat reservation holds, cart checkout, and booking expiration.
- **Key Responsibilities:**
  - Atomic seat locking with 10-minute expiration countdown.
  - Cart composition and checkout orchestration.
  - Booking reference generation and customer booking histories.

## 8. Payments (`apps/payments`)
- **Mission:** Razorpay payment gateway integration, webhook signature validation, transaction audit trails, and refunds.
- **Key Responsibilities:**
  - Creation of Razorpay orders (`razorpay_order_id`).
  - Cryptographic verification of `razorpay_signature` via HMAC-SHA256.
  - Webhook ingest and idempotent processing.
  - Refund record tracking.

## 9. QR Verification (`apps/qr_verification`)
- **Mission:** Secure QR ticket generation and rapid gate entry validation.
- **Key Responsibilities:**
  - Generation of encrypted, signed QR payloads containing ticket UUID + HMAC token.
  - Gatekeeper scanning interface.
  - Real-time duplicate scan detection and admission event logging.

## 10. Notifications (`apps/notifications`)
- **Mission:** Transactional customer messaging (Email/SMS/Push).
- **Key Responsibilities:**
  - Booking confirmation emails with PDF/inline QR ticket attachments.
  - Event reminder dispatches (24 hours prior).
  - Cancellation and refund notifications.

## 11. Reviews (`apps/reviews`)
- **Mission:** Post-event attendee feedback, ratings, and moderation.
- **Key Responsibilities:**
  - Verified-buyer-only review submission enforcement.
  - Star ratings and attendee testimonials.
  - Content moderation flags.

## 12. Analytics (`apps/analytics`)
- **Mission:** Business intelligence, revenue reporting, and operational dashboards.
- **Key Responsibilities:**
  - Organizer revenue dashboards (sales velocity, ticket breakdowns).
  - Platform-level admin metric aggregations.
  - Export utilities (CSV / Financial summaries).

