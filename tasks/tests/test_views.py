from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Project, Team, Position

PROJECT_FORMAT_URL = reverse("tasks:project-list")


class PublicProjectTests(TestCase):
    """
        Test that login is required to view the project list.
        It should redirect to the login page.
    """
    def test_login_required(self):
        res = self.client.get(PROJECT_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateProjectTests(TestCase):
    def setUp(self):
        """
            Set up the test environment by creating a user, team, and project.
        """
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",

        )
        self.client.force_login(self.user)

        self.worker = get_user_model().objects.create_user(
            username="testworker",
            password="password123"
        )

        self.team = Team.objects.create(
            name="TestTeam",
            description="Test description lorem ipsum",
            lead=self.worker
        )
        self.team.members.set([self.worker])

    def test_retrieve_project(self):
        """
            Test that a logged-in user can retrieve and view the project list.
            Ensure the project list matches the projects in the database.
        """
        Project.objects.create(
            name="Test Project",
            description="Something test project",
            budget=2000.00,
            deadline=date(2023, 12, 31),

        )
        response = self.client.get(PROJECT_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        projects = Project.objects.all()
        self.assertEqual(list(response.context["project_list"]),
                         list(projects))
        self.assertTemplateUsed(response, "tasks/project_list.html")


class PrivateWorkerTests(TestCase):
    def setUp(self):
        """
            Set up the test environment by creating a user and position for the worker.
        """
        self.user = get_user_model().objects.create_user(
            username="test",
            password="passtest553"
        )
        self.client.force_login(self.user)
        self.qa_position = Position.objects.create(name="QA")

    def test_create_worker(self):
        """
            Test that a worker can be created via the form and the data is correctly stored.
        """
        url = reverse("tasks:worker-create")

        form_data = {
            "username": "usertest",
            "password1": "testpass12",
            "password2": "testpass12",
            "first_name": "nametest",
            "last_name": "lasttest",
            "position": self.qa_position.id
        }

        response = self.client.post(url, data=form_data)

        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.position.id, form_data["position"])
