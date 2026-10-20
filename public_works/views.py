from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    redirect,
    
)
from django.db.models import Sum, Avg
from django.utils import timezone
from .forms import RoadProblemReportForm, TrafficIncidentReportForm
from .models import( RoadProblemReport,Road,RoadConstructionMaintenanceProject,
                    TrafficRoadSafetyInformation,  TrafficIncidentReport,ParkingFacility,
    ParkingFee,PublicWorksProject,
    ParkingPayment,TransportInformationAdvisory,
    ParkingReceipt,PublicWorksFacility,)

def home(request):
    services = [
       {
    "name": "Road Problem Reporting",
    "icon": "bi-exclamation-triangle",
    "description": "Report potholes, damaged roads and other road-related problems.",
    "color": "danger",
    "url": "public_works:road_problem_report",
},
       {
    "name": "Roads & Road Network",
    "icon": "bi-signpost-2",
    "description": "Access information about roads and the road network.",
    "color": "primary",
    "url": "public_works:road_infrastructure_services",
},
        {
            "name": "Road Construction & Maintenance",
            "icon": "bi-cone-striped",
            "description": "View road construction and maintenance projects.",
            "color": "warning",
            "url": "public_works:road_construction_projects",
        },
       {
    "name": "Traffic & Road Safety",
    "icon": "bi-shield-check",
    "description": "Access traffic information, road safety guidance and road-user awareness.",
    "color": "warning",
    "url": "public_works:traffic_road_safety",
},
        {
            "name": "Traffic Incident Reporting",
            "icon": "bi-car-front",
            "description": "Report traffic-related incidents and road safety concerns.",
            "color": "danger",
            "url": "public_works:traffic_incident_report",
        },
        {
            "name": "Parking Services",
            "icon": "bi-p-square",
            "description": "Access parking services, fees, revenues, taxes and payments.",
            "color": "info",
          "url": "public_works:parking_services",
        },
        {
            "name": "Public Works Facilities",
            "icon": "bi-building",
            "description": "View information about public works facilities.",
            "color": "secondary",
            "url": "public_works:public_works_facilities",
        },
        {
            "name": "Transport Information & Advisories",
            "icon": "bi-info-circle",
            "description": "View official transport information and public advisories.",
            "color": "dark",
            "url": "public_works:transport_information",
        },
        {
            "name": "Public Works Projects",
            "icon": "bi-kanban",
            "description": "View public works and infrastructure development projects.",
            "color": "success",
             "url": "public_works:public_works_projects",
        },
        {
            "name": "Public Works & Transport Statistics",
            "icon": "bi-bar-chart",
            "description": "View public works and transport service statistics.",
            "color": "primary",
             "url": "public_works:public_works_statistics",
        },
    ]

    context = {
        "services": services,
    }

    return render(
        request,
        "public_works/home.html",
        context
    )
def report_road_problem(request):

    if request.method == "POST":

        form = RoadProblemReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            messages.success(
                request,
                "Road problem successfully reported."
            )

            return redirect(
                "public_works:road_problem_success",
                reference_number=report.reference_number
            )

    else:
        form = RoadProblemReportForm()

    return render(
        request,
        "public_works/report_road_problem.html",
        {
            "form": form
        }
    )


def road_problem_success(
    request,
    reference_number
):

    report = get_object_or_404(
        RoadProblemReport,
        reference_number=reference_number
    )

    return render(
        request,
        "public_works/road_problem_success.html",
        {
            "report": report
        }
    )


