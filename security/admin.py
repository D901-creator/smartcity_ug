from django.contrib import admin

from .models import( SecurityIncidentReport,EmergencySafetyInformation,
                    MissingPersonCommunityNotice,  SecurityFacilityContact,SecurityReportRequest,
                    CommunitySafetyProgramme, SecurityAdvisory)


@admin.register(SecurityIncidentReport)
class SecurityIncidentReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "incident_type",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "incident_type",
        "status",
        "district",
        "created_at",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "phone_number",
        "email",
        "district",
        "location",
        "description",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(EmergencySafetyInformation)
class EmergencySafetyInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "district",
        "emergency_number",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "category",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "summary",
        "information",
        "district",
        "emergency_number",
        "contact_name",
        "contact_organization",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(CommunitySafetyProgramme)
class CommunitySafetyProgrammeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "programme_type",
        "district",
        "status",
        "start_date",
        "end_date",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "programme_type",
        "status",
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
        "participating_organization",
    )

    list_editable = (
        "status",
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
@admin.register(SecurityAdvisory)
class SecurityAdvisoryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "advisory_type",
        "district",
        "priority",
        "is_featured",
        "is_published",
        "start_date",
        "end_date",
    )

    list_filter = (
        "advisory_type",
        "priority",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "message",
        "district",
        "location",
        "issuing_organization",
    )

    list_editable = (
        "priority",
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(MissingPersonCommunityNotice)
class MissingPersonCommunityNoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "notice_type",
        "person_name",
        "district",
        "status",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "notice_type",
        "status",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "person_name",
        "summary",
        "description",
        "district",
        "location",
        "last_seen_location",
        "issuing_organization",
    )

    list_editable = (
        "status",
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(SecurityFacilityContact)
class SecurityFacilityContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility_type",
        "district",
        "city",
        "is_emergency_facility",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "facility_type",
        "district",
        "city",
        "is_emergency_facility",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "name",
        "district",
        "city",
        "location",
        "address",
        "phone_number",
        "emergency_number",
        "email",
        "contact_person",
    )

    list_editable = (
        "is_emergency_facility",
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(SecurityReportRequest)
class SecurityReportRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "subject",
        "request_type",
        "citizen_name",
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
        "district",
        "location",
        "subject",
        "description",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )