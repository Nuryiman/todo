from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class User(AbstractUser):
    """Моделька для кастомного пользователя"""

    last_name = None

    email = None

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

