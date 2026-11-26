"""Authentication forms for login and user registration."""
import re
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from apps.accounts.models import User


class LoginForm(forms.Form):
    """Form for user and admin login."""

    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                "id": "id_email",
                "class": "form-input",
                "placeholder": "name@company.com",
                "autocomplete": "email",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "id": "id_password",
                "class": "form-input",
                "placeholder": "Enter your password",
                "autocomplete": "current-password",
                "required": True,
            }
        ),
    )
    remember_me = forms.BooleanField(
        label="Remember me",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "id": "id_remember_me",
                "class": "form-checkbox",
            }
        ),
    )

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()


class RegisterForm(forms.Form):
    """Form for public user registration (USER role only)."""

    full_name = forms.CharField(
        label="Full Name",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "id": "id_full_name",
                "class": "form-input",
                "placeholder": "Enter your full name",
                "autocomplete": "name",
                "required": True,
            }
        ),
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                "id": "id_email",
                "class": "form-input",
                "placeholder": "name@company.com",
                "autocomplete": "email",
                "required": True,
            }
        ),
    )
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "id": "id_phone_number",
                "class": "form-input",
                "placeholder": "+91 98765 43210",
                "autocomplete": "tel",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "id": "id_password",
                "class": "form-input",
                "placeholder": "Create a strong password",
                "autocomplete": "new-password",
                "required": True,
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "id": "id_confirm_password",
                "class": "form-input",
                "placeholder": "Re-enter your password",
                "autocomplete": "new-password",
                "required": True,
            }
        ),
    )
    terms_accepted = forms.BooleanField(
        label="I agree to the Terms and Conditions",
        required=True,
        error_messages={"required": "You must accept the Terms and Conditions to create an account."},
        widget=forms.CheckboxInput(
            attrs={
                "id": "id_terms_accepted",
                "class": "form-checkbox",
                "required": True,
            }
        ),
    )

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"].strip()
        if len(full_name) < 2:
            raise ValidationError("Full name must be at least 2 characters.")
        return full_name

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("An account with this email address already exists.")
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"].strip()
        digits = re.sub(r"\D", "", phone)
        if len(digits) < 7 or len(digits) > 15:
            raise ValidationError("Please enter a valid phone number (7 to 15 digits).")
        return phone

    def clean_password(self):
        password = self.cleaned_data.get("password", "")
        has_upper = bool(re.search(r"[A-Z]", password))
        has_lower = bool(re.search(r"[a-z]", password))
        has_digit = bool(re.search(r"\d", password))
        has_special = bool(re.search(r"[^A-Za-z0-9]", password))
        if not (has_upper and has_lower and has_digit and has_special):
            raise ValidationError("Password does not meet all 4 requirements.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data

