from django.contrib import admin

from .models import (
    FarmerProfile,
    Farm,
    Crop,
    CropProduction,
    LivestockRecord,
    MarketListing,
    BuyerRequest,
    MarketMatch,
    AgriculturalInput,
    ExtensionService,
    AgriculturalProject,
    AgriculturalProgram,
    DiseaseReport,
    IrrigationProject,
    Cooperative,
    Fisher,
FishingActivity,
AquacultureFarm,
FishProcessingFacility,
FishMarketListing,
)

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "farmer_name",
        "phone_number",
        "district",
        "farmer_type",
        "farm_size_acres",
        "is_verified",
    )
    list_filter = ("farmer_type", "district", "is_verified")
    search_fields = ("farmer_name", "phone_number", "district")


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = (
        "farm_name",
        "farmer",
        "district",
        "size_acres",
        "irrigation_available",
    )
    list_filter = ("district", "irrigation_available")
    search_fields = ("farm_name", "district")


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "growing_period_days",
        "is_active",
    )
    list_filter = ("category", "is_active")
    search_fields = ("name", "category")


@admin.register(CropProduction)
class CropProductionAdmin(admin.ModelAdmin):
    list_display = (
        "farmer",
        "crop",
        "season",
        "expected_quantity",
        "actual_quantity",
        "status",
    )
    list_filter = ("season", "status", "crop")


@admin.register(LivestockRecord)
class LivestockRecordAdmin(admin.ModelAdmin):
    list_display = (
        "farmer",
        "livestock_type",
        "breed",
        "number_of_animals",
        "health_status",
    )
    list_filter = ("livestock_type", "health_status")


@admin.register(MarketListing)
class MarketListingAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "farmer",
        "quantity",
        "price_per_unit",
        "district",
        "status",
    )
    list_filter = ("category", "district", "status")
    search_fields = ("product_name", "district")


@admin.register(BuyerRequest)
class BuyerRequestAdmin(admin.ModelAdmin):
    list_display = (
        "buyer_name",
        "product_required",
        "quantity_required",
        "district",
        "status",
    )
    list_filter = ("district", "status")
    search_fields = ("buyer_name", "product_required")


@admin.register(AgriculturalInput)
class AgriculturalInputAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "input_type",
        "supplier",
        "district",
        "price",
        "is_available",
    )
    list_filter = ("input_type", "district", "is_available")
    search_fields = ("name", "supplier")


@admin.register(ExtensionService)
class ExtensionServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "district",
        "service_type",
        "scheduled_date",
    )
    list_filter = ("district", "service_type")


@admin.register(AgriculturalProject)
class AgriculturalProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
        "implementing_organization",
        "target_beneficiaries",
        "status",
    )
    list_filter = ("district", "status")
    search_fields = ("name", "implementing_organization")


@admin.register(AgriculturalProgram)
class AgriculturalProgramAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "target_group",
        "district",
        "application_open",
    )
    list_filter = ("district", "application_open")
    search_fields = ("name", "target_group")


@admin.register(DiseaseReport)
class DiseaseReportAdmin(admin.ModelAdmin):
    list_display = (
        "farmer",
        "crop_or_animal",
        "district",
        "urgency",
        "status",
        "created_at",
    )
    list_filter = ("district", "urgency", "status")


@admin.register(IrrigationProject)
class IrrigationProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
        "beneficiaries",
        "hectares_supported",
        "status",
    )
    list_filter = ("district", "status")


@admin.register(Cooperative)
class CooperativeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
        "main_activity",
        "member_count",
    )
    list_filter = ("district",)
    search_fields = ("name", "district")
@admin.register(MarketMatch)
class MarketMatchAdmin(admin.ModelAdmin):
    list_display = (
        "buyer_request",
        "market_listing",
        "match_score",
        "matched_product",
        "matched_quantity",
        "matched_district",
        "matched_price",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "matched_product",
        "matched_quantity",
        "matched_district",
        "matched_price",
    )

    search_fields = (
        "buyer_request__product_required",
        "market_listing__product_name",
        "market_listing__farmer__farmer_name",
    )
    # ============================================================
# PHASE 3 — FISHING & FISHERIES ADMIN
# ============================================================


@admin.register(Fisher)
class FisherAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "fisher_type",
        "district",
        "registration_number",
        "number_of_boats",
        "active",
        "created_at",
    )

    list_filter = (
        "fisher_type",
        "district",
        "active",
    )

    search_fields = (
        "name",
        "phone_number",
        "registration_number",
        "district",
        "location",
        "fishing_community",
    )


@admin.register(FishingActivity)
class FishingActivityAdmin(admin.ModelAdmin):

    list_display = (
        "fisher",
        "water_body",
        "fishing_area",
        "fishing_method",
        "fishing_date",
        "species",
        "quantity",
        "unit",
    )

    list_filter = (
        "fishing_method",
        "water_body",
        "fishing_date",
    )

    search_fields = (
        "fisher__name",
        "water_body",
        "fishing_area",
        "species",
    )


@admin.register(AquacultureFarm)
class AquacultureFarmAdmin(admin.ModelAdmin):

    list_display = (
        "farm_name",
        "owner_name",
        "farm_type",
        "district",
        "fish_species",
        "production_capacity",
        "capacity_unit",
        "active",
    )

    list_filter = (
        "farm_type",
        "district",
        "active",
    )

    search_fields = (
        "farm_name",
        "owner_name",
        "phone_number",
        "district",
        "location",
        "fish_species",
    )


@admin.register(FishProcessingFacility)
class FishProcessingFacilityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility_type",
        "owner_or_organization",
        "district",
        "processing_capacity",
        "capacity_unit",
        "active",
    )

    list_filter = (
        "facility_type",
        "district",
        "active",
    )

    search_fields = (
        "name",
        "owner_or_organization",
        "district",
        "location",
        "phone_number",
    )


@admin.register(FishMarketListing)
class FishMarketListingAdmin(admin.ModelAdmin):

    list_display = (
        "fish_species",
        "seller_name",
        "quantity",
        "unit",
        "price_per_unit",
        "district",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "fish_species",
        "district",
    )

    search_fields = (
        "seller_name",
        "phone_number",
        "fish_species",
        "product_description",
        "district",
        "location",
    )