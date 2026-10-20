
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q 
from django.db.models import Count

from .forms import (LandTitleApplicationForm, 
                    UrbanPlanningInformation,DevelopmentBuildingApplicationForm,
                    LandPropertyRequestForm,HousingPropertyRequestForm)
from .models import( LandInformation, LandTitleApplication,DevelopmentBuildingApplication,
                    LandHousingPlanningNotice,
                    LandHousingPlanningProject,
                     
                    
                    
                    LandPropertyRequest, HousingInformation, HousingPropertyRequest)

def home(request):
    services = [
        {
            "name": "Land Services & Information",
            "icon": "bi-map",
            "description": "Access land-related information and public services.",
            "url": "lands:land_services",
            "color": "primary",
        },
        {
            "name": "Land Titles & Land Information",
            "icon": "bi-file-earmark-text",
            "description": "Learn about land titles, applications and land information.",
          "url": "lands:land_services",
            "color": "success",
        },
        {
            "name": "Land & Property Requests",
            "icon": "bi-house-check",
            "description": "Submit and follow land and property-related requests.",
            "url": "lands:property_requests",
            "color": "info",
        },
        {
            "name": "Housing Services & Information",
            "icon": "bi-house",
            "description": "Access housing information and related public services.",
             "url": "lands:housing_services",
            "color": "warning",
        },
        {
            "name": "Housing & Property Requests",
            "icon": "bi-building",
            "description": "Submit housing and property-related requests.",
            "url": "lands:housing_property_requests",
            "color": "secondary",
        },
        {
            "name": "Urban Planning & Development",
            "icon": "bi-buildings",
            "description": "Access urban planning and development information.",
            "url": "lands:urban_planning",
            "color": "dark",
        },
        {
            "name": "Development & Building Applications",
            "icon": "bi-cone-striped",
            "description": "Access information about development and building applications.",
            "url": "lands:development_building",
            "color": "danger",
        },
        {
            "name": "Land, Housing & Planning Projects",
            "icon": "bi-kanban",
            "description": "View projects related to land, housing and urban development.",
           "url": "lands:planning_projects",
            "color": "primary",
        },
        {
            "name": "Lands, Housing & Planning Notices",
            "icon": "bi-megaphone",
            "description": "View official notices and public information.",
            "url": "lands:planning_notices",
            "color": "warning",
        },
        {
            "name": "Lands, Housing & Urban Planning Statistics",
            "icon": "bi-bar-chart",
            "description": "View statistics and service information.",
            "url": "lands:statistics",
            "color": "success",
        },
    ]

    context = {
        "services": services,
    }

    return render(request, "lands/home.html", context)
def land_services(request):
    information = LandInformation.objects.filter(
        is_published=True
    )

    context = {
        "information": information,
    }

    return render(
        request,
        "lands/land_services.html",
        context
    )


def land_title_apply(request):

    if request.method == "POST":
        form = LandTitleApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            application = form.save()

            messages.success(
                request,
                "Your land-title request has been submitted successfully."
            )

            return redirect(
                "lands:land_title_success",
                application_id=application.id
            )

    else:
        form = LandTitleApplicationForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "lands/land_title_apply.html",
        context
    )


def land_title_success(request, application_id):

    application = get_object_or_404(
        LandTitleApplication,
        id=application_id
    )

    context = {
        "application": application,
    }

    return render(
        request,
        "lands/land_title_success.html",
        context
    )
    
def property_requests(request):

    requests = LandPropertyRequest.objects.all()

    context = {
        "requests": requests,
    }

    return render(
        request,
        "lands/property_requests.html",
        context
    )


def property_request_create(request):

    if request.method == "POST":

        form = LandPropertyRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            property_request = form.save()

            messages.success(
                request,
                "Your land and property request has been submitted successfully."
            )

            return redirect(
                "lands:property_request_success",
                request_id=property_request.id
            )

    else:

        form = LandPropertyRequestForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "lands/property_request_form.html",
        context
    )


def property_request_success(request, request_id):

    property_request = get_object_or_404(
        LandPropertyRequest,
        id=request_id
    )

    context = {
        "property_request": property_request,
    }

    return render(
        request,
        "lands/property_request_success.html",
        context
    )
    
def housing_services(request):
    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()

    housing_information = HousingInformation.objects.filter(
        is_published=True
    )

    if search:
        housing_information = housing_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
        )

    if information_type:
        housing_information = housing_information.filter(
            information_type=information_type
        )

    context = {
        "housing_information": housing_information,
        "information_types": HousingInformation.INFORMATION_TYPES,
        "search": search,
        "selected_type": information_type,
    }

    return render(
        request,
        "lands/housing_services.html",
        context
    )


def housing_detail(request, information_id):
    information = get_object_or_404(
        HousingInformation,
        id=information_id,
        is_published=True
    )

    context = {
        "information": information,
    }

    return render(
        request,
        "lands/housing_detail.html",
        context
    )
    
def housing_property_requests(request):

    requests = HousingPropertyRequest.objects.all()

    context = {
        "requests": requests,
    }

    return render(
        request,
        "lands/housing_property_requests.html",
        context
    )


def housing_property_request_create(request):

    if request.method == "POST":

        form = HousingPropertyRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            housing_request = form.save()

            messages.success(
                request,
                "Your housing and property request has been submitted successfully."
            )

            return redirect(
                "lands:housing_property_request_success",
                request_id=housing_request.id
            )

    else:

        form = HousingPropertyRequestForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "lands/housing_property_request_form.html",
        context
    )


def housing_property_request_success(request, request_id):

    housing_request = get_object_or_404(
        HousingPropertyRequest,
        id=request_id
    )

    context = {
        "housing_request": housing_request,
    }

    return render(
        request,
        "lands/housing_property_request_success.html",
        context
    )
def urban_planning(request):

    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()

    planning_information = UrbanPlanningInformation.objects.filter(
        is_published=True
    )

    if search:
        planning_information = planning_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
        )

    if information_type:
        planning_information = planning_information.filter(
            information_type=information_type
        )

    context = {
        "planning_information": planning_information,
        "information_types": UrbanPlanningInformation.INFORMATION_TYPES,
        "search": search,
        "selected_type": information_type,
    }

    return render(
        request,
        "lands/urban_planning.html",
        context
    )


def urban_planning_detail(request, information_id):

    information = get_object_or_404(
        UrbanPlanningInformation,
        id=information_id,
        is_published=True
    )

    context = {
        "information": information,
    }

    return render(
        request,
        "lands/urban_planning_detail.html",
        context
    )
def development_building_applications(request):

    applications = DevelopmentBuildingApplication.objects.all()

    context = {
        "applications": applications,
    }

    return render(
        request,
        "lands/development_building_applications.html",
        context
    )


def development_building_application_create(request):

    if request.method == "POST":

        form = DevelopmentBuildingApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save()

            messages.success(
                request,
                "Your development and building application has been submitted successfully."
            )

            return redirect(
                "lands:development_building_success",
                application_id=application.id
            )

    else:

        form = DevelopmentBuildingApplicationForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "lands/development_building_form.html",
        context
    )


def development_building_success(request, application_id):

    application = get_object_or_404(
        DevelopmentBuildingApplication,
        id=application_id
    )

    context = {
        "application": application,
    }

    return render(
        request,
        "lands/development_building_success.html",
        context
    )
    
def planning_projects(request):
    search = request.GET.get("search", "").strip()
    project_type = request.GET.get("type", "").strip()
    status = request.GET.get("status", "").strip()

    projects = LandHousingPlanningProject.objects.filter(
        is_published=True
    )

    if search:
        projects = projects.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(implementing_organization__icontains=search)
        )

    if project_type:
        projects = projects.filter(
            project_type=project_type
        )

    if status:
        projects = projects.filter(
            status=status
        )

    context = {
        "projects": projects,
        "project_types": LandHousingPlanningProject.PROJECT_TYPES,
        "statuses": LandHousingPlanningProject.STATUS_CHOICES,
        "search": search,
        "selected_type": project_type,
        "selected_status": status,
    }

    return render(
        request,
        "lands/planning_projects.html",
        context
    )


