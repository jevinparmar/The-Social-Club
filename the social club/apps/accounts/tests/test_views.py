"""Tests for accounts authentication, role-based access control, and dashboards."""
from django.test import Client, TestCase
from django.urls import reverse

from apps.accounts.models import User


class AuthenticationAndDashboardTests(TestCase):
    """Test suite covering registration, login, logout, RBAC, and blank dashboards."""

    def setUp(self):
        self.client = Client()
        self.login_url = reverse("accounts:login")
        self.register_url = reverse("accounts:register")
        self.logout_url = reverse("accounts:logout")
        self.user_dashboard_url = reverse("accounts:user_dashboard")
        self.admin_dashboard_url = reverse("accounts:admin_dashboard")

        self.user_password = "StrongUserPass!2026"
        self.admin_password = "StrongAdminPass!2026"

        self.normal_user = User.objects.create_user(
            email="user@example.com",
            full_name="Normal User",
            phone_number="+919876543210",
            password=self.user_password,
        )
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            full_name="Admin User",
            phone_number="+919876543211",
            password=self.admin_password,
        )

    def test_1_normal_user_can_register(self):
        response = self.client.post(
            self.register_url,
            {
                "full_name": "New Member",
                "email": "newmember@example.com",
                "phone_number": "+919876543212",
                "password": "StrongPassword!2026",
                "confirm_password": "StrongPassword!2026",
                "terms_accepted": True,
            },
        )
        self.assertRedirects(response, self.login_url)
        created = User.objects.get(email="newmember@example.com")
        self.assertEqual(created.role, User.Role.USER)
        self.assertTrue(created.check_password("StrongPassword!2026"))

    def test_2_duplicate_email_registration_rejected(self):
        response = self.client.post(
            self.register_url,
            {
                "full_name": "Duplicate User",
                "email": "user@example.com",
                "phone_number": "+919876543213",
                "password": "StrongPassword!2026",
                "confirm_password": "StrongPassword!2026",
                "terms_accepted": True,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An account with this email address already exists.")
        self.assertEqual(User.objects.filter(email="user@example.com").count(), 1)

    def test_3_and_4_user_can_login_and_redirects_to_user_dashboard(self):
        response = self.client.post(
            self.login_url,
            {"email": "user@example.com", "password": self.user_password},
        )
        self.assertRedirects(response, self.user_dashboard_url)

    def test_5_and_6_admin_can_login_and_redirects_to_admin_dashboard(self):
        response = self.client.post(
            self.login_url,
            {"email": "admin@example.com", "password": self.admin_password},
        )
        self.assertRedirects(response, self.admin_dashboard_url)

    def test_7_guest_cannot_access_either_dashboard(self):
        res_user = self.client.get(self.user_dashboard_url)
        self.assertRedirects(res_user, f"{self.login_url}?next={self.user_dashboard_url}")

        res_admin = self.client.get(self.admin_dashboard_url)
        self.assertRedirects(res_admin, f"{self.login_url}?next={self.admin_dashboard_url}")

    def test_8_normal_user_cannot_access_admin_dashboard(self):
        self.client.force_login(self.normal_user)
        response = self.client.get(self.admin_dashboard_url)
        self.assertEqual(response.status_code, 403)

    def test_9_admin_cannot_access_user_dashboard(self):
        self.client.force_login(self.admin_user)
        response = self.client.get(self.user_dashboard_url)
        self.assertEqual(response.status_code, 403)

    def test_10_invalid_password_rejected(self):
        response = self.client.post(
            self.login_url,
            {"email": "user@example.com", "password": "WrongPassword123"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid email address or password.")

    def test_11_logout_destroys_session_and_prevents_dashboard_access(self):
        self.client.force_login(self.normal_user)
        res_logout = self.client.get(self.logout_url)
        self.assertRedirects(res_logout, self.login_url)

        res_dash = self.client.get(self.user_dashboard_url)
        self.assertRedirects(res_dash, f"{self.login_url}?next={self.user_dashboard_url}")

    def test_12_dashboards_display_only_required_centered_text(self):
        self.client.force_login(self.normal_user)
        res_user = self.client.get(self.user_dashboard_url)
        self.assertEqual(res_user.status_code, 200)
        self.assertContains(res_user, "User Side Dashboard")

        self.client.force_login(self.admin_user)
        res_admin = self.client.get(self.admin_dashboard_url)
        self.assertEqual(res_admin.status_code, 200)
        self.assertContains(res_admin, "Admin Side Dashboard")

    def test_14_csrf_protection_enforced(self):
        csrf_client = Client(enforce_csrf_checks=True)
        response = csrf_client.post(
            self.login_url,
            {"email": "user@example.com", "password": self.user_password},
        )
        self.assertEqual(response.status_code, 403)
