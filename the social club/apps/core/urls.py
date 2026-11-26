"""Core app URL routing."""
from django.urls import path
from apps.core.views.health import health_check

app_name = "core"

urlpatterns = [
    path("health/", health_check, name="health_check"),
]
