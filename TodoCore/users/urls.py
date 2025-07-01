from django.urls import path

from users.views import RegisterView, LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_url"),
    path("login/", LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView.as_view(), name='logout'),

]