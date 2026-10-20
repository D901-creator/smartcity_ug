from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    WaterFacility,
    WaterProblemReport,ClimateEnvironmentalInformation,
    SanitationProblemReport, WasteManagementService,TreeForestSite,EnvironmentalProject,WetlandNaturalResource,
    EnvironmentalProblemReport,DrainageWastewaterReport,WaterProject,EnvironmentalFacility,
    PollutionReport, EnvironmentalIncidentReport,
)

from .forms import (
    WaterProblemReportForm,   PollutionReportForm,
    SanitationProblemReportForm,EnvironmentalIncidentReportForm,
    EnvironmentalProblemReportForm, DrainageWastewaterReportForm,
)
def home(request):
    context = {
        "stats": {
            "water_facilities": WaterFacility.objects.count(),

            "operational_water_facilities": (
                WaterFacility.objects.filter(
                    is_operational=True
                ).count()
            ),

            "water_reports": WaterProblemReport.objects.count(),
        },

        "facilities": WaterFacility.objects.filter(
            is_operational=True
        )[:6],
    }

    return render(
        request,
        "water/home.html",
        context
    )
    
def report_water_problem(request):

    if request.method == "POST":

        form = WaterProblemReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                (
                    "Your water problem has been successfully "
                    f"submitted. Reference: {report.reference_number}"
                )
            )

            return redirect(
                "water:report_success",
                reference_number=report.reference_number
            )

    else:

        form = WaterProblemReportForm()

    return render(
        request,
        "water/report_water_problem.html",
        {
            "form": form
        }
    )
    
def report_success(request, reference_number):

    report = WaterProblemReport.objects.filter(
        reference_number=reference_number
    ).first()

    return render(
        request,
        "water/report_success.html",
        {
            "report": report
        }
    )
    
def report_sanitation_problem(request):
    if request.method == "POST":
        form = SanitationProblemReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            report = form.save()

            messages.success(
                request,
                (
                    "Your sanitation problem has been "
                    "successfully submitted. "
                    f"Reference: {report.reference_number}"
                )
            )

            return redirect(
                "water:sanitation_report_success",
                reference_number=report.reference_number
            )

    else:
        form = SanitationProblemReportForm()

    return render(
        request,
        "water/report_sanitation_problem.html",
        {
            "form": form
        }
    )


def sanitation_report_success(request, reference_number):
    report = SanitationProblemReport.objects.filter(
        reference_number=reference_number
    ).first()

    return render(
        request,
        "water/sanitation_report_success.html",
        {
            "report": report
        }
    )
    
def report_environmental_problem(request):

    if request.method == "POST":

        form = EnvironmentalProblemReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                (
                    "Your environmental problem has been "
                    "successfully submitted. "
                    f"Reference: {report.reference_number}"
                )
            )

            return redirect(
                "water:environment_report_success",
                reference_number=report.reference_number
            )

    else:

        form = EnvironmentalProblemReportForm()

    return render(
        request,
        "water/report_environmental_problem.html",
        {
            "form": form
        }
    )


def environment_report_success(
    request,
    reference_number
):

    report = EnvironmentalProblemReport.objects.filter(
        reference_number=reference_number
    ).first()

    return render(
        request,
        "water/environment_report_success.html",
        {
            "report": report
        }
    )
    
def environmental_services(request):

    services = [
        {
            "name": "Environmental Problem Reporting",
            "icon": "bi-exclamation-triangle",
            "description": (
                "Report environmental problems affecting "
                "your community."
            ),
            "color": "success",
            "url": "water:report_environmental_problem",
        },

        {
            "name": "Waste Management",
            "icon": "bi-recycle",
            "description": (
                "Access information and services related "
                "to waste management."
            ),
            "color": "success",
        },

        {
            "name": "Pollution Control",
            "icon": "bi-cloud-haze2",
            "description": (
                "Access environmental pollution information "
                "and reporting services."
            ),
            "color": "success",
        },

        {
            "name": "Trees & Forests",
            "icon": "bi-tree",
            "description": (
                "Access tree planting, forestry and "
                "conservation services."
            ),
            "color": "success",
        },

        {
            "name": "Wetlands & Natural Resources",
            "icon": "bi-water",
            "description": (
                "Access information about wetlands and "
                "natural-resource protection."
            ),
            "color": "success",
        },

        {
            "name": "Climate & Environment",
            "icon": "bi-cloud-sun",
            "description": (
                "Access climate and environmental "
                "information."
            ),
            "color": "success",
        },
    ]

    return render(
        request,
        "water/environmental_services.html",
        {
            "services": services
        }
    )
def water_facilities(request):
    facilities = WaterFacility.objects.all()

    district = request.GET.get("district", "").strip()
    facility_type = request.GET.get("facility_type", "").strip()
    status = request.GET.get("status", "").strip()

    if district:
        facilities = facilities.filter(
            district__icontains=district
        )

    if facility_type:
        facilities = facilities.filter(
            facility_type=facility_type
        )

    if status == "operational":
        facilities = facilities.filter(
            is_operational=True
        )

    elif status == "not_operational":
        facilities = facilities.filter(
            is_operational=False
        )

    context = {
        "facilities": facilities,
        "district": district,
        "facility_type": facility_type,
        "status": status,
        "facility_types": WaterFacility.FACILITY_TYPES,
        "total_count": facilities.count(),
    }

    return render(
        request,
        "water/water_facilities.html",
        context
    )


def water_facility_detail(request, facility_id):
    facility = get_object_or_404(
        WaterFacility,
        id=facility_id
    )

    return render(
        request,
        "water/water_facility_detail.html",
        {
            "facility": facility
        }
    )
    
def water_supply_information(request):
    facilities = WaterFacility.objects.all()

    district = request.GET.get("district", "").strip()
    facility_type = request.GET.get("facility_type", "").strip()
    status = request.GET.get("status", "").strip()

    if district:
        facilities = facilities.filter(
            district__icontains=district
        )

    if facility_type:
        facilities = facilities.filter(
            facility_type=facility_type
        )

    if status == "operational":
        facilities = facilities.filter(
            is_operational=True
        )

    elif status == "not_operational":
        facilities = facilities.filter(
            is_operational=False
        )

    operational_count = facilities.filter(
        is_operational=True
    ).count()

    non_operational_count = facilities.filter(
        is_operational=False
    ).count()

    context = {
        "facilities": facilities,
        "district": district,
        "facility_type": facility_type,
        "status": status,
        "facility_types": WaterFacility.FACILITY_TYPES,
        "operational_count": operational_count,
        "non_operational_count": non_operational_count,
        "total_count": facilities.count(),
    }

    return render(
        request,
        "water/water_supply_information.html",
        context
    )
    
def drainage_wastewater(request):

    reports = DrainageWastewaterReport.objects.all()

    district = request.GET.get("district", "").strip()

    status = request.GET.get("status", "").strip()

    if district:
        reports = reports.filter(
            district__icontains=district
        )

    if status:
        reports = reports.filter(
            status=status
        )

    context = {
        "reports": reports,
        "district": district,
        "status": status,
        "status_choices": (
            DrainageWastewaterReport.STATUS_CHOICES
        ),
        "total_reports": reports.count(),
    }

    return render(
        request,
        "water/drainage_wastewater.html",
        context
    )


def report_drainage_wastewater(request):

    if request.method == "POST":

        form = DrainageWastewaterReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                (
                    "Your drainage/wastewater problem "
                    "has been successfully submitted. "
                    f"Reference: {report.reference_number}"
                )
            )

            return redirect(
                "water:drainage_wastewater_success",
                reference_number=report.reference_number
            )

    else:

        form = DrainageWastewaterReportForm()

    return render(
        request,
        "water/report_drainage_wastewater.html",
        {
            "form": form
        }
    )


def drainage_wastewater_success(
    request,
    reference_number
):

    report = get_object_or_404(
        DrainageWastewaterReport,
        reference_number=reference_number
    )

    return render(
        request,
        "water/drainage_wastewater_success.html",
        {
            "report": report
        }
    )
    
