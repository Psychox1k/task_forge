from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Team, Worker, Project, Task, Tag, TaskType, Position


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username",
                   "class": "form-control form-control-lg"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password",
                   "class": "form-control form-control-lg"}
        )
    )


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        required=True,
        widget=forms.SelectMultiple(
            attrs={
                "class": "select2",
                "style": "width: 100%",
                "data-placeholder": "Choose Members",
            }
        ),
    )

    lead = forms.ModelChoiceField(
        queryset=Worker.objects.all(), widget=forms.Select, required=True
    )

    class Meta:
        model = Team
        fields = ["name", "description", "members", "lead"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "members" in self.data:
            try:
                member_ids = self.data.getlist("members")
                self.fields["lead"].queryset = Worker.objects.filter(
                    id__in=member_ids)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["lead"].queryset = self.instance.members.all()


class ProjectForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        required=True,
        widget=forms.SelectMultiple(
            attrs={
                "class": "select2",
                "style": "width: 100%",
                "data-placeholder": "Choose Teams",
            }
        ),
    )

    class Meta:
        model = Project
        exclude = ["created_at", "updated_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["deadline"].widget = forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        )


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class": "select2",
                "data-placeholder": "Choose tags",
            }
        ),
    )

    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "select2",
                "data-placeholder": "Choose assignees",
            }
        ),
    )

    class Meta:
        model = Task
        exclude = ["is_completed"]
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                },
                format="%Y-%m-%dT%H:%M",
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"