def road_problem_reports(request):

    reports = RoadProblemReport.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    problem_type = request.GET.get(
        "problem_type",
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

    if problem_type:
        reports = reports.filter(
            problem_type=problem_type
        )

    if status:
        reports = reports.filter(
            status=status
        )

    context = {
        "reports": reports,
        "district": district,
        "problem_type": problem_type,
        "status": status,
        "problem_types": RoadProblemReport.PROBLEM_TYPES,
        "status_choices": RoadProblemReport.STATUS_CHOICES,
        "total_reports": reports.count(),
    }

    return render(
        request,
        "public_works/road_problem_reports.html",
        context
    )


def road_problem_detail(
    request,
    report_id
):

    report = get_object_or_404(
        RoadProblemReport,
        id=report_id
    )

    return render(
        request,
        "public_works/road_problem_detail.html",
        {
            "report": report
        }
    )
    
def road_infrastructure_services(request):
    services = [
        {
            "name": "Road Maintenance",
            "slug": "road-maintenance",
            "icon": "bi-tools",
            "description": "Access information about road maintenance activities and services.",
            "color": "primary",
        },
        {
            "name": "Road Rehabilitation",
            "slug": "road-rehabilitation",
            "icon": "bi-arrow-repeat",
            "description": "View information about road rehabilitation and improvement services.",
            "color": "success",
        },
        {
            "name": "Road Safety Infrastructure",
            "slug": "road-safety-infrastructure",
            "icon": "bi-shield-check",
            "description": "Access information about road safety infrastructure.",
            "color": "warning",
        },
        {
            "name": "Road Signs & Markings",
            "slug": "road-signs-markings",
            "icon": "bi-signpost",
            "description": "Access information about road signs, markings and related infrastructure.",
            "color": "info",
        },
        {
            "name": "Pedestrian Infrastructure",
            "slug": "pedestrian-infrastructure",
            "icon": "bi-person-walking",
            "description": "View information about pedestrian-related road infrastructure.",
            "color": "secondary",
        },
        {
            "name": "Roadside Infrastructure",
            "slug": "roadside-infrastructure",
            "icon": "bi-signpost-split",
            "description": "Access information about roadside infrastructure and facilities.",
            "color": "dark",
        },
        {
            "name": "Infrastructure Information",
            "slug": "infrastructure-information",
            "icon": "bi-info-circle",
            "description": "Find public information about roads and related infrastructure.",
            "color": "success",
        },
    ]

    return render(
        request,
        "public_works/road_infrastructure_services.html",
        {"services": services}
    )


def road_infrastructure_service_detail(request, slug):
    service_information = {
        "road-maintenance": {
            "title": "Road Maintenance",
            "icon": "bi-tools",
            "description": (
                "Information about routine and planned road maintenance "
                "activities."
            ),
            "items": [
                "Routine road maintenance",
                "Pothole and road-surface maintenance",
                "Road shoulder maintenance",
                "Road maintenance schedules",
                "Maintenance service information",
                "Road maintenance reporting",
            ],
        },

        "road-rehabilitation": {
            "title": "Road Rehabilitation",
            "icon": "bi-arrow-repeat",
            "description": (
                "Information about road rehabilitation, upgrading and "
                "improvement activities."
            ),
            "items": [
                "Road rehabilitation information",
                "Road upgrading activities",
                "Road improvement projects",
                "Rehabilitation locations",
                "Project progress information",
                "Public road improvement information",
            ],
        },

        "road-safety-infrastructure": {
            "title": "Road Safety Infrastructure",
            "icon": "bi-shield-check",
            "description": (
                "Information about infrastructure intended to improve "
                "road-user safety."
            ),
            "items": [
                "Road safety barriers",
                "Safety signs",
                "Traffic safety infrastructure",
                "Pedestrian safety infrastructure",
                "Road safety improvement information",
                "Safety-related infrastructure reporting",
            ],
        },

        "road-signs-markings": {
            "title": "Road Signs & Markings",
            "icon": "bi-signpost",
            "description": (
                "Information about road signs, road markings and other "
                "traffic guidance infrastructure."
            ),
            "items": [
                "Road signs",
                "Traffic signs",
                "Road markings",
                "Pedestrian crossings",
                "Directional signs",
                "Road-sign and marking problems",
            ],
        },

        "pedestrian-infrastructure": {
            "title": "Pedestrian Infrastructure",
            "icon": "bi-person-walking",
            "description": (
                "Information about infrastructure provided for pedestrians "
                "and other vulnerable road users."
            ),
            "items": [
                "Footpaths",
                "Sidewalks",
                "Pedestrian crossings",
                "Pedestrian safety infrastructure",
                "Accessible pedestrian facilities",
                "Pedestrian infrastructure information",
            ],
        },

        "roadside-infrastructure": {
            "title": "Roadside Infrastructure",
            "icon": "bi-signpost-split",
            "description": (
                "Information about infrastructure located along roads and "
                "road corridors."
            ),
            "items": [
                "Roadside facilities",
                "Roadside signs",
                "Safety barriers",
                "Roadside structures",
                "Road corridor information",
                "Roadside infrastructure reporting",
            ],
        },

        "infrastructure-information": {
            "title": "Infrastructure Information",
            "icon": "bi-info-circle",
            "description": (
                "Public information about roads and related infrastructure "
                "services."
            ),
            "items": [
                "Road infrastructure information",
                "Road classifications",
                "Infrastructure services",
                "Road development information",
                "Maintenance information",
                "Public works infrastructure updates",
            ],
        },
    }

    service = service_information.get(slug)

    if not service:
        return render(
            request,
            "public_works/road_infrastructure_service_not_found.html",
            status=404
        )

    return render(
        request,
        "public_works/road_infrastructure_service_detail.html",
        {"service": service}
    )
    
def roads_network(request):

    roads = Road.objects.all()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    road_class = request.GET.get(
        "road_class",
        ""
    ).strip()

    condition = request.GET.get(
        "condition",
        ""
    ).strip()

    surface_type = request.GET.get(
        "surface_type",
        ""
    ).strip()

    if district:
        roads = roads.filter(
            district__icontains=district
        )

    if road_class:
        roads = roads.filter(
            road_class=road_class
        )

    if condition:
        roads = roads.filter(
            condition=condition
        )

    if surface_type:
        roads = roads.filter(
            surface_type=surface_type
        )

    context = {
        "roads": roads,

        "district": district,

        "road_class": road_class,

        "condition": condition,

        "surface_type": surface_type,

        "road_classes": Road.ROAD_CLASS_CHOICES,

        "conditions": Road.CONDITION_CHOICES,

        "surface_types": Road.SURFACE_CHOICES,

        "total_roads": roads.count(),
    }

    return render(
        request,
        "public_works/roads_network.html",
        context
    )
    
def road_construction_projects(request):

    projects = RoadConstructionMaintenanceProject.objects.all()

    district = request.GET.get("district", "").strip()
    project_type = request.GET.get("project_type", "").strip()
    status = request.GET.get("status", "").strip()

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
            RoadConstructionMaintenanceProject
            .PROJECT_TYPE_CHOICES
        ),

        "status_choices": (
            RoadConstructionMaintenanceProject
            .STATUS_CHOICES
        ),

        "total_projects": projects.count(),
    }

    return render(
        request,
        "public_works/road_construction_projects.html",
        context
    )


