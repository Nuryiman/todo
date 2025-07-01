from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from tasks.models import Task, TASK_STATUS_CHOICES


class TasksListView(View, LoginRequiredMixin):
    """Вьюшка для списка задач"""

    def get(self, request, *args, **kwargs):
        user = request.user
        all_tasks = Task.objects.filter(owner=user)
        all_tasks_count = all_tasks.count()
        completed_tasks = all_tasks.filter(owner=user, status=TASK_STATUS_CHOICES["Completed"])
        active_tasks = all_tasks.filter(owner=user, status=TASK_STATUS_CHOICES["Active"])
        completed_tasks_count = completed_tasks.count()
        context = {
            "all_tasks": all_tasks,
            "all_tasks_count": all_tasks_count,
            "completed_tasks": completed_tasks,
            "active_tasks": active_tasks,
            "completed_tasks_count": completed_tasks_count
        }
        return render(request, 'tasks_list.html', context)


class AddTaskView(View):

    def post(self, request, *args, **kwargs):

        data = request.POST
        task = data['task']

        user = request.user
        if not user.is_authenticated:
            return redirect("login_url")
        if not task:
            return redirect("tasks")
        Task.objects.create(
            owner=user,
            description=task,
        )
        return redirect("tasks")


class CompleteTaskView(View):

    def post(self, request, *args, **kwargs):

        task_id = kwargs['id']
        try:
            task = Task.objects.get(id=task_id)
            task.status = TASK_STATUS_CHOICES["Completed"]
            task.save()
            return redirect("tasks")
        except Task.DoesNotExist:
            return redirect("tasks")

class DeleteTaskView(View):

    def post(self, request, *args, **kwargs):

        task_id = kwargs['id']
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return redirect("tasks")
        except Task.DoesNotExist:
            return redirect("tasks")


class RestoreTaskView(View):


    def post(self, request, *args, **kwargs):

        task_id = kwargs['id']
        try:
            task = Task.objects.get(id=task_id)
            task.status = TASK_STATUS_CHOICES["Active"]
            task.save()
            return redirect("tasks")
        except Task.DoesNotExist:
            return redirect("tasks")
