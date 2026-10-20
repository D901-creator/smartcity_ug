from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.db.models import Count
from .models import (ElectricityServiceInformation, ElectricityServiceInformation,
    MiningDevelopmentInformation,EnergyMineralRequest,
    EnergyServiceInformation, EnergyProject,  MineralResourceInformation,)

from .forms import ElectricityProblemReportForm, ElectricityProblemReport,EnergyMineralRequestForm
def home(request):

    services = [
            {
    "name": "Energy & Mineral Development",
    "icon": "bi-lightning-charge",
    "description": "Access electricity, energy and mineral development services.",
    "color": "service-yellow",
    "url": "energy:home",
},
        {
            "name": "Electricity Services",
            "icon": "bi-lightning-charge",
            "description": (
                "Access electricity service information, "
                "supply information, safety information and contacts."
            ),
            "color": "warning",
           "url": "energy:electricity_services",
        },
        {
            "name": "Electricity Problem Reporting",
            "icon": "bi-exclamation-triangle",
            "description": (
                "Report electricity outages, damaged poles, "
                "power lines and other electricity problems."
            ),
            "color": "danger",
            "url": "energy:electricity_problem_report",
        },
        {
            "name": "Energy Services & Information",
            "icon": "bi-battery-charging",
            "description": (
                "Access information about energy services, "
                "clean energy and energy development."
            ),
            "color": "success",
            "url": "energy:energy_services",
        },
        {
            "name": "Energy Projects",
            "icon": "bi-building-gear",
            "description": (
                "View electricity, renewable energy and other "
                "energy development projects."
            ),
            "color": "primary",
           "url": "energy:energy_projects",
        },
        {
            "name": "Mineral Resources Information",
            "icon": "bi-gem",
            "description": (
                "Access public information about mineral resources "
                "and mineral development."
            ),
            "color": "secondary",
            "url": "energy:mineral_resources",
        },
        {
            "name": "Mining & Mineral Development",
            "icon": "bi-hammer",
            "description": (
                "Access mining and mineral development information, "
                "public notices and responsible development information."
            ),
            "color": "dark",
           "url": "energy:mining_development",
        },
        {
            "name": "Energy & Mineral Reports / Requests",
            "icon": "bi-clipboard-check",
            "description": (
                "Submit energy, electricity and mineral-related "
                "reports and service requests."
            ),
            "color": "info",
            "url": "energy:energy_mineral_request",
        },
        {
            "name": "Energy & Mineral Development Statistics",
            "icon": "bi-bar-chart-line",
            "description": (
                "View statistics about energy services, projects, "
                "electricity and mineral development."
            ),
            "color": "success",
            "url": "energy:statistics",
        },
    ]

    context = {
        "services": services,
    }

    return render(
        request,
        "energy/home.html",
        context
    )
    
def electricity_services(request):

    information = ElectricityServiceInformation.objects.filter(
        is_published=True
    )

    category = request.GET.get(
        "category",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if category:
        information = information.filter(
            category=category
        )

    if district:
        information = information.filter(
            district__icontains=district
        )

    context = {
        "information": information,
        "category": category,
        "district": district,
        "categories": (
            ElectricityServiceInformation.CATEGORY_CHOICES
        ),
        "total_information": information.count(),
    }

    return render(
        request,
        "energy/electricity_services.html",
        context
    )


def electricity_service_detail(request, information_id):

    information = get_object_or_404(
        ElectricityServiceInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "energy/electricity_service_detail.html",
        {
            "information": information
        }
    )
def electricity_problem_report(request):

    if request.method == "POST":

        form = ElectricityProblemReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            return redirect(
                "energy:electricity_problem_success",
                report_id=report.id
            )

    else:

        form = ElectricityProblemReportForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "energy/electricity_problem_report.html",
        context
    )


def electricity_problem_success(request, report_id):

    report = get_object_or_404(
        ElectricityProblemReport,
        id=report_id
    )

    return render(
        request,
        "energy/electricity_problem_success.html",
        {
            "report": report,
        }
    )
    
def energy_services(request):

    information = EnergyServiceInformation.objects.filter(
        is_published=True
    )

    category = request.GET.get(
        "category",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if category:
        information = information.filter(
            category=category
        )

    if district:
        information = information.filter(
            district__icontains=district
        )

    context = {
        "information": information,
        "category": category,
        "district": district,
        "categories": (
            EnergyServiceInformation.CATEGORY_CHOICES
        ),
        "total_information": information.count(),
    }

    return render(
        request,
        "energy/energy_services.html",
        context
    )


def energy_service_detail(request, information_id):

    information = get_object_or_404(
        EnergyServiceInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "energy/energy_service_detail.html",
        {
            "information": information
        }
    )
    
def energy_projects(request):

    projects = EnergyProject.objects.filter(
        is_published=True
    )

    project_type = request.GET.get(
        "project_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if project_type:
        projects = projects.filter(
            project_type=project_type
        )

    if status:
        projects = projects.filter(
            status=status
        )

    if district:
        projects = projects.filter(
            district__icontains=district
        )

    context = {
        "projects": projects,
        "project_type": project_type,
        "status": status,
        "district": district,

        "project_types": (
            EnergyProject.PROJECT_TYPE_CHOICES
        ),

        "statuses": (
            EnergyProject.STATUS_CHOICES
        ),

        "total_projects": projects.count(),
    }

    return render(
        request,
        "energy/projects.html",
        context
    )


def energy_project_detail(request, project_id):

    project = get_object_or_404(
        EnergyProject,
        id=project_id,
        is_published=True
    )

    return render(
        request,
        "energy/project_detail.html",
        {
            "project": project,
        }
    )
    
def mineral_resources(request):

    minerals = MineralResourceInformation.objects.filter(
        is_published=True
    )

    mineral_type = request.GET.get(
        "mineral_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if mineral_type:
        minerals = minerals.filter(
            mineral_type=mineral_type
        )

    if district:
        minerals = minerals.filter(
            district__icontains=district
        )

    context = {
        "minerals": minerals,
        "mineral_type": mineral_type,
        "district": district,

        "mineral_types": (
            MineralResourceInformation.MINERAL_TYPE_CHOICES
        ),

        "total_minerals": minerals.count(),
    }

    return render(
        request,
        "energy/mineral_resources.html",
        context
    )


def mineral_resource_detail(request, mineral_id):

    mineral = get_object_or_404(
        MineralResourceInformation,
        id=mineral_id,
        is_published=True
    )

    return render(
        request,
        "energy/mineral_resource_detail.html",
        {
            "mineral": mineral,
        }
    )
    
def mining_development(request):

    activities = MiningDevelopmentInformation.objects.filter(
        is_published=True
    )

    activity_type = request.GET.get(
        "activity_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if activity_type:
        activities = activities.filter(
            activity_type=activity_type
        )

    if status:
        activities = activities.filter(
            status=status
        )

    if district:
        activities = activities.filter(
            district__icontains=district
        )

    context = {
        "activities": activities,
        "activity_type": activity_type,
        "status": status,
        "district": district,

        "activity_types": (
            MiningDevelopmentInformation.ACTIVITY_CHOICES
        ),

        "statuses": (
            MiningDevelopmentInformation.STATUS_CHOICES
        ),

        "total_activities": activities.count(),
    }

    return render(
        request,
        "energy/mining_development.html",
        context
    )


def mining_development_detail(request, activity_id):

    activity = get_object_or_404(
        MiningDevelopmentInformation,
        id=activity_id,
        is_published=True
    )

    return render(
        request,
        "energy/mining_development_detail.html",
        {
            "activity": activity,
        }
    )
    
def energy_mineral_request(request):

    if request.method == "POST":

        form = EnergyMineralRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                "Your energy or mineral request has been submitted successfully."
            )

            return redirect(
                "energy:energy_mineral_request_success",
                request_id=report.pk
            )

    else:

        form = EnergyMineralRequestForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "energy/energy_mineral_request.html",
        context
    )


def energy_mineral_request_success(
    request,
    request_id
):

    report = get_object_or_404(
        EnergyMineralRequest,
        pk=request_id
    )

    context = {
        "report": report,
    }

    return render(
        request,
        "energy/energy_mineral_request_success.html",
        context
    )
    
def energy_mineral_statistics(request):

    electricity_information_count = (
        ElectricityServiceInformation.objects
        .filter(is_published=True)
        .count()
    )

    electricity_problem_count = (
        ElectricityProblemReport.objects
        .count()
    )

    energy_information_count = (
        EnergyServiceInformation.objects
        .filter(is_published=True)
        .count()
    )

    energy_project_count = (
        EnergyProject.objects
        .filter(is_published=True)
        .count()
    )

    mineral_resource_count = (
        MineralResourceInformation.objects
        .filter(is_published=True)
        .count()
    )

    mining_development_count = (
        MiningDevelopmentInformation.objects
        .filter(is_published=True)
        .count()
    )

    energy_request_count = (
        EnergyMineralRequest.objects
        .count()
    )

    request_status_counts = (
        EnergyMineralRequest.objects
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    project_status_counts = (
        EnergyProject.objects
        .filter(is_published=True)
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    problem_status_counts = (
        ElectricityProblemReport.objects
        .values("status")
        .annotate(total=Count("id"))
        .order_by("status")
    )

    context = {
        "electricity_information_count":
            electricity_information_count,

        "electricity_problem_count":
            electricity_problem_count,

        "energy_information_count":
            energy_information_count,

        "energy_project_count":
            energy_project_count,

        "mineral_resource_count":
            mineral_resource_count,

        "mining_development_count":
            mining_development_count,

        "energy_request_count":
            energy_request_count,

        "request_status_counts":
            request_status_counts,

        "project_status_counts":
            project_status_counts,

        "problem_status_counts":
            problem_status_counts,
    }

    return render(
        request,
        "energy/statistics.html",
        context
    )