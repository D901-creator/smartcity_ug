from django.db import models
from django.conf import settings


class FarmerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="farmer_profile",
        null=True,
        blank=True,
    )

    farmer_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    district = models.CharField(max_length=100)
    subcounty = models.CharField(max_length=100, blank=True)
    village = models.CharField(max_length=100, blank=True)

    farmer_type = models.CharField(
        max_length=50,
        choices=[
            ("smallholder", "Smallholder Farmer"),
            ("commercial", "Commercial Farmer"),
            ("cooperative", "Cooperative Farmer"),
            ("youth", "Youth Farmer"),
            ("women", "Women Farmer"),
        ],
        default="smallholder",
    )

    farm_size_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    crops = models.TextField(
        blank=True,
        help_text="Main crops produced by the farmer"
    )

    livestock = models.TextField(
        blank=True,
        help_text="Main livestock kept by the farmer"
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.farmer_name


class Farm(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="farms"
    )

    farm_name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)

    size_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    soil_type = models.CharField(max_length=100, blank=True)

    irrigation_available = models.BooleanField(default=False)

    ownership_type = models.CharField(
        max_length=50,
        choices=[
            ("owned", "Owned"),
            ("leased", "Leased"),
            ("family", "Family Land"),
            ("community", "Community Land"),
        ],
        default="owned",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.farm_name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    growing_period_days = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CropProduction(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="crop_productions"
    )

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="crop_productions"
    )

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="productions"
    )

    season = models.CharField(max_length=100)

    planting_date = models.DateField(
        null=True,
        blank=True
    )

    expected_harvest_date = models.DateField(
        null=True,
        blank=True
    )

    expected_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    actual_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    unit = models.CharField(
        max_length=30,
        default="kg"
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("planned", "Planned"),
            ("growing", "Growing"),
            ("harvested", "Harvested"),
            ("sold", "Sold"),
        ],
        default="planned",
    )

    def __str__(self):
        return f"{self.farmer} - {self.crop}"


class LivestockRecord(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="livestock_records"
    )

    livestock_type = models.CharField(max_length=100)

    breed = models.CharField(
        max_length=100,
        blank=True
    )

    number_of_animals = models.PositiveIntegerField(
        default=0
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    health_status = models.CharField(
        max_length=100,
        default="Healthy"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.livestock_type} - {self.farmer}"


class MarketListing(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="market_listings"
    )

    product_name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=100,
        blank=True
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=30,
        default="kg"
    )

    price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    district = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("available", "Available"),
            ("reserved", "Reserved"),
            ("sold", "Sold"),
        ],
        default="available",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product_name


class BuyerRequest(models.Model):
    buyer_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    product_required = models.CharField(
        max_length=200
    )

    quantity_required = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=30,
        default="kg"
    )

    district = models.CharField(
        max_length=100
    )

    maximum_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("open", "Open"),
            ("matched", "Matched"),
            ("completed", "Completed"),
        ],
        default="open",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product_required


class AgriculturalInput(models.Model):
    name = models.CharField(
        max_length=200
    )

    input_type = models.CharField(
        max_length=100,
        choices=[
            ("seed", "Seeds"),
            ("fertilizer", "Fertilizer"),
            ("pesticide", "Pesticide"),
            ("feed", "Animal Feed"),
            ("equipment", "Equipment"),
            ("machinery", "Machinery"),
            ("other", "Other"),
        ]
    )

    supplier = models.CharField(
        max_length=200,
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class ExtensionService(models.Model):
    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    officer_name = models.CharField(
        max_length=200,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    service_type = models.CharField(
        max_length=100,
        choices=[
            ("training", "Farmer Training"),
            ("field_visit", "Field Visit"),
            ("consultation", "Consultation"),
            ("demonstration", "Demonstration Farm"),
            ("advisory", "Agricultural Advisory"),
        ]
    )

    scheduled_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class AgriculturalProject(models.Model):
    name = models.CharField(
        max_length=250
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100
    )

    implementing_organization = models.CharField(
        max_length=250
    )

    target_beneficiaries = models.PositiveIntegerField(
        default=0
    )

    budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    end_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("planned", "Planned"),
            ("active", "Active"),
            ("completed", "Completed"),
        ],
        default="planned",
    )

    def __str__(self):
        return self.name


class AgriculturalProgram(models.Model):
    name = models.CharField(
        max_length=250
    )

    description = models.TextField()

    target_group = models.CharField(
        max_length=200
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    application_open = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class DiseaseReport(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="disease_reports"
    )

    crop_or_animal = models.CharField(
        max_length=200
    )

    symptoms = models.TextField()

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    urgency = models.CharField(
        max_length=30,
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
            ("emergency", "Emergency"),
        ],
        default="medium",
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("reported", "Reported"),
            ("assigned", "Assigned"),
            ("investigating", "Investigating"),
            ("resolved", "Resolved"),
        ],
        default="reported",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.crop_or_animal


class IrrigationProject(models.Model):
    name = models.CharField(
        max_length=200
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200
    )

    beneficiaries = models.PositiveIntegerField(
        default=0
    )

    hectares_supported = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("planned", "Planned"),
            ("construction", "Under Construction"),
            ("operational", "Operational"),
            ("maintenance", "Maintenance"),
        ],
        default="planned",
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name


