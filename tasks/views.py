from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import TeamForm, ProjectForm
from .models import Team, Project, Task, Worker
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
    success_url = reverse_lazy("task:team-list")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasks:project-list")