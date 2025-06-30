from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    """Моделька для задач"""

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Пользователь")
    description = models.TextField(max_length=400, )