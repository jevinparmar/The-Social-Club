"""Authentication business logic services."""
from django.contrib.auth import authenticate, login

from apps.accounts.models import User


def register_user(*, full_name: str, email: str, phone_number: str, password: str) -> User:
    """
    Register a new standard USER account.
    Admin accounts can never be created through public registration.
    """
    return User.objects.create_user(
        email=email,
        full_name=full_name,
        phone_number=phone_number,
        password=password,
        role=User.Role.USER,
    )


def authenticate_and_login(request, *, email: str, password: str, remember_me: bool = False):
    """
    Authenticate user credentials and establish session.
    Returns (user, redirect_url) if valid, or (None, None) if invalid.
    """
    user = authenticate(request, username=email.strip().lower(), password=password)
    if user is None or not user.is_active:
        return None, None

    login(request, user)

    if not remember_me:
        request.session.set_expiry(0)
    else:
        request.session.set_expiry(1209600)  # 14 days

    redirect_url = "/admin-panel/dashboard/" if user.is_admin_role else "/dashboard/"
    return user, redirect_url

