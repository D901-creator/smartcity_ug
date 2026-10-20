
import csv
import logging
from datetime import date, timedelta
from functools import wraps
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from accounts.models import AccountProfile
from notifications.models import Notification
from officer.models import CitizenRequest, RequestStatusHistory

from health.models import HealthProject
from education.models import EducationProject
from agriculture.models import AgriculturalProject, IrrigationProject
from water.models import WaterProject, EnvironmentalProject
from public_works.models import (
    PublicWorksProject,
    RoadConstructionMaintenanceProject,
)
from energy.models import EnergyProject
from lands.models import LandHousingPlanningProject
from economic_development.models import EconomicProject
from tourism.models import TourismProjectOpportunity
from audit.models import AuditLog
from tasks.models import Task


User = get_user_model()
logger = logging.getLogger(__name__)


# ============================================================
# DEPARTMENT HEAD ACCESS CONTROL
# ============================================================

def department_head_required(view_func):
    """
    Allow only authenticated, approved department heads
    to access department-head portal views.
    """

    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        profile = AccountProfile.objects.filter(
            user=request.user
        ).first()

        if profile is None:
            messages.error(
                request,
                "Your account profile could not be found.",
            )
            return redirect("accounts:login")

        if profile.role != AccountProfile.Role.DEPARTMENT_HEAD:
            messages.error(
                request,
                "Access denied. Department Head access is required.",
            )
            return redirect("accounts:login")

        if (
            profile.verification_status
            != AccountProfile.VerificationStatus.APPROVED
        ):
            messages.warning(
                request,
                "Your Department Head account must be approved first.",
            )
            return redirect("accounts:verification_pending")

        return view_func(request, *args, **kwargs)

    return wrapper


# ============================================================
# OFFICER QUERYSET
# ============================================================

def officer_users():
    """
    Return users identified as officers by their profile role
    or by membership in the existing Officer/Officers groups.
    """

    return User.objects.filter(
        Q(account_profile__role=AccountProfile.Role.OFFICER)
        | Q(groups__name__in=["Officer", "Officers"])
    ).distinct()

def department_request_queryset(profile):
    """
    Return citizen requests belonging only to this Department Head's
    department, regardless of district or city.
    """
    if not profile.department_id:
        return CitizenRequest.objects.none()

    return CitizenRequest.objects.filter(
        department__iexact=profile.department.name
    )


def department_task_queryset(profile):
    """
    Return tasks assigned to this department only.
    """
    if not profile.department_id:
        return Task.objects.none()

    return Task.objects.filter(
        department__iexact=profile.department.name
    )
# ============================================================
# DASHBOARD
# ============================================================

@department_head_required
def dashboard(request):
    profile = AccountProfile.objects.get(user=request.user)
    department_id = profile.department_id

    officers = officer_users().filter(
        account_profile__department_id=department_id
    )

    requests_qs = department_request_queryset(profile)

    context = {
        "page_title": "Department Head Dashboard",
        "today": timezone.localdate(),
        "request_count": requests_qs.count(),
        "officer_count": officers.count(),
        "project_count": None,
        "resolved_count": requests_qs.filter(
            status=CitizenRequest.Status.RESOLVED
        ).count(),
    }

    return render(
        request,
        "department_head/dashboard.html",
        context,
    )


# ============================================================
# OFFICERS DIRECTORY
# ============================================================

@department_head_required
def officers_directory(request):
    profile = AccountProfile.objects.get(user=request.user)

    officers = officer_users().select_related(
        "account_profile",
        "account_profile__department",
    ).filter(
        account_profile__department_id=profile.department_id
    )

    search = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()

    if search:
        officers = officers.filter(
            Q(username__icontains=search)
            | Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(email__icontains=search)
            | Q(account_profile__full_name__icontains=search)
            | Q(account_profile__phone_number__icontains=search)
        )

    if status == "active":
        officers = officers.filter(is_active=True)
    elif status == "inactive":
        officers = officers.filter(is_active=False)

    context = {
        "page_title": "Officers Directory",
        "officers": officers.order_by("username"),
        "search": search,
        "selected_status": status,
        "total_officers": officers.count(),
        "active_officers": officers.filter(is_active=True).count(),
        "inactive_officers": officers.filter(is_active=False).count(),
    }

    return render(
        request,
        "department_head/officers.html",
        context,
    )


# ============================================================
# OFFICER DETAILS
# ============================================================

