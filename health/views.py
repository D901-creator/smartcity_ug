from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    HealthEmergencyInformationForm,
    HealthFacilityForm,
    HealthFacilityReportForm,
    HealthInformationForm,
    HealthProjectForm,
    HealthRequestForm,
    HealthServiceForm,
    MedicalEquipmentForm,
    MedicineInformationForm,
)

from .models import (
    HealthEmergencyInformation,
    HealthFacility,
    HealthFacilityReport,
    HealthInformation,
    HealthProject,
    HealthRequest,
    HealthService,
    MedicalEquipment,
    MedicineInformation,
)


# ============================================================
# HEALTH HOME
# ============================================================

def home(request):
    """
    Main citizen Health Services page.
    """

    facilities = HealthFacility.objects.filter(
        is_published=True
    )

    services = HealthService.objects.filter(
        is_published=True
    )

    projects = HealthProject.objects.filter(
        is_published=True
    ).order_by("-created_at")

    information = HealthInformation.objects.filter(
        is_published=True
    ).order_by("-created_at")

    emergency_information = HealthEmergencyInformation.objects.filter(
        is_published=True
    ).order_by("title")

    context = {
        "page_title": "Health Services",
        "page_description": (
            "Access health facilities, health services, health information, "
            "emergency information, health projects and citizen health "
            "reporting services."
        ),

        "total_facilities": facilities.count(),
        "total_services": services.count(),
        "total_projects": projects.count(),
        "total_information": information.count(),

        "featured_facilities": facilities.filter(
            is_featured=True
        )[:6],

        "featured_services": services.filter(
            is_featured=True
        )[:6],

        "recent_projects": projects[:6],

        "featured_information": information.filter(
            is_featured=True
        )[:6],

        "emergency_information": emergency_information[:6],
    }

    return render(
        request,
        "health/home.html",
        context
    )


# ============================================================
# HEALTH FACILITIES
# ============================================================

def facilities(request):

    queryset = HealthFacility.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    facility_type = request.GET.get("facility_type", "").strip()
    district = request.GET.get("district", "").strip()
    emergency = request.GET.get("emergency", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(city__icontains=search)
            | Q(location__icontains=search)
        )

    if facility_type:
        queryset = queryset.filter(
            facility_type=facility_type
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    if emergency == "yes":
        queryset = queryset.filter(
            emergency_available=True
        )

    context = {
        "page_title": "Hospitals & Health Facilities",
        "facilities": queryset,
        "search": search,
        "facility_type": facility_type,
        "district": district,
        "emergency": emergency,
        "facility_types": HealthFacility.FACILITY_TYPES,
    }

    return render(
        request,
        "health/facilities.html",
        context
    )


def facility_detail(request, facility_id):

    facility = get_object_or_404(
        HealthFacility,
        id=facility_id,
        is_published=True
    )

    medicines = MedicineInformation.objects.filter(
        facility=facility,
        is_published=True
    )[:10]

    equipment = MedicalEquipment.objects.filter(
        facility=facility,
        is_published=True
    )[:10]

    emergency_information = HealthEmergencyInformation.objects.filter(
        facility=facility,
        is_published=True
    )[:10]

    context = {
        "page_title": facility.title,
        "facility": facility,
        "medicines": medicines,
        "equipment": equipment,
        "emergency_information": emergency_information,
    }

    return render(
        request,
        "health/facility_detail.html",
        context
    )


# ============================================================
# HEALTH SERVICES
# ============================================================

def services(request):

    queryset = HealthService.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    service_type = request.GET.get("service_type", "").strip()
    district = request.GET.get("district", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
        )

    if service_type:
        queryset = queryset.filter(
            service_type=service_type
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    context = {
        "page_title": "Health Services",
        "services": queryset,
        "search": search,
        "service_type": service_type,
        "district": district,
        "service_types": HealthService.SERVICE_TYPES,
    }

    return render(
        request,
        "health/services.html",
        context
    )


def service_detail(request, service_id):

    service = get_object_or_404(
        HealthService,
        id=service_id,
        is_published=True
    )

    context = {
        "page_title": service.title,
        "service": service,
    }

    return render(
        request,
        "health/service_detail.html",
        context
    )


# ============================================================
# MEDICINES
# ============================================================

def medicines(request):

    queryset = MedicineInformation.objects.filter(
        is_published=True
    ).select_related("facility")

    search = request.GET.get("search", "").strip()
    availability = request.GET.get(
        "availability",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(category__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(facility__title__icontains=search)
        )

    if availability:
        queryset = queryset.filter(
            availability_status=availability
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    context = {
        "page_title": "Medicines & Medical Supplies",
        "medicines": queryset,
        "search": search,
        "availability": availability,
        "district": district,
        "availability_choices": (
            MedicineInformation.AVAILABILITY_STATUS
        ),
    }

    return render(
        request,
        "health/medicines.html",
        context
    )


def medicine_detail(request, medicine_id):

    medicine = get_object_or_404(
        MedicineInformation.objects.select_related(
            "facility"
        ),
        id=medicine_id,
        is_published=True
    )

    return render(
        request,
        "health/medicine_detail.html",
        {
            "page_title": medicine.title,
            "medicine": medicine,
        }
    )


# ============================================================
# MEDICAL EQUIPMENT
# ============================================================

def equipment(request):

    queryset = MedicalEquipment.objects.filter(
        is_published=True
    ).select_related("facility")

    search = request.GET.get("search", "").strip()
    status = request.GET.get("status", "").strip()
    district = request.GET.get("district", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(equipment_type__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(facility__title__icontains=search)
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    context = {
        "page_title": "Medical Equipment",
        "equipment": queryset,
        "search": search,
        "status": status,
        "district": district,
        "status_choices": (
            MedicalEquipment.STATUS_CHOICES
        ),
    }

    return render(
        request,
        "health/equipment.html",
        context
    )


def equipment_detail(request, equipment_id):

    item = get_object_or_404(
        MedicalEquipment.objects.select_related(
            "facility"
        ),
        id=equipment_id,
        is_published=True
    )

    return render(
        request,
        "health/equipment_detail.html",
        {
            "page_title": item.title,
            "equipment": item,
        }
    )


# ============================================================
# HEALTH REQUESTS
# ============================================================

def health_requests(request):

    queryset = HealthRequest.objects.all()

    search = request.GET.get(
        "search",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    request_type = request.GET.get(
        "request_type",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(reference_number__icontains=search)
            | Q(citizen_name__icontains=search)
            | Q(subject__icontains=search)
            | Q(description__icontains=search)
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if request_type:
        queryset = queryset.filter(
            request_type=request_type
        )

    context = {
        "page_title": "Health Requests",
        "requests": queryset,
        "search": search,
        "status": status,
        "request_type": request_type,
        "status_choices": HealthRequest.STATUS_CHOICES,
        "request_types": HealthRequest.REQUEST_TYPES,
    }

    return render(
        request,
        "health/requests.html",
        context
    )


def health_request_create(request):

    if request.method == "POST":

        form = HealthRequestForm(
            request.POST
        )

        if form.is_valid():

            health_request = form.save()

            messages.success(
                request,
                (
                    "Your health request has been submitted "
                    f"successfully. Reference: "
                    f"{health_request.reference_number}"
                )
            )

            return redirect(
                "health:request_success",
                reference_number=(
                    health_request.reference_number
                )
            )

    else:

        form = HealthRequestForm()

    return render(
        request,
        "health/request_form.html",
        {
            "page_title": "Submit Health Request",
            "form": form,
        }
    )


def request_success(
    request,
    reference_number
):

    health_request = get_object_or_404(
        HealthRequest,
        reference_number=reference_number
    )

    return render(
        request,
        "health/request_success.html",
        {
            "page_title": "Health Request Submitted",
            "health_request": health_request,
        }
    )


def health_request_detail(
    request,
    request_id
):

    health_request = get_object_or_404(
        HealthRequest,
        id=request_id
    )

    return render(
        request,
        "health/request_detail.html",
        {
            "page_title": (
                health_request.reference_number
            ),
            "health_request": health_request,
        }
    )


# ============================================================
# HOSPITAL / HEALTH FACILITY REPORTING
# ============================================================

def facility_reports(request):

    queryset = HealthFacilityReport.objects.all()

    search = request.GET.get(
        "search",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    report_type = request.GET.get(
        "report_type",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(reference_number__icontains=search)
            | Q(reporter_name__icontains=search)
            | Q(subject__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if report_type:
        queryset = queryset.filter(
            report_type=report_type
        )

    context = {
        "page_title": "Health Facility Reports",
        "reports": queryset,
        "search": search,
        "status": status,
        "report_type": report_type,
        "status_choices": (
            HealthFacilityReport.STATUS_CHOICES
        ),
        "report_types": (
            HealthFacilityReport.REPORT_TYPES
        ),
    }

    return render(
        request,
        "health/facility_reports.html",
        context
    )


def facility_report_create(request):

    if request.method == "POST":

        form = HealthFacilityReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                (
                    "Your health facility report has been "
                    "submitted successfully. Reference: "
                    f"{report.reference_number}"
                )
            )

            return redirect(
                "health:report_success",
                reference_number=(
                    report.reference_number
                )
            )

    else:

        form = HealthFacilityReportForm()

    return render(
        request,
        "health/facility_report_form.html",
        {
            "page_title": (
                "Report a Hospital or Health Facility Problem"
            ),
            "form": form,
        }
    )


def report_success(
    request,
    reference_number
):

    report = get_object_or_404(
        HealthFacilityReport,
        reference_number=reference_number
    )

    return render(
        request,
        "health/report_success.html",
        {
            "page_title": "Health Facility Report Submitted",
            "report": report,
        }
    )


def facility_report_detail(
    request,
    report_id
):

    report = get_object_or_404(
        HealthFacilityReport,
        id=report_id
    )

    return render(
        request,
        "health/facility_report_detail.html",
        {
            "page_title": report.reference_number,
            "report": report,
        }
    )


# ============================================================
# HEALTH PROJECTS
# ============================================================

def projects(request):

    queryset = HealthProject.objects.filter(
        is_published=True
    )

    search = request.GET.get(
        "search",
        ""
    ).strip()

    project_type = request.GET.get(
        "project_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(implementing_organization__icontains=search)
        )

    if project_type:
        queryset = queryset.filter(
            project_type=project_type
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    context = {
        "page_title": "Health Projects & Programmes",
        "projects": queryset,
        "search": search,
        "project_type": project_type,
        "district": district,
        "status": status,
        "project_types": HealthProject.PROJECT_TYPES,
        "status_choices": HealthProject.STATUS_CHOICES,
    }

    return render(
        request,
        "health/projects.html",
        context
    )


def project_detail(request, project_id):

    project = get_object_or_404(
        HealthProject,
        id=project_id,
        is_published=True
    )

    return render(
        request,
        "health/project_detail.html",
        {
            "page_title": project.title,
            "project": project,
        }
    )


# ============================================================
# HEALTH INFORMATION
# ============================================================

def information(request):

    queryset = HealthInformation.objects.filter(
        is_published=True
    )

    search = request.GET.get(
        "search",
        ""
    ).strip()

    information_type = request.GET.get(
        "information_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(key_points__icontains=search)
            | Q(district__icontains=search)
        )

    if information_type:
        queryset = queryset.filter(
            information_type=information_type
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    context = {
        "page_title": "Health Information",
        "information": queryset,
        "search": search,
        "information_type": information_type,
        "district": district,
        "information_types": (
            HealthInformation.INFORMATION_TYPES
        ),
    }

    return render(
        request,
        "health/information.html",
        context
    )


def information_detail(
    request,
    information_id
):

    item = get_object_or_404(
        HealthInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "health/information_detail.html",
        {
            "page_title": item.title,
            "information": item,
        }
    )


# ============================================================
# EMERGENCY INFORMATION
# ============================================================

def emergency_information(request):

    queryset = HealthEmergencyInformation.objects.filter(
        is_published=True
    ).select_related("facility")

    search = request.GET.get(
        "search",
        ""
    ).strip()

    emergency_type = request.GET.get(
        "emergency_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(emergency_type__icontains=search)
            | Q(description__icontains=search)
            | Q(emergency_number__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(facility__title__icontains=search)
        )

    if emergency_type:
        queryset = queryset.filter(
            emergency_type__icontains=emergency_type
        )

    if district:
        queryset = queryset.filter(
            district__icontains=district
        )

    context = {
        "page_title": "Emergency Health Information",
        "emergency_information": queryset,
        "search": search,
        "emergency_type": emergency_type,
        "district": district,
    }

    return render(
        request,
        "health/emergency_information.html",
        context
    )


def emergency_information_detail(
    request,
    emergency_id
):

    item = get_object_or_404(
        HealthEmergencyInformation.objects.select_related(
            "facility"
        ),
        id=emergency_id,
        is_published=True
    )

    return render(
        request,
        "health/emergency_information_detail.html",
        {
            "page_title": item.title,
            "emergency": item,
        }
    )


# ============================================================
# HEALTH STATISTICS
# ============================================================

def statistics(request):

    facilities = HealthFacility.objects.filter(
        is_published=True
    )

    services = HealthService.objects.filter(
        is_published=True
    )

    medicines = MedicineInformation.objects.filter(
        is_published=True
    )

    equipment_items = MedicalEquipment.objects.filter(
        is_published=True
    )

    projects_queryset = HealthProject.objects.filter(
        is_published=True
    )

    information_queryset = HealthInformation.objects.filter(
        is_published=True
    )

    emergency_queryset = HealthEmergencyInformation.objects.filter(
        is_published=True
    )

    requests_queryset = HealthRequest.objects.all()

    reports_queryset = HealthFacilityReport.objects.all()

    # --------------------------------------------------------
    # BASIC TOTALS
    # --------------------------------------------------------

    total_facilities = facilities.count()
    total_services = services.count()
    total_medicines = medicines.count()
    total_equipment = equipment_items.count()
    total_projects = projects_queryset.count()
    total_information = information_queryset.count()
    total_emergency_information = emergency_queryset.count()
    total_requests = requests_queryset.count()
    total_reports = reports_queryset.count()

    # --------------------------------------------------------
    # FACILITIES BY TYPE
    # --------------------------------------------------------

    facilities_by_type = list(
        facilities.values(
            "facility_type"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # FACILITIES BY DISTRICT
    # --------------------------------------------------------

    facilities_by_district = list(
        facilities.exclude(
            district=""
        ).values(
            "district"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # SERVICES BY TYPE
    # --------------------------------------------------------

    services_by_type = list(
        services.values(
            "service_type"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # MEDICINES BY AVAILABILITY
    # --------------------------------------------------------

    medicines_by_availability = list(
        medicines.values(
            "availability_status"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # EQUIPMENT BY STATUS
    # --------------------------------------------------------

    equipment_by_status = list(
        equipment_items.values(
            "status"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # PROJECTS BY STATUS
    # --------------------------------------------------------

    projects_by_status = list(
        projects_queryset.values(
            "status"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # REQUESTS BY STATUS
    # --------------------------------------------------------

    requests_by_status = list(
        requests_queryset.values(
            "status"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # REPORTS BY STATUS
    # --------------------------------------------------------

    reports_by_status = list(
        reports_queryset.values(
            "status"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # REPORTS BY TYPE
    # --------------------------------------------------------

    reports_by_type = list(
        reports_queryset.values(
            "report_type"
        ).annotate(
            total=Count("id")
        ).order_by("-total")
    )

    # --------------------------------------------------------
    # CONTEXT
    # --------------------------------------------------------

    context = {
        "page_title": "Health Statistics",

        "total_facilities": total_facilities,
        "total_services": total_services,
        "total_medicines": total_medicines,
        "total_equipment": total_equipment,
        "total_projects": total_projects,
        "total_information": total_information,
        "total_emergency_information": (
            total_emergency_information
        ),
        "total_requests": total_requests,
        "total_reports": total_reports,

        "facilities_by_type": facilities_by_type,
        "facilities_by_district": facilities_by_district,

        "services_by_type": services_by_type,

        "medicines_by_availability": (
            medicines_by_availability
        ),

        "equipment_by_status": equipment_by_status,

        "projects_by_status": projects_by_status,

        "requests_by_status": requests_by_status,

        "reports_by_status": reports_by_status,

        "reports_by_type": reports_by_type,
    }

    return render(
        request,
        "health/statistics.html",
        context
    )


# ============================================================
# OPTIONAL CONTENT MANAGEMENT VIEWS
# ============================================================
# These views are included so the models/forms are ready for
# future authorized Officer/Admin integration.
#
# Authentication/RBAC will be connected later.
# ============================================================


def facility_create(request):

    if request.method == "POST":

        form = HealthFacilityForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            facility = form.save()

            messages.success(
                request,
                f"Health facility '{facility.title}' created."
            )

            return redirect(
                "health:facility_detail",
                facility_id=facility.id
            )

    else:

        form = HealthFacilityForm()

    return render(
        request,
        "health/facility_form.html",
        {
            "page_title": "Add Health Facility",
            "form": form,
        }
    )


def service_create(request):

    if request.method == "POST":

        form = HealthServiceForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            service = form.save()

            messages.success(
                request,
                f"Health service '{service.title}' created."
            )

            return redirect(
                "health:service_detail",
                service_id=service.id
            )

    else:

        form = HealthServiceForm()

    return render(
        request,
        "health/service_form.html",
        {
            "page_title": "Add Health Service",
            "form": form,
        }
    )


def medicine_create(request):

    if request.method == "POST":

        form = MedicineInformationForm(
            request.POST
        )

        if form.is_valid():

            medicine = form.save()

            messages.success(
                request,
                f"Medicine information '{medicine.title}' created."
            )

            return redirect(
                "health:medicine_detail",
                medicine_id=medicine.id
            )

    else:

        form = MedicineInformationForm()

    return render(
        request,
        "health/medicine_form.html",
        {
            "page_title": "Add Medicine Information",
            "form": form,
        }
    )


def equipment_create(request):

    if request.method == "POST":

        form = MedicalEquipmentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            item = form.save()

            messages.success(
                request,
                f"Medical equipment '{item.title}' created."
            )

            return redirect(
                "health:equipment_detail",
                equipment_id=item.id
            )

    else:

        form = MedicalEquipmentForm()

    return render(
        request,
        "health/equipment_form.html",
        {
            "page_title": "Add Medical Equipment",
            "form": form,
        }
    )


def project_create(request):

    if request.method == "POST":

        form = HealthProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            project = form.save()

            messages.success(
                request,
                f"Health project '{project.title}' created."
            )

            return redirect(
                "health:project_detail",
                project_id=project.id
            )

    else:

        form = HealthProjectForm()

    return render(
        request,
        "health/project_form.html",
        {
            "page_title": "Add Health Project",
            "form": form,
        }
    )


def information_create(request):

    if request.method == "POST":

        form = HealthInformationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            item = form.save()

            messages.success(
                request,
                f"Health information '{item.title}' created."
            )

            return redirect(
                "health:information_detail",
                information_id=item.id
            )

    else:

        form = HealthInformationForm()

    return render(
        request,
        "health/information_form.html",
        {
            "page_title": "Add Health Information",
            "form": form,
        }
    )


def emergency_information_create(request):

    if request.method == "POST":

        form = HealthEmergencyInformationForm(
            request.POST
        )

        if form.is_valid():

            item = form.save()

            messages.success(
                request,
                (
                    "Emergency health information "
                    f"'{item.title}' created."
                )
            )

            return redirect(
                "health:emergency_information_detail",
                emergency_id=item.id
            )

    else:

        form = HealthEmergencyInformationForm()

    return render(
        request,
        "health/emergency_information_form.html",
        {
            "page_title": "Add Emergency Information",
            "form": form,
        }
    )