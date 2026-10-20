from django.shortcuts import render
from django.db.models import Q

from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from .models import (
    ICTService,
    ICTInfrastructure,
    ICTInnovation,
    ICTOpportunity,
      NationalGuidanceInformation,
    CivicProgramme,
)


def home(request):
    context = {
        "page_title": "ICT Services",
        "page_description": (
            "Access ICT, digital government, connectivity, "
            "innovation and technology information through "
            "Smart City Uganda."
        ),
    }

    return render(
        request,
        "ict/home.html",
        context
    )
    
def services(request):

    queryset = ICTService.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    service_type = request.GET.get("service_type", "").strip()
    district = request.GET.get("district", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search)
        )

    if service_type:
        queryset = queryset.filter(
            service_type=service_type
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    context = {
        "services": queryset,
        "service_types": ICTService.SERVICE_TYPES,
        "search": search,
        "selected_type": service_type,
        "selected_district": district,
    }

    return render(
        request,
        "ict/services.html",
        context
    )


def service_detail(request, service_id):

    service = get_object_or_404(
        ICTService,
        id=service_id,
        is_published=True
    )

    return render(
        request,
        "ict/service_detail.html",
        {
            "service": service
        }
    )
    
    
def infrastructure(request):

    queryset = ICTInfrastructure.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    infrastructure_type = request.GET.get(
        "infrastructure_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search)
        )

    if infrastructure_type:
        queryset = queryset.filter(
            infrastructure_type=infrastructure_type
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/infrastructure.html",
        {
            "infrastructure": queryset,
            "infrastructure_types": (
                ICTInfrastructure.INFRASTRUCTURE_TYPES
            ),
            "search": search,
            "selected_type": infrastructure_type,
            "selected_district": district,
        }
    )


def infrastructure_detail(request, infrastructure_id):

    item = get_object_or_404(
        ICTInfrastructure,
        id=infrastructure_id,
        is_published=True
    )

    return render(
        request,
        "ict/infrastructure_detail.html",
        {
            "item": item
        }
    )


def innovations(request):

    queryset = ICTInnovation.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    innovation_type = request.GET.get(
        "innovation_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search)
        )

    if innovation_type:
        queryset = queryset.filter(
            innovation_type=innovation_type
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/innovations.html",
        {
            "innovations": queryset,
            "innovation_types": (
                ICTInnovation.INNOVATION_TYPES
            ),
            "search": search,
            "selected_type": innovation_type,
            "selected_district": district,
        }
    )


def innovation_detail(request, innovation_id):

    innovation = get_object_or_404(
        ICTInnovation,
        id=innovation_id,
        is_published=True
    )

    return render(
        request,
        "ict/innovation_detail.html",
        {
            "innovation": innovation
        }
    )


def opportunities(request):

    queryset = ICTOpportunity.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    opportunity_type = request.GET.get(
        "opportunity_type",
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

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search)
        )

    if opportunity_type:
        queryset = queryset.filter(
            opportunity_type=opportunity_type
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/opportunities.html",
        {
            "opportunities": queryset,
            "opportunity_types": (
                ICTOpportunity.OPPORTUNITY_TYPES
            ),
            "statuses": (
                ICTOpportunity.STATUS_CHOICES
            ),
            "search": search,
            "selected_type": opportunity_type,
            "selected_status": status,
            "selected_district": district,
        }
    )


def opportunity_detail(request, opportunity_id):

    opportunity = get_object_or_404(
        ICTOpportunity,
        id=opportunity_id,
        is_published=True
    )

    return render(
        request,
        "ict/opportunity_detail.html",
        {
            "opportunity": opportunity
        }
    )


def infrastructure_innovation_opportunities(request):

    return render(
        request,
        "ict/infrastructure_innovation_opportunities.html"
    )
    
