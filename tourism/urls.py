from django.urls import path

from . import views


app_name = "tourism"


urlpatterns = [

    # 16.1
    path(
        "",
        views.home,
        name="home"
    ),

    # 16.2
    path(
        "destinations/",
        views.destinations,
        name="destinations"
    ),

    path(
        "destinations/<int:destination_id>/",
        views.destination_detail,
        name="destination_detail"
    ),

    # 16.3 Tourism Services
    path(
        "services/",
        views.tourism_services,
        name="tourism_services"
    ),

    path(
        "services/<int:service_id>/",
        views.tourism_service_detail,
        name="tourism_service_detail"
    ),

    # 16.3 Cultural Heritage
    path(
        "cultural-heritage/",
        views.cultural_heritage,
        name="cultural_heritage"
    ),

    path(
        "cultural-heritage/<int:site_id>/",
        views.cultural_heritage_detail,
        name="cultural_heritage_detail"
    ),
        # 16.4 Tourism Events
    path(
        "events/",
        views.tourism_events,
        name="tourism_events"
    ),

    path(
        "events/<int:event_id>/",
        views.tourism_event_detail,
        name="tourism_event_detail"
    ),

    # 16.4 Wildlife Conservation
    path(
        "wildlife-conservation/",
        views.wildlife_conservation,
        name="wildlife_conservation"
    ),

    path(
        "wildlife-conservation/<int:information_id>/",
        views.wildlife_conservation_detail,
        name="wildlife_conservation_detail"
    ),

    # 16.4 Tourism Projects & Opportunities
    path(
        "opportunities/",
        views.tourism_opportunities,
        name="tourism_opportunities"
    ),

    path(
        "opportunities/<int:opportunity_id>/",
        views.tourism_opportunity_detail,
        name="tourism_opportunity_detail"
    ),
    path(
    "events-conservation-opportunities/",
    views.events_conservation_opportunities,
    name="events_conservation_opportunities"
),
    
    path(
    "statistics/",
    views.tourism_statistics,
    name="statistics"
),
]