from django.contrib import admin

from .models import (FinancialPlanningInformation,BusinessRegistrationRequest,EconomicFinancialRecord,
                       TradeMarketInformation,CooperativeRequest,FundingBudgetInformation,
    TradeMarketRequest,CooperativeInformation,EconomicProject,FundingBudgetRequest,
                     
                     BusinessRegistrationInformation)


@admin.register(FinancialPlanningInformation)
class FinancialPlanningInformationAdmin(admin.ModelAdmin):

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
    
@admin.register(BusinessRegistrationInformation)
class BusinessRegistrationInformationAdmin(admin.ModelAdmin):

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
        "requirements",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(BusinessRegistrationRequest)
class BusinessRegistrationRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "business_name",
        "business_type",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "business_type",
        "status",
        "district",
    )

    search_fields = (
        "reference_number",
        "applicant_name",
        "phone_number",
        "email",
        "business_name",
        "district",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
@admin.register(TradeMarketInformation)
class TradeMarketInformationAdmin(admin.ModelAdmin):

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
        "requirements",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(TradeMarketRequest)
class TradeMarketRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "subject",
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
        "district",
        "location",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(CooperativeInformation)
class CooperativeInformationAdmin(admin.ModelAdmin):

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
        "location",
    )


@admin.register(CooperativeRequest)
class CooperativeRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "subject",
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
        "cooperative_name",
        "subject",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
@admin.register(EconomicProject)
class EconomicProjectAdmin(admin.ModelAdmin):

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
        "summary",
        "description",
        "district",
        "location",
        "implementing_organization",
    )
    
@admin.register(FundingBudgetInformation)
class FundingBudgetInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "information_type",
        "organization",
        "district",
        "deadline",
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
        "organization",
        "district",
        "eligibility",
    )


@admin.register(FundingBudgetRequest)
class FundingBudgetRequestAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "subject",
        "citizen_name",
        "district",
        "request_type",
        "requested_amount",
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
        "subject",
        "citizen_name",
        "phone_number",
        "email",
        "district",
    )
    
@admin.register(EconomicFinancialRecord)
class EconomicFinancialRecordAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "financial_type",
        "district",
        "financial_year",
        "allocated_amount",
        "approved_amount",
        "disbursed_amount",
        "spent_amount",
        "status",
    )

    list_filter = (
        "financial_type",
        "status",
        "financial_year",
        "district",
    )

    search_fields = (
        "title",
        "district",
        "organization",
        "project_name",
        "financial_year",
    )