
from django.urls import path
from . import views

app_name = "department_head"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("officers/", views.officers_directory, name="officers"),
    path(
        "officers/<int:user_id>/",
        views.officer_detail,
        name="officer_detail",
    ),

    path("requests/", views.requests_list, name="requests"),
    path(
        "requests/<int:request_id>/decision/",
        views.request_decision,
        name="request_decision",
    ),

    path("performance/", views.performance, name="performance"),
    path("projects/", views.projects_list, name="projects"),
    path("reports/", views.reports, name="reports"),
    path("tasks/", views.tasks_list, name="tasks"),
    path("accountability/", views.accountability, name="accountability"),

    path("notifications/", views.notifications_page, name="notifications"),
    path(
        "notifications/<int:notification_id>/read/",
        views.notification_read,
        name="notification_read",
    ),

    path("my-profile/", views.my_profile, name="my_profile"),
    path("settings/", views.department_head_settings, name="settings"),
    path("logout/", views.department_head_logout, name="logout"),
]
