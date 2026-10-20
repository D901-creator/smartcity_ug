
from django.urls import path
from . import views

app_name = "citizen"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