def road_construction_project_detail(
    request,
    project_id
):

    project = get_object_or_404(
        RoadConstructionMaintenanceProject,
        id=project_id
    )

    return render(
        request,
        "public_works/road_construction_project_detail.html",
        {
            "project": project
        }
    )
    
def traffic_road_safety(request):

    information = TrafficRoadSafetyInformation.objects.filter(
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
            TrafficRoadSafetyInformation
            .CATEGORY_CHOICES
        ),

        "total_information": information.count(),
    }

    return render(
        request,
        "public_works/traffic_road_safety.html",
        context
    )


def traffic_road_safety_detail(
    request,
    information_id
):

    information = get_object_or_404(
        TrafficRoadSafetyInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "public_works/traffic_road_safety_detail.html",
        {
            "information": information
        }
    )
    
def report_traffic_incident(request):

    if request.method == "POST":

        form = TrafficIncidentReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            incident = form.save()

            messages.success(
                request,
                "Traffic incident successfully reported."
            )

            return redirect(
                "public_works:traffic_incident_success",
                reference_number=incident.reference_number
            )

    else:

        form = TrafficIncidentReportForm()

    return render(
        request,
        "public_works/report_traffic_incident.html",
        {
            "form": form
        }
    )


def traffic_incident_success(
    request,
    reference_number
):

    incident = get_object_or_404(
        TrafficIncidentReport,
        reference_number=reference_number
    )

    return render(
        request,
        "public_works/traffic_incident_success.html",
        {
            "incident": incident
        }
    )


def traffic_incident_reports(request):

    reports = TrafficIncidentReport.objects.all()

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

        reports = reports.filter(
            district__icontains=district
        )

    if incident_type:

        reports = reports.filter(
            incident_type=incident_type
        )

    if status:

        reports = reports.filter(
            status=status
        )

    context = {
        "reports": reports,
        "district": district,
        "incident_type": incident_type,
        "status": status,

        "incident_types": (
            TrafficIncidentReport.INCIDENT_TYPES
        ),

        "status_choices": (
            TrafficIncidentReport.STATUS_CHOICES
        ),

        "total_reports": reports.count(),
    }

    return render(
        request,
        "public_works/traffic_incident_reports.html",
        context
    )