@department_head_required
def officer_detail(request, user_id):
    profile = AccountProfile.objects.get(user=request.user)

    officer = get_object_or_404(
        officer_users().select_related(
            "account_profile",
            "account_profile__department",
        ).filter(
            account_profile__department_id=profile.department_id
        ),
        pk=user_id,
    )

    return render(
        request,
        "department_head/officer_detail.html",
        {
            "page_title": "Officer Details",
            "officer": officer,
        },
    )


# ============================================================
# CITIZEN REQUESTS
# ============================================================

@department_head_required
def requests_list(request):
    profile = AccountProfile.objects.get(user=request.user)
    requests_qs = department_request_queryset(profile).order_by("-created_at")

    search = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()
    priority = request.GET.get("priority", "").strip()

    if search:
        requests_qs = requests_qs.filter(
            Q(subject__icontains=search)
            | Q(description__icontains=search)
        )

    if status:
        requests_qs = requests_qs.filter(status=status)

    if priority:
        requests_qs = requests_qs.filter(priority=priority)

    return render(
        request,
        "department_head/requests.html",
        {
            "page_title": "Citizen Requests",
            "requests": requests_qs,
            "search": search,
            "selected_status": status,
            "selected_priority": priority,
            "total_requests": requests_qs.count(),
        },
    )


# ============================================================
# REQUEST DECISIONS
# ============================================================

@department_head_required
@require_http_methods(["GET", "POST"])
def request_decision(request, request_id):
    profile = AccountProfile.objects.get(user=request.user)

    citizen_request = get_object_or_404(
    department_request_queryset(profile),
    pk=request_id,
)

    if request.method == "GET":
        return render(
            request,
            "department_head/request_decision.html",
            {
                "page_title": "Request Decision",
                "citizen_request": citizen_request,
                "statuses": CitizenRequest.Status.choices,
            },
        )

    new_status = request.POST.get("status", "").strip()
    note = request.POST.get("note", "").strip()

    valid_statuses = {
        value for value, label in CitizenRequest.Status.choices
    }

    if new_status not in valid_statuses:
        messages.error(
            request,
            "Please select a valid request status.",
        )
        return redirect(
            "department_head:request_decision",
            request_id=citizen_request.pk,
        )

    with transaction.atomic():
        citizen_request = get_object_or_404(
            department_request_queryset(profile).select_for_update(),
            pk=request_id,
)

        previous_status = citizen_request.status

        if previous_status != new_status:
            citizen_request.status = new_status

            if new_status == CitizenRequest.Status.RESOLVED:
                citizen_request.resolved_at = timezone.now()
            elif previous_status == CitizenRequest.Status.RESOLVED:
                citizen_request.resolved_at = None

            citizen_request.save(
                update_fields=[
                    "status",
                    "resolved_at",
                    "updated_at",
                ]
            )

            RequestStatusHistory.objects.create(
                request=citizen_request,
                previous_status=previous_status,
                new_status=new_status,
                changed_by=request.user,
                note=note,
            )

        elif note:
            RequestStatusHistory.objects.create(
                request=citizen_request,
                previous_status=previous_status,
                new_status=new_status,
                changed_by=request.user,
                note=note,
            )

    messages.success(
        request,
        "The request decision has been recorded.",
    )

    return redirect("department_head:requests")


# ============================================================
# PERFORMANCE
# ============================================================

@department_head_required
def performance(request):
    today = timezone.localdate()
    start_date = today - timedelta(days=29)

    profile = AccountProfile.objects.get(user=request.user)
    all_requests = department_request_queryset(profile)
    recent_requests = all_requests.filter(
        created_at__date__gte=start_date,
        created_at__date__lte=today,
    )

    total_requests = all_requests.count()

    resolved_requests = all_requests.filter(
        status=CitizenRequest.Status.RESOLVED
    ).count()

    pending_requests = all_requests.filter(
        status=CitizenRequest.Status.PENDING
    ).count()

    in_progress_requests = all_requests.filter(
        status=CitizenRequest.Status.IN_PROGRESS
    ).count()

    waiting_requests = all_requests.filter(
        status=CitizenRequest.Status.WAITING
    ).count()

    resolution_rate = (
        round(resolved_requests / total_requests * 100, 1)
        if total_requests
        else 0
    )

    daily_requests = (
        recent_requests.values("created_at__date")
        .annotate(total=Count("id"))
        .order_by("created_at__date")
    )

    daily_resolved = all_requests.filter(
        resolved_at__date__gte=start_date,
        resolved_at__date__lte=today,
    ).count()

    return render(
        request,
        "department_head/performance.html",
        {
            "page_title": "Performance",
            "total_requests": total_requests,
            "recent_request_count": recent_requests.count(),
            "resolved_requests": resolved_requests,
            "pending_requests": pending_requests,
            "in_progress_requests": in_progress_requests,
            "waiting_requests": waiting_requests,
            "resolution_rate": resolution_rate,
            "daily_requests": daily_requests,
            "daily_resolved": daily_resolved,
            "start_date": start_date,
            "today": today,
        },
    )


