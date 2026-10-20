
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from notifications.models import Notification


def city_admin_access_required(user):
    """Allow authorized City Admin portal users."""
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.is_staff
            or user.groups.filter(
                name__in=[
                    "City Admin",
                    "City Admins",
                    "System Administrator",
                    "System Administrators",
                ]
            ).exists()
        )
    )


@login_required
def notification_list(request):
    if not city_admin_access_required(request.user):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    notifications = Notification.objects.filter(
        recipient=request.user,
        is_dismissed=False,
    ).order_by("-created_at")

    context = {
        "notifications": notifications,
        "unread_notification_count": notifications.filter(
            is_read=False
        ).count(),
        "active_section": "notifications",
    }

    return render(
        request,
        "city_admin/notifications.html",
        context,
    )


@login_required
@require_POST
def mark_notification_read(request, notification_id):
    if not city_admin_access_required(request.user):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    notification = get_object_or_404(
        Notification,
        id=notification_id,
        recipient=request.user,
        is_dismissed=False,
    )

    notification.is_read = True
    notification.save(update_fields=["is_read"])

    messages.success(request, "Notification marked as read.")
    return redirect("city_admin:notifications")


@login_required
@require_POST
def mark_all_notifications_read(request):
    if not city_admin_access_required(request.user):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    Notification.objects.filter(
        recipient=request.user,
        is_read=False,
        is_dismissed=False,
    ).update(is_read=True)

    messages.success(request, "All notifications marked as read.")
    return redirect("city_admin:notifications")