def traffic_incident_detail(
    request,
    incident_id
):

    incident = get_object_or_404(
        TrafficIncidentReport,
        id=incident_id
    )

    return render(
        request,
        "public_works/traffic_incident_detail.html",
        {
            "incident": incident
        }
    )
    
def parking_services(request):

    facilities = ParkingFacility.objects.all()

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

    if status:
        facilities = facilities.filter(
            status=status
        )

    context = {
        "facilities": facilities,
        "district": district,
        "facility_type": facility_type,
        "status": status,
        "facility_types": ParkingFacility.FACILITY_TYPES,
        "status_choices": ParkingFacility.STATUS_CHOICES,
        "total_facilities": facilities.count(),
    }

    return render(
        request,
        "public_works/parking_services.html",
        context
    )
    
def parking_facility_detail(
    request,
    facility_id
):

    facility = get_object_or_404(
        ParkingFacility,
        id=facility_id
    )

    fees = facility.fees.filter(
        is_active=True
    )

    return render(
        request,
        "public_works/parking_facility_detail.html",
        {
            "facility": facility,
            "fees": fees,
        }
    )
    
def parking_payment(request, facility_id, fee_id):

    facility = get_object_or_404(
        ParkingFacility,
        id=facility_id
    )

    fee = get_object_or_404(
        ParkingFee,
        id=fee_id,
        facility=facility,
        is_active=True
    )

    if request.method == "POST":

        citizen_name = request.POST.get(
            "citizen_name",
            ""
        ).strip()

        phone_number = request.POST.get(
            "phone_number",
            ""
        ).strip()

        vehicle_registration = request.POST.get(
            "vehicle_registration",
            ""
        ).strip()

        payment_method = request.POST.get(
            "payment_method",
            ""
        ).strip()

        if not citizen_name or not phone_number:
            messages.error(
                request,
                "Please provide your name and phone number."
            )

        elif not vehicle_registration:
            messages.error(
                request,
                "Please provide the vehicle registration number."
            )

        elif payment_method not in dict(
            ParkingPayment.PAYMENT_METHODS
        ):
            messages.error(
                request,
                "Please select a valid payment method."
            )

        else:

            payment = ParkingPayment.objects.create(
                citizen_name=citizen_name,
                phone_number=phone_number,
                vehicle_registration=vehicle_registration,
                facility=facility,
                fee=fee,
                payment_method=payment_method,
                amount=fee.amount,
                tax_amount=fee.tax_amount,
                status=ParkingPayment.STATUS_PENDING,
                payment_instructions=(
                    "Follow the payment instructions provided "
                    "for the selected payment method."
                ),
            )

            messages.success(
                request,
                "Parking payment request created successfully."
            )

            return redirect(
                "public_works:parking_payment_confirmation",
                payment_reference=payment.payment_reference
            )

    return render(
        request,
        "public_works/parking_payment.html",
        {
            "facility": facility,
            "fee": fee,
            "payment_methods": ParkingPayment.PAYMENT_METHODS,
        }
    )
    
def parking_payment_confirmation(
    request,
    payment_reference
):

    payment = get_object_or_404(
        ParkingPayment,
        payment_reference=payment_reference
    )

    return render(
        request,
        "public_works/parking_payment_confirmation.html",
        {
            "payment": payment
        }
    )
    
def parking_receipt(
    request,
    payment_reference
):

    payment = get_object_or_404(
        ParkingPayment,
        payment_reference=payment_reference
    )

    receipt = None

    if payment.status == ParkingPayment.STATUS_PAID:

        receipt, created = ParkingReceipt.objects.get_or_create(
            payment=payment,
            defaults={
                "issued_to": payment.citizen_name,
                "vehicle_registration": (
                    payment.vehicle_registration
                ),
                "facility_name": payment.facility.name,
                "amount_paid": payment.total_amount,
                "payment_method": payment.get_payment_method_display(),
                "confirmation_message": (
                    "Parking payment successfully confirmed."
                ),
            }
        )

    return render(
        request,
        "public_works/parking_receipt.html",
        {
            "payment": payment,
            "receipt": receipt,
        }
    )
def public_works_facilities(request):

    facilities = PublicWorksFacility.objects.all()

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

    if status:
        facilities = facilities.filter(
            status=status
        )

    context = {
        "facilities": facilities,
        "district": district,
        "facility_type": facility_type,
        "status": status,

        "facility_types": (
            PublicWorksFacility.FACILITY_TYPES
        ),

        "status_choices": (
            PublicWorksFacility.STATUS_CHOICES
        ),

        "total_facilities": facilities.count(),
    }

    return render(
        request,
        "public_works/public_works_facilities.html",
        context
    )
