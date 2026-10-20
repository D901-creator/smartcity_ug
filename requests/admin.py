from django.contrib import admin

from .models import CitizenRequest


@admin.register(CitizenRequest)
class CitizenRequestAdmin(admin.ModelAdmin):

    list_display = (
        "request_number",
        "title",
        "citizen",
        "department",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "department",
    )

    search_fields = (
        "request_number",
        "title",
        "description",
        "citizen__username",
        "department",
        "location",
    )

    readonly_fields = (
        "request_number",
        "citizen",
        "created_at",
        "updated_at",
    )