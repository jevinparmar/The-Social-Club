"""
Health check view for system monitoring.
"""
from django.http import JsonResponse


def health_check(request):
    """Simple liveness probe endpoint."""
    return JsonResponse({"status": "healthy", "service": "morrow-events"})

