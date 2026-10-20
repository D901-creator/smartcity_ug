from django.contrib import admin

from .models import (TourismDestination,TourismService,
    CulturalHeritageSite,TourismEvent,
    WildlifeConservationInformation,
    TourismProjectOpportunity,)


@admin.register(TourismDestination)
class TourismDestinationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "destination_type",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "destination_type",
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
        "attractions",
        "activities",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )
    
@admin.register(TourismService)
class TourismServiceAdmin(admin.ModelAdmin):

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
        "services_offered",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )


@admin.register(CulturalHeritageSite)
class CulturalHeritageSiteAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "site_type",
        "district",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "site_type",
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
        "historical_information",
        "cultural_significance",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )
    
@admin.register(TourismEvent)
class TourismEventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_type",
        "district",
        "start_date",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "event_type",
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
        "organizer",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )


@admin.register(WildlifeConservationInformation)
class WildlifeConservationInformationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "conservation_type",
        "district",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "conservation_type",
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
        "wildlife_information",
        "conservation_actions",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )


@admin.register(TourismProjectOpportunity)
class TourismProjectOpportunityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "opportunity_type",
        "district",
        "status",
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
        "district",
        "location",
        "summary",
        "description",
        "objectives",
        "benefits",
    )

    list_editable = (
        "status",
        "is_featured",
        "is_published",
    )