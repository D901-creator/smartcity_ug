from django.urls import path

from . import views


app_name = "ict"


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

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
    "infrastructure/",
    views.infrastructure,
    name="infrastructure"
),

path(
    "infrastructure/<int:infrastructure_id>/",
    views.infrastructure_detail,
    name="infrastructure_detail"
),

path(
    "innovations/",
    views.innovations,
    name="innovations"
),

path(
    "innovations/<int:innovation_id>/",
    views.innovation_detail,
    name="innovation_detail"
),

path(
    "opportunities/",
    views.opportunities,
    name="opportunities"
),

path(
    "opportunities/<int:opportunity_id>/",
    views.opportunity_detail,
    name="opportunity_detail"
),

path(
    "infrastructure-innovation-opportunities/",
    views.infrastructure_innovation_opportunities,
    name="infrastructure_innovation_opportunities"
),
path(
    "national-guidance/",
    views.national_guidance,
    name="national_guidance"
),

path(
    "national-guidance/<int:information_id>/",
    views.national_guidance_detail,
    name="national_guidance_detail"
),

path(
    "civic-programmes/",
    views.civic_programmes,
    name="civic_programmes"
),

path(
    "civic-programmes/<int:programme_id>/",
    views.civic_programme_detail,
    name="civic_programme_detail"
),

path(
    "national-guidance-civic-information/",
    views.national_guidance_civic_information,
    name="national_guidance_civic_information"
),
path(
    "statistics/",
    views.statistics,
    name="statistics"
),
path(
    "connectivity/",
    views.connectivity,
    name="connectivity",
),

path(
    "digital-literacy/",
    views.digital_literacy,
    name="digital_literacy",
),

path(
    "ict-support/",
    views.ict_support,
    name="ict_support",
),

path(
    "ict-opportunities/",
    views.ict_opportunities,
    name="ict_opportunities",
),
]