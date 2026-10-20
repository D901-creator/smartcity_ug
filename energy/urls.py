from django.urls import path

from . import views


app_name = "energy"


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "electricity/",
        views.electricity_services,
        name="electricity_services"
    ),

    path(
        "electricity/<int:information_id>/",
        views.electricity_service_detail,
        name="electricity_service_detail"
    ),
    path(
        "electricity/report/",
        views.electricity_problem_report,
        name="electricity_problem_report"
    ),

    path(
        "electricity/report/success/<int:report_id>/",
        views.electricity_problem_success,
        name="electricity_problem_success"
    ),
    path(
        "services/",
        views.energy_services,
        name="energy_services"
    ),

    path(
        "services/<int:information_id>/",
        views.energy_service_detail,
        name="energy_service_detail"
    ),
    path(
        "projects/",
        views.energy_projects,
        name="energy_projects"
    ),

    path(
        "projects/<int:project_id>/",
        views.energy_project_detail,
        name="energy_project_detail"
    ),
    path(
        "minerals/",
        views.mineral_resources,
        name="mineral_resources"
    ),

    path(
        "minerals/<int:mineral_id>/",
        views.mineral_resource_detail,
        name="mineral_resource_detail"
    ),
    path(
        "mining/",
        views.mining_development,
        name="mining_development"
    ),

    path(
        "mining/<int:activity_id>/",
        views.mining_development_detail,
        name="mining_development_detail"
    ),
    
    path(
    "reports-requests/",
    views.energy_mineral_request,
    name="energy_mineral_request",
),

path(
    "reports-requests/success/<int:request_id>/",
    views.energy_mineral_request_success,
    name="energy_mineral_request_success",
),

path(
    "statistics/",
    views.energy_mineral_statistics,
    name="statistics",
),
]