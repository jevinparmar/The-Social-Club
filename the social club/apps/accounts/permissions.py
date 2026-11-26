"""Permission classes and role-based access decorators for accounts."""
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def role_required(allowed_role):
    """
    Decorator to enforce server-side role-based access control.
    - Unauthenticated users are redirected to login.
    - Authenticated users without the required role receive 403 Forbidden.
    """
    def decorator(view_func):
        @login_required(login_url="/login/")
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role != allowed_role:
                raise PermissionDenied("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def anonymous_required(redirect_to=None):
    """Redirect already authenticated users to their respective dashboard."""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.is_admin_role:
                    return redirect("/admin-panel/dashboard/")
                return redirect("/dashboard/")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
