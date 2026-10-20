from django.contrib import admin

from .models import (ElectricityServiceInformation,ElectricityProblemReport,
                     MineralResourceInformation, EnergyServiceInformation,
                    EnergyMineralRequest,
                     EnergyProject,MiningDevelopmentInformation
)

@admin.register(ElectricityServiceInformation)
class ElectricityServiceInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "district",
        "source_organization",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "category",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "district",
        "summary",
        "information",
        "source_organization",
        "contact_phone",
        "contact_email",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(ElectricityProblemReport)
class ElectricityProblemReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "problem_type",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "problem_type",
        "status",
        "district",
        "created_at",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "district",
        "location",
        "description",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(EnergyServiceInformation)
class EnergyServiceInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "district",
        "source_organization",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "category",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "district",
        "summary",
        "information",
        "source_organization",
        "contact_phone",
        "contact_email",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(EnergyProject)
class EnergyProjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "project_type",
        "district",
        "status",
        "implementing_organization",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "project_type",
        "status",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "name",
        "district",
        "location",
        "description",
        "implementing_organization",
        "contractor",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
@admin.register(MineralResourceInformation)
class MineralResourceInformationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "mineral_type",
        "district",
        "source_organization",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "mineral_type",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "name",
        "district",
        "location",
        "description",
        "uses",
        "development_information",
        "source_organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(MiningDevelopmentInformation)
class MiningDevelopmentInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "activity_type",
        "mineral",
        "district",
        "status",
        "responsible_organization",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "activity_type",
        "status",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "mineral",
        "district",
        "location",
        "description",
        "development_information",
        "community_information",
        "environmental_information",
        "responsible_organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(EnergyMineralRequest)
class EnergyMineralRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "request_type",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "request_type",
        "status",
        "district",
        "created_at",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "email",
        "subject",
        "district",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )