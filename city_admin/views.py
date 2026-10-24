import json
from functools import wraps
from decimal import Decimal, InvalidOperation

from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q, Count
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST, require_http_methods

from accounts.models import AccountProfile, VerificationSubmission
from audit.models import AuditLog
from departments.models import Ministry, Department, Sector, Service
from locations.models import District
from officer.models import CitizenRequest as OfficerRequest
from requests.models import CitizenRequest as ServiceRequest
from services.models import (
    GovernmentService,
    ServiceRequest as GovernmentServiceRequest,
)

from city_admin.access import is_city_admin

from .forms import (
    VerificationReviewForm,
    MinistryForm,
    DepartmentForm,
    SectorForm,
    DepartmentServiceForm,
    AdminUserEditForm,
    SystemSettingsForm,
)
from .models import SystemSettings


User = get_user_model()


# ============================================================
# SHARED CITY ADMIN ACCESS CONTROL
# ============================================================

def city_admin_required(view_func):
    """
    Require an authenticated user who passes the shared City Admin policy.

    All City Admin views should use this decorator so that access rules
    remain consistent across the portal.
    """
    @wraps(view_func)
    @login_required(login_url="accounts:login")
    def wrapped_view(request, *args, **kwargs):
        if not is_city_admin(request.user):
            raise PermissionDenied(
                "You are not authorized to access the City Admin portal."
            )

        return view_func(request, *args, **kwargs)

    return wrapped_view


def _require_city_admin(user):
    """Protect sensitive operations with the shared authorization policy."""
    if not is_city_admin(user):
        raise PermissionDenied(
            "Only authorized administrators can perform this operation."
        )


# ============================================================
# CITY ADMIN DASHBOARD
# ============================================================

@city_admin_required
def city_admin_dashboard(request):
    """Display live statistics for the Smart City Uganda admin portal."""

    total_citizens = AccountProfile.objects.filter(
        role="citizen"
    ).count()

    total_officers = AccountProfile.objects.filter(
        role="officer"
    ).count()

    total_department_heads = AccountProfile.objects.filter(
        role="department_head"
    ).count()

    pending_verifications = VerificationSubmission.objects.filter(
        status__iexact="pending"
    ).count()

    total_departments = Department.objects.count()

    officer_request_count = OfficerRequest.objects.count()
    service_request_count = ServiceRequest.objects.count()

    total_requests = officer_request_count + service_request_count

    recent_activity = AuditLog.objects.select_related(
        "user"
    ).order_by("-created_at")[:8]

    context = {
        "active_section": "dashboard",
        "total_citizens": total_citizens,
        "total_officers": total_officers,
        "total_department_heads": total_department_heads,
        "pending_verifications": pending_verifications,
        "total_departments": total_departments,
        "total_requests": total_requests,
        "officer_request_count": officer_request_count,
        "service_request_count": service_request_count,
        "recent_activity": recent_activity,
    }

    return render(request, "city_admin/dashboard.html", context)


# ============================================================
# CITY ADMIN USER MANAGEMENT
# ============================================================

@city_admin_required
def city_admin_users(request):
    """List and search existing Smart City Uganda account profiles."""

    profiles = AccountProfile.objects.select_related("user").all()

    search_query = request.GET.get("q", "").strip()
    selected_role = request.GET.get("role", "").strip()

    if search_query:
        profiles = profiles.filter(
            Q(full_name__icontains=search_query)
            | Q(user__username__icontains=search_query)
            | Q(user__email__icontains=search_query)
            | Q(phone_number__icontains=search_query)
        )

    valid_roles = {"citizen", "officer", "department_head"}

    if selected_role in valid_roles:
        profiles = profiles.filter(role=selected_role)

    paginator = Paginator(profiles.order_by("full_name"), 20)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "active_section": "users",
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_role": selected_role,
        "total_users": profiles.count(),
    }

    return render(request, "city_admin/users.html", context)


@city_admin_required
def city_admin_user_detail(request, profile_id):
    """Show an account profile and its verification submissions."""

    profile = get_object_or_404(
        AccountProfile.objects.select_related(
            "user",
            "department",
            "district",
            "city",
        ),
        pk=profile_id,
    )

    verification_submissions = VerificationSubmission.objects.filter(
        profile=profile
    ).order_by("-submitted_at")

    context = {
        "active_section": "users",
        "profile": profile,
        "verification_submissions": verification_submissions,
    }

    return render(request, "city_admin/user_detail.html", context)


@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_user_edit(request, profile_id):
    """Edit an account profile through the existing profile form."""

    profile = get_object_or_404(
        AccountProfile.objects.select_related("user"),
        pk=profile_id,
    )

    if request.method == "POST":
        form = AdminUserEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "User account updated successfully.")
            return redirect(
                "city_admin:user_detail",
                profile_id=profile.pk,
            )
    else:
        form = AdminUserEditForm(instance=profile)

    return render(
        request,
        "city_admin/user_edit.html",
        {
            "active_section": "users",
            "profile": profile,
            "form": form,
        },
    )


@city_admin_required
@require_POST
def city_admin_toggle_user_status(request, profile_id):
    """
    Keep suspension and reactivation disabled until the project has
    an implemented, audited account-status workflow.
    """

    profile = get_object_or_404(
        AccountProfile.objects.select_related("user"),
        pk=profile_id,
    )

    action = request.POST.get("action")

    if action == "suspend":
        messages.error(
            request,
            "Suspension is disabled until administrator authorization "
            "and audit logging are implemented.",
        )
    elif action == "reactivate":
        messages.error(
            request,
            "Reactivation is disabled until administrator authorization "
            "and audit logging are implemented.",
        )
    else:
        messages.error(request, "Invalid account action.")

    return redirect(
        "city_admin:user_detail",
        profile_id=profile.pk,
    )


# ============================================================
# VERIFICATION LIST AND REVIEW
# ============================================================

@city_admin_required
def city_admin_verifications(request):
    """List and filter existing verification submissions."""

    submissions = VerificationSubmission.objects.select_related(
        "profile",
        "profile__user",
    ).order_by("-submitted_at")

    search_query = request.GET.get("q", "").strip()
    selected_status = request.GET.get("status", "").strip().lower()

    if search_query:
        submissions = submissions.filter(
            Q(profile__full_name__icontains=search_query)
            | Q(profile__user__username__icontains=search_query)
            | Q(identification_number__icontains=search_query)
            | Q(id_number__icontains=search_query)
            | Q(staff_id__icontains=search_query)
        )

    valid_statuses = {"pending", "approved", "rejected"}

    if selected_status in valid_statuses:
        submissions = submissions.filter(
            status__iexact=selected_status
        )

    total_matching = submissions.count()
    page_obj = Paginator(submissions, 20).get_page(
        request.GET.get("page")
    )

    context = {
        "active_section": "verifications",
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_status": selected_status,
        "total_matching": total_matching,
    }

    return render(request, "city_admin/verifications.html", context)


@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_verification_review(request, submission_id):
    """
    Display an individual verification submission.

    This page intentionally does not approve or reject submissions.
    Use the verification-applications view for those decisions.
    """

    submission = get_object_or_404(
        VerificationSubmission.objects.select_related(
            "profile",
            "profile__user",
        ),
        pk=submission_id,
    )

    if request.method == "POST":
        form = VerificationReviewForm(request.POST)

        if form.is_valid():
            messages.error(
                request,
                "Use the verification applications page to process "
                "verification decisions.",
            )
            return redirect(
                "city_admin:verification_review",
                submission_id=submission.pk,
            )
    else:
        form = VerificationReviewForm()

    context = {
        "active_section": "verifications",
        "submission": submission,
        "form": form,
    }

    return render(
        request,
        "city_admin/verification_review.html",
        context,
    )


# ============================================================
# MINISTRIES, DEPARTMENTS, SECTORS AND SERVICES
# ============================================================

