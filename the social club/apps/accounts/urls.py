"""URL routing for accounts and dashboards."""
from django.urls import path

from apps.accounts.views import (
    admin_dashboard_view,
    login_view,
    logout_view,
    register_view,
    root_redirect_view,
    user_dashboard_view,
)

app_name = "accounts"

urlpatterns = [
    path("", root_redirect_view, name="root"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", user_dashboard_view, name="user_dashboard"),
    path("admin-panel/dashboard/", admin_dashboard_view, name="admin_dashboard"),
]
