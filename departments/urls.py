
from django.urls import path

from . import views

app_name = "departments"

urlpatterns = [
    


    path("services/", views.service_directory, name="service_directory"),
    path(
        "services/<int:service_id>/",
        views.service_detail,
        name="service_detail",
    ),
     # Staff dashboard
    path(
        "dashboard/",
        views.department_services_dashboard,
        name="department_services_dashboard",
    ),

    # Department management
    path("manage/", views.manage_departments, name="manage_departments"),
    path(
        "manage/add/",
        views.department_add,
        name="department_add",
    ),
    path(
        "manage/<int:pk>/edit/",
        views.department_edit,
        name="department_edit",
    ),

    # Service configuration
    path(
        "configure/",
        views.manage_services,
        name="manage_services",
    ),
    path(
        "configure/add/",
        views.service_add,
        name="service_add",
    ),
    path(
        "configure/<int:pk>/edit/",
        views.service_edit,
        name="service_edit",
    ),
]
