from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import TaskType, Position, Team, Task
from django.utils import timezone


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            username="testworker",
            password="password123"
        )

        self.tasktype = TaskType.objects.create(name="Test Task Type")

        self.qa_position = Position.objects.create(name="QA")

        self.team = Team.objects.create(
            name="TestTeam",
            description="Test description lorem ipsum",
            lead=self.worker
        )
        self.team.members.set([self.worker])

        self.task = Task.objects.create(
            name="Do Test",
            description="You need to do Test",
            deadline=timezone.now(),
            priority="medium",
            task_type=self.tasktype
        )

    def test_task_str(self):
        expected_str = "Do Test (priority: medium)"
        self.assertEqual(str(self.task), expected_str)

    def test_tasktype_str(self):
        expected_str = "Test Task Type"
        self.assertEqual(str(self.tasktype), expected_str)

    def test_team_str(self):
        expected_str = "TestTeam"
        self.assertEqual(str(self.team), expected_str)

    def test_worker_team_membership(self):
        """Test if worker can be added to a team"""
        self.team.members.add(self.worker)
        self.assertIn(self.worker, self.team.members.all())
