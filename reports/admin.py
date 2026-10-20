
from django.contrib import admin
from .models import CitizenReport


@admin.register(CitizenReport)
class CitizenReportAdmin(admin.ModelAdmin):
    list_display = (
        "report_number",
        "title",
        "citizen",
        "department",
        "priority",
        "status",
        "created_at",
    )

    list_filter = ("status", "priority", "department")

    search_fields = (
        "report_number",
        "title",
        "description",
        "citizen__username",
        "department",
        "location",
    )

    readonly_fields = (
        "report_number",
        "citizen",
        "created_at",
        "updated_at",
    )
