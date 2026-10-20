from django.urls import path
from . import views

app_name = "announcements"

urlpatterns = [
    path("", views.announcement_list, name="list"),
    path("create/", views.announcement_create, name="create"),
    path(
        "<int:announcement_id>/archive/",
        views.announcement_archive,
        name="archive",
    ),
]