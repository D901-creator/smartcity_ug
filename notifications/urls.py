
from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    # Existing citizen notification pages
    path("", views.notification_list, name="list"),
    path("<int:notification_id>/", views.notification_detail, name="detail"),
    path("<int:notification_id>/read/", views.mark_notification_read, name="mark_read"),
    path("mark-all-read/", views.mark_all_notifications_read, name="mark_all_read"),
    path("<int:notification_id>/delete/", views.delete_notification, name="delete"),
    path("<int:notification_id>/dismiss/", views.dismiss_notification, name="dismiss"),
    path("clear-read/", views.clear_read_notifications, name="clear_read"),

    # Officer notification page
    path("officer/", views.officer_notification_list, name="officer_list"),
]
