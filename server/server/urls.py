from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.mainpage),
    path("example", views.examplepage),
    path("introduction/", include('introduction.urls')),
    path("simulation/", include('simulation.urls')),
    path("history/", include('history.urls')),
    path("billboardchart/", include('billboardchart.urls')),
]
