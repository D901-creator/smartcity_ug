import csv

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from audit.models import AuditLog
from .models import SecurityEvent


def require_security_admin(user):
    """Restrict security and audit records to approved administrators."""
    allowed_groups = [
        "City Admin",
        "City Admins",
        "System Administrator",
        "System Administrators",
    ]

    allowed = (
        user.is_authenticated
        and (
            user.is_superuser
            or user.is_staff
            or user.groups.filter(name__in=allowed_groups).exists()
        )
    )

    if not allowed:
        raise PermissionDenied(
            "You are not authorized to access security and audit records."
        )


def get_client_ip(request):
    """
    Use REMOTE_ADDR by default.

    Do not blindly trust X-Forwarded-For unless your deployment has a
    correctly configured trusted proxy.
    """
    return request.META.get("REMOTE_ADDR") or None


def record_security_event(
    *,
    event_type="other",
    severity="medium",
    summary,
    details="",
    user=None,
    ip_address=None,
    request_path="",
):
    """
    Reusable helper for recording a security event.

    Call this helper from a trusted server-side view or service when a
    relevant event is actually detected. It does not detect events itself.
    """
    valid_types = {choice[0] for choice in SecurityEvent.EVENT_TYPE_CHOICES}
    valid_severities = {
        choice[0] for choice in SecurityEvent.SEVERITY_CHOICES
    }

    if event_type not in valid_types:
        event_type = "other"

    if severity not in valid_severities:
        severity = "medium"

    return SecurityEvent.objects.create(
        event_type=event_type,
        severity=severity,
        summary=str(summary)[:250],
        details=str(details),
        user=user if getattr(user, "is_authenticated", False) else None,
        ip_address=ip_address,
        request_path=str(request_path)[:500],
    )


@login_required
def security_dashboard(request):
    require_security_admin(request.user)

    events = SecurityEvent.objects.select_related(
        "user", "reviewed_by"
    )

    context = {
        "active_section": "security_audit",
        "total_events": events.count(),
        "new_events": events.filter(status="new").count(),
        "investigating_events": events.filter(
            status="investigating"
        ).count(),
        "high_priority_events": events.filter(
            severity__in=["high", "critical"]
        ).exclude(status__in=["resolved", "dismissed"]).count(),
        "recent_events": events[:10],
        "recent_audit_logs": AuditLog.objects.select_related(
            "user"
        ).order_by("-created_at")[:10],
    }

    return render(
        request,
        "city_admin/security_dashboard.html",
        context,
    )


@login_required
def security_events(request):
    require_security_admin(request.user)

    events = SecurityEvent.objects.select_related(
        "user", "reviewed_by"
    )

    search = request.GET.get("q", "").strip()
    severity = request.GET.get("severity", "").strip()
    status = request.GET.get("status", "").strip()
    event_type = request.GET.get("event_type", "").strip()

    if search:
        events = events.filter(
            Q(summary__icontains=search)
            | Q(details__icontains=search)
            | Q(ip_address__icontains=search)
            | Q(request_path__icontains=search)
            | Q(user__username__icontains=search)
        )

    valid_severities = {
        choice[0] for choice in SecurityEvent.SEVERITY_CHOICES
    }
    valid_statuses = {
        choice[0] for choice in SecurityEvent.STATUS_CHOICES
    }
    valid_types = {
        choice[0] for choice in SecurityEvent.EVENT_TYPE_CHOICES
    }

    if severity in valid_severities:
        events = events.filter(severity=severity)

    if status in valid_statuses:
        events = events.filter(status=status)

    if event_type in valid_types:
        events = events.filter(event_type=event_type)

    context = {
        "active_section": "security_audit",
        "events": events[:300],
        "search": search,
        "selected_severity": severity,
        "selected_status": status,
        "selected_event_type": event_type,
        "severity_choices": SecurityEvent.SEVERITY_CHOICES,
        "status_choices": SecurityEvent.STATUS_CHOICES,
        "event_type_choices": SecurityEvent.EVENT_TYPE_CHOICES,
    }

    return render(
        request,
        "city_admin/security_events.html",
        context,
    )


@login_required
def audit_trail(request):
    require_security_admin(request.user)

    logs = AuditLog.objects.select_related("user").order_by("-created_at")

    search = request.GET.get("q", "").strip()

    if search:
        logs = logs.filter(
            Q(action__icontains=search)
            | Q(details__icontains=search)
            | Q(ip_address__icontains=search)
            | Q(user__username__icontains=search)
        )

    context = {
        "active_section": "security_audit",
        "audit_logs": logs[:300],
        "search": search,
    }

    return render(
        request,
        "city_admin/audit_trail.html",
        context,
    )


@login_required
def security_event_detail(request, event_id):
    require_security_admin(request.user)

    event = get_object_or_404(
        SecurityEvent.objects.select_related("user", "reviewed_by"),
        pk=event_id,
    )

    return render(
        request,
        "city_admin/security_event_detail.html",
        {
            "active_section": "security_audit",
            "event": event,
        },
    )


@login_required
@require_POST
def update_security_event(request, event_id):
    require_security_admin(request.user)

    event = get_object_or_404(SecurityEvent, pk=event_id)

    allowed_statuses = {
        choice[0] for choice in SecurityEvent.STATUS_CHOICES
    }
    new_status = request.POST.get("status", "").strip()
    review_notes = request.POST.get("review_notes", "").strip()

    if new_status not in allowed_statuses:
        messages.error(request, "Choose a valid investigation status.")
        return redirect(
            "city_admin:security_event_detail",
            event_id=event.pk,
        )

    event.status = new_status
    event.review_notes = review_notes
    event.reviewed_by = request.user
    event.reviewed_at = timezone.now()
    event.save(
        update_fields=[
            "status",
            "review_notes",
            "reviewed_by",
            "reviewed_at",
            "updated_at",
        ]
    )

    # Reuse the existing audit log instead of creating a duplicate audit model.
    AuditLog.objects.create(
        user=request.user,
        action="security_event_reviewed",
        details=(
            f"Reviewed security event #{event.pk}; "
            f"status changed to {new_status}."
        ),
        ip_address=get_client_ip(request),
    )

    messages.success(request, "Security event review saved.")

    return redirect(
        "city_admin:security_event_detail",
        event_id=event.pk,
    )


@login_required
def export_audit_csv(request):
    require_security_admin(request.user)

    logs = AuditLog.objects.select_related("user").order_by("-created_at")

    search = request.GET.get("q", "").strip()
    if search:
        logs = logs.filter(
            Q(action__icontains=search)
            | Q(details__icontains=search)
            | Q(ip_address__icontains=search)
            | Q(user__username__icontains=search)
        )

    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="smart-city-audit.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "Timestamp",
        "Username",
        "Action",
        "Details",
        "IP Address",
    ])

    for entry in logs.iterator(chunk_size=500):
        writer.writerow([
            entry.created_at.isoformat() if entry.created_at else "",
            entry.user.get_username() if entry.user else "",
            entry.action,
            entry.details,
            entry.ip_address or "",
        ])

    return response