def national_guidance(request):
    queryset = NationalGuidanceInformation.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    information_type = request.GET.get(
        "information_type", ""
    ).strip()
    district = request.GET.get(
        "district", ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search) |
            Q(key_points__icontains=search)
        )

    if information_type:
        queryset = queryset.filter(
            information_type=information_type
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    context = {
        "information": queryset,
        "information_types": (
            NationalGuidanceInformation.INFORMATION_TYPES
        ),
        "search": search,
        "selected_type": information_type,
        "selected_district": district,
    }

    return render(
        request,
        "ict/national_guidance.html",
        context
    )


def national_guidance_detail(request, information_id):

    information = get_object_or_404(
        NationalGuidanceInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "ict/national_guidance_detail.html",
        {
            "information": information
        }
    )


def civic_programmes(request):

    queryset = CivicProgramme.objects.filter(
        is_published=True
    )

    search = request.GET.get(
        "search", ""
    ).strip()

    programme_type = request.GET.get(
        "programme_type", ""
    ).strip()

    status = request.GET.get(
        "status", ""
    ).strip()

    district = request.GET.get(
        "district", ""
    ).strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search)
        )

    if programme_type:
        queryset = queryset.filter(
            programme_type=programme_type
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    context = {
        "programmes": queryset,
        "programme_types": (
            CivicProgramme.PROGRAMME_TYPES
        ),
        "statuses": (
            CivicProgramme.STATUS_CHOICES
        ),
        "search": search,
        "selected_type": programme_type,
        "selected_status": status,
        "selected_district": district,
    }

    return render(
        request,
        "ict/civic_programmes.html",
        context
    )


def civic_programme_detail(
    request,
    programme_id
):

    programme = get_object_or_404(
        CivicProgramme,
        id=programme_id,
        is_published=True
    )

    return render(
        request,
        "ict/civic_programme_detail.html",
        {
            "programme": programme
        }
    )


def national_guidance_civic_information(request):

    return render(
        request,
        "ict/national_guidance_civic_information.html"
    )
    
def statistics(request):
    # ICT SERVICES
    total_services = ICTService.objects.filter(
        is_published=True
    ).count()

    services_by_type = (
        ICTService.objects
        .filter(is_published=True)
        .values("service_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    services_by_district = (
        ICTService.objects
        .filter(is_published=True)
        .exclude(district="")
        .values("district")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # ICT INFRASTRUCTURE
    total_infrastructure = ICTInfrastructure.objects.filter(
        is_published=True
    ).count()

    infrastructure_by_type = (
        ICTInfrastructure.objects
        .filter(is_published=True)
        .values("infrastructure_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    infrastructure_by_district = (
        ICTInfrastructure.objects
        .filter(is_published=True)
        .exclude(district="")
        .values("district")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # ICT INNOVATION
    total_innovations = ICTInnovation.objects.filter(
        is_published=True
    ).count()

    innovations_by_type = (
        ICTInnovation.objects
        .filter(is_published=True)
        .values("innovation_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    innovations_by_district = (
        ICTInnovation.objects
        .filter(is_published=True)
        .exclude(district="")
        .values("district")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # ICT OPPORTUNITIES
    total_opportunities = ICTOpportunity.objects.filter(
        is_published=True
    ).count()

    opportunities_by_type = (
        ICTOpportunity.objects
        .filter(is_published=True)
        .values("opportunity_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    opportunities_by_status = (
        ICTOpportunity.objects
        .filter(is_published=True)
        .values("status")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # NATIONAL GUIDANCE
    total_guidance = NationalGuidanceInformation.objects.filter(
        is_published=True
    ).count()

    guidance_by_type = (
        NationalGuidanceInformation.objects
        .filter(is_published=True)
        .values("information_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    guidance_by_district = (
        NationalGuidanceInformation.objects
        .filter(is_published=True)
        .exclude(district="")
        .values("district")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # CIVIC PROGRAMMES
    total_programmes = CivicProgramme.objects.filter(
        is_published=True
    ).count()

    programmes_by_type = (
        CivicProgramme.objects
        .filter(is_published=True)
        .values("programme_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    programmes_by_status = (
        CivicProgramme.objects
        .filter(is_published=True)
        .values("status")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    context = {
        "total_services": total_services,
        "services_by_type": services_by_type,
        "services_by_district": services_by_district,

        "total_infrastructure": total_infrastructure,
        "infrastructure_by_type": infrastructure_by_type,
        "infrastructure_by_district": infrastructure_by_district,

        "total_innovations": total_innovations,
        "innovations_by_type": innovations_by_type,
        "innovations_by_district": innovations_by_district,

        "total_opportunities": total_opportunities,
        "opportunities_by_type": opportunities_by_type,
        "opportunities_by_status": opportunities_by_status,

        "total_guidance": total_guidance,
        "guidance_by_type": guidance_by_type,
        "guidance_by_district": guidance_by_district,

        "total_programmes": total_programmes,
        "programmes_by_type": programmes_by_type,
        "programmes_by_status": programmes_by_status,
    }

    return render(
        request,
        "ict/statistics.html",
        context
    )
    
def connectivity(request):
    """
    Citizen-facing connectivity and internet infrastructure page.
    Uses the existing ICTInfrastructure model.
    """
    queryset = ICTInfrastructure.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    infrastructure_type = request.GET.get(
        "infrastructure_type", ""
    ).strip()
    district = request.GET.get("district", "").strip()

    # Connectivity-focused infrastructure
    queryset = queryset.filter(
        infrastructure_type__in=[
            "internet",
            "telecommunication",
            "network",
            "digital_access",
        ]
    )

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search) |
            Q(services_available__icontains=search) |
            Q(coverage_information__icontains=search)
        )

    if infrastructure_type:
        queryset = queryset.filter(
            infrastructure_type=infrastructure_type
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/connectivity.html",
        {
            "connectivity": queryset,
            "infrastructure_types": [
                item for item in ICTInfrastructure.INFRASTRUCTURE_TYPES
                if item[0] in [
                    "internet",
                    "telecommunication",
                    "network",
                    "digital_access",
                ]
            ],
            "search": search,
            "selected_type": infrastructure_type,
            "selected_district": district,
        }
    )


def digital_literacy(request):
    """
    Citizen-facing digital literacy and digital skills information.
    Uses the existing ICTService model.
    """
    queryset = ICTService.objects.filter(
        is_published=True,
        service_type="digital_literacy"
    )

    search = request.GET.get("search", "").strip()
    district = request.GET.get("district", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search) |
            Q(eligibility__icontains=search) |
            Q(requirements__icontains=search)
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/digital_literacy.html",
        {
            "services": queryset,
            "search": search,
            "selected_district": district,
        }
    )


def ict_support(request):
    """
    Citizen-facing ICT support information.
    Uses the existing ICTService model.
    """
    queryset = ICTService.objects.filter(
        is_published=True,
        service_type="ict_support"
    )

    search = request.GET.get("search", "").strip()
    district = request.GET.get("district", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search) |
            Q(contact_information__icontains=search)
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/ict_support.html",
        {
            "services": queryset,
            "search": search,
            "selected_district": district,
        }
    )


def ict_opportunities(request):
    """
    Citizen-facing ICT opportunities.
    Uses the existing ICTOpportunity model.
    """
    queryset = ICTOpportunity.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    opportunity_type = request.GET.get(
        "opportunity_type", ""
    ).strip()
    status = request.GET.get("status", "").strip()
    district = request.GET.get("district", "").strip()

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(description__icontains=search) |
            Q(objectives__icontains=search) |
            Q(benefits__icontains=search)
        )

    if opportunity_type:
        queryset = queryset.filter(
            opportunity_type=opportunity_type
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if district:
        queryset = queryset.filter(
            district__iexact=district
        )

    return render(
        request,
        "ict/ict_opportunities.html",
        {
            "opportunities": queryset,
            "opportunity_types": ICTOpportunity.OPPORTUNITY_TYPES,
            "statuses": ICTOpportunity.STATUS_CHOICES,
            "search": search,
            "selected_type": opportunity_type,
            "selected_status": status,
            "selected_district": district,
        }
    )