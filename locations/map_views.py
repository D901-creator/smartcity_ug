
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseForbidden
from django.shortcuts import render
import json

from accounts.models import AccountProfile
from reports.models import CitizenReport
from requests.models import CitizenRequest as ServiceRequest
from officer.models import CitizenRequest as OfficerRequest
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import District

@login_required
def issue_map(request):
    profile = (
        AccountProfile.objects
        .select_related("district", "district__region")
        .filter(user=request.user)
        .first()
    )

    if profile is None:
        return HttpResponseForbidden(
            "Your account does not have a registered location profile."
        )

    allowed_roles = {
        AccountProfile.Role.CITIZEN,
        AccountProfile.Role.OFFICER,
        AccountProfile.Role.DEPARTMENT_HEAD,
    }

    if profile.role not in allowed_roles:
        return HttpResponseForbidden("You cannot access this map.")

    district = profile.district

    issues = []

    report_qs = CitizenReport.objects.filter(
        district_ref=district
    ).order_by("-created_at")

    service_qs = ServiceRequest.objects.filter(
        district_ref=district
    ).order_by("-created_at")

    officer_qs = OfficerRequest.objects.filter(
        district_ref=district
    ).order_by("-created_at")

    unmapped_count = 0

    def add_issues(queryset, kind, title_field, number_field):
        nonlocal unmapped_count

        for item in queryset:
            lat = item.latitude
            lon = item.longitude

            if lat is None or lon is None:
                unmapped_count += 1
                continue

            issues.append({
                "title": getattr(item, title_field),
                "reference": str(getattr(item, number_field)),
                "kind": kind,
                "status": item.get_status_display(),
                "latitude": float(lat),
                "longitude": float(lon),
            })

    add_issues(
        report_qs, "Report", "title", "report_number"
    )
    add_issues(
        service_qs, "Service request", "title", "request_number"
    )
    add_issues(
        officer_qs, "Officer request", "subject", "reference"
    )

    center = {
        "latitude": (
            float(district.latitude)
            if district.latitude is not None
            else 1.3733
        ),
        "longitude": (
            float(district.longitude)
            if district.longitude is not None
            else 32.2903
        ),
    }

    return render(
        request,
        "locations/issue_map.html",
        {
            "profile": profile,
            "district": district,
            "center": center,
            "issues_json": json.dumps(
                issues, cls=DjangoJSONEncoder
            ),
            "mapped_count": len(issues),
            "unmapped_count": unmapped_count,
        },
    )

@staff_member_required
def admin_generate_district_map(request):
    districts = District.objects.select_related("region").order_by(
        "region__name", "name"
    )

    district_id = request.POST.get("district_id") or request.GET.get("district_id")
    selected_district = None

    if district_id:
        selected_district = District.objects.filter(
            pk=district_id
        ).select_related("region").first()

    if request.method == "POST":
        if not selected_district:
            messages.error(request, "Please select a valid district.")
        else:
            latitude = request.POST.get("latitude", "").strip()
            longitude = request.POST.get("longitude", "").strip()

            try:
                lat = float(latitude)
                lon = float(longitude)

                if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    raise ValueError

                selected_district.latitude = lat
                selected_district.longitude = lon
                selected_district.save(
                    update_fields=["latitude", "longitude"]
                )

                messages.success(
                    request,
                    f"Map coordinates saved for {selected_district.name}."
                )

                return redirect(
                    f"{reverse('locations:admin_district_map')}"
                    f"?district_id={selected_district.pk}"
                )

            except (TypeError, ValueError):
                messages.error(
                    request,
                    "Enter valid latitude and longitude values."
                )

    return render(
        request,
        "locations/admin_district_map.html",
        {
            "districts": districts,
            "selected_district": selected_district,
        },
    )