def transport_information_advisories(request):

    advisories = TransportInformationAdvisory.objects.filter(
        status=TransportInformationAdvisory.STATUS_PUBLISHED
    )

    district = request.GET.get(
        "district",
        ""
    ).strip()

    category = request.GET.get(
        "category",
        ""
    ).strip()

    priority = request.GET.get(
        "priority",
        ""
    ).strip()

    if district:
        advisories = advisories.filter(
            district__icontains=district
        )

    if category:
        advisories = advisories.filter(
            category=category
        )

    if priority:
        advisories = advisories.filter(
            priority=priority
        )

    context = {
        "advisories": advisories,

        "district": district,
        "category": category,
        "priority": priority,

        "categories": (
            TransportInformationAdvisory.CATEGORY_CHOICES
        ),

        "priorities": (
            TransportInformationAdvisory.PRIORITY_CHOICES
        ),

        "total_advisories": advisories.count(),
    }

    return render(
        request,
        "public_works/transport_information.html",
        context
    )
    
def transport_information_detail(
    request,
    advisory_id
):

    advisory = get_object_or_404(
        TransportInformationAdvisory,
        id=advisory_id,
        status=TransportInformationAdvisory.STATUS_PUBLISHED
    )

    return render(
        request,
        "public_works/transport_information_detail.html",
        {
            "advisory": advisory
        }
    )
    
def public_works_projects(request):

    projects = PublicWorksProject.objects.all()

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
            PublicWorksProject.PROJECT_TYPES
        ),

        "status_choices": (
            PublicWorksProject.STATUS_CHOICES
        ),

        "total_projects": projects.count(),
    }

    return render(
        request,
        "public_works/public_works_projects.html",
        context
    )
    
def public_works_project_detail(
    request,
    project_id
):

    project = get_object_or_404(
        PublicWorksProject,
        id=project_id
    )

    return render(
        request,
        "public_works/public_works_project_detail.html",
        {
            "project": project
        }
    )
    