def water_projects(request):

    projects = WaterProject.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        projects = projects.filter(
            district__icontains=district
        )

    if status:
        projects = projects.filter(
            status=status
        )

    context = {
        "projects": projects,
        "district": district,
        "status": status,
        "status_choices": WaterProject.STATUS_CHOICES,
        "total_projects": projects.count(),
    }

    return render(
        request,
        "water/water_projects.html",
        context
    )
    
def environmental_facilities(request):

    facilities = EnvironmentalFacility.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    facility_type = request.GET.get(
        "facility_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        facilities = facilities.filter(
            district__icontains=district
        )

    if facility_type:
        facilities = facilities.filter(
            facility_type=facility_type
        )

    if status == "operational":
        facilities = facilities.filter(
            is_operational=True
        )

    elif status == "not_operational":
        facilities = facilities.filter(
            is_operational=False
        )

    context = {
        "facilities": facilities,
        "district": district,
        "facility_type": facility_type,
        "status": status,
        "facility_types": EnvironmentalFacility.FACILITY_TYPES,
        "total_count": facilities.count(),
    }

    return render(
        request,
        "water/environmental_facilities.html",
        context
    )


def environmental_facility_detail(
    request,
    facility_id
):

    facility = get_object_or_404(
        EnvironmentalFacility,
        id=facility_id
    )

    return render(
        request,
        "water/environmental_facility_detail.html",
        {
            "facility": facility
        }
    )
    
def waste_management(request):

    services = WasteManagementService.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    service_type = request.GET.get(
        "service_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        services = services.filter(
            district__icontains=district
        )

    if service_type:
        services = services.filter(
            service_type=service_type
        )

    if status == "operational":
        services = services.filter(
            is_operational=True
        )

    elif status == "not_operational":
        services = services.filter(
            is_operational=False
        )

    context = {
        "services": services,
        "district": district,
        "service_type": service_type,
        "status": status,
        "service_types": (
            WasteManagementService.SERVICE_TYPES
        ),
        "frequency_choices": (
            WasteManagementService.FREQUENCY_CHOICES
        ),
        "total_services": services.count(),
    }

    return render(
        request,
        "water/waste_management.html",
        context
    )
    
def pollution_reports(request):

    reports = PollutionReport.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    pollution_type = request.GET.get(
        "pollution_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        reports = reports.filter(
            district__icontains=district
        )

    if pollution_type:
        reports = reports.filter(
            pollution_type=pollution_type
        )

    if status:
        reports = reports.filter(
            status=status
        )

    context = {
        "reports": reports,
        "district": district,
        "pollution_type": pollution_type,
        "status": status,
        "pollution_types": (
            PollutionReport.POLLUTION_TYPES
        ),
        "status_choices": (
            PollutionReport.STATUS_CHOICES
        ),
        "total_reports": reports.count(),
    }

    return render(
        request,
        "water/pollution_reports.html",
        context
    )


def report_pollution(request):

    if request.method == "POST":

        form = PollutionReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                (
                    "Your pollution report has been "
                    "successfully submitted. "
                    f"Reference: {report.reference_number}"
                )
            )

            return redirect(
                "water:pollution_report_success",
                reference_number=report.reference_number
            )

    else:

        form = PollutionReportForm()

    return render(
        request,
        "water/report_pollution.html",
        {
            "form": form
        }
    )


def pollution_report_success(
    request,
    reference_number
):

    report = get_object_or_404(
        PollutionReport,
        reference_number=reference_number
    )

    return render(
        request,
        "water/pollution_report_success.html",
        {
            "report": report
        }
    )
    
def trees_forests(request):

    sites = TreeForestSite.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    site_type = request.GET.get(
        "site_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        sites = sites.filter(
            district__icontains=district
        )

    if site_type:
        sites = sites.filter(
            site_type=site_type
        )

    if status == "operational":
        sites = sites.filter(
            is_operational=True
        )

    elif status == "not_operational":
        sites = sites.filter(
            is_operational=False
        )

    context = {
        "sites": sites,
        "district": district,
        "site_type": site_type,
        "status": status,
        "site_types": TreeForestSite.SITE_TYPES,
        "total_sites": sites.count(),
    }

    return render(
        request,
        "water/trees_forests.html",
        context
    )


