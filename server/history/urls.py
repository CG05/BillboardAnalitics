from .views import history
from django.urls import path, include

app_name = "history"

urlpatterns = [
    path("", history)
]