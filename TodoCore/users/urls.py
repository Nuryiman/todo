from django.urls import path

from users.views import RegisterView, LoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_url"),
    path("login/", LoginView.as_view(), name="login_url")
]