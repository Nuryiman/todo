from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from users.models import User


class RegisterView(View):
    """Вьюшка для регистрации"""

    def get(self, request, *args, **kwargs):
        return render(request, "users/register.html", {})

    def post(self, request, *args, **kwargs):

        data = request.POST
        username = data.get("username", "")
        password1 = data.get("password1", "")
        password2 = data.get("password2", "")
        if not username or not password1:
            messages.error(request, "Введите Имя пользователя и пароль")
        try:
            user = User.objects.get(username=username)
            messages.error(request, "Пользователь с таким именем уже зарегистрирован")
        except User.DoesNotExist:
            if password1 != password2:
                messages.error(request, "Пароли не совпадают")
            else:
                new_user = User.objects.create_user(
                    username=username,
                    password=password1
                )
                login(request, new_user)
                return redirect("tasks")
        return render(request, "users/register.html", {})


class LoginView(View):
    """Вью для логина"""

    def get(self, request, *args, **kwargs):

        return render(request, "users/login.html", context={})

    def post(self, request, *args, **kwargs):

        data = request.POST
        username = data.get("username", "")
        password = data.get("password", "")
        print(username)

        if not username or not password:
            messages.error(request, "Введите Имя пользователя и пароль")

        try:
            user = User.objects.get(username=username)
            correct = user.check_password(password)
            if correct:
                login(request, user)
                return redirect('tasks')
            else:
                messages.error(request, "Неправильный пароль")
        except User.DoesNotExist:
            messages.error(request, "Пользователь с таким именем еще е зарегистрирован")
        return render(request, "users/login.html", {})
