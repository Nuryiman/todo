from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class TasksListView(View):
    """Вьюшка для списка задач"""

    def get(self, request, *args, **kwargs):
        return render(request, 'tasks_list.html', {})