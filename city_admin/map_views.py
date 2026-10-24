
import json

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required

from city_admin.access import is_city_admin
from locations.models import District
from reports.models import CitizenReport
from requests.models import CitizenRequest as ServiceRequest
from officer.models import CitizenRequest as OfficerRequest


@login_required
@require_GET
def district_issue_map(request):
    if not is_city_admin(request.user):
        raise PermissionDenied(
            "You are not authorized to access district maps."
        )

    districts = District.objects.select_related(
        "region"
    ).order_by("region__name", "name")

    district_id = request.GET.get("district")
    selected_district = None
    markers = []
    district_markers = []
    unlocated_count = 0

    # Show all districts that have saved coordinates.
    for district in districts:
        if (
            district.latitude is not None
            and district.longitude is not None
        ):
            district_markers.append({
                "name": district.name,
                "region": (
                    district.region.name if district.region else ""
                ),
                "latitude": float(district.latitude),
                "longitude": float(district.longitude),
                "url": f"?district={district.pk}",
            })

    # Load individual issues only when a district is selected.
    if district_id:
        selected_district = get_object_or_404(
            District,
            pk=district_id,
        )

        reports = CitizenReport.objects.filter(
            district_ref=selected_district
        )

        for item in reports:
            if item.latitude is not None and item.longitude is not None:
                markers.append({
                    "type": "Citizen report",
                    "reference": str(item.report_number),
                    "title": item.title,
                    "status": item.get_status_display(),
                    "department": str(item.department),
                    "location": item.location or "",
                    "latitude": float(item.latitude),
                    "longitude": float(item.longitude),
                    "date": item.created_at.strftime("%d %b %Y"),
                })
            else:
                unlocated_count += 1

        service_requests = ServiceRequest.objects.filter(
            district_ref=selected_district
        )

        for item in service_requests:
            if item.latitude is not None and item.longitude is not None:
                markers.append({
                    "type": "Service request",
                    "reference": str(item.request_number),
                    "title": item.title,
                    "status": item.get_status_display(),
                    "department": str(item.department),
                    "location": item.location or "",
                    "latitude": float(item.latitude),
                    "longitude": float(item.longitude),
                    "date": item.created_at.strftime("%d %b %Y"),
                })
            else:
                unlocated_count += 1

        officer_requests = OfficerRequest.objects.filter(
            district_ref=selected_district
        )

        for item in officer_requests:
            if item.latitude is not None and item.longitude is not None:
                markers.append({
                    "type": "Officer workflow request",
                    "reference": str(item.reference),
                    "title": item.subject,
                    "status": item.get_status_display(),
                    "department": str(item.department),
                    "location": item.district or item.city or "",
                    "latitude": float(item.latitude),
                    "longitude": float(item.longitude),
                    "date": item.created_at.strftime("%d %b %Y"),
                })
            else:
                unlocated_count += 1

    center = {
        "latitude": 1.3733,
        "longitude": 32.2903,
    }

    if (
        selected_district
        and selected_district.latitude is not None
        and selected_district.longitude is not None
    ):
        center = {
            "latitude": float(selected_district.latitude),
            "longitude": float(selected_district.longitude),
        }

    return render(
        request,
        "city_admin/district_issue_map.html",
        {
            "districts": districts,
            "selected_district": selected_district,
            "district_markers_json": json.dumps(district_markers),
            "markers_json": json.dumps(markers),
            "center_json": json.dumps(center),
            "located_count": len(markers),
            "district_count": len(district_markers),
            "unlocated_count": unlocated_count,
        },
    )
