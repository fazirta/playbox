from django.urls import path
from main.views import landing

app_name = 'main'

urlpatterns = [
    path('', landing, name='landing'),
]
