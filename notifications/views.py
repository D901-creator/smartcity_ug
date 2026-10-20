
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Notification


def _visible_notifications(user):
    return Notification.objects.filter(
        recipient=user,
        is_dismissed=False,
    ).order_by("-created_at")


@login_required
def notification_list(request):
    notifications = _visible_notifications(request.user)
    status = request.GET.get("status", "all")

    if status == "unread":
        notifications = notifications.filter(is_read=False)
    elif status == "read":
        notifications = notifications.filter(is_read=True)

    context = {
        "notifications": notifications,
        "unread_count": _visible_notifications(request.user)
        .filter(is_read=False).count(),
        "active_status": status,
    }

    return render(
        request,
        "notifications/notification_list.html",
        context,
    )


@login_required
def notification_detail(request, notification_id):
    notification = get_object_or_404(
        _visible_notifications(request.user),
        id=notification_id,
    )

    if not notification.is_read:
        notification.is_read = True
        notification.save(update_fields=["is_read"])

    return render(
        request,
        "notifications/notification_detail.html",
        {"notification": notification},
    )


@login_required
@require_POST
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(
        _visible_notifications(request.user),
        id=notification_id,
    )
    notification.is_read = True
    notification.save(update_fields=["is_read"])
    return redirect("notifications:list")


@login_required
@require_POST
def mark_all_notifications_read(request):
    _visible_notifications(request.user).filter(
        is_read=False
    ).update(is_read=True)
    return redirect("notifications:list")


@login_required
@require_POST
def dismiss_notification(request, notification_id):
    notification = get_object_or_404(
        _visible_notifications(request.user),
        id=notification_id,
    )
    notification.is_dismissed = True
    notification.save(update_fields=["is_dismissed"])
    return redirect("notifications:list")


@login_required
@require_POST
def clear_read_notifications(request):
    _visible_notifications(request.user).filter(
        is_read=True
    ).update(is_dismissed=True)
    return redirect("notifications:list")


@login_required
@require_POST
def delete_notification(request, notification_id):
    # Keep the existing citizen URL working.
    return dismiss_notification(request, notification_id)


@login_required
def officer_notification_list(request):
    notifications = _visible_notifications(request.user)
    status = request.GET.get("status", "all")

    if status == "unread":
        notifications = notifications.filter(is_read=False)
    elif status == "read":
        notifications = notifications.filter(is_read=True)

    context = {
        "notifications": notifications,
        "unread_count": _visible_notifications(request.user)
        .filter(is_read=False).count(),
        "active_status": status,
    }

    return render(
        request,
        "officer/notifications.html",
        context,
    )
