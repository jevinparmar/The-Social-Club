# MORROW - Database Architecture & Schema Design

## 1. Storage Engine & Database Choice

- **Database:** PostgreSQL 15+ (Production)
- **Driver:** `psycopg` (v3) with connection pooling (`CONN_MAX_AGE=600`)
- **Key Characteristics:** ACID compliance, row-level locking (`SELECT ... FOR UPDATE`), JSONB support for flexible metadata, and strict foreign key integrity.

---

## 2. Core Entities & Relational Map

### 2.1 Accounts & Authentication
- `users`: Core user entity extending Django AbstractUser (email as username, password hash, role flags).
- `user_profiles`: Avatar, phone number, bio, city, communication preferences.

### 2.2 Organizers
- `organizer_profiles`: Organization name, registration number, verification status (`pending`, `verified`, `rejected`), commission rate, contact info.

### 2.3 Events & Venues
- `venues`: Venue name, address, city, state, postal code, total capacity, geo-coordinates.
- `venue_seat_layouts`: Section definitions, row maps, seat numbering matrix, tier assignments.
- `event_categories`: Music, Tech, Sports, Arts, Networking, Comedy, etc.
- `events`: Title, slug, description, category FK, organizer FK, venue FK, banner URL, start time, end time, status (`draft`, `published`, `cancelled`, `completed`).
- `event_schedules`: Detailed daily/session timelines for multi-day or multi-track events.

### 2.4 Ticketing & Inventory
- `ticket_types`: General Admission, VIP, Early Bird, Student (price, quantity allocated, sales start/end, max per order).
- `seats`: Specific physical or virtual seat coordinates (`section`, `row`, `number`, status).
- `seat_reservations`: Temporary reservation lock table with timestamped expiration (`reserved_at`, `expires_at`, `session_id`/`user_id`).

### 2.5 Bookings & Transactions
- `bookings`: Booking reference number, user FK, event FK, total amount, discount, tax, status (`pending`, `confirmed`, `cancelled`, `expired`, `refunded`), creation timestamp.
- `booking_items`: Ticket type FK, seat FK (nullable for open seating), unit price, attendee name.

### 2.6 Payments & Financial Audits
- `payments`: Transaction reference, booking FK, payment gateway (`razorpay`), razorpay_order_id, razorpay_payment_id, razorpay_signature, amount, currency, status (`created`, `captured`, `failed`, `refunded`), response payload (JSONB).
- `refunds`: Payment FK, refund amount, reason, razorpay_refund_id, status.

### 2.7 Verification & Access Control
- `qr_tickets`: Booking item FK, unique cryptographically signed verification token, QR image path, issued timestamp, check-in status (`valid`, `checked_in`, `revoked`).
- `admission_logs`: QR ticket FK, scanned_at, scanned_by (verifier user FK), gate identifier, scan result (`admitted`, `duplicate_attempt`, `invalid`).

---

## 3. High-Concurrency Seat Locking Strategy

To prevent race conditions when thousands of users attempt to purchase limited tickets simultaneously:
1. When user initiates seat selection: An entry is inserted into `seat_reservations` with status `LOCKED` and `expires_at = NOW() + INTERVAL '10 minutes'`.
2. A database row-level lock (`SELECT ... FOR UPDATE`) is acquired during the reservation transaction.
3. If checkout completes: The reservation transitions to `BOOKED` within the atomic payment confirmation transaction.
4. If payment fails or timeout expires: A lightweight background worker or selector evaluation automatically releases expired locks.

---

## 4. Indexing & Optimization Strategy

1. **Composite Indices:**
   - `events(city, status, start_time)` - Supports high-frequency public event searches.
   - `bookings(user_id, status, created_at)` - Powers customer booking history pages.
   - `qr_tickets(token_hash)` - Enables sub-millisecond gate check-in lookups.
2. **Unique Constraints:**
   - Unique seat allocation per event schedule: `UNIQUE(event_schedule_id, seat_id)` where status is active.
   - Unique gateway references: `UNIQUE(razorpay_order_id)`, `UNIQUE(razorpay_payment_id)`.

