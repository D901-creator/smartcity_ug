from django.contrib import admin

from .models import (
    HealthFacility,
    HealthService,
    MedicineInformation,
    MedicalEquipment,
    HealthRequest,
    HealthFacilityReport,
    HealthProject,
    HealthInformation,
    HealthEmergencyInformation,
)


# ============================================================
# 1. HEALTH FACILITIES
# ============================================================

@admin.register(HealthFacility)
class HealthFacilityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "facility_type",
        "district",
        "telephone",
        "emergency_available",
        "is_published",
    )

    list_filter = (
        "facility_type",
        "emergency_available",
        "is_featured",
        "is_published",
        "district",
    )

    search_fields = (
        "title",
        "district",
        "city",
        "location",
        "telephone",
        "email",
    )

    ordering = ("title",)


# ============================================================
# 2. HEALTH SERVICES
# ============================================================

@admin.register(HealthService)
class HealthServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "service_type",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "service_type",
        "is_featured",
        "is_published",
        "district",
    )

    search_fields = (
        "title",
        "summary",
        "description",
        "district",
    )

    ordering = ("title",)


# ============================================================
# 3. MEDICINE INFORMATION
# ============================================================

@admin.register(MedicineInformation)
class MedicineInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "availability_status",
        "facility",
        "district",
        "last_updated",
        "is_published",
    )

    list_filter = (
        "availability_status",
        "is_published",
        "district",
    )

    search_fields = (
        "title",
        "category",
        "description",
        "district",
        "facility__title",
    )

    ordering = ("title",)


# ============================================================
# 4. MEDICAL EQUIPMENT
# ============================================================

@admin.register(MedicalEquipment)
class MedicalEquipmentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "equipment_type",
        "status",
        "facility",
        "district",
        "is_published",
    )

    list_filter = (
        "status",
        "is_published",
        "district",
    )

    search_fields = (
        "title",
        "equipment_type",
        "description",
        "district",
        "facility__title",
    )

    ordering = ("title",)


# ============================================================
# 5. CITIZEN HEALTH REQUESTS
# ============================================================

@admin.register(HealthRequest)
class HealthRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "request_type",
        "subject",
        "facility",
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
        "citizen_email",
        "citizen_phone",
        "subject",
        "description",
        "district",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# ============================================================
# 6. CITIZEN HOSPITAL / HEALTH FACILITY REPORTS
# ============================================================

@admin.register(HealthFacilityReport)
class HealthFacilityReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "reporter_name",
        "report_type",
        "facility",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "report_type",
        "status",
        "district",
        "created_at",
    )

    search_fields = (
        "reference_number",
        "reporter_name",
        "reporter_email",
        "reporter_phone",
        "subject",
        "description",
        "district",
        "location",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# ============================================================
# 7. HEALTH PROJECTS & PROGRAMMES
# ============================================================

@admin.register(HealthProject)
class HealthProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project_type",
        "district",
        "status",
        "start_date",
        "expected_completion_date",
        "is_featured",
        "is_published",
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
        "summary",
        "description",
        "district",
        "location",
        "implementing_organization",
    )

    ordering = ("-created_at",)


# ============================================================
# 8. HEALTH INFORMATION
# ============================================================

@admin.register(HealthInformation)
class HealthInformationAdmin(admin.ModelAdmin):

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

    ordering = ("-created_at",)


# ============================================================
# 9. EMERGENCY INFORMATION
# ============================================================

@admin.register(HealthEmergencyInformation)
class HealthEmergencyInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "emergency_type",
        "emergency_number",
        "facility",
        "district",
        "is_published",
    )

    list_filter = (
        "emergency_type",
        "district",
        "is_published",
    )

    search_fields = (
        "title",
        "emergency_type",
        "description",
        "emergency_number",
        "district",
        "location",
        "facility__title",
    )

    ordering = ("title",)