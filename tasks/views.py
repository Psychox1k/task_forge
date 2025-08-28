from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import (
    TeamForm,
    ProjectForm,
    WorkerCreationForm,
    TaskForm,
    TaskTypeForm,
    TagForm,
    PositionForm,
)
from .models import Team, Project, Task, Worker, Tag, TaskType, Position
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    num_projects = Project.objects.count()
    num_teams = Team.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_projects": num_projects,
        "num_teams": num_teams,
        "num_workers": num_workers,
    }

    return render(request, "tasks/index.html", context)


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 2

    def get_queryset(self):
        queryset = Worker.objects.all()
        username = self.request.GET.get("username", "")
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.GET.get("username", "")
        return context


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 5

    def get_queryset(self):
        queryset = Team.objects.all()
        name = self.request.GET.get("name", "")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get("name", "")
        return context


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 10

    def get_queryset(self):
        queryset = Position.objects.all()
        name = self.request.GET.get("name", "")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get("name", "")
        return context


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 5

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.GET.get("name", "")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get("name", "")
        return context


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.all()
        name = self.request.GET.get("name", "")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get("name", "")
        return context


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 10

    def get_queryset(self):
        queryset = Tag.objects.all()
        name = self.request.GET.get("name", "")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get("name", "")
        return context


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    paginate_by = 10

    def get_queryset(self):
        queryset = TaskType.objects.all()
        name = self.request.GET.get("name", "")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get("name", "")
        return context


class UserTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(assignees=self.request.user)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasks:team-list")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasks:project-list")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasks:position-list")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("tasks:tasktype-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasks:position-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("tasks:tasktype-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasks:team-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasks:project-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasks:tasktype-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("tasks:team-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:worker-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasks:project-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


@login_required
def mark_as_done(request, pk):
    task = get_object_or_404(Task, id=pk)

    worker = request.user

    can_complete = worker in task.assignees.all() or (
        task.project and task.project.teams.filter(lead=worker).exists()
    )

    if can_complete:
        task.is_completed = True
        task.save()
        return redirect(f"/tasks/{pk}/?success=1")

    return redirect(f"/tasks/{pk}/?error=1")
