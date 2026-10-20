from django.urls import path

from . import views


app_name = "requests"


urlpatterns = [

    path(
        "",
        views.my_requests,
        name="my_requests",
    ),

    path(
        "create/",
        views.create_request,
        name="create_request",
    ),

    path(
        "<int:request_id>/",
        views.request_detail,
        name="request_detail",
    ),
]