class Cooperative(models.Model):
    name = models.CharField(
        max_length=250
    )

    registration_number = models.CharField(
        max_length=100,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    main_activity = models.CharField(
        max_length=200
    )

    member_count = models.PositiveIntegerField(
        default=0
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name 
    
    
class MarketMatch(models.Model):
    STATUS_NEW = "new"
    STATUS_CONTACTED = "contacted"
    STATUS_ACCEPTED = "accepted"
    STATUS_REJECTED = "rejected"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_CONTACTED, "Contacted"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_COMPLETED, "Completed"),
    ]

    buyer_request = models.ForeignKey(
        BuyerRequest,
        on_delete=models.CASCADE,
        related_name="matches"
    )

    market_listing = models.ForeignKey(
        MarketListing,
        on_delete=models.CASCADE,
        related_name="matches"
    )

    match_score = models.PositiveIntegerField(default=0)

    matched_product = models.BooleanField(default=False)
    matched_quantity = models.BooleanField(default=False)
    matched_district = models.BooleanField(default=False)
    matched_price = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )

    buyer_message = models.TextField(
        blank=True,
        help_text="Message from the buyer to the farmer."
    )

    farmer_message = models.TextField(
        blank=True,
        help_text="Message from the farmer to the buyer."
    )

    agreed_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    agreed_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    transaction_notes = models.TextField(
        blank=True
    )

    contacted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    accepted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

class Meta:
    ordering = ["-match_score", "-created_at"]

    constraints = [
        models.UniqueConstraint(
            fields=["buyer_request", "market_listing"],
            name="unique_buyer_listing_match"
        )
    ]

    def __str__(self):
        return (
            f"{self.buyer_request.product_required} → "
            f"{self.market_listing.product_name}"
        )
        
        # ============================================================
# PHASE 3 — FISHING & FISHERIES
# ============================================================

class Fisher(models.Model):

    FISHER_TYPES = [
        ("individual", "Individual Fisher"),
        ("group", "Fishing Group"),
        ("cooperative", "Fishing Cooperative"),
        ("commercial", "Commercial Fisher"),
    ]

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30, blank=True)
    fisher_type = models.CharField(
        max_length=30,
        choices=FISHER_TYPES,
        default="individual"
    )

    district = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)

    fishing_community = models.CharField(
        max_length=200,
        blank=True
    )

    registration_number = models.CharField(
        max_length=100,
        unique=True
    )

    number_of_boats = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.registration_number})"


class FishingActivity(models.Model):

    FISHING_METHODS = [
        ("boat", "Boat Fishing"),
        ("shore", "Shore Fishing"),
        ("net", "Net Fishing"),
        ("hook", "Hook and Line"),
        ("other", "Other"),
    ]

    fisher = models.ForeignKey(
        Fisher,
        on_delete=models.CASCADE,
        related_name="fishing_activities"
    )

    water_body = models.CharField(max_length=200)

    fishing_area = models.CharField(
        max_length=200,
        blank=True
    )

    fishing_method = models.CharField(
        max_length=30,
        choices=FISHING_METHODS
    )

    fishing_date = models.DateField()

    species = models.CharField(
        max_length=200,
        blank=True
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    unit = models.CharField(
        max_length=50,
        default="kg"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fishing_date"]

    def __str__(self):
        return (
            f"{self.water_body} - "
            f"{self.fishing_date}"
        )


class AquacultureFarm(models.Model):

    FARM_TYPES = [
        ("pond", "Fish Pond"),
        ("cage", "Cage Farming"),
        ("tank", "Tank Farming"),
        ("other", "Other"),
    ]

    owner_name = models.CharField(max_length=200)

    phone_number = models.CharField(
        max_length=30,
        blank=True
    )

    farm_name = models.CharField(
        max_length=200
    )

    farm_type = models.CharField(
        max_length=30,
        choices=FARM_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    number_of_units = models.PositiveIntegerField(
        default=1
    )

    fish_species = models.CharField(
        max_length=200,
        blank=True
    )

    production_capacity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    capacity_unit = models.CharField(
        max_length=50,
        default="kg"
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["farm_name"]

    def __str__(self):
        return self.farm_name


class FishProcessingFacility(models.Model):

    FACILITY_TYPES = [
        ("processing", "Fish Processing Facility"),
        ("drying", "Fish Drying Facility"),
        ("smoking", "Fish Smoking Facility"),
        ("cold_storage", "Cold Storage"),
        ("other", "Other"),
    ]

    name = models.CharField(
        max_length=200
    )

    facility_type = models.CharField(
        max_length=40,
        choices=FACILITY_TYPES
    )

    owner_or_organization = models.CharField(
        max_length=250,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True
    )

    processing_capacity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    capacity_unit = models.CharField(
        max_length=50,
        default="kg"
    )

    services = models.TextField(
        blank=True,
        help_text="List the processing or value-addition services."
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class FishMarketListing(models.Model):

    LISTING_STATUS = [
        ("available", "Available"),
        ("sold", "Sold"),
        ("reserved", "Reserved"),
        ("inactive", "Inactive"),
    ]

    seller_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True
    )

    fish_species = models.CharField(
        max_length=150
    )

    product_description = models.TextField(
        blank=True
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=50,
        default="kg"
    )

    price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=LISTING_STATUS,
        default="available"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.fish_species} - "
            f"{self.quantity} {self.unit}"
        )