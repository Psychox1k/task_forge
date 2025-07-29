from django.shortcuts import render
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


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker

class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team

class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project

class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task