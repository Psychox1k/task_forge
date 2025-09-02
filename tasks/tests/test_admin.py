from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tasks.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.qa_position = Position.objects.create(name="QA")

        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="password_test"
        )

        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="testworker",
            position=self.qa_position
        )

    def test_worker_changelist(self):
        """
        Test that the worker changelist page is accessible
        and displays the related Position (QA).
        """
        url = reverse("admin:tasks_worker_changelist")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "QA")

    def test_worker_change_page(self):
        """
        Test that the worker change page is accessible
        and contains the position selection field.
        """
        url = reverse("admin:tasks_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Change worker")
        self.assertContains(res, 'name="position"')

    def test_worker_add_page(self):
        """
        Test that the worker add page is accessible
        and contains the position selection field.
        """
        url = reverse("admin:tasks_worker_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'name="position"')

    def test_admin_requires_staff_for_non_admin(self):
        """
        Test that a non-staff user cannot access the admin site
        and is redirected to the admin login page.
        """
        self.client.logout()
        self.client.force_login(self.worker)
        url = reverse("admin:index")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 302)
        self.assertIn("/admin/login/", res["Location"])