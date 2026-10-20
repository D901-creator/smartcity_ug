
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from accounts.models import AccountProfile


@login_required
def home(request):
    # Greeting based on the configured local time.
    current_hour = timezone.localtime().hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Retrieve the profile of the logged-in user.
    profile = AccountProfile.objects.filter(
        user=request.user
    ).select_related("district", "city").first()

    # Use the real profile details when available.
    if profile:
        citizen_name = (
            profile.full_name
            or request.user.get_full_name()
            or request.user.get_username()
        )

        district_name = profile.district.name if profile.district else None
        city_name = profile.city.name if profile.city else None

        if city_name:
            location_name = city_name
            location_type = "City"
        elif district_name:
            location_name = district_name
            location_type = "District"
        else:
            location_name = None
            location_type = None

    else:
        citizen_name = (
            request.user.get_full_name()
            or request.user.get_username()
        )
        location_name = None
        location_type = None

    context = {
        "greeting": greeting,

        "citizen": {
            "name": citizen_name,
            "district": district_name if profile else None,
            "city": city_name if profile else None,
            "location_name": location_name,
            "location_type": location_type,
        },

        "stats": {
            "total_requests": 12,
            "pending_requests": 5,
            "completed_requests": 7,
            "notifications": 3,
        },

        "recent_requests": [
            {
                "reference": "SCU-2026-00125",
                "service": "Water & Sanitation",
                "description": "Reported a water supply problem",
                "status": "Pending",
                "date": "01 Oct 2026",
            },
            {
                "reference": "SCU-2026-00118",
                "service": "Public Works & Transport",
                "description": "Reported a damaged road",
                "status": "In Progress",
                "date": "29 Sep 2026",
            },
            {
                "reference": "SCU-2026-00097",
                "service": "Health Services",
                "description": "Requested information about a health facility",
                "status": "Completed",
                "date": "25 Sep 2026",
            },
        ],

        "services": [
            {
                "name": "Health Services",
                "icon": "bi-heart-pulse",
                "description": "Access health services and submit health-related requests.",
                "color": "service-red",
            },
            {
                "name": "Education",
                "icon": "bi-mortarboard",
                "description": "Access education services and information.",
                "color": "service-blue",
            },
            {
                "name": "Agriculture",
                "icon": "bi-tree",
                "description": "Access agricultural services and support.",
                "color": "service-green",
            },
            {
                "name": "Water & Sanitation",
                "icon": "bi-droplet",
                "description": "Report water and sanitation problems.",
                "color": "service-cyan",
            },
            {
                "name": "Public Works & Transport",
                "icon": "bi-cone-striped",
                "description": "Report roads, drainage and transport issues.",
                "color": "service-orange",
            },
            {
                "name": "Electricity & Energy",
                "icon": "bi-lightning-charge",
                "description": "Access electricity and energy-related services.",
                "color": "service-yellow",
            },
            {
                "name": "Environment",
                "icon": "bi-flower1",
                "description": "Report environmental concerns and access services.",
                "color": "service-teal",
            },
            {
                "name": "Security",
                "icon": "bi-shield-check",
                "description": "Report security and community safety concerns.",
                "color": "service-purple",
            },
            {
                "name": "Urban Planning",
                "icon": "bi-buildings",
                "description": "Access planning, construction and development services.",
                "color": "service-indigo",
            },
            {
                "name": "Business & Trade",
                "icon": "bi-shop",
                "description": "Access business and trade-related services.",
                "color": "service-pink",
            },
            {
                "name": "Permits & IDs",
                "icon": "bi-person-vcard",
                "description": "Access permits, identification and registration services.",
                "color": "service-dark",
            },
            {
                "name": "Revenue & Taxes",
                "icon": "bi-cash-coin",
                "description": "Access revenue, fees and tax-related services.",
                "color": "service-gold",
            },
            {
                "name": "ICT Services",
                "icon": "bi-cpu",
                "description": "Access digital government and ICT services.",
                "color": "service-slate",
            },
            {
                "name": "Community Development",
                "icon": "bi-people",
                "description": "Access community development programmes and services.",
                "color": "service-community",
            },
        ],

        "announcements": [
            {
                "title": "Smart City Uganda Digital Services",
                "message": "Citizens can use the platform to submit and track government service requests.",
                "date": "01 Oct 2026",
            },
            {
                "title": "Public Service Reporting",
                "message": "Use the appropriate service department when submitting a new report.",
                "date": "30 Sep 2026",
            },
        ],
    }

    return render(
        request,
        "dashboard/citizen_dashboard.html",
        context,
    )



def public_home(request):
    """Public landing page for Smart City Uganda."""
    return render(request, "public_home.html")