from django.urls import path

from tasks.views import TasksListView

urlpatterns = [
    path('list', TasksListView.as_view(), name='tasks')
]