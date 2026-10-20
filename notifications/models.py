from django.conf import settings
from django.db import models


class Notification(models.Model):
    TYPE_CHOICES = [
        ("request", "Request"),
        ("report", "Report"),
        ("announcement", "Announcement"),
        ("message", "Message"),
        ("application", "Application"),
        ("payment", "Payment"),
        ("job", "Job Opportunity"),
        ("system", "System Alert"),
    ]

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        default="system",
    )

    is_read = models.BooleanField(default=False)
    is_dismissed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.recipient}"