# MORROW - Entity Relationship Diagram (ERD)

## Conceptual Entity Relationship Diagram

```mermaid
erDiagram
    USER ||--o| USER_PROFILE : has
    USER ||--o| ORGANIZER_PROFILE : operates_as
    USER ||--o{ BOOKING : places
    USER ||--o{ REVIEW : writes
    
    ORGANIZER_PROFILE ||--o{ EVENT : organizes
    
    CATEGORY ||--o{ EVENT : categorizes
    VENUE ||--o{ VENUE_SEAT_LAYOUT : defines
    VENUE ||--o{ EVENT : hosts
    
    EVENT ||--o{ EVENT_SCHEDULE : schedules
    EVENT ||--o{ TICKET_TYPE : offers
    EVENT ||--o{ BOOKING : receives
    EVENT ||--o{ REVIEW : receives
    
    TICKET_TYPE ||--o{ BOOKING_ITEM : specifies
    VENUE_SEAT_LAYOUT ||--o{ SEAT : contains
    SEAT ||--o{ SEAT_RESERVATION : locks
    SEAT ||--o{ BOOKING_ITEM : allocates
    
    BOOKING ||--|{ BOOKING_ITEM : includes
    BOOKING ||--o| PAYMENT : pays_with
    
    PAYMENT ||--o{ REFUND : processes
    
    BOOKING_ITEM ||--|| QR_TICKET : generates
    QR_TICKET ||--o{ ADMISSION_LOG : logs_entry
    
    USER ||--o{ NOTIFICATION : receives
```

---

## Cardinality & Key Relationship Highlights

1. **User to Organizer Profile (1:0..1):** A user account may upgrade and register as an approved event organizer.
2. **Event to Ticket Types (1:N):** An event can offer multiple pricing tiers (e.g., Early Bird, VIP, Balcony).
3. **Venue to Seats (1:N):** Venues define fixed physical seating geometry or open-standing capacities.
4. **Booking to Booking Items (1:N):** One checkout transaction can contain tickets for multiple attendees or seats.
5. **Booking Item to QR Ticket (1:1):** Every individual admitted ticket receives its own distinct, cryptographically signed QR token to prevent credential sharing.
6. **QR Ticket to Admission Logs (1:N):** Tracks all scan attempts at the gate (admissions, timestamped duplicate scan flags).

