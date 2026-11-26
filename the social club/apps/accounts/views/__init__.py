"""Package initialization for accounts.views."""
from .auth_views import (
    admin_dashboard_view,
    login_view,
    logout_view,
    register_view,
    root_redirect_view,
    user_dashboard_view,
)

__all__ = [
    "root_redirect_view",
    "login_view",
    "register_view",
    "logout_view",
    "user_dashboard_view",
    "admin_dashboard_view",
]