def public_works_transport_statistics(request):

    district = request.GET.get(
        "district",
        ""
    ).strip()

    # ---------------------------------
    # Base querysets
    # ---------------------------------

    roads = Road.objects.all()

    road_reports = RoadProblemReport.objects.all()

    projects = PublicWorksProject.objects.all()

    facilities = PublicWorksFacility.objects.all()

    advisories = TransportInformationAdvisory.objects.filter(
        status=TransportInformationAdvisory.STATUS_PUBLISHED
    )

    parking_facilities = ParkingFacility.objects.all()

    parking_payments = ParkingPayment.objects.all()

    # ---------------------------------
    # Traffic incident queryset
    # ---------------------------------

    traffic_incidents = TrafficIncidentReport.objects.all()

    # ---------------------------------
    # District filter
    # ---------------------------------

    if district:

        roads = roads.filter(
            district__icontains=district
        )

        road_reports = road_reports.filter(
            district__icontains=district
        )

        projects = projects.filter(
            district__icontains=district
        )

        facilities = facilities.filter(
            district__icontains=district
        )

        advisories = advisories.filter(
            district__icontains=district
        )

        parking_facilities = parking_facilities.filter(
            district__icontains=district
        )

        parking_payments = parking_payments.filter(
            facility__district__icontains=district
        )

        traffic_incidents = traffic_incidents.filter(
            district__icontains=district
        )

    # ---------------------------------
    # Road statistics
    # ---------------------------------

    roads_count = roads.count()

    operational_roads_count = roads.filter(
        is_operational=True
    ).count()

    good_roads_count = roads.filter(
        condition=Road.CONDITION_GOOD
    ).count()

    poor_roads_count = roads.filter(
        condition=Road.CONDITION_POOR
    ).count()

    critical_roads_count = roads.filter(
        condition=Road.CONDITION_CRITICAL
    ).count()

    total_road_length = roads.aggregate(
        total=Sum("length_km")
    )["total"] or 0

    # ---------------------------------
    # Road problem statistics
    # ---------------------------------

    road_reports_count = road_reports.count()

    road_reports_pending = road_reports.exclude(
        status__in=[
            RoadProblemReport.STATUS_RESOLVED,
            RoadProblemReport.STATUS_REJECTED,
        ]
    ).count()

    road_reports_resolved = road_reports.filter(
        status=RoadProblemReport.STATUS_RESOLVED
    ).count()

    # ---------------------------------
    # Project statistics
    # ---------------------------------

    projects_count = projects.count()

    ongoing_projects_count = projects.filter(
        status=PublicWorksProject.STATUS_ONGOING
    ).count()

    completed_projects_count = projects.filter(
        status=PublicWorksProject.STATUS_COMPLETED
    ).count()

    planned_projects_count = projects.filter(
        status=PublicWorksProject.STATUS_PLANNED
    ).count()

    project_average_completion = projects.aggregate(
        average=Avg("completion_percentage")
    )["average"] or 0

    # ---------------------------------
    # Public works facilities
    # ---------------------------------

    facilities_count = facilities.count()

    operational_facilities_count = facilities.filter(
        status=PublicWorksFacility.STATUS_OPERATIONAL
    ).count()

    # ---------------------------------
    # Traffic statistics
    # ---------------------------------

    traffic_incidents_count = traffic_incidents.count()

    traffic_incidents_resolved = traffic_incidents.filter(
        status="resolved"
    ).count()

    traffic_incidents_pending = traffic_incidents.exclude(
        status="resolved"
    ).count()

    # ---------------------------------
    # Parking statistics
    # ---------------------------------

    parking_facilities_count = parking_facilities.count()

    operational_parking_count = parking_facilities.filter(
        status=ParkingFacility.STATUS_OPERATIONAL
    ).count()

    parking_payments_count = parking_payments.count()

    parking_paid_count = parking_payments.filter(
        status=ParkingPayment.STATUS_PAID
    ).count()

    parking_pending_count = parking_payments.filter(
        status__in=[
            ParkingPayment.STATUS_PENDING,
            ParkingPayment.STATUS_PROCESSING,
        ]
    ).count()

    parking_revenue = parking_payments.filter(
        status=ParkingPayment.STATUS_PAID
    ).aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    # ---------------------------------
    # Transport advisories
    # ---------------------------------

    advisories_count = advisories.count()

    urgent_advisories_count = advisories.filter(
        priority=TransportInformationAdvisory.PRIORITY_URGENT
    ).count()

    high_advisories_count = advisories.filter(
        priority=TransportInformationAdvisory.PRIORITY_HIGH
    ).count()

    # ---------------------------------
    # Overall totals
    # ---------------------------------

    total_records = (
        roads_count
        + road_reports_count
        + projects_count
        + facilities_count
        + traffic_incidents_count
        + parking_facilities_count
        + parking_payments_count
        + advisories_count
    )

    context = {

        "district": district,

        # Roads
        "roads_count": roads_count,
        "operational_roads_count": operational_roads_count,
        "good_roads_count": good_roads_count,
        "poor_roads_count": poor_roads_count,
        "critical_roads_count": critical_roads_count,
        "total_road_length": total_road_length,

        # Road reports
        "road_reports_count": road_reports_count,
        "road_reports_pending": road_reports_pending,
        "road_reports_resolved": road_reports_resolved,

        # Projects
        "projects_count": projects_count,
        "ongoing_projects_count": ongoing_projects_count,
        "completed_projects_count": completed_projects_count,
        "planned_projects_count": planned_projects_count,
        "project_average_completion": round(
            project_average_completion,
            1
        ),

        # Facilities
        "facilities_count": facilities_count,
        "operational_facilities_count": (
            operational_facilities_count
        ),

        # Traffic
        "traffic_incidents_count": traffic_incidents_count,
        "traffic_incidents_resolved": (
            traffic_incidents_resolved
        ),
        "traffic_incidents_pending": (
            traffic_incidents_pending
        ),

        # Parking
        "parking_facilities_count": (
            parking_facilities_count
        ),
        "operational_parking_count": (
            operational_parking_count
        ),
        "parking_payments_count": (
            parking_payments_count
        ),
        "parking_paid_count": parking_paid_count,
        "parking_pending_count": parking_pending_count,
        "parking_revenue": parking_revenue,

        # Advisories
        "advisories_count": advisories_count,
        "urgent_advisories_count": (
            urgent_advisories_count
        ),
        "high_advisories_count": (
            high_advisories_count
        ),

        # Overall
        "total_records": total_records,
    }

    return render(
        request,
        "public_works/public_works_statistics.html",
        context
    )