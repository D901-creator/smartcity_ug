from django.contrib import admin

from .models import (WaterFacility, WaterProblemReport,SanitationProblemReport,
                     WaterProject, EnvironmentalFacility, EnvironmentalProject,
                     WasteManagementService,PollutionReport, TreeForestSite,
                      WetlandNaturalResource, ClimateEnvironmentalInformation,
                      EnvironmentalIncidentReport

)


@admin.register(WaterFacility)
class WaterFacilityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility_type",
        "district",
        "location",
        "is_operational",
    )

    list_filter = (
        "facility_type",
        "district",
        "is_operational",
    )

    search_fields = (
        "name",
        "district",
        "location",
    )


@admin.register(WaterProblemReport)
class WaterProblemReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "problem_type",
        "district",
        "urgency",
        "status",
        "created_at",
    )

    list_filter = (
        "problem_type",
        "urgency",
        "status",
        "district",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "district",
        "location",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
@admin.register(SanitationProblemReport)
class SanitationProblemReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "problem_type",
        "district",
        "urgency",
        "status",
        "created_at",
    )

    list_filter = (
        "problem_type",
        "urgency",
        "status",
        "district",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "district",
        "location",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
@admin.register(WaterProject)
class WaterProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_code",
        "name",
        "district",
        "status",
        "completion_percentage",
        "start_date",
        "expected_completion_date",
    )

    list_filter = (
        "status",
        "district",
    )

    search_fields = (
        "project_code",
        "name",
        "district",
        "location",
        "implementing_agency",
    )

    readonly_fields = (
        "project_code",
        "created_at",
        "updated_at",
    )
    
@admin.register(EnvironmentalFacility)
class EnvironmentalFacilityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility_type",
        "district",
        "location",
        "is_operational",
    )

    list_filter = (
        "facility_type",
        "district",
        "is_operational",
    )

    search_fields = (
        "name",
        "district",
        "location",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(WasteManagementService)
class WasteManagementServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "service_type",
        "district",
        "service_area",
        "collection_frequency",
        "is_operational",
    )

    list_filter = (
        "service_type",
        "collection_frequency",
        "district",
        "is_operational",
    )

    search_fields = (
        "name",
        "district",
        "service_area",
        "description",
        "contact_phone",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(PollutionReport)
class PollutionReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "pollution_type",
        "district",
        "urgency",
        "status",
        "created_at",
    )

    list_filter = (
        "pollution_type",
        "urgency",
        "status",
        "district",
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
    
@admin.register(TreeForestSite)
class TreeForestSiteAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "site_type",
        "district",
        "location",
        "is_operational",
    )

    list_filter = (
        "site_type",
        "district",
        "is_operational",
    )

    search_fields = (
        "name",
        "district",
        "location",
        "tree_species",
        "description",
        "planting_information",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(EnvironmentalProject)
class EnvironmentalProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_code",
        "name",
        "project_type",
        "district",
        "status",
        "completion_percentage",
        "start_date",
        "expected_completion_date",
    )

    list_filter = (
        "project_type",
        "status",
        "district",
    )

    search_fields = (
        "project_code",
        "name",
        "district",
        "location",
        "description",
        "implementing_agency",
    )

    readonly_fields = (
        "project_code",
        "created_at",
        "updated_at",
    )
    
@admin.register(WetlandNaturalResource)
class WetlandNaturalResourceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "resource_type",
        "district",
        "location",
        "is_protected",
        "is_active",
    )

    list_filter = (
        "resource_type",
        "district",
        "is_protected",
        "is_active",
    )

    search_fields = (
        "name",
        "district",
        "location",
        "description",
    )
    
@admin.register(ClimateEnvironmentalInformation)
class ClimateEnvironmentalInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "district",
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
        "summary",
        "content",
        "district",
        "source_organization",
    )
@admin.register(EnvironmentalIncidentReport)
class EnvironmentalIncidentReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "incident_type",
        "district",
        "urgency",
        "status",
        "created_at",
    )

    list_filter = (
        "incident_type",
        "urgency",
        "status",
        "district",
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