def planning_project_detail(request, project_id):
    project = get_object_or_404(
        LandHousingPlanningProject,
        id=project_id,
        is_published=True
    )

    return render(
        request,
        "lands/planning_project_detail.html",
        {
            "project": project
        }
    )
def planning_notices(request):
    search = request.GET.get("search", "").strip()
    notice_type = request.GET.get("type", "").strip()
    priority = request.GET.get("priority", "").strip()

    notices = LandHousingPlanningNotice.objects.filter(
        is_published=True
    )

    if search:
        notices = notices.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(content__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(issuing_organization__icontains=search)
        )

    if notice_type:
        notices = notices.filter(
            notice_type=notice_type
        )

    if priority:
        notices = notices.filter(
            priority=priority
        )

    context = {
        "notices": notices,
        "notice_types": LandHousingPlanningNotice.NOTICE_TYPES,
        "priorities": LandHousingPlanningNotice.PRIORITY_CHOICES,
        "search": search,
        "selected_type": notice_type,
        "selected_priority": priority,
    }

    return render(
        request,
        "lands/planning_notices.html",
        context
    )


def planning_notice_detail(request, notice_id):
    notice = get_object_or_404(
        LandHousingPlanningNotice,
        id=notice_id,
        is_published=True
    )

    return render(
        request,
        "lands/planning_notice_detail.html",
        {
            "notice": notice
        }
    )
def statistics(request):
    land_information_count = LandInformation.objects.filter(
        is_published=True
    ).count()

    land_title_application_count = LandTitleApplication.objects.count()

    land_property_request_count = LandPropertyRequest.objects.count()

    housing_information_count = HousingInformation.objects.filter(
        is_published=True
    ).count()

    housing_property_request_count = HousingPropertyRequest.objects.count()

    urban_planning_information_count = UrbanPlanningInformation.objects.filter(
        is_published=True
    ).count()

    development_application_count = DevelopmentBuildingApplication.objects.count()

    planning_project_count = LandHousingPlanningProject.objects.filter(
        is_published=True
    ).count()

    planning_notice_count = LandHousingPlanningNotice.objects.filter(
        is_published=True
    ).count()

    land_title_status_counts = (
        LandTitleApplication.objects
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    property_request_status_counts = (
        LandPropertyRequest.objects
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    housing_request_status_counts = (
        HousingPropertyRequest.objects
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    development_application_status_counts = (
        DevelopmentBuildingApplication.objects
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    project_status_counts = (
        LandHousingPlanningProject.objects
        .filter(is_published=True)
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    notice_priority_counts = (
        LandHousingPlanningNotice.objects
        .filter(is_published=True)
        .values("priority")
        .annotate(total=Count("id"))
        .order_by("priority")
    )

    context = {
        "land_information_count": land_information_count,
        "land_title_application_count": land_title_application_count,
        "land_property_request_count": land_property_request_count,
        "housing_information_count": housing_information_count,
        "housing_property_request_count": housing_property_request_count,
        "urban_planning_information_count": urban_planning_information_count,
        "development_application_count": development_application_count,
        "planning_project_count": planning_project_count,
        "planning_notice_count": planning_notice_count,

        "land_title_status_counts": land_title_status_counts,
        "property_request_status_counts": property_request_status_counts,
        "housing_request_status_counts": housing_request_status_counts,
        "development_application_status_counts": development_application_status_counts,
        "project_status_counts": project_status_counts,
        "notice_priority_counts": notice_priority_counts,
    }

    return render(
        request,
        "lands/statistics.html",
        context
    )