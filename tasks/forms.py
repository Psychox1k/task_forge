from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_select2.forms import ModelSelect2MultipleWidget

from .models import Team, Worker, Project, Task, Tag


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control form-control-lg'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control form-control-lg'
        })
    )


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    lead = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta:
        model = Team
        fields = ['name', 'description', 'members', 'lead']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'members' in self.data:
            try:
                member_ids = self.data.getlist('members')
                self.fields['lead'].queryset = Worker.objects.filter(id__in=member_ids)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['lead'].queryset = self.instance.members.all()


class ProjectForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Project
        fields = "__all__"
        exclude = ['created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['deadline'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class": "select2",
                "style": "width: 100%",
                "data-placeholder": "Choose Assingnees"
            }
        )
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "select2",
                "style": "width: 100%",
                "data-placeholder": "Choose tag"
            }
        )
    )

    class Meta:
        model = Task
        exclude = ["is_completed"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
