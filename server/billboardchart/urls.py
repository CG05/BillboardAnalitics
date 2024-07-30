from .views import billboardchart
from django.urls import path, re_path
from django.views.generic import RedirectView
from datetime import datetime

app_name = "billboardchart"

urlpatterns = [
    path("", RedirectView.as_view(url='/billboardchart/' + datetime.now().strftime('%Y-%m-%d'), permanent=True)),
    re_path(r'^(\d{4}-\d{2}-\d{2})$', billboardchart),
]