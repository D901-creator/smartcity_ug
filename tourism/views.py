from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .models import (TourismDestination, TourismService,
    CulturalHeritageSite,TourismEvent,
    WildlifeConservationInformation,
    TourismProjectOpportunity,)

def home(request):
    services = [
        {
            "name": "Tourism Destinations & Attractions",
            "icon": "bi-geo-alt",
            "description": (
                "Explore tourist destinations, attractions, national parks, "
                "wildlife areas and tourism guides across Uganda."
            ),
            "url": "tourism:destinations",
            "color": "primary",
        },
        {
            "name": "Tourism Services & Cultural Heritage",
            "icon": "bi-building",
            "description": (
                "Access accommodation and tourism services together with "
                "information about Uganda's cultural heritage and sites."
            ),
            "url": "tourism:tourism_services",
            "color": "success",
        },
        {
            "name": "Events, Conservation & Opportunities",
            "icon": "bi-calendar-event",
            "description": (
                "Discover tourism events, wildlife conservation information, "
                "tourism projects and development opportunities."
            ),
           "url": "tourism:events_conservation_opportunities",
            "color": "warning",
        },
        {
            "name": "Tourism & Wildlife Statistics",
            "icon": "bi-bar-chart-line",
            "description": (
                "View tourism and wildlife statistics, reports, charts and "
                "other information published through Smart City Uganda."
            ),
            "url": "tourism:statistics",
            "color": "info",
        },
    ]

    context = {
        "services": services,
    }

    return render(
        request,
        "tourism/home.html",
        context
    )
    
def destinations(request):

    search = request.GET.get("search", "").strip()
    destination_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    destination_list = TourismDestination.objects.filter(
        is_published=True
    )

    if search:
        destination_list = destination_list.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(location__icontains=search)
            | Q(district__icontains=search)
            | Q(attractions__icontains=search)
            | Q(activities__icontains=search)
        )

    if destination_type:
        destination_list = destination_list.filter(
            destination_type=destination_type
        )

    if district:
        destination_list = destination_list.filter(
            district__iexact=district
        )

    districts = (
        TourismDestination.objects
        .filter(is_published=True)
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "destinations": destination_list,
        "destination_types": TourismDestination.DESTINATION_TYPES,
        "districts": districts,
        "search": search,
        "selected_type": destination_type,
        "selected_district": district,
    }

    return render(
        request,
        "tourism/destinations.html",
        context
    )


def destination_detail(request, destination_id):

    destination = get_object_or_404(
        TourismDestination,
        id=destination_id,
        is_published=True
    )

    return render(
        request,
        "tourism/destination_detail.html",
        {
            "destination": destination
        }
    )
    
def tourism_services(request):

    search = request.GET.get("search", "").strip()
    service_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    services = TourismService.objects.filter(
        is_published=True
    )

    if search:
        services = services.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(location__icontains=search)
            | Q(district__icontains=search)
            | Q(services_offered__icontains=search)
        )

    if service_type:
        services = services.filter(
            service_type=service_type
        )

    if district:
        services = services.filter(
            district__iexact=district
        )

    districts = (
        TourismService.objects
        .filter(is_published=True)
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "services": services,
        "service_types": TourismService.SERVICE_TYPES,
        "districts": districts,
        "search": search,
        "selected_type": service_type,
        "selected_district": district,
    }

    return render(
        request,
        "tourism/services.html",
        context
    )
def tourism_service_detail(request, service_id):

    service = get_object_or_404(
        TourismService,
        id=service_id,
        is_published=True
    )

    return render(
        request,
        "tourism/service_detail.html",
        {
            "service": service
        }
    )
    
def cultural_heritage(request):

    search = request.GET.get("search", "").strip()
    site_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    sites = CulturalHeritageSite.objects.filter(
        is_published=True
    )

    if search:
        sites = sites.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(location__icontains=search)
            | Q(district__icontains=search)
            | Q(historical_information__icontains=search)
            | Q(cultural_significance__icontains=search)
        )

    if site_type:
        sites = sites.filter(
            site_type=site_type
        )

    if district:
        sites = sites.filter(
            district__iexact=district
        )

    districts = (
        CulturalHeritageSite.objects
        .filter(is_published=True)
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "sites": sites,
        "site_types": CulturalHeritageSite.SITE_TYPES,
        "districts": districts,
        "search": search,
        "selected_type": site_type,
        "selected_district": district,
    }

    return render(
        request,
        "tourism/cultural_heritage.html",
        context
    )
    
def cultural_heritage_detail(request, site_id):

    site = get_object_or_404(
        CulturalHeritageSite,
        id=site_id,
        is_published=True
    )

    return render(
        request,
        "tourism/cultural_heritage_detail.html",
        {
            "site": site
        }
    )
    
