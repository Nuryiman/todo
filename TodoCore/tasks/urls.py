from django.urls import path

from tasks.views import TasksListView, AddTaskView, CompleteTaskView, DeleteTaskView, RestoreTaskView

urlpatterns = [
    path('list/', TasksListView.as_view(), name='tasks'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('complete_task/<int:id>', CompleteTaskView.as_view(), name='complete_task'),
    path('delete_task/<int:id>', DeleteTaskView.as_view(), name='delete_task'),
    path('restore_task/<int:id>', RestoreTaskView.as_view(), name='restore_task')
]