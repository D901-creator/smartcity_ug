
from django.contrib import admin

from .models import (
    JobOpportunity,
    SkillsOpportunity,
    EmploymentInformation,
)


@admin.register(JobOpportunity)
class JobOpportunityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "employment_type",
        "sector",
        "district",
        "status",
        "deadline",
        "is_published",
    )

    list_filter = (
        "employment_type",
        "sector",
        "status",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "organization",
        "summary",
        "description",
        "district",
        "location",
    )

    list_editable = (
        "status",
        "is_published",
    )


@admin.register(SkillsOpportunity)
class SkillsOpportunityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "opportunity_type",
        "district",
        "status",
        "closing_date",
        "is_published",
    )

    list_filter = (
        "opportunity_type",
        "status",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "organization",
        "summary",
        "description",
        "district",
        "location",
    )

    list_editable = (
        "status",
        "is_published",
    )


@admin.register(EmploymentInformation)
class EmploymentInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "information_type",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "information_type",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "content",
        "key_points",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )
