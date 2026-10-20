from django.contrib import admin

from .models import (
    EducationInstitution,
    EducationRequest,
    EducationProgramme,
    ScholarshipOpportunity,
    TeacherService,
    AdministratorService,
    EducationFunding,
    ExaminationInformation,
    EducationService,
    GovernmentEducationProgramme,
    EducationApplication,
    EducationProject,
    EducationNotice,
    EducationProblemReport,
    EducationInformation,
    EducationStatistic,
    LearningResource,
)


# ============================================================
# 1. EDUCATION INSTITUTIONS
# ============================================================

@admin.register(EducationInstitution)
class EducationInstitutionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "institution_type",
        "ownership",
        "district",
        "location",
        "phone_number",
        "is_active",
        "created_at",
    )

    list_filter = (
        "institution_type",
        "ownership",
        "district",
        "is_active",
    )

    search_fields = (
        "name",
        "district",
        "location",
        "phone_number",
        "email",
        "programs",
    )

    ordering = ("name",)


# ============================================================
# 2. EDUCATION REQUESTS
# ============================================================

@admin.register(EducationRequest)
class EducationRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "request_type",
        "institution",
        "citizen_district",
        "status",
        "submitted_at",
    )

    list_filter = (
        "request_type",
        "status",
        "citizen_district",
        "submitted_at",
    )

    search_fields = (
        "reference_number",
        "citizen_name",
        "citizen_phone",
        "citizen_district",
        "description",
    )

    readonly_fields = (
        "submitted_at",
        "updated_at",
    )

    ordering = ("-submitted_at",)


# ============================================================
# 3. EDUCATION PROGRAMMES & COURSES
# ============================================================

@admin.register(EducationProgramme)
class EducationProgrammeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "programme_type",
        "institution",
        "district",
        "start_date",
        "closing_date",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "programme_type",
        "district",
        "is_featured",
        "is_published",
        "start_date",
        "closing_date",
    )

    search_fields = (
        "title",
        "description",
        "requirements",
        "institution__name",
        "district",
    )

    ordering = ("title",)


# ============================================================
# 4. SCHOLARSHIPS & BURSARIES
# ============================================================

@admin.register(ScholarshipOpportunity)
class ScholarshipOpportunityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "opportunity_type",
        "provider",
        "target_group",
        "district",
        "status",
        "opening_date",
        "closing_date",
        "is_featured",
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
        "provider",
        "description",
        "target_group",
        "district",
    )

    ordering = ("-created_at",)


# ============================================================
# 5. TEACHERS' SERVICES
# ============================================================

@admin.register(TeacherService)
class TeacherServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "service_type",
        "provider",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "service_type",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "provider",
        "district",
        "contact_information",
    )

    ordering = ("title",)


# ============================================================
# 6. SCHOOL ADMINISTRATORS' SERVICES
# ============================================================

@admin.register(AdministratorService)
class AdministratorServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "service_type",
        "provider",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "service_type",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "provider",
        "district",
        "contact_information",
    )

    ordering = ("title",)


# ============================================================
# 7. EDUCATION FUNDING
# ============================================================

@admin.register(EducationFunding)
class EducationFundingAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "funding_type",
        "provider",
        "target_group",
        "district",
        "status",
        "opening_date",
        "closing_date",
        "is_published",
    )

    list_filter = (
        "funding_type",
        "status",
        "district",
        "is_published",
    )

    search_fields = (
        "title",
        "provider",
        "description",
        "target_group",
        "district",
    )

    ordering = ("-created_at",)


# ============================================================
# 8. EXAMINATIONS & ACADEMIC INFORMATION
# ============================================================

@admin.register(ExaminationInformation)
class ExaminationInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "information_type",
        "district",
        "published_date",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "information_type",
        "district",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "requirements",
        "district",
    )

    ordering = ("-created_at",)


# ============================================================
# 9. EDUCATION SERVICES & REQUIREMENTS
# ============================================================

@admin.register(EducationService)
class EducationServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "service_type",
        "is_published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "service_type",
        "is_published",
    )

    search_fields = (
        "title",
        "summary",
        "description",
        "requirements",
        "eligibility",
    )

    ordering = ("title",)


