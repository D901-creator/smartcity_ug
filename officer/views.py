
import uuid
from datetime import date
from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST, require_http_methods

from accounts.models import AccountProfile
from tasks.models import Task

from .forms import OfficerReplyForm, OfficerRequestStatusForm
from .models import (
    CitizenRequest,
    RequestReply,
    RequestStatusHistory,
    OfficerAttendance,
)


# ============================================================
# OFFICER AUTHENTICATION AND AUTHORIZATION
# ============================================================

def government_officer_required(view_func):
    """
    Permit only authenticated, approved officer accounts.
    Use this decorator on officer-only views.
    """

    @login_required
    @wraps(view_func)
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

        if profile.role != AccountProfile.Role.OFFICER:
            messages.error(
                request,
                "Access denied. A government officer account is required.",
            )
            return redirect("accounts:login")

        if (
            profile.verification_status
            != AccountProfile.VerificationStatus.APPROVED
        ):
            messages.warning(
                request,
                "Your officer account must be approved before accessing the portal.",
            )
            return redirect("accounts:verification_pending")

        return view_func(request, *args, **kwargs)

    return wrapper


def _is_officer(user):
    """Return True only for an approved officer or a superuser."""
    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    profile = AccountProfile.objects.filter(
        user=user
    ).first()

    return bool(
        profile
        and profile.role == AccountProfile.Role.OFFICER
        and profile.verification_status
        == AccountProfile.VerificationStatus.APPROVED
    )


def _officer_access_required(request):
    """Apply the shared authentication and officer-approval rules."""
    if not request.user.is_authenticated:
        messages.info(
            request,
            "Please sign in to access the Officer Portal.",
        )
        return redirect("accounts:login")

    # Keep superuser access for administration and troubleshooting.
    if request.user.is_superuser:
        return None

    profile = AccountProfile.objects.filter(
        user=request.user
    ).first()

    if profile is None:
        messages.error(
            request,
            "Your account profile could not be found.",
        )
        return redirect("accounts:login")

    if profile.role != AccountProfile.Role.OFFICER:
        messages.error(
            request,
            "You do not have permission to access the Officer Portal.",
        )
        return redirect("accounts:login")

    if (
        profile.verification_status
        != AccountProfile.VerificationStatus.APPROVED
    ):
        messages.warning(
            request,
            "Your officer account is awaiting approval.",
        )
        return redirect("accounts:verification_pending")

    return None


# ============================================================
# OFFICER DASHBOARD
# ============================================================

