from django.urls import path

from . import views


app_name = "security"


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "incident-report/",
        views.incident_report,
        name="incident_report"
    ),

    path(
        "incident-report/success/<int:report_id>/",
        views.incident_report_success,
        name="incident_report_success"
    ),
    path(
    "emergency-information/",
    views.emergency_information,
    name="emergency_information"
),
    path(
    "programmes/",
    views.programmes,
    name="programmes"
),
path(
    "advisories/",
    views.advisories,
    name="advisories"
),

path(
    "notices/",
    views.notices,
    name="notices"
),
path(
    "facilities/",
    views.facilities,
    name="facilities"
),

path(
    "reports-requests/",
    views.security_request,
    name="requests"
),

path(
    "reports-requests/success/<int:request_id>/",
    views.request_success,
    name="request_success"
),
path(
    "statistics/",
    views.statistics,
    name="statistics"
),
]