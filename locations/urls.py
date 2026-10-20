
from django.urls import path
from . import map_views

app_name = "locations"

urlpatterns = [
    path("map/", map_views.issue_map, name="issue_map"),
    path(
        "admin-map/",
        map_views.admin_generate_district_map,
        name="admin_district_map",
    ),
]