def tree_forest_detail(
    request,
    site_id
):

    site = get_object_or_404(
        TreeForestSite,
        id=site_id
    )

    return render(
        request,
        "water/tree_forest_detail.html",
        {
            "site": site
        }
    )
def environmental_projects(request):

    projects = EnvironmentalProject.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    project_type = request.GET.get(
        "project_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        projects = projects.filter(
            district__icontains=district
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
        "district": district,
        "project_type": project_type,
        "status": status,
        "project_types": (
            EnvironmentalProject.PROJECT_TYPES
        ),
        "status_choices": (
            EnvironmentalProject.STATUS_CHOICES
        ),
        "total_projects": projects.count(),
    }

    return render(
        request,
        "water/environmental_projects.html",
        context
    )


def environmental_project_detail(
    request,
    project_id
):

    project = get_object_or_404(
        EnvironmentalProject,
        id=project_id
    )

    return render(
        request,
        "water/environmental_project_detail.html",
        {
            "project": project
        }
    )
    
def wetlands_natural_resources(request):

    resources = WetlandNaturalResource.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    resource_type = request.GET.get(
        "resource_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        resources = resources.filter(
            district__icontains=district
        )

    if resource_type:
        resources = resources.filter(
            resource_type=resource_type
        )

    if status == "protected":
        resources = resources.filter(
            is_protected=True
        )

    elif status == "active":
        resources = resources.filter(
            is_active=True
        )

    elif status == "inactive":
        resources = resources.filter(
            is_active=False
        )

    context = {
        "resources": resources,
        "district": district,
        "resource_type": resource_type,
        "status": status,
        "resource_types": (
            WetlandNaturalResource.RESOURCE_TYPES
        ),
        "total_resources": resources.count(),
    }

    return render(
        request,
        "water/wetlands_natural_resources.html",
        context
    )


def wetland_natural_resource_detail(
    request,
    resource_id
):

    resource = get_object_or_404(
        WetlandNaturalResource,
        id=resource_id
    )

    return render(
        request,
        "water/wetland_natural_resource_detail.html",
        {
            "resource": resource
        }
    )
def climate_environmental_information(request):

    information = ClimateEnvironmentalInformation.objects.filter(
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
            ClimateEnvironmentalInformation.CATEGORY_CHOICES
        ),
        "total_information": information.count(),
    }

    return render(
        request,
        "water/climate_environmental_information.html",
        context
    )


def climate_environmental_information_detail(
    request,
    information_id
):

    information = get_object_or_404(
        ClimateEnvironmentalInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "water/climate_environmental_information_detail.html",
        {
            "information": information
        }
    )
    
