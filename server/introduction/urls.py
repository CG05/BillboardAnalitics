from .views import introduction
from django.urls import path, include

app_name = "introduction"

urlpatterns = [
    path("", introduction)
]