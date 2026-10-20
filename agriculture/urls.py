from django.urls import path
from . import views

app_name = "agriculture"

urlpatterns = [

    # Main Agriculture dashboard
    path(
        "",
        views.home,
        name="home"
    ),

    # Farmer management
    path(
        "farmers/",
        views.farmers,
        name="farmers"
    ),

    path(
        "farmers/register/",
        views.register_farmer,
        name="register_farmer"
    ),

    # Farm management
    path(
        "farms/",
        views.farms,
        name="farms"
    ),

    path(
        "farms/register/",
        views.register_farm,
        name="register_farm"
    ),
    path(
    "crop-production/",
    views.crop_production,
    name="crop_production"
),

path(
    "crop-production/register/",
    views.register_crop_production,
    name="register_crop_production"
),

path(
    "livestock/",
    views.livestock,
    name="livestock"
),

path(
    "livestock/register/",
    views.register_livestock,
    name="register_livestock"
),
path("market/", views.market, name="market"),
path(
    "market/list-product/",
    views.create_market_listing,
    name="create_market_listing"
),
path(
    "market/buyer-request/",
    views.create_buyer_request,
    name="create_buyer_request"
),
  path("matches/",views.matches, name="matches"),
  path(
    "matches/<int:match_id>/",
    views.match_detail,
    name="match_detail"
),

path(
    "matches/<int:match_id>/respond/",
    views.respond_to_match,
    name="respond_to_match"
),
path(
    "inputs/",
    views.agricultural_inputs,
    name="agricultural_inputs"
),

path(
    "inputs/add/",
    views.create_agricultural_input,
    name="create_agricultural_input"
),

path(
    "extension-services/",
    views.extension_services,
    name="extension_services"
),

path(
    "extension-services/add/",
    views.create_extension_service,
    name="create_extension_service"
),
    path(
        "projects/",
        views.agricultural_projects,
        name="agricultural_projects"
    ),

    path(
        "projects/add/",
        views.create_agricultural_project,
        name="create_agricultural_project"
    ),

    path(
        "programmes/",
        views.agricultural_programs,
        name="agricultural_programs"
    ),

    path(
        "programmes/add/",
        views.create_agricultural_program,
        name="create_agricultural_program"
    ),
path(
    "disease-reports/",
    views.disease_reports,
    name="disease_reports"
),

path(
    "disease-reports/report/",
    views.create_disease_report,
    name="create_disease_report"
),
path(
    "irrigation/",
    views.irrigation_projects,
    name="irrigation_projects"
),

path(
    "irrigation/add/",
    views.create_irrigation_project,
    name="create_irrigation_project"
),
path(
    "cooperatives/",
    views.cooperatives,
    name="cooperatives"
),
path(
    "statistics/",
    views.agricultural_statistics,
    name="agricultural_statistics"
),

# ============================================================
# PHASE 3 — FISHING & FISHERIES
# ============================================================

path(
    "fishing/fishers/",
    views.fishing_fishers,
    name="fishing_fishers",
),

path(
    "fishing/capture/",
    views.capture_fisheries,
    name="capture_fisheries",
),

path(
    "fishing/aquaculture/",
    views.aquaculture,
    name="aquaculture",
),

path(
    "fishing/processing/",
    views.fish_processing,
    name="fish_processing",
),

path(
    "fishing/marketing/",
    views.fish_marketing,
    name="fish_marketing",
),
]