@city_admin_required
def city_admin_departments(request):
    ministries = Ministry.objects.all()
    departments = Department.objects.select_related("ministry").all()

    context = {
        "active_section": "departments",
        "ministries": ministries,
        "departments": departments,
        "ministry_count": ministries.count(),
        "department_count": departments.count(),
        "active_department_count": departments.filter(
            is_active=True
        ).count(),
    }

    return render(request, "city_admin/departments.html", context)


@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Department created successfully.")
            return redirect("city_admin:departments")
    else:
        form = DepartmentForm()

    return render(
        request,
        "city_admin/department_form.html",
        {
            "form": form,
            "active_section": "departments",
            "page_title": "Create Department",
        },
    )


@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_ministry_create(request):
    if request.method == "POST":
        form = MinistryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ministry created successfully.")
            return redirect("city_admin:departments")
    else:
        form = MinistryForm()

    return render(
        request,
        "city_admin/department_form.html",
        {
            "form": form,
            "active_section": "departments",
            "page_title": "Create Ministry",
        },
    )


@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_sector_create(request):
    if request.method == "POST":
        form = SectorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Sector created successfully.")
            return redirect("city_admin:departments")
    else:
        form = SectorForm()

    return render(
        request,
        "city_admin/department_form.html",
        {
            "form": form,
            "active_section": "departments",
            "page_title": "Create Sector",
        },
    )


@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_service_create(request):
    if request.method == "POST":
        form = DepartmentServiceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Department service created successfully.",
            )
            return redirect("city_admin:departments")
    else:
        form = DepartmentServiceForm()

    return render(
        request,
        "city_admin/department_form.html",
        {
            "form": form,
            "active_section": "departments",
            "page_title": "Create Department Service",
        },
    )


# ============================================================
# ANALYTICS
# ============================================================

@city_admin_required
def city_admin_analytics(request):
    """Show request and service statistics from existing models."""

    officer_requests = OfficerRequest.objects.all()
    citizen_service_requests = ServiceRequest.objects.all()
    government_service_requests = GovernmentServiceRequest.objects.all()

    officer_total = officer_requests.count()
    citizen_service_total = citizen_service_requests.count()
    government_service_total = government_service_requests.count()

    total_requests = (
        officer_total
        + citizen_service_total
        + government_service_total
    )

    officer_open = officer_requests.exclude(
        status__in=["resolved", "closed"]
    ).count()

    citizen_service_open = citizen_service_requests.exclude(
        status__in=["resolved", "closed"]
    ).count()

    government_service_open = government_service_requests.exclude(
        status__in=["completed", "rejected"]
    ).count()

    open_requests = (
        officer_open
        + citizen_service_open
        + government_service_open
    )

    completed_requests = (
        officer_requests.filter(
            status__in=["resolved", "closed"]
        ).count()
        + citizen_service_requests.filter(
            status__in=["resolved", "closed"]
        ).count()
        + government_service_requests.filter(
            status="completed"
        ).count()
    )

    def make_status_rows(queryset, choices):
        counts = queryset.values("status").annotate(
            total=Count("id")
        ).order_by("status")

        labels = dict(choices)

        rows = [
            {
                "label": labels.get(
                    item["status"],
                    item["status"].replace("_", " ").title(),
                ),
                "count": item["total"],
            }
            for item in counts
        ]

        maximum = max(
            (item["count"] for item in rows),
            default=0,
        )

        for item in rows:
            item["percent"] = (
                round(item["count"] * 100 / maximum)
                if maximum
                else 0
            )

        return rows

    officer_status_rows = make_status_rows(
        officer_requests,
        OfficerRequest.Status.choices,
    )

    citizen_service_status_rows = make_status_rows(
        citizen_service_requests,
        ServiceRequest.STATUS_CHOICES,
    )

    government_service_status_rows = make_status_rows(
        government_service_requests,
        GovernmentServiceRequest.STATUS_CHOICES,
    )

    category_counts = GovernmentService.objects.values(
        "category"
    ).annotate(
        total=Count("id")
    ).order_by("-total", "category")

    category_labels = dict(GovernmentService.CATEGORY_CHOICES)

    service_categories = [
        {
            "label": category_labels.get(
                item["category"],
                item["category"].replace("_", " ").title(),
            ),
            "count": item["total"],
        }
        for item in category_counts
    ]

    context = {
        "active_section": "analytics",
        "officer_total": officer_total,
        "citizen_service_total": citizen_service_total,
        "government_service_total": government_service_total,
        "total_requests": total_requests,
        "open_requests": open_requests,
        "completed_requests": completed_requests,
        "active_government_services": GovernmentService.objects.filter(
            is_active=True
        ).count(),
        "officer_status_rows": officer_status_rows,
        "citizen_service_status_rows": citizen_service_status_rows,
        "government_service_status_rows": government_service_status_rows,
        "service_categories": service_categories,
    }

    return render(request, "city_admin/analytics.html", context)


# ============================================================
# DISTRICT MAP MANAGEMENT
# ============================================================


# ============================================================
# DISTRICT MAP MANAGEMENT
# ============================================================

@city_admin_required
@require_http_methods(["GET", "POST"])
def district_map_generator(request):
    """Manage district coordinates and show the Uganda map."""

    districts = District.objects.select_related(
        "region"
    ).order_by("region__name", "name")

    district_id = (
        request.POST.get("district_id")
        or request.GET.get("district_id")
    )

    selected_district = None

    if district_id:
        selected_district = districts.filter(
            pk=district_id
        ).first()

    if request.method == "POST":
        if not selected_district:
            messages.error(request, "Please select a valid district.")
        else:
            try:
                latitude = Decimal(
                    request.POST.get("latitude", "").strip()
                )
                longitude = Decimal(
                    request.POST.get("longitude", "").strip()
                )

                # Approximate geographic limits of Uganda.
                # These are rectangular bounds, not the exact border.
                if (
                    not latitude.is_finite()
                    or not longitude.is_finite()
                    or not Decimal("-1.6") <= latitude <= Decimal("4.3")
                    or not Decimal("29.5") <= longitude <= Decimal("35.1")
                ):
                    raise InvalidOperation

                selected_district.latitude = latitude
                selected_district.longitude = longitude

                selected_district.save(
                    update_fields=["latitude", "longitude"]
                )

                messages.success(
                    request,
                    f"Coordinates saved for {selected_district.name}."
                )

                return redirect(
                    f"{reverse('city_admin:district_map')}"
                    f"?district_id={selected_district.pk}"
                )

            except (InvalidOperation, ValueError, TypeError):
                messages.error(
                    request,
                    "Coordinates must be within Uganda's approximate "
                    "latitude and longitude range. Select a point on "
                    "the Uganda map and try again."
                )

    # Only districts with saved coordinates receive overview markers.
    district_markers = []

    for district in districts:
        if (
            district.latitude is not None
            and district.longitude is not None
        ):
            district_markers.append({
                "id": district.pk,
                "name": district.name,
                "region": (
                    district.region.name if district.region else ""
                ),
                "latitude": float(district.latitude),
                "longitude": float(district.longitude),
            })

    context = {
        "active_section": "district_map",
        "districts": districts,
        "selected_district": selected_district,
        "district_markers_json": json.dumps(district_markers),
        "uganda_center_latitude": 1.3733,
        "uganda_center_longitude": 32.2903,
    }

    return render(
        request,
        "city_admin/district_map.html",
        context,
    )

# ============================================================
# DJANGO USER UPDATE AND DELETE
# ============================================================

class AdminUserUpdateForm(forms.ModelForm):
    """Fields an administrator may edit for a user account."""

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "is_active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


@city_admin_required
def user_update(request, user_id):
    """Edit basic account details without changing administrator privileges."""

    target_user = get_object_or_404(User, pk=user_id)

    if request.method == "POST":
        form = AdminUserUpdateForm(
            request.POST,
            instance=target_user,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"User '{target_user.username}' was updated successfully.",
            )
            return redirect("city_admin:user_management")
    else:
        form = AdminUserUpdateForm(instance=target_user)

    return render(
        request,
        "city_admin/user_update.html",
        {
            "form": form,
            "target_user": target_user,
            "active_section": "users",
        },
    )


