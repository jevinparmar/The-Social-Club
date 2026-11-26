"""Authentication and dashboard views for MORROW."""
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from apps.accounts.forms import LoginForm, RegisterForm
from apps.accounts.models import User
from apps.accounts.permissions import anonymous_required, role_required
from apps.accounts.services import authenticate_and_login, register_user


def root_redirect_view(request):
    """Redirect root URL to dashboard if authenticated, otherwise to login."""
    if request.user.is_authenticated:
        if request.user.is_admin_role:
            return redirect("/admin-panel/dashboard/")
        return redirect("/dashboard/")
    return redirect("/login/")


@anonymous_required()
def login_view(request):
    """Handle login for both ADMIN and USER roles."""
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user, redirect_url = authenticate_and_login(
            request,
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            remember_me=form.cleaned_data.get("remember_me", False),
        )
        if user is not None:
            return redirect(redirect_url)
        form.add_error(None, "Invalid email address or password.")

    return render(request, "accounts/login.html", {"form": form})


@anonymous_required()
def register_view(request):
    """Handle public registration for USER accounts only."""
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        register_user(
            full_name=form.cleaned_data["full_name"],
            email=form.cleaned_data["email"],
            phone_number=form.cleaned_data["phone_number"],
            password=form.cleaned_data["password"],
        )
        messages.success(request, "Account created successfully. Please sign in.")
        return redirect("/login/")

    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    """Destroy authenticated session and redirect to login."""
    logout(request)
    return redirect("/login/")


@role_required(User.Role.USER)
def user_dashboard_view(request):
    """Blank User Side Dashboard."""
    return render(request, "accounts/user_dashboard.html")


@role_required(User.Role.ADMIN)
def admin_dashboard_view(request):
    """Blank Admin Side Dashboard."""
    return render(request, "admin/admin_dashboard.html")

