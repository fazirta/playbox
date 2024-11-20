from authentication.views import login, logout
from django.urls import path

app_name = "authentication"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