@city_admin_required
@require_POST
def user_delete(request, user_id):
    """Delete an ordinary user account using a POST request."""

    target_user = get_object_or_404(User, pk=user_id)

    if target_user.pk == request.user.pk:
        messages.error(
            request,
            "You cannot delete the account you are currently using.",
        )
        return redirect("city_admin:user_management")

    if target_user.is_staff or target_user.is_superuser:
        messages.error(
            request,
            "Staff and superuser accounts cannot be deleted from this page.",
        )
        return redirect("city_admin:user_management")

    username = target_user.get_username()
    target_user.delete()

    messages.success(
        request,
        f"User '{username}' was deleted successfully.",
    )

    return redirect("city_admin:user_management")


# ============================================================
# VERIFICATION APPLICATION APPROVAL AND REJECTION
# ============================================================

@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_verification_applications(request):
    """Review pending verification applications."""

    if request.method == "POST":
        submission_id = request.POST.get("submission_id")
        action = request.POST.get("action", "").strip()
        review_reason = request.POST.get("review_reason", "").strip()

        if action not in {"approve", "reject"}:
            messages.error(request, "Invalid verification action.")
            return redirect("city_admin:verification_applications")

        if action == "reject" and not review_reason:
            messages.error(
                request,
                "Enter a reason before rejecting an application.",
            )
            return redirect("city_admin:verification_applications")

        with transaction.atomic():
            submission = get_object_or_404(
                VerificationSubmission.objects.select_for_update().select_related(
                    "profile",
                    "profile__user",
                ),
                pk=submission_id,
            )

            if submission.status != VerificationSubmission.Status.PENDING:
                messages.warning(
                    request,
                    "This application has already been reviewed.",
                )
                return redirect("city_admin:verification_applications")

            profile = submission.profile

            if action == "approve":
                submission.status = (
                    VerificationSubmission.Status.APPROVED
                )
                profile.verification_status = (
                    AccountProfile.VerificationStatus.APPROVED
                )
                submission.review_reason = ""

                success_message = (
                    f"Verification approved for {profile.full_name}."
                )
            else:
                submission.status = (
                    VerificationSubmission.Status.REJECTED
                )
                profile.verification_status = (
                    AccountProfile.VerificationStatus.REJECTED
                )
                submission.review_reason = review_reason

                success_message = (
                    f"Verification rejected for {profile.full_name}."
                )

            submission.reviewed_at = timezone.now()

            submission.save(
                update_fields=[
                    "status",
                    "review_reason",
                    "reviewed_at",
                ]
            )

            profile.save(
                update_fields=["verification_status", "updated_at"]
            )

        messages.success(request, success_message)
        return redirect("city_admin:verification_applications")

    submissions = (
        VerificationSubmission.objects
        .filter(status=VerificationSubmission.Status.PENDING)
        .select_related("profile", "profile__user")
        .order_by("submitted_at")
    )

    context = {
        "submissions": submissions,
        "pending_count": submissions.count(),
        "active_section": "verifications",
    }

    return render(
        request,
        "city_admin/verification_review.html",
        context,
    )


# ============================================================
# CITY ADMIN SYSTEM SETTINGS
# ============================================================

@city_admin_required
@require_http_methods(["GET", "POST"])
def city_admin_settings(request):
    """View and update platform settings for authorized administrators."""

    settings = SystemSettings.load()

    if request.method == "POST":
        form = SystemSettingsForm(
            request.POST,
            instance=settings,
        )

        if form.is_valid():
            updated_settings = form.save(commit=False)

            # Keep this page tied to the single settings record.
            updated_settings.pk = 1
            updated_settings.save()

            messages.success(
                request,
                "System settings have been saved successfully.",
            )

            return redirect("city_admin:settings")

        messages.error(
            request,
            "Please correct the errors shown below.",
        )
    else:
        form = SystemSettingsForm(instance=settings)

    return render(
        request,
        "city_admin/settings.html",
        {
            "active_section": "settings",
            "settings": settings,
            "form": form,
        },
    )