def tourism_events(request):

    search = request.GET.get("search", "").strip()
    event_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    events = TourismEvent.objects.filter(
        is_published=True
    )

    if search:
        events = events.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(location__icontains=search)
            | Q(district__icontains=search)
            | Q(organizer__icontains=search)
        )

    if event_type:
        events = events.filter(
            event_type=event_type
        )

    if district:
        events = events.filter(
            district__iexact=district
        )

    districts = (
        TourismEvent.objects
        .filter(is_published=True)
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "events": events,
        "event_types": TourismEvent.EVENT_TYPES,
        "districts": districts,
        "search": search,
        "selected_type": event_type,
        "selected_district": district,
    }

    return render(
        request,
        "tourism/events.html",
        context
    )
    
def tourism_event_detail(request, event_id):

    event = get_object_or_404(
        TourismEvent,
        id=event_id,
        is_published=True
    )

    return render(
        request,
        "tourism/event_detail.html",
        {
            "event": event
        }
    )
    
def wildlife_conservation(request):

    search = request.GET.get("search", "").strip()
    conservation_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    information = WildlifeConservationInformation.objects.filter(
        is_published=True
    )

    if search:
        information = information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(wildlife_information__icontains=search)
            | Q(conservation_actions__icontains=search)
            | Q(district__icontains=search)
        )

    if conservation_type:
        information = information.filter(
            conservation_type=conservation_type
        )

    if district:
        information = information.filter(
            district__iexact=district
        )

    districts = (
        WildlifeConservationInformation.objects
        .filter(is_published=True)
        .exclude(district="")
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "information": information,
        "conservation_types": (
            WildlifeConservationInformation.CONSERVATION_TYPES
        ),
        "districts": districts,
        "search": search,
        "selected_type": conservation_type,
        "selected_district": district,
    }

    return render(
        request,
        "tourism/wildlife_conservation.html",
        context
    )
    
def wildlife_conservation_detail(request, information_id):

    information = get_object_or_404(
        WildlifeConservationInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "tourism/wildlife_conservation_detail.html",
        {
            "information": information
        }
    )
def tourism_opportunities(request):

    search = request.GET.get("search", "").strip()
    opportunity_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()
    status = request.GET.get("status", "").strip()

    opportunities = TourismProjectOpportunity.objects.filter(
        is_published=True
    )

    if search:
        opportunities = opportunities.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(objectives__icontains=search)
            | Q(benefits__icontains=search)
            | Q(district__icontains=search)
        )

    if opportunity_type:
        opportunities = opportunities.filter(
            opportunity_type=opportunity_type
        )

    if district:
        opportunities = opportunities.filter(
            district__iexact=district
        )

    if status:
        opportunities = opportunities.filter(
            status=status
        )

    districts = (
        TourismProjectOpportunity.objects
        .filter(is_published=True)
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "opportunities": opportunities,
        "opportunity_types": (
            TourismProjectOpportunity.OPPORTUNITY_TYPES
        ),
        "statuses": TourismProjectOpportunity.STATUS_CHOICES,
        "districts": districts,
        "search": search,
        "selected_type": opportunity_type,
        "selected_status": status,
        "selected_district": district,
    }

    return render(
        request,
        "tourism/opportunities.html",
        context
    )
    
def tourism_opportunity_detail(request, opportunity_id):

    opportunity = get_object_or_404(
        TourismProjectOpportunity,
        id=opportunity_id,
        is_published=True
    )

    return render(
        request,
        "tourism/opportunity_detail.html",
        {
            "opportunity": opportunity
        }
    )
def events_conservation_opportunities(request):

    return render(
        request,
        "tourism/events_conservation_opportunities.html"
    )
    
def tourism_statistics(request):
    # Main tourism figures
    total_destinations = TourismDestination.objects.filter(
        is_published=True
    ).count()

    total_events = TourismEvent.objects.filter(
        is_published=True
    ).count()

    total_conservation = WildlifeConservationInformation.objects.filter(
        is_published=True
    ).count()

    total_opportunities = TourismProjectOpportunity.objects.filter(
        is_published=True
    ).count()

    # Upcoming events
    from django.utils import timezone

    today = timezone.now().date()

    upcoming_events = TourismEvent.objects.filter(
        is_published=True,
        start_date__gte=today
    ).count()

    # Event statistics
    events_by_type = list(
        TourismEvent.objects.filter(
            is_published=True
        )
        .values("event_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # Conservation statistics
    conservation_by_type = list(
        WildlifeConservationInformation.objects.filter(
            is_published=True
        )
        .values("conservation_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # Opportunity statistics
    opportunities_by_status = list(
        TourismProjectOpportunity.objects.filter(
            is_published=True
        )
        .values("status")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    opportunities_by_type = list(
        TourismProjectOpportunity.objects.filter(
            is_published=True
        )
        .values("opportunity_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # Tourism destinations by district
    destinations_by_district = list(
        TourismDestination.objects.filter(
            is_published=True
        )
        .values("district")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    context = {
        "total_destinations": total_destinations,
        "total_events": total_events,
        "total_conservation": total_conservation,
        "total_opportunities": total_opportunities,
        "upcoming_events": upcoming_events,

        "events_by_type": events_by_type,
        "conservation_by_type": conservation_by_type,
        "opportunities_by_status": opportunities_by_status,
        "opportunities_by_type": opportunities_by_type,
        "destinations_by_district": destinations_by_district,
    }

    return render(
        request,
        "tourism/statistics.html",
        context
    )