"""
URL Configuration for MORROW Event Management & Ticket Booking System.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Core system endpoints (health check, landing)
    path("", include("apps.core.urls", namespace="core")),
    path("", include("apps.accounts.urls", namespace="accounts")),
    
    # App route namespaces
    path("organizer/", include("apps.organizers.urls", namespace="organizers")),
    path("events/", include("apps.events.urls", namespace="events")),
    path("venues/", include("apps.venues.urls", namespace="venues")),
    path("ticketing/", include("apps.ticketing.urls", namespace="ticketing")),
    path("bookings/", include("apps.bookings.urls", namespace="bookings")),
    path("payments/", include("apps.payments.urls", namespace="payments")),
    path("verify/", include("apps.qr_verification.urls", namespace="qr_verification")),
    path("notifications/", include("apps.notifications.urls", namespace="notifications")),
    path("reviews/", include("apps.reviews.urls", namespace="reviews")),
    path("analytics/", include("apps.analytics.urls", namespace="analytics")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

