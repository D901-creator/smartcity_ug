from django.conf import settings
from django.db import models
import uuid


class CitizenReport(models.Model):

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    PRIORITY_CHOICES = [
        ("normal", "Normal"),
        ("urgent", "Urgent"),
    ]

    report_number = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
    )

    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="citizen_reports",
    )

    assigned_officer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_citizen_reports",
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
    )

    district_ref = models.ForeignKey(
        "locations.District",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mapped_reports",
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="normal",
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

        if not self.report_number:
            self.report_number = (
                f"SCR-{uuid.uuid4().hex[:10].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.report_number} - {self.title}"
    
    
    