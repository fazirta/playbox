from django.urls import path
from main.views import landing, create

app_name = "main"

urlpatterns = [
    path("", landing, name="landing"),
    path("create", create, name="create"),
]
