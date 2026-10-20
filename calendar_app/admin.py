
from django.contrib import admin
from .models import CalendarEvent


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "start_time",
        "end_time",
        "created_by",
    )

    list_filter = ("category", "status", "start_time")
    search_fields = (
        "title",
        "description",
        "location",
        "created_by__username",
    )

    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "start_time"
    ordering = ("start_time",)