# ============================================================
# PROJECTS
# ============================================================

@department_head_required
def projects_list(request):
    search = request.GET.get("q", "").strip()
    selected_status = request.GET.get("status", "").strip()

    project_sources = [
        ("Health", HealthProject, "title", "status"),
        ("Education", EducationProject, "title", "status"),
        ("Agriculture", AgriculturalProject, "name", "status"),
        ("Irrigation", IrrigationProject, "name", "status"),
        ("Water", WaterProject, "name", "status"),
        ("Environment", EnvironmentalProject, "name", "status"),
        ("Public Works", PublicWorksProject, "name", "status"),
        (
            "Roads",
            RoadConstructionMaintenanceProject,
            "name",
            "status",
        ),
        ("Energy", EnergyProject, "name", "status"),
        (
            "Lands & Housing",
            LandHousingPlanningProject,
            "title",
            "status",
        ),
        (
            "Economic Development",
            EconomicProject,
            "title",
            "status",
        ),
        (
            "Tourism",
            TourismProjectOpportunity,
            "title",
            "status",
        ),
    ]

    projects = []

    for department_name, model, name_field, status_field in project_sources:
        queryset = model.objects.all()

        if search:
            filters = Q(**{f"{name_field}__icontains": search})
            field_names = {
                field.name for field in model._meta.get_fields()
            }

            if "district" in field_names:
                filters |= Q(district__icontains=search)

            if "location" in field_names:
                filters |= Q(location__icontains=search)

            queryset = queryset.filter(filters)

        if selected_status:
            queryset = queryset.filter(
                **{status_field: selected_status}
            )

        for item in queryset:
            projects.append({
                "id": item.pk,
                "name": getattr(item, name_field, ""),
                "department": department_name,
                "district": getattr(item, "district", ""),
                "location": getattr(item, "location", ""),
                "status": getattr(item, status_field, ""),
                "start_date": getattr(item, "start_date", None),
                "completion_date": getattr(
                    item,
                    "expected_completion_date",
                    getattr(item, "end_date", None),
                ),
                "progress": getattr(
                    item,
                    "completion_percentage",
                    None,
                ),
                "budget": getattr(
                    item,
                    "project_budget",
                    getattr(item, "budget", None),
                ),
                "model_name": model.__name__,
            })

    projects.sort(
        key=lambda project: project["start_date"] or date.min,
        reverse=True,
    )

    return render(
        request,
        "department_head/projects.html",
        {
            "page_title": "Projects Management",
            "projects": projects,
            "total_projects": len(projects),
            "search": search,
            "selected_status": selected_status,
            "ongoing_projects": sum(
                1 for project in projects
                if str(project["status"]).lower() in (
                    "ongoing",
                    "in_progress",
                    "in progress",
                )
            ),
            "completed_projects": sum(
                1 for project in projects
                if str(project["status"]).lower() in (
                    "completed",
                    "complete",
                )
            ),
        },
    )


# ============================================================
# REPORTS AND CSV EXPORT
# ============================================================

