
from django.urls import path
from . import views

app_name = "officer"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("requests/", views.assigned_requests, name="assigned_requests"),
    path(
        "requests/<int:request_id>/",
        views.request_detail,
        name="request_detail",
    ),
    
path("cases/", views.cases, name="cases"),

path("tasks/", views.my_tasks, name="my_tasks"),
path(
    "tasks/<int:task_id>/update/",
    views.update_task_status,
    name="update_task_status",
),
path("attendance/", views.attendance, name="attendance"),
path("attendance/check-in/", views.attendance_check_in, name="attendance_check_in"),
path("attendance/check-out/", views.attendance_check_out, name="attendance_check_out"),
path("performance/", views.performance, name="performance"),

]
