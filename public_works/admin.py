from django.contrib import admin

from .models import (RoadProblemReport, Road, TrafficRoadSafetyInformation,
                     RoadConstructionMaintenanceProject,  TrafficIncidentReport,ParkingFacility,
    ParkingFee,PublicWorksFacility,
    ParkingPayment,PublicWorksProject,
    ParkingReceipt,  TransportInformationAdvisory,)


@admin.register(RoadProblemReport)
class RoadProblemReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "citizen_name",
        "problem_type",
        "district",
        "road_name",
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
        "road_name",
        "district",
        "location",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
    
@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "road_code",
        "district",
        "road_class",
        "surface_type",
        "condition",
        "length_km",
        "is_operational",
    )

    list_filter = (
        "road_class",
        "surface_type",
        "condition",
        "is_operational",
        "district",
    )

    search_fields = (
        "name",
        "road_code",
        "district",
        "start_location",
        "end_location",
    )
    
@admin.register(RoadConstructionMaintenanceProject)
class RoadConstructionMaintenanceProjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "project_code",
        "district",
        "project_type",
        "status",
        "completion_percentage",
        "start_date",
        "expected_completion_date",
        "implementing_agency",
    )

    list_filter = (
        "project_type",
        "status",
        "district",
    )

    search_fields = (
        "name",
        "project_code",
        "district",
        "location",
        "implementing_agency",
        "contractor",
    )

    readonly_fields = (
        "project_code",
        "created_at",
        "updated_at",
    )
    
@admin.register(TrafficRoadSafetyInformation)
class TrafficRoadSafetyInformationAdmin(admin.ModelAdmin):

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
        "district",
        "summary",
        "content",
        "safety_contact",
        "contact_phone",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
@admin.register(TrafficIncidentReport)
class TrafficIncidentReportAdmin(admin.ModelAdmin):

    list_display = (
        "reference_number",
        "incident_type",
        "citizen_name",
        "district",
        "road_name",
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
        "road_name",
        "location",
    )

    readonly_fields = (
        "reference_number",
        "created_at",
        "updated_at",
    )
@admin.register(ParkingFacility)
class ParkingFacilityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility_code",
        "district",
        "facility_type",
        "total_spaces",
        "available_spaces",
        "status",
    )

    list_filter = (
        "facility_type",
        "status",
        "district",
    )

    search_fields = (
        "name",
        "facility_code",
        "district",
        "location",
    )

    readonly_fields = (
        "facility_code",
        "created_at",
        "updated_at",
    )
    
@admin.register(ParkingFee)
class ParkingFeeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility",
        "fee_type",
        "amount",
        "tax_amount",
        "is_active",
    )

    list_filter = (
        "fee_type",
        "is_active",
        "facility",
    )

    search_fields = (
        "name",
        "facility__name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
@admin.register(ParkingPayment)
class ParkingPaymentAdmin(admin.ModelAdmin):

    list_display = (
        "payment_reference",
        "citizen_name",
        "vehicle_registration",
        "facility",
        "total_amount",
        "payment_method",
        "status",
        "created_at",
    )

    list_filter = (
        "payment_method",
        "status",
        "facility",
    )

    search_fields = (
        "payment_reference",
        "citizen_name",
        "phone_number",
        "vehicle_registration",
        "transaction_reference",
    )

    readonly_fields = (
        "payment_reference",
        "total_amount",
        "created_at",
        "updated_at",
    )
    
@admin.register(ParkingReceipt)
class ParkingReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "receipt_number",
        "issued_to",
        "vehicle_registration",
        "facility_name",
        "amount_paid",
        "payment_method",
        "issued_at",
    )

    search_fields = (
        "receipt_number",
        "issued_to",
        "vehicle_registration",
        "facility_name",
    )

    readonly_fields = (
        "receipt_number",
        "issued_at",
    )
@admin.register(PublicWorksFacility)
class PublicWorksFacilityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "facility_code",
        "district",
        "facility_type",
        "status",
        "contact_phone",
        "operating_hours",
    )

    list_filter = (
        "facility_type",
        "status",
        "district",
    )

    search_fields = (
        "name",
        "facility_code",
        "district",
        "location",
        "contact_phone",
    )

    readonly_fields = (
        "facility_code",
        "created_at",
        "updated_at",
    )
    
@admin.register(TransportInformationAdvisory)
class TransportInformationAdvisoryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "advisory_code",
        "category",
        "priority",
        "district",
        "status",
        "published_at",
        "expires_at",
    )

    list_filter = (
        "category",
        "priority",
        "status",
        "district",
    )

    search_fields = (
        "title",
        "advisory_code",
        "district",
        "affected_location",
        "summary",
        "information",
        "source_organization",
    )

    readonly_fields = (
        "advisory_code",
        "created_at",
        "updated_at",
    )
    
@admin.register(PublicWorksProject)
class PublicWorksProjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "project_code",
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
        "name",
        "project_code",
        "district",
        "location",
        "implementing_agency",
        "contractor",
    )

    readonly_fields = (
        "project_code",
        "created_at",
        "updated_at",
    )