# ============================================================
# 10. GOVERNMENT EDUCATION PROGRAMMES
# ============================================================

@admin.register(GovernmentEducationProgramme)
class GovernmentEducationProgrammeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "programme_type",
        "implementing_organization",
        "district",
        "status",
        "start_date",
        "closing_date",
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
        "description",
        "objectives",
        "implementing_organization",
        "district",
    )

    ordering = ("-created_at",)


# ============================================================
# 11. EDUCATION REGISTRATION & APPLICATIONS
# ============================================================

@admin.register(EducationApplication)
class EducationApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "applicant_name",
        "application_type",
        "institution",
        "programme",
        "status",
        "submitted_at",
    )

    list_filter = (
        "application_type",
        "status",
        "applicant_district",
        "submitted_at",
    )

    search_fields = (
        "reference_number",
        "applicant_name",
        "applicant_phone",
        "applicant_email",
        "applicant_district",
        "subject",
        "description",
    )

    readonly_fields = (
        "submitted_at",
        "updated_at",
    )

    ordering = ("-submitted_at",)


# ============================================================
# 12. EDUCATION PROJECTS & INFRASTRUCTURE
# ============================================================

@admin.register(EducationProject)
class EducationProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project_type",
        "implementing_organization",
        "district",
        "location",
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
        "description",
        "objectives",
        "implementing_organization",
        "district",
        "location",
    )

    ordering = ("-created_at",)


# ============================================================
# 13. EDUCATION UPDATES & NOTICES
# ============================================================

@admin.register(EducationNotice)
class EducationNoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "notice_type",
        "district",
        "important_date",
        "published_date",
        "is_important",
        "is_published",
    )

    list_filter = (
        "notice_type",
        "district",
        "is_important",
        "is_published",
        "published_date",
    )

    search_fields = (
        "title",
        "summary",
        "content",
        "district",
    )

    ordering = ("-created_at",)


# ============================================================
# 14. EDUCATION PROBLEM REPORTS
# ============================================================

@admin.register(EducationProblemReport)
class EducationProblemReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "reporter_name",
        "report_type",
        "institution",
        "district",
        "status",
        "submitted_at",
    )

    list_filter = (
        "report_type",
        "status",
        "district",
        "submitted_at",
    )

    search_fields = (
        "reference_number",
        "reporter_name",
        "reporter_phone",
        "reporter_email",
        "subject",
        "description",
        "district",
        "institution__name",
    )

    readonly_fields = (
        "submitted_at",
        "updated_at",
    )

    ordering = ("-submitted_at",)


# ============================================================
# 15. EDUCATION INFORMATION & GUIDANCE
# ============================================================

@admin.register(EducationInformation)
class EducationInformationAdmin(admin.ModelAdmin):

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
        "key_points",
        "district",
    )

    ordering = ("-created_at",)


# ============================================================
# 16. EDUCATION STATISTICS & REPORTS
# ============================================================

@admin.register(EducationStatistic)
class EducationStatisticAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "statistic_type",
        "value",
        "unit",
        "district",
        "year",
        "source",
        "is_published",
    )

    list_filter = (
        "statistic_type",
        "district",
        "year",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "district",
        "source",
    )

    ordering = (
        "-year",
        "title",
    )
    
@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "education_level",
        "class_level",
        "subject",
        "resource_type",
        "source_organization",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "education_level",
        "resource_type",
        "access_type",
        "language",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "subject",
        "topic",
        "description",
        "source_organization",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "education_level",
                    "class_level",
                    "subject",
                    "topic",
                    "resource_type",
                )
            },
        ),

        (
            "Learning Content",
            {
                "fields": (
                    "description",
                    "learning_objectives",
                )
            },
        ),

        (
            "Access Information",
            {
                "fields": (
                    "access_type",
                    "resource_url",
                    "download_file",
                    "access_instructions",
                )
            },
        ),

        (
            "Source Information",
            {
                "fields": (
                    "source_organization",
                    "language",
                    "publication_year",
                )
            },
        ),

        (
            "Presentation",
            {
                "fields": (
                    "thumbnail",
                    "is_featured",
                    "is_published",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )