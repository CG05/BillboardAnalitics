from .views import simulation
from django.urls import path, include

app_name = "simulation"

urlpatterns = [
    path("", simulation)
]