from django.contrib import admin
from .models import( LandInformation, LandTitleApplication,
                    UrbanPlanningInformation,DevelopmentBuildingApplication, LandHousingPlanningProject,
                    LandHousingPlanningNotice,
                    HousingPropertyRequest,   LandPropertyRequest,HousingInformation
)

@admin.register(LandInformation)
class LandInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "information_type",
        "is_published",
        "updated_at",
    )

    list_filter = (
        "information_type",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "description",
    )


@admin.register(LandTitleApplication)
class LandTitleApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "applicant_name",
        "application_type",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "application_type",
        "status",
        "district",
    )

    search_fields = (
        "reference_number",
        "applicant_name",
        "phone_number",
        "email",
        "land_reference",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(LandPropertyRequest)
class LandPropertyRequestAdmin(admin.ModelAdmin):

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
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "email",
        "subject",
        "property_reference",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(HousingInformation)
class HousingInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "information_type",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "information_type",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "description",
        "district",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(HousingPropertyRequest)
class HousingPropertyRequestAdmin(admin.ModelAdmin):

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
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "email",
        "subject",
        "property_reference",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(UrbanPlanningInformation)
class UrbanPlanningInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "information_type",
        "district",
        "location",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "information_type",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "description",
        "district",
        "location",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(DevelopmentBuildingApplication)
class DevelopmentBuildingApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "applicant_name",
        "application_type",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "application_type",
        "status",
        "district",
    )

    search_fields = (
        "reference_number",
        "applicant_name",
        "phone_number",
        "email",
        "project_title",
        "property_reference",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
@admin.register(LandHousingPlanningProject)
class LandHousingPlanningProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project_type",
        "district",
        "status",
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
        "title",
        "district",
        "location",
        "summary",
        "description",
        "implementing_organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
@admin.register(LandHousingPlanningNotice)
class LandHousingPlanningNoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "notice_type",
        "district",
        "priority",
        "is_featured",
        "is_published",
        "published_at",
    )

    list_filter = (
        "notice_type",
        "priority",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "content",
        "district",
        "location",
        "issuing_organization",
    )

    readonly_fields = (
        "published_at",
        "updated_at",
    )