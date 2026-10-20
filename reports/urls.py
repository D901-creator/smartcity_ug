from django.urls import path

from . import views


app_name = "reports"


urlpatterns = [
    path(
        "",
        views.my_reports,
        name="my_reports",
    ),

    path(
        "create/",
        views.create_report,
        name="create_report",
    ),

    path(
        "<int:report_id>/",
        views.report_detail,
        name="report_detail",
    ),
     path("officer/", views.officer_reports, name="officer_reports"),
    path(
        "officer/<int:report_id>/",
        views.officer_report_detail,
        name="officer_report_detail",
    ),
]

