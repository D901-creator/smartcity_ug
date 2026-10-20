from django.urls import path
from . import views


app_name = "lands"


urlpatterns = [
    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "land-services/",
        views.land_services,
        name="land_services"
    ),

    path(
        "land-title/apply/",
        views.land_title_apply,
        name="land_title_apply"
    ),

    path(
        "land-title/success/<int:application_id>/",
        views.land_title_success,
        name="land_title_success"
    ),
    
    path(
    "property-requests/",
    views.property_requests,
    name="property_requests"
),

path(
    "property-requests/new/",
    views.property_request_create,
    name="property_request_create"
),

path(
    "property-requests/success/<int:request_id>/",
    views.property_request_success,
    name="property_request_success"
),

path(
    "housing/",
    views.housing_services,
    name="housing_services"
),

path(
    "housing/<int:information_id>/",
    views.housing_detail,
    name="housing_detail"
),
path(
    "housing-property-requests/",
    views.housing_property_requests,
    name="housing_property_requests"
),

path(
    "housing-property-requests/new/",
    views.housing_property_request_create,
    name="housing_property_request_create"
),

path(
    "housing-property-requests/success/<int:request_id>/",
    views.housing_property_request_success,
    name="housing_property_request_success"
),
path(
    "urban-planning/",
    views.urban_planning,
    name="urban_planning"
),

path(
    "urban-planning/<int:information_id>/",
    views.urban_planning_detail,
    name="urban_planning_detail"
),
path(
    "development-building/",
    views.development_building_applications,
    name="development_building"
),

path(
    "development-building/new/",
    views.development_building_application_create,
    name="development_building_create"
),

path(
    "development-building/success/<int:application_id>/",
    views.development_building_success,
    name="development_building_success"
),
path(
    "projects/",
    views.planning_projects,
    name="planning_projects"
),

path(
    "projects/<int:project_id>/",
    views.planning_project_detail,
    name="planning_project_detail"
),
path(
    "notices/",
    views.planning_notices,
    name="planning_notices"
),

path(
    "notices/<int:notice_id>/",
    views.planning_notice_detail,
    name="planning_notice_detail"
),
path("statistics/", views.statistics, name="statistics"),
]