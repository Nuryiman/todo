from django.contrib.auth import get_user_model
from django.db import models


TASK_STATUS_CHOICES = {
    "Completed": "Выполнено",
    "Active": "Активно",
}

class Task(models.Model):
    """Моделька для задач"""

    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE,
                              verbose_name="Пользователь",
                              related_name="tasks"
                              )
    description = models.TextField(max_length=400, verbose_name="Описание")

    status = models.CharField(max_length=100,
                              choices=TASK_STATUS_CHOICES,
                              verbose_name="Статус задачи",
                              default=TASK_STATUS_CHOICES["Active"]
                              )