def environmental_incidents(request):

    incidents = EnvironmentalIncidentReport.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    incident_type = request.GET.get(
        "incident_type",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if district:
        incidents = incidents.filter(
            district__icontains=district
        )

    if incident_type:
        incidents = incidents.filter(
            incident_type=incident_type
        )

    if status:
        incidents = incidents.filter(
            status=status
        )

    context = {
        "incidents": incidents,
        "district": district,
        "incident_type": incident_type,
        "status": status,
        "incident_types": (
            EnvironmentalIncidentReport.INCIDENT_TYPES
        ),
        "status_choices": (
            EnvironmentalIncidentReport.STATUS_CHOICES
        ),
        "total_incidents": incidents.count(),
    }

    return render(
        request,
        "water/environmental_incidents.html",
        context
    )


def report_environmental_incident(request):

    if request.method == "POST":

        form = EnvironmentalIncidentReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            incident = form.save()

            messages.success(
                request,
                "Environmental incident successfully reported."
            )

            return redirect(
                "water:environmental_incident_success",
                reference_number=incident.reference_number
            )

    else:

        form = EnvironmentalIncidentReportForm()

    return render(
        request,
        "water/report_environmental_incident.html",
        {
            "form": form
        }
    )


def environmental_incident_success(
    request,
    reference_number
):

    incident = get_object_or_404(
        EnvironmentalIncidentReport,
        reference_number=reference_number
    )

    return render(
        request,
        "water/environmental_incident_success.html",
        {
            "incident": incident
        }
    )


def environmental_incident_detail(
    request,
    incident_id
):

    incident = get_object_or_404(
        EnvironmentalIncidentReport,
        id=incident_id
    )

    return render(
        request,
        "water/environmental_incident_detail.html",
        {
            "incident": incident
        }
    )
def get_request_status_steps(report):
    current_status = report.status

    status_order = [
        "submitted",
        "received",
        "investigating",
        "in_progress",
        "resolved",
    ]

    if current_status == "rejected":
        return [
            {
                "code": "submitted",
                "label": "Submitted",
                "completed": True,
            },
            {
                "code": "rejected",
                "label": "Rejected",
                "completed": True,
            },
        ]

    try:
        current_index = status_order.index(
            current_status
        )
    except ValueError:
        current_index = 0

    steps = []

    for index, status_code in enumerate(status_order):

        labels = {
            "submitted": "Submitted",
            "received": "Received",
            "investigating": "Investigating",
            "in_progress": "In Progress",
            "resolved": "Resolved",
        }

        steps.append(
            {
                "code": status_code,
                "label": labels[status_code],
                "completed": index <= current_index,
                "current": index == current_index,
            }
        )

    return steps
    
def citizen_request_tracking(request):

    reference_number = request.GET.get(
        "reference_number",
        ""
    ).strip().upper()

    report_type = request.GET.get(
        "report_type",
        ""
    ).strip()

    report = None
    report_category = None
    not_found = False

    # -----------------------------------------
    # SEARCH WATER PROBLEM
    # -----------------------------------------
    if reference_number:

        if not report_type or report_type == "water":
            try:
                report = WaterProblemReport.objects.get(
                    reference_number=reference_number
                )
                report_category = "Water Problem"
            except WaterProblemReport.DoesNotExist:
                pass

        # -----------------------------------------
        # SEARCH DRAINAGE & WASTEWATER
        # -----------------------------------------
        if report is None and (
            not report_type or report_type == "drainage"
        ):
            try:
                report = DrainageWastewaterReport.objects.get(
                    reference_number=reference_number
                )
                report_category = "Drainage & Wastewater"
            except DrainageWastewaterReport.DoesNotExist:
                pass

        # -----------------------------------------
        # SEARCH POLLUTION
        # -----------------------------------------
        if report is None and (
            not report_type or report_type == "pollution"
        ):
            try:
                report = PollutionReport.objects.get(
                    reference_number=reference_number
                )
                report_category = "Pollution"
            except PollutionReport.DoesNotExist:
                pass

        # -----------------------------------------
        # SEARCH ENVIRONMENTAL INCIDENT
        # -----------------------------------------
        if report is None and (
            not report_type or report_type == "incident"
        ):
            try:
                report = EnvironmentalIncidentReport.objects.get(
                    reference_number=reference_number
                )
                report_category = "Environmental Incident"
            except EnvironmentalIncidentReport.DoesNotExist:
                pass

        # -----------------------------------------
        # NOTHING FOUND
        # -----------------------------------------
        if report is None:
            not_found = True

    # -----------------------------------------
    # STATUS STEPS
    # -----------------------------------------
    status_steps = []

    if report:
        status_steps = get_request_status_steps(report)

    # -----------------------------------------
    # RETURN PAGE
    # -----------------------------------------
    return render(
        request,
        "water/citizen_request_tracking.html",
        {
            "reference_number": reference_number,
            "report_type": report_type,
            "report": report,
            "report_category": report_category,
            "not_found": not_found,
            "status_steps": status_steps,
        }
    )
    
def water_environment_statistics(request):
    district = request.GET.get("district", "").strip()

    # Water
    water_facilities = WaterFacility.objects.all()
    water_reports = WaterProblemReport.objects.all()
    drainage_reports = DrainageWastewaterReport.objects.all()
    water_projects = WaterProject.objects.all()

    # Environment
    environmental_facilities = EnvironmentalFacility.objects.all()
    waste_services = WasteManagementService.objects.all()
    pollution_reports = PollutionReport.objects.all()
    tree_forest_sites = TreeForestSite.objects.all()
    environmental_projects = EnvironmentalProject.objects.all()
    wetlands_resources = WetlandNaturalResource.objects.all()
    climate_information = ClimateEnvironmentalInformation.objects.filter(
        is_published=True
    )
    environmental_incidents = EnvironmentalIncidentReport.objects.all()

    # Apply district filter
    if district:
        water_facilities = water_facilities.filter(
            district__icontains=district
        )
        water_reports = water_reports.filter(
            district__icontains=district
        )
        drainage_reports = drainage_reports.filter(
            district__icontains=district
        )
        water_projects = water_projects.filter(
            district__icontains=district
        )
        environmental_facilities = environmental_facilities.filter(
            district__icontains=district
        )
        waste_services = waste_services.filter(
            district__icontains=district
        )
        pollution_reports = pollution_reports.filter(
            district__icontains=district
        )
        tree_forest_sites = tree_forest_sites.filter(
            district__icontains=district
        )
        environmental_projects = environmental_projects.filter(
            district__icontains=district
        )
        wetlands_resources = wetlands_resources.filter(
            district__icontains=district
        )
        climate_information = climate_information.filter(
            district__icontains=district
        )
        environmental_incidents = environmental_incidents.filter(
            district__icontains=district
        )

    context = {
        "district": district,

        # Water statistics
        "water_facilities_count": water_facilities.count(),
        "operational_water_facilities_count": water_facilities.filter(
            is_operational=True
        ).count(),

        "water_reports_count": water_reports.count(),
        "water_pending_count": water_reports.exclude(
            status__in=["resolved", "rejected"]
        ).count(),
        "water_resolved_count": water_reports.filter(
            status="resolved"
        ).count(),

        "drainage_reports_count": drainage_reports.count(),
        "drainage_resolved_count": drainage_reports.filter(
            status="resolved"
        ).count(),

        "water_projects_count": water_projects.count(),
        "water_ongoing_projects_count": water_projects.filter(
            status="ongoing"
        ).count(),
        "water_completed_projects_count": water_projects.filter(
            status="completed"
        ).count(),

        # Environmental statistics
        "environmental_facilities_count": environmental_facilities.count(),
        "waste_services_count": waste_services.count(),
        "pollution_reports_count": pollution_reports.count(),
        "pollution_resolved_count": pollution_reports.filter(
            status="resolved"
        ).count(),

        "tree_forest_sites_count": tree_forest_sites.count(),
        "environmental_projects_count": environmental_projects.count(),
        "environmental_ongoing_projects_count": environmental_projects.filter(
            status="ongoing"
        ).count(),

        "wetlands_resources_count": wetlands_resources.count(),

        "climate_information_count": climate_information.count(),

        "environmental_incidents_count": environmental_incidents.count(),
        "environmental_incidents_resolved_count": environmental_incidents.filter(
            status="resolved"
        ).count(),
    }

    return render(
        request,
        "water/water_environment_statistics.html",
        context
    )
    
def environment(request):
    context = {
        "environmental_facilities_count": EnvironmentalFacility.objects.count(),
        "waste_services_count": WasteManagementService.objects.count(),
        "pollution_reports_count": PollutionReport.objects.count(),
        "tree_forest_sites_count": TreeForestSite.objects.count(),
        "wetlands_resources_count": WetlandNaturalResource.objects.count(),
        "environmental_projects_count": EnvironmentalProject.objects.count(),
        "climate_information_count": ClimateEnvironmentalInformation.objects.filter(
            is_published=True
        ).count(),
        "environmental_incidents_count": EnvironmentalIncidentReport.objects.count(),
    }

    return render(
        request,
        "water/environment.html",
        context
    )