@login_required
def dashboard(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    total_requests = CitizenRequest.objects.count()

    pending_requests = CitizenRequest.objects.filter(
        status=CitizenRequest.Status.PENDING
    ).count()

    in_progress_requests = CitizenRequest.objects.filter(
        status=CitizenRequest.Status.IN_PROGRESS
    ).count()

    resolved_requests = CitizenRequest.objects.filter(
        status=CitizenRequest.Status.RESOLVED
    ).count()

    recent_requests = (
        CitizenRequest.objects.select_related(
            "citizen",
            "assigned_officer",
        )
        .order_by("-created_at")[:5]
    )

    pending_tasks = Task.objects.filter(
        assigned_to=request.user,
        status=Task.Status.ASSIGNED,
    ).count()

    context = {
        "total_requests": total_requests,
        "pending_requests": pending_requests,
        "in_progress_requests": in_progress_requests,
        "resolved_requests": resolved_requests,
        "open_cases": 0,
        "pending_tasks": pending_tasks,
        "recent_requests": recent_requests,
    }

    return render(request, "officer/dashboard.html", context)


# ============================================================
# ASSIGNED CITIZEN REQUESTS
# ============================================================

@login_required
def assigned_requests(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    requests_list = CitizenRequest.objects.select_related(
        "citizen",
        "assigned_officer",
    ).all()

    search_query = request.GET.get("q", "").strip()
    selected_status = request.GET.get("status", "").strip()
    selected_department = request.GET.get("department", "").strip()

    if search_query:
        filters = (
            Q(subject__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(department__icontains=search_query)
            | Q(citizen__username__icontains=search_query)
        )

        try:
            reference = uuid.UUID(search_query)
            filters |= Q(reference=reference)
        except (ValueError, AttributeError):
            pass

        requests_list = requests_list.filter(filters)

    if selected_status in CitizenRequest.Status.values:
        requests_list = requests_list.filter(
            status=selected_status
        )

    if selected_department:
        requests_list = requests_list.filter(
            department=selected_department
        )

    departments = (
        CitizenRequest.objects.order_by("department")
        .values_list("department", flat=True)
        .distinct()
    )

    context = {
        "requests_list": requests_list,
        "search_query": search_query,
        "selected_status": selected_status,
        "selected_department": selected_department,
        "departments": departments,
        "status_choices": CitizenRequest.Status.choices,
    }

    return render(
        request,
        "officer/assigned_requests.html",
        context,
    )


# ============================================================
# CASES
# ============================================================

@login_required
def cases(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    # Placeholder until the existing cases app is integrated.
    context = {
        "cases": [],
        "total_cases": 0,
        "open_cases": 0,
        "in_progress_cases": 0,
        "resolved_cases": 0,
        "search_query": request.GET.get("q", "").strip(),
        "selected_status": request.GET.get("status", "").strip(),
        "selected_priority": request.GET.get("priority", "").strip(),
        "status_choices": [],
        "priority_choices": [],
    }

    return render(request, "officer/cases.html", context)


# ============================================================
# REQUEST DETAILS, REPLIES AND STATUS HISTORY
# ============================================================

@login_required
@require_http_methods(["GET", "POST"])
def request_detail(request, request_id):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    citizen_request = get_object_or_404(
        CitizenRequest.objects.select_related(
            "citizen",
            "assigned_officer",
        ),
        pk=request_id,
    )

    reply_form = OfficerReplyForm()
    status_form = OfficerRequestStatusForm()

    if request.method == "POST":
        action = request.POST.get("action", "").strip()

        if action == "reply":
            reply_form = OfficerReplyForm(
                request.POST,
                request.FILES,
            )

            if reply_form.is_valid():
                with transaction.atomic():
                    reply = reply_form.save(commit=False)
                    reply.request = citizen_request
                    reply.sender = request.user
                    reply.sender_type = RequestReply.SenderType.OFFICER
                    reply.save()

                messages.success(
                    request,
                    "Your reply has been saved.",
                )

                return redirect(
                    "officer:request_detail",
                    request_id=citizen_request.pk,
                )

            messages.error(
                request,
                "Please correct the reply form.",
            )

        elif action == "status":
            status_form = OfficerRequestStatusForm(request.POST)

            if status_form.is_valid():
                new_status = status_form.cleaned_data["new_status"]
                note = status_form.cleaned_data["note"]

                with transaction.atomic():
                    citizen_request = (
                        CitizenRequest.objects.select_for_update()
                        .get(pk=citizen_request.pk)
                    )

                    previous_status = citizen_request.status

                    if previous_status != new_status:
                        citizen_request.status = new_status

                        if new_status == CitizenRequest.Status.RESOLVED:
                            citizen_request.resolved_at = timezone.now()
                        elif (
                            previous_status
                            == CitizenRequest.Status.RESOLVED
                        ):
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
                    "The request status has been updated.",
                )

                return redirect(
                    "officer:request_detail",
                    request_id=citizen_request.pk,
                )

            messages.error(
                request,
                "Please correct the status form.",
            )

        else:
            messages.error(request, "Unknown request action.")

    replies = citizen_request.replies.select_related("sender").all()

    status_history = (
        citizen_request.status_history.select_related("changed_by").all()
    )

    context = {
        "citizen_request": citizen_request,
        "reply_form": reply_form,
        "status_form": status_form,
        "replies": replies,
        "status_history": status_history,
    }

    return render(
        request,
        "officer/request_detail.html",
        context,
    )


# ============================================================
# OFFICER TASKS
# ============================================================

@login_required
def my_tasks(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    tasks = Task.objects.filter(
        assigned_to=request.user
    ).order_by("due_date", "-created_at")

    return render(
        request,
        "officer/my_tasks.html",
        {"tasks": tasks},
    )


@login_required
@require_POST
def update_task_status(request, task_id):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    task = get_object_or_404(
        Task,
        pk=task_id,
        assigned_to=request.user,
    )

    new_status = request.POST.get("status")

    allowed_statuses = {
        Task.Status.ASSIGNED,
        Task.Status.IN_PROGRESS,
        Task.Status.COMPLETED,
        Task.Status.BLOCKED,
    }

    if new_status not in allowed_statuses:
        messages.error(request, "Invalid task status.")
        return redirect("officer:my_tasks")

    task.status = new_status

    if new_status == Task.Status.COMPLETED:
        task.completed_at = timezone.now()
    else:
        task.completed_at = None

    task.save(
        update_fields=[
            "status",
            "completed_at",
            "updated_at",
        ]
    )

    messages.success(request, "Task status updated.")
    return redirect("officer:my_tasks")


# ============================================================
# OFFICER ATTENDANCE
# ============================================================

@login_required
def attendance(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    today = timezone.localdate()

    record = OfficerAttendance.objects.filter(
        officer=request.user,
        attendance_date=today,
    ).first()

    history = OfficerAttendance.objects.filter(
        officer=request.user
    ).order_by("-attendance_date")[:30]

    return render(
        request,
        "officer/attendance.html",
        {
            "record": record,
            "history": history,
            "today": today,
        },
    )


@login_required
@require_POST
def attendance_check_in(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    today = timezone.localdate()
    now = timezone.now()

    record, created = OfficerAttendance.objects.get_or_create(
        officer=request.user,
        attendance_date=today,
        defaults={
            "check_in": now,
            "status": OfficerAttendance.Status.PRESENT,
        },
    )

    if not created and record.check_in is None:
        record.check_in = now
        record.save(update_fields=["check_in"])

    elif not created:
        messages.info(
            request,
            "You have already checked in today.",
        )
        return redirect("officer:attendance")

    messages.success(
        request,
        "Check-in recorded successfully.",
    )

    return redirect("officer:attendance")


@login_required
@require_POST
def attendance_check_out(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    today = timezone.localdate()

    record = OfficerAttendance.objects.filter(
        officer=request.user,
        attendance_date=today,
    ).first()

    if not record or not record.check_in:
        messages.error(
            request,
            "Check in before checking out.",
        )

    elif record.check_out:
        messages.info(
            request,
            "You have already checked out today.",
        )

    else:
        record.check_out = timezone.now()
        record.save(update_fields=["check_out"])

        messages.success(
            request,
            "Check-out recorded successfully.",
        )

    return redirect("officer:attendance")


# ============================================================
# OFFICER PERFORMANCE
# ============================================================

@login_required
def performance(request):
    access_redirect = _officer_access_required(request)
    if access_redirect:
        return access_redirect

    today = timezone.localdate()

    assigned = CitizenRequest.objects.filter(
        assigned_officer=request.user
    )

    total_requests = assigned.count()

    resolved_requests = assigned.filter(
        status=CitizenRequest.Status.RESOLVED
    ).count()

    closed_requests = assigned.filter(
        status=CitizenRequest.Status.CLOSED
    ).count()

    active_requests = assigned.filter(
        status__in=[
            CitizenRequest.Status.PENDING,
            CitizenRequest.Status.ACKNOWLEDGED,
            CitizenRequest.Status.IN_PROGRESS,
            CitizenRequest.Status.WAITING,
        ]
    ).count()

    completed = resolved_requests + closed_requests

    completion_rate = (
        round(completed * 100 / total_requests, 1)
        if total_requests
        else 0
    )

    attendance_records = OfficerAttendance.objects.filter(
        officer=request.user
    )

    attendance_summary = {
        "present": attendance_records.filter(
            status=OfficerAttendance.Status.PRESENT
        ).count(),
        "late": attendance_records.filter(
            status=OfficerAttendance.Status.LATE
        ).count(),
        "absent": attendance_records.filter(
            status=OfficerAttendance.Status.ABSENT
        ).count(),
        "on_leave": attendance_records.filter(
            status=OfficerAttendance.Status.ON_LEAVE
        ).count(),
    }

    recent_requests = assigned.order_by("-updated_at")[:10]

    return render(
        request,
        "officer/performance.html",
        {
            "total_requests": total_requests,
            "resolved_requests": resolved_requests,
            "closed_requests": closed_requests,
            "active_requests": active_requests,
            "completion_rate": completion_rate,
            "attendance_summary": attendance_summary,
            "recent_requests": recent_requests,
            "today": today,
        },
    )
