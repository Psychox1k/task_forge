from django.test import TestCase
from tasks.forms import WorkerCreationForm
from tasks.models import Position


class FormsTest(TestCase):
    def test_worker_creation_form_with_position_first_last_name_is_valid(self) -> None:

        self.qa_position = Position.objects.create(name="QA")
        form_data = {
            "username": "usertest",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
            "position": self.qa_position,
            "first_name": "Nametest",
            "last_name": "Lasttest",
        }
        form = WorkerCreationForm(data=form_data)

        self.assertTrue(form.is_valid(), msg=f"Form errors: {form.errors}")

        expected_fields = ["username", "first_name",
                           "last_name", "position"]
        for field in expected_fields:
            self.assertIn(field, form.cleaned_data)
            self.assertEqual(
                form.cleaned_data[field],
                form_data[field],
                msg=f"Field '{field}' doesn't match:"
                    f" {form.cleaned_data[field]} != {form_data[field]}"
            )
