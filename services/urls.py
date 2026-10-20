from django.urls import path

from . import views


app_name = "services"


urlpatterns = [

    path(
        "",
        views.service_list,
        name="list"
    ),

    path(
        "<int:service_id>/",
        views.service_detail,
        name="detail"
    ),

    path(
        "<int:service_id>/request/",
        views.service_request,
        name="request"
    ),

    path(
        "request/<str:reference_number>/success/",
        views.request_success,
        name="request_success"
    ),

]