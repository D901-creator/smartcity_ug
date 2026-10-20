from django.urls import path

from . import views


app_name = "water"


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "report-problem/",
        views.report_water_problem,
        name="report_water_problem"
    ),

    path(
        "report-success/<str:reference_number>/",
        views.report_success,
        name="report_success"
    ),
   path(
    "report-problem/",
    views.report_water_problem,
    name="report_water_problem"
),

path(
    "report-success/<str:reference_number>/",
    views.report_success,
    name="report_success"
),
path(
    "environment/services/",
    views.environmental_services,
    name="environmental_services"
),

path(
    "environment/report/",
    views.report_environmental_problem,
    name="report_environmental_problem"
),

path(
    "environment/report-success/<str:reference_number>/",
    views.environment_report_success,
    name="environment_report_success"
),
path(
    "facilities/",
    views.water_facilities,
    name="water_facilities"
),

path(
    "facilities/<int:facility_id>/",
    views.water_facility_detail,
    name="water_facility_detail"
),
path(
    "supply-information/",
    views.water_supply_information,
    name="water_supply_information"
),
    path(
    "drainage-wastewater/",
    views.drainage_wastewater,
    name="drainage_wastewater"
),

path(
    "drainage-wastewater/report/",
    views.report_drainage_wastewater,
    name="report_drainage_wastewater"
),

path(
    "drainage-wastewater/success/<str:reference_number>/",
    views.drainage_wastewater_success,
    name="drainage_wastewater_success"
),
   path(
    "projects/",
    views.water_projects,
    name="water_projects"
),
 path(
    "environmental-facilities/",
    views.environmental_facilities,
    name="environmental_facilities"
),

path(
    "environmental-facilities/<int:facility_id>/",
    views.environmental_facility_detail,
    name="environmental_facility_detail"
),  
    path(
    "waste-management/",
    views.waste_management,
    name="waste_management"
),
    
    path(
    "pollution/",
    views.pollution_reports,
    name="pollution_reports"
),

path(
    "pollution/report/",
    views.report_pollution,
    name="report_pollution"
),

path(
    "pollution/success/<str:reference_number>/",
    views.pollution_report_success,
    name="pollution_report_success"
),
path(
    "trees-forests/",
    views.trees_forests,
    name="trees_forests"
),

path(
    "trees-forests/<int:site_id>/",
    views.tree_forest_detail,
    name="tree_forest_detail"
),
path(
    "environmental-projects/",
    views.environmental_projects,
    name="environmental_projects"
),

path(
    "environmental-projects/<int:project_id>/",
    views.environmental_project_detail,
    name="environmental_project_detail"
),

path(
    "wetlands-natural-resources/",
    views.wetlands_natural_resources,
    name="wetlands_natural_resources"
),

path(
    "wetlands-natural-resources/<int:resource_id>/",
    views.wetland_natural_resource_detail,
    name="wetland_natural_resource_detail"
),
path(
    "climate-information/",
    views.climate_environmental_information,
    name="climate_environmental_information"
),

path(
    "climate-information/<int:information_id>/",
    views.climate_environmental_information_detail,
    name="climate_environmental_information_detail"
),
path(
    "environmental-incidents/",
    views.environmental_incidents,
    name="environmental_incidents"
),

path(
    "environmental-incidents/report/",
    views.report_environmental_incident,
    name="report_environmental_incident"
),

path(
    "environmental-incidents/success/<str:reference_number>/",
    views.environmental_incident_success,
    name="environmental_incident_success"
),

path(
    "environmental-incidents/<int:incident_id>/",
    views.environmental_incident_detail,
    name="environmental_incident_detail"
),
path(
    "request-tracking/",
    views.citizen_request_tracking,
    name="citizen_request_tracking"
),
path(
    "statistics/",
    views.water_environment_statistics,
    name="water_environment_statistics"
),
path(
    "environment/",
    views.environment,
    name="environment"
),
]