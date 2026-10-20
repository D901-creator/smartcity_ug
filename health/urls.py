from django.urls import path

from . import views


app_name = "health"


urlpatterns = [

    # ========================================================
    # HEALTH HOME
    # ========================================================

    path(
        "",
        views.home,
        name="home"
    ),


    # ========================================================
    # HEALTH FACILITIES
    # ========================================================

    path(
        "facilities/",
        views.facilities,
        name="facilities"
    ),

    path(
        "facilities/<int:facility_id>/",
        views.facility_detail,
        name="facility_detail"
    ),

    path(
        "facilities/new/",
        views.facility_create,
        name="facility_create"
    ),


    # ========================================================
    # HEALTH SERVICES
    # ========================================================

    path(
        "services/",
        views.services,
        name="services"
    ),

    path(
        "services/<int:service_id>/",
        views.service_detail,
        name="service_detail"
    ),

    path(
        "services/new/",
        views.service_create,
        name="service_create"
    ),


    # ========================================================
    # MEDICINES
    # ========================================================

    path(
        "medicines/",
        views.medicines,
        name="medicines"
    ),

    path(
        "medicines/<int:medicine_id>/",
        views.medicine_detail,
        name="medicine_detail"
    ),

    path(
        "medicines/new/",
        views.medicine_create,
        name="medicine_create"
    ),


    # ========================================================
    # MEDICAL EQUIPMENT
    # ========================================================

    path(
        "equipment/",
        views.equipment,
        name="equipment"
    ),

    path(
        "equipment/<int:equipment_id>/",
        views.equipment_detail,
        name="equipment_detail"
    ),

    path(
        "equipment/new/",
        views.equipment_create,
        name="equipment_create"
    ),


    # ========================================================
    # HEALTH REQUESTS
    # ========================================================

    path(
        "requests/",
        views.health_requests,
        name="requests"
    ),

    path(
        "requests/new/",
        views.health_request_create,
        name="request_create"
    ),

    path(
        "requests/success/<str:reference_number>/",
        views.request_success,
        name="request_success"
    ),

    path(
        "requests/<int:request_id>/",
        views.health_request_detail,
        name="request_detail"
    ),


    # ========================================================
    # HOSPITAL / HEALTH FACILITY REPORTS
    # ========================================================

    path(
        "reports/",
        views.facility_reports,
        name="facility_reports"
    ),

    path(
        "reports/new/",
        views.facility_report_create,
        name="facility_report_create"
    ),

    path(
        "reports/success/<str:reference_number>/",
        views.report_success,
        name="report_success"
    ),

    path(
        "reports/<int:report_id>/",
        views.facility_report_detail,
        name="facility_report_detail"
    ),


    # ========================================================
    # HEALTH PROJECTS
    # ========================================================

    path(
        "projects/",
        views.projects,
        name="projects"
    ),

    path(
        "projects/<int:project_id>/",
        views.project_detail,
        name="project_detail"
    ),

    path(
        "projects/new/",
        views.project_create,
        name="project_create"
    ),


    # ========================================================
    # HEALTH INFORMATION
    # ========================================================

    path(
        "information/",
        views.information,
        name="information"
    ),

    path(
        "information/<int:information_id>/",
        views.information_detail,
        name="information_detail"
    ),

    path(
        "information/new/",
        views.information_create,
        name="information_create"
    ),


    # ========================================================
    # EMERGENCY INFORMATION
    # ========================================================

    path(
        "emergency/",
        views.emergency_information,
        name="emergency_information"
    ),

    path(
        "emergency/<int:emergency_id>/",
        views.emergency_information_detail,
        name="emergency_information_detail"
    ),

    path(
        "emergency/new/",
        views.emergency_information_create,
        name="emergency_information_create"
    ),


    # ========================================================
    # HEALTH STATISTICS
    # ========================================================

    path(
        "statistics/",
        views.statistics,
        name="statistics"
    ),
]