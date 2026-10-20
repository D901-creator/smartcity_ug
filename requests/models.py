from django.conf import settings
from django.db import models
import uuid


class CitizenRequest(models.Model):

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("pending", "Pending"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    request_number = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
    )

    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="citizen_service_requests",
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    department = models.CharField(
        max_length=200,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    district_ref = models.ForeignKey(
        "locations.District",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mapped_service_requests",
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="submitted",
    )

    official_response = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs):

        if not self.request_number:
            self.request_number = (
                f"SCRQ-{uuid.uuid4().hex[:10].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.request_number} - {self.title}"