@department_head_required
def reports(request):
    profile = AccountProfile.objects.get(user=request.user)
    requests_qs = department_request_queryset(profile)
    status = request.GET.get("status", "").strip()
    start_date = request.GET.get("start_date", "").strip()
    end_date = request.GET.get("end_date", "").strip()

    valid_statuses = {
        value for value, label in CitizenRequest.Status.choices
    }

    if status in valid_statuses:
        requests_qs = requests_qs.filter(status=status)

    if start_date:
        requests_qs = requests_qs.filter(
            created_at__date__gte=start_date
        )

    if end_date:
        requests_qs = requests_qs.filter(
            created_at__date__lte=end_date
        )

    if request.GET.get("export") == "csv":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="smartcity_requests_report.csv"'
        )

        writer = csv.writer(response)
        writer.writerow([
            "Reference",
            "Status",
            "Priority",
            "Created At",
        ])

        for item in requests_qs.order_by("-created_at"):
            writer.writerow([
                item.reference,
                item.status,
                item.priority,
                item.created_at.strftime("%Y-%m-%d %H:%M"),
            ])

        return response

    return render(
        request,
        "department_head/reports.html",
        {
            "page_title": "Department Reports",
            "requests": requests_qs.order_by("-created_at")[:200],
            "total_count": requests_qs.count(),
            "resolved_count": requests_qs.filter(
                status=CitizenRequest.Status.RESOLVED
            ).count(),
            "pending_count": requests_qs.filter(
                status=CitizenRequest.Status.PENDING
            ).count(),
            "status_choices": CitizenRequest.Status.choices,
            "selected_status": status,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


# ============================================================
# TASKS
# ============================================================

@department_head_required
def tasks_list(request):
    profile = AccountProfile.objects.get(user=request.user)
    tasks = department_task_queryset(profile).order_by("-id")
    return render(
        request,
        "department_head/tasks.html",
        {
            "page_title": "Department Tasks",
            "tasks": tasks,
        },
    )


# ============================================================
# ACCOUNTABILITY AND AUDIT
# ============================================================

@department_head_required
def accountability(request):
    logs = AuditLog.objects.all().order_by("-id")

    return render(
        request,
        "department_head/accountability.html",
        {
            "page_title": "Accountability & Audit",
            "logs": logs[:200],
            "total_logs": logs.count(),
        },
    )


# ============================================================
# NOTIFICATIONS
# ============================================================

@department_head_required
def notifications_page(request):
    notifications = Notification.objects.filter(
        recipient=request.user,
        is_dismissed=False,
    )

    return render(
        request,
        "department_head/notifications.html",
        {
            "page_title": "Notifications",
            "notifications": notifications,
            "unread_count": notifications.filter(
                is_read=False
            ).count(),
        },
    )


@department_head_required
@require_http_methods(["POST"])
def notification_read(request, notification_id):
    notification = get_object_or_404(
        Notification,
        pk=notification_id,
        recipient=request.user,
    )

    notification.is_read = True
    notification.save(update_fields=["is_read"])

    return redirect("department_head:notifications")


# ============================================================
# MY PROFILE
# ============================================================

@department_head_required
@require_http_methods(["GET", "POST"])
def my_profile(request):
    profile = AccountProfile.objects.get(user=request.user)

    if request.method == "POST":
        full_name = request.POST.get(
            "full_name",
            profile.full_name,
        ).strip()

        phone_number = request.POST.get(
            "phone_number",
            profile.phone_number,
        ).strip()

        email = request.POST.get("email", "").strip().lower()

        if not email:
            messages.error(request, "Email address is required.")

        elif User.objects.filter(
            email__iexact=email
        ).exclude(
            pk=request.user.pk
        ).exists():
            messages.error(
                request,
                "That email address is already in use.",
            )

        else:
            request.user.email = email
            request.user.save(update_fields=["email"])

            profile.full_name = full_name
            profile.phone_number = phone_number

            if request.FILES.get("profile_picture"):
                profile.profile_picture = request.FILES[
                    "profile_picture"
                ]

            profile.save()

            messages.success(
                request,
                "Your profile has been updated.",
            )

            return redirect("department_head:my_profile")

    return render(
        request,
        "department_head/my_profile.html",
        {
            "page_title": "My Profile",
            "profile": profile,
        },
    )


# ============================================================
# SETTINGS
# ============================================================

@department_head_required
@require_http_methods(["GET", "POST"])
def department_head_settings(request):
    if request.method == "POST":
        theme = request.POST.get("theme", "light")

        allowed_themes = [
            "light",
            "green",
            "blue",
            "dark",
            "black",
        ]

        if theme not in allowed_themes:
            messages.error(request, "Invalid theme selected.")

        else:
            request.session["active_theme"] = theme

            messages.success(
                request,
                "Settings saved successfully.",
            )

            return redirect("department_head:settings")

    return render(
        request,
        "department_head/settings.html",
        {
            "page_title": "Settings",
            "active_theme": request.session.get(
                "active_theme",
                "light",
            ),
        },
    )


# ============================================================
# LOGOUT — SHARED AUTHENTICATION
# ============================================================

@login_required
@require_POST
def department_head_logout(request):
    logout(request)
    return redirect("/")
