from django.contrib import admin

from .models import GovernmentService, ServiceRequest


@admin.register(GovernmentService)
class GovernmentServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "estimated_days",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "short_description",
        "description",
    )


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "service",
        "citizen_name",
        "citizen_district",
        "status",
        "submitted_at",
    )

    list_filter = (
        "status",
        "service__category",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "citizen_phone",
        "citizen_district",
    )

    readonly_fields = (
        "reference_number",
        "submitted_at",
        "updated_at",
    )