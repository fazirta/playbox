from authentication.views import register, login, logout
from django.urls import path

app_name = "authentication"

urlpatterns = [
    path("register/", register, name="login"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
