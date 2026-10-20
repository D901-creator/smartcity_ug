from .models import Notification


def notification_context(request):
    if not request.user.is_authenticated:
        return {
            "unread_notification_count": 0,
            "nav_notifications": [],
        }

    notifications = Notification.objects.filter(
        recipient=request.user,
        is_dismissed=False,
    ).order_by("-created_at")

    return {
        "unread_notification_count": notifications.filter(
            is_read=False
        ).count(),
        "nav_notifications": list(notifications[:5]),
    }
