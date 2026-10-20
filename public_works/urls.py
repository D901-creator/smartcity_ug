from django.urls import path

from . import views


app_name = "public_works"


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "road-problems/report/",
        views.report_road_problem,
        name="road_problem_report"
    ),

    path(
        "road-problems/success/<str:reference_number>/",
        views.road_problem_success,
        name="road_problem_success"
    ),

    path(
        "road-problems/",
        views.road_problem_reports,
        name="road_problem_reports"
    ),

    path(
        "road-problems/<int:report_id>/",
        views.road_problem_detail,
        name="road_problem_detail"
    ),
    path(
    "road-infrastructure-services/",
    views.road_infrastructure_services,
    name="road_infrastructure_services"
),
    path(
    "road-infrastructure-services/<slug:slug>/",
    views.road_infrastructure_service_detail,
    name="road_infrastructure_service_detail"
),
   path(
    "roads/",
    views.roads_network,
    name="roads_network"
),
  path(
    "road-projects/",
    views.road_construction_projects,
    name="road_construction_projects"
),

path(
    "road-projects/<int:project_id>/",
    views.road_construction_project_detail,
    name="road_construction_project_detail"
),
path(
    "traffic-road-safety/",
    views.traffic_road_safety,
    name="traffic_road_safety"
),

path(
    "traffic-road-safety/<int:information_id>/",
    views.traffic_road_safety_detail,
    name="traffic_road_safety_detail"
),
  path(
    "traffic-incidents/report/",
    views.report_traffic_incident,
    name="traffic_incident_report"
),

path(
    "traffic-incidents/success/<str:reference_number>/",
    views.traffic_incident_success,
    name="traffic_incident_success"
),

path(
    "traffic-incidents/",
    views.traffic_incident_reports,
    name="traffic_incident_reports"
),

path(
    "traffic-incidents/<int:incident_id>/",
    views.traffic_incident_detail,
    name="traffic_incident_detail"
),
path(
    "parking/",
    views.parking_services,
    name="parking_services"
),

path(
    "parking/<int:facility_id>/",
    views.parking_facility_detail,
    name="parking_facility_detail"
),

path(
    "parking/<int:facility_id>/fee/<int:fee_id>/pay/",
    views.parking_payment,
    name="parking_payment"
),

path(
    "parking/payment/<str:payment_reference>/",
    views.parking_payment_confirmation,
    name="parking_payment_confirmation"
),

path(
    "parking/payment/<str:payment_reference>/receipt/",
    views.parking_receipt,
    name="parking_receipt"
),
path(
    "facilities/",
    views.public_works_facilities,
    name="public_works_facilities"
),
path(
    "transport-information/",
    views.transport_information_advisories,
    name="transport_information"
),

path(
    "transport-information/<int:advisory_id>/",
    views.transport_information_detail,
    name="transport_information_detail"
),
path(
    "projects/",
    views.public_works_projects,
    name="public_works_projects"
),

path(
    "projects/<int:project_id>/",
    views.public_works_project_detail,
    name="public_works_project_detail"
),
path(
    "statistics/",
    views.public_works_transport_statistics,
    name="public_works_statistics"
),
]