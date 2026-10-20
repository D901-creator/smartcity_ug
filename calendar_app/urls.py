
from django.urls import path
from . import views

app_name = "calendar_app"

urlpatterns = [
    path("", views.calendar_view, name="calendar"),
    path("events/create/", views.create_event, name="create_event"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
    path(
        "events/<int:event_id>/edit/",
        views.edit_event,
        name="edit_event",
    ),
    path(
        "events/<int:event_id>/delete/",
        views.delete_event,
        name="delete_event",
    ),
]
