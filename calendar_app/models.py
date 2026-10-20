
from django.conf import settings
from django.db import models
from django.utils import timezone


class CalendarEvent(models.Model):
    class Category(models.TextChoices):
        MEETING = "meeting", "Meeting"
        FIELD_VISIT = "field_visit", "Field Visit"
        DEADLINE = "deadline", "Deadline"
        APPOINTMENT = "appointment", "Appointment"
        TASK = "task", "Task"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.MEETING,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED,
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)

    # The officer who created the event.
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="calendar_events_created",
    )

    # Optional reminder before the event.
    reminder_minutes = models.PositiveIntegerField(
        default=15,
        help_text="Minutes before the event to send a reminder.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=["start_time"]),
            models.Index(fields=["status", "start_time"]),
        ]

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                raise ValidationError({
                    "end_time": "The end time must be after the start time."
                })

    def __str__(self):
        return f"{self.title} — {self.start_time:%Y-%m-%d %H:%M}"

    @property
    def is_overdue(self):
        return (
            self.end_time < timezone.now()
            and self.status not in [
                self.Status.COMPLETED,
                self.Status.CANCELLED,
            ]
        )
