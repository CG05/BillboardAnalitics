from .views import billboardchart
from django.urls import path, include

app_name = "billboardchart"

urlpatterns = [
    path("", billboardchart)
]