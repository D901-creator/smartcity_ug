from django.db import models


class WaterFacility(models.Model):
    FACILITY_WATER_POINT = "water_point"
    FACILITY_BOREHOLE = "borehole"
    FACILITY_WELL = "well"
    FACILITY_TANK = "water_tank"
    FACILITY_TREATMENT = "treatment_plant"
    FACILITY_OTHER = "other"

    FACILITY_TYPES = [
        (FACILITY_WATER_POINT, "Water Point"),
        (FACILITY_BOREHOLE, "Borehole"),
        (FACILITY_WELL, "Well"),
        (FACILITY_TANK, "Water Tank"),
        (FACILITY_TREATMENT, "Water Treatment Plant"),
        (FACILITY_OTHER, "Other"),
    ]

    name = models.CharField(max_length=200)

    facility_type = models.CharField(
        max_length=30,
        choices=FACILITY_TYPES
    )

    district = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_operational = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["district", "name"]

    def __str__(self):
        return f"{self.name} - {self.district}"
class WaterProblemReport(models.Model):

    PROBLEM_NO_WATER = "no_water"
    PROBLEM_BROKEN_POINT = "broken_water_point"
    PROBLEM_BROKEN_BOREHOLE = "broken_borehole"
    PROBLEM_LEAKING_PIPE = "leaking_pipe"
    PROBLEM_CONTAMINATED = "contaminated_water"
    PROBLEM_LOW_PRESSURE = "low_pressure"
    PROBLEM_DAMAGED_INFRASTRUCTURE = "damaged_infrastructure"
    PROBLEM_OTHER = "other"

    PROBLEM_TYPES = [
        (PROBLEM_NO_WATER, "No Water Supply"),
        (PROBLEM_BROKEN_POINT, "Broken Water Point"),
        (PROBLEM_BROKEN_BOREHOLE, "Broken Borehole"),
        (PROBLEM_LEAKING_PIPE, "Leaking Water Pipe"),
        (PROBLEM_CONTAMINATED, "Contaminated Water"),
        (PROBLEM_LOW_PRESSURE, "Low Water Pressure"),
        (
            PROBLEM_DAMAGED_INFRASTRUCTURE,
            "Damaged Water Infrastructure"
        ),
        (PROBLEM_OTHER, "Other"),
    ]

    URGENCY_LOW = "low"
    URGENCY_MEDIUM = "medium"
    URGENCY_HIGH = "high"
    URGENCY_EMERGENCY = "emergency"

    URGENCY_CHOICES = [
        (URGENCY_LOW, "Low"),
        (URGENCY_MEDIUM, "Medium"),
        (URGENCY_HIGH, "High"),
        (URGENCY_EMERGENCY, "Emergency"),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_INVESTIGATING = "investigating"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    problem_type = models.CharField(
        max_length=40,
        choices=PROBLEM_TYPES
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="water_problem_reports/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"WTR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_problem_type_display()}"
        )
        
class SanitationProblemReport(models.Model):
    PROBLEM_BLOCKED_DRAINAGE = "blocked_drainage"
    PROBLEM_SEWAGE_OVERFLOW = "sewage_overflow"
    PROBLEM_BROKEN_PUBLIC_TOILET = "broken_public_toilet"
    PROBLEM_POOR_SANITATION = "poor_sanitation"
    PROBLEM_SOLID_WASTE = "solid_waste"
    PROBLEM_OPEN_DEFECATION = "open_defecation"
    PROBLEM_CONTAMINATED_AREA = "contaminated_area"
    PROBLEM_BROKEN_SEWER = "broken_sewer"
    PROBLEM_OTHER = "other"

    PROBLEM_TYPES = [
        (PROBLEM_BLOCKED_DRAINAGE, "Blocked Drainage"),
        (PROBLEM_SEWAGE_OVERFLOW, "Sewage Overflow"),
        (PROBLEM_BROKEN_PUBLIC_TOILET, "Broken Public Toilet"),
        (PROBLEM_POOR_SANITATION, "Poor Sanitation"),
        (PROBLEM_SOLID_WASTE, "Solid Waste / Garbage Problem"),
        (PROBLEM_OPEN_DEFECATION, "Open Defecation"),
        (PROBLEM_CONTAMINATED_AREA, "Contaminated Sanitation Area"),
        (PROBLEM_BROKEN_SEWER, "Broken Sewer Line"),
        (PROBLEM_OTHER, "Other"),
    ]

    URGENCY_LOW = "low"
    URGENCY_MEDIUM = "medium"
    URGENCY_HIGH = "high"
    URGENCY_EMERGENCY = "emergency"

    URGENCY_CHOICES = [
        (URGENCY_LOW, "Low"),
        (URGENCY_MEDIUM, "Medium"),
        (URGENCY_HIGH, "High"),
        (URGENCY_EMERGENCY, "Emergency"),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_INVESTIGATING = "investigating"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(max_length=200)

    phone_number = models.CharField(max_length=30)

    problem_type = models.CharField(
        max_length=40,
        choices=PROBLEM_TYPES
    )

    description = models.TextField()

    district = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="sanitation_problem_reports/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"SAN-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_problem_type_display()}"
        )
        
class EnvironmentalProblemReport(models.Model):

    PROBLEM_ILLEGAL_DUMPING = "illegal_dumping"
    PROBLEM_POLLUTION = "pollution"
    PROBLEM_DEFORESTATION = "deforestation"
    PROBLEM_WETLAND_DESTRUCTION = "wetland_destruction"
    PROBLEM_BUSH_BURNING = "bush_burning"
    PROBLEM_LAND_DEGRADATION = "land_degradation"
    PROBLEM_AIR_POLLUTION = "air_pollution"
    PROBLEM_WATER_POLLUTION = "water_pollution"
    PROBLEM_OTHER = "other"

    PROBLEM_TYPES = [
        (
            PROBLEM_ILLEGAL_DUMPING,
            "Illegal Dumping / Waste Disposal"
        ),
        (
            PROBLEM_POLLUTION,
            "Environmental Pollution"
        ),
        (
            PROBLEM_DEFORESTATION,
            "Deforestation"
        ),
        (
            PROBLEM_WETLAND_DESTRUCTION,
            "Wetland Destruction"
        ),
        (
            PROBLEM_BUSH_BURNING,
            "Bush Burning"
        ),
        (
            PROBLEM_LAND_DEGRADATION,
            "Land Degradation"
        ),
        (
            PROBLEM_AIR_POLLUTION,
            "Air Pollution"
        ),
        (
            PROBLEM_WATER_POLLUTION,
            "Water Pollution"
        ),
        (
            PROBLEM_OTHER,
            "Other Environmental Problem"
        ),
    ]

    URGENCY_LOW = "low"
    URGENCY_MEDIUM = "medium"
    URGENCY_HIGH = "high"
    URGENCY_EMERGENCY = "emergency"

    URGENCY_CHOICES = [
        (URGENCY_LOW, "Low"),
        (URGENCY_MEDIUM, "Medium"),
        (URGENCY_HIGH, "High"),
        (URGENCY_EMERGENCY, "Emergency"),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_INVESTIGATING = "investigating"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    problem_type = models.CharField(
        max_length=40,
        choices=PROBLEM_TYPES
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="environmental_problem_reports/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.reference_number:

            import uuid

            self.reference_number = (
                f"ENV-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:

        ordering = ["-created_at"]

    def __str__(self):

        return (
            f"{self.reference_number} - "
            f"{self.get_problem_type_display()}"
        )
class DrainageWastewaterReport(models.Model):
    PROBLEM_BLOCKED_DRAIN = "blocked_drain"
    PROBLEM_DAMAGED_DRAIN = "damaged_drain"
    PROBLEM_FLOODING = "flooding"
    PROBLEM_SEWAGE_OVERFLOW = "sewage_overflow"
    PROBLEM_BROKEN_SEWER = "broken_sewer"
    PROBLEM_WASTEWATER_DISCHARGE = "wastewater_discharge"
    PROBLEM_OTHER = "other"

    PROBLEM_TYPES = [
        (PROBLEM_BLOCKED_DRAIN, "Blocked Drainage"),
        (PROBLEM_DAMAGED_DRAIN, "Damaged Drainage"),
        (PROBLEM_FLOODING, "Drainage Causing Flooding"),
        (PROBLEM_SEWAGE_OVERFLOW, "Sewage Overflow"),
        (PROBLEM_BROKEN_SEWER, "Broken Sewer Line"),
        (PROBLEM_WASTEWATER_DISCHARGE, "Wastewater Discharge"),
        (PROBLEM_OTHER, "Other"),
    ]

    URGENCY_LOW = "low"
    URGENCY_MEDIUM = "medium"
    URGENCY_HIGH = "high"
    URGENCY_EMERGENCY = "emergency"

    URGENCY_CHOICES = [
        (URGENCY_LOW, "Low"),
        (URGENCY_MEDIUM, "Medium"),
        (URGENCY_HIGH, "High"),
        (URGENCY_EMERGENCY, "Emergency"),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_INVESTIGATING = "investigating"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(max_length=200)

    phone_number = models.CharField(max_length=30)

    problem_type = models.CharField(
        max_length=40,
        choices=PROBLEM_TYPES
    )

    description = models.TextField()

    district = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="drainage_wastewater_reports/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"DWW-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_problem_type_display()}"
        )
        
class WaterProject(models.Model):
    STATUS_PLANNED = "planned"
    STATUS_ONGOING = "ongoing"
    STATUS_COMPLETED = "completed"
    STATUS_SUSPENDED = "suspended"

    STATUS_CHOICES = [
        (STATUS_PLANNED, "Planned"),
        (STATUS_ONGOING, "Ongoing"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_SUSPENDED, "Suspended"),
    ]

    name = models.CharField(max_length=200)

    project_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    district = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PLANNED
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    expected_completion_date = models.DateField(
        null=True,
        blank=True
    )

    completion_percentage = models.PositiveIntegerField(
        default=0
    )

    implementing_agency = models.CharField(
        max_length=200,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.project_code:
            import uuid

            self.project_code = (
                f"WPR-{uuid.uuid4().hex[:8].upper()}"
            )

        if self.completion_percentage > 100:
            self.completion_percentage = 100

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.project_code} - {self.name}"
    
class EnvironmentalFacility(models.Model):

    FACILITY_WASTE_COLLECTION = "waste_collection"
    FACILITY_RECYCLING = "recycling_center"
    FACILITY_WASTE_SITE = "waste_site"
    FACILITY_TREE_NURSERY = "tree_nursery"
    FACILITY_WETLAND = "wetland_area"
    FACILITY_CONSERVATION = "conservation_area"
    FACILITY_ENVIRONMENT_CENTER = "environment_center"
    FACILITY_WASTEWATER = "wastewater_treatment"
    FACILITY_OTHER = "other"

    FACILITY_TYPES = [
        (
            FACILITY_WASTE_COLLECTION,
            "Waste Collection Point"
        ),
        (
            FACILITY_RECYCLING,
            "Recycling Center"
        ),
        (
            FACILITY_WASTE_SITE,
            "Waste Management Site"
        ),
        (
            FACILITY_TREE_NURSERY,
            "Tree Nursery"
        ),
        (
            FACILITY_WETLAND,
            "Wetland Area"
        ),
        (
            FACILITY_CONSERVATION,
            "Conservation Area"
        ),
        (
            FACILITY_ENVIRONMENT_CENTER,
            "Environmental Information Center"
        ),
        (
            FACILITY_WASTEWATER,
            "Wastewater Treatment Facility"
        ),
        (
            FACILITY_OTHER,
            "Other"
        ),
    ]

    name = models.CharField(
        max_length=200
    )

    facility_type = models.CharField(
        max_length=40,
        choices=FACILITY_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_operational = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["district", "name"]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class WasteManagementService(models.Model):

    SERVICE_COLLECTION = "collection"
    SERVICE_RECYCLING = "recycling"
    SERVICE_COMPOSTING = "composting"
    SERVICE_CLEANUP = "cleanup"
    SERVICE_WASTE_DISPOSAL = "waste_disposal"
    SERVICE_PUBLIC_AWARENESS = "public_awareness"
    SERVICE_OTHER = "other"

    SERVICE_TYPES = [
        (
            SERVICE_COLLECTION,
            "Waste Collection",
        ),
        (
            SERVICE_RECYCLING,
            "Recycling Service",
        ),
        (
            SERVICE_COMPOSTING,
            "Composting Service",
        ),
        (
            SERVICE_CLEANUP,
            "Community Cleanup",
        ),
        (
            SERVICE_WASTE_DISPOSAL,
            "Waste Disposal Service",
        ),
        (
            SERVICE_PUBLIC_AWARENESS,
            "Waste Awareness Programme",
        ),
        (
            SERVICE_OTHER,
            "Other",
        ),
    ]

    FREQUENCY_DAILY = "daily"
    FREQUENCY_WEEKLY = "weekly"
    FREQUENCY_MONTHLY = "monthly"
    FREQUENCY_SCHEDULED = "scheduled"
    FREQUENCY_OTHER = "other"

    FREQUENCY_CHOICES = [
        (
            FREQUENCY_DAILY,
            "Daily",
        ),
        (
            FREQUENCY_WEEKLY,
            "Weekly",
        ),
        (
            FREQUENCY_MONTHLY,
            "Monthly",
        ),
        (
            FREQUENCY_SCHEDULED,
            "Scheduled",
        ),
        (
            FREQUENCY_OTHER,
            "Other",
        ),
    ]

    name = models.CharField(
        max_length=200
    )

    service_type = models.CharField(
        max_length=40,
        choices=SERVICE_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    service_area = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    collection_frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES,
        blank=True
    )

    collection_days = models.CharField(
        max_length=255,
        blank=True,
        help_text="Example: Monday and Thursday"
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_operational = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "district",
            "name",
        ]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class PollutionReport(models.Model):

    POLLUTION_AIR = "air"
    POLLUTION_WATER = "water"
    POLLUTION_SOIL = "soil"
    POLLUTION_SMOKE = "smoke"
    POLLUTION_CHEMICAL = "chemical"
    POLLUTION_INDUSTRIAL = "industrial"
    POLLUTION_OIL = "oil_spill"
    POLLUTION_NOISE = "noise"
    POLLUTION_ILLEGAL_DUMPING = "illegal_dumping"
    POLLUTION_OTHER = "other"

    POLLUTION_TYPES = [
        (POLLUTION_AIR, "Air Pollution"),
        (POLLUTION_WATER, "Water Pollution"),
        (POLLUTION_SOIL, "Soil / Land Pollution"),
        (POLLUTION_SMOKE, "Smoke Pollution"),
        (POLLUTION_CHEMICAL, "Chemical Pollution"),
        (POLLUTION_INDUSTRIAL, "Industrial Pollution"),
        (POLLUTION_OIL, "Oil / Fuel Spill"),
        (POLLUTION_NOISE, "Noise Pollution"),
        (POLLUTION_ILLEGAL_DUMPING, "Illegal Dumping"),
        (POLLUTION_OTHER, "Other"),
    ]

    URGENCY_LOW = "low"
    URGENCY_MEDIUM = "medium"
    URGENCY_HIGH = "high"
    URGENCY_EMERGENCY = "emergency"

    URGENCY_CHOICES = [
        (URGENCY_LOW, "Low"),
        (URGENCY_MEDIUM, "Medium"),
        (URGENCY_HIGH, "High"),
        (URGENCY_EMERGENCY, "Emergency"),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_INVESTIGATING = "investigating"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    pollution_type = models.CharField(
        max_length=40,
        choices=POLLUTION_TYPES
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="pollution_reports/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"POL-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_pollution_type_display()}"
        )
        
class TreeForestSite(models.Model):

    SITE_FOREST = "forest"
    SITE_FOREST_RESERVE = "forest_reserve"
    SITE_TREE_NURSERY = "tree_nursery"
    SITE_TREE_PLANTING = "tree_planting"
    SITE_CONSERVATION = "conservation"
    SITE_URBAN_GREEN = "urban_green"
    SITE_OTHER = "other"

    SITE_TYPES = [
        (
            SITE_FOREST,
            "Forest Area",
        ),
        (
            SITE_FOREST_RESERVE,
            "Forest Reserve",
        ),
        (
            SITE_TREE_NURSERY,
            "Tree Nursery",
        ),
        (
            SITE_TREE_PLANTING,
            "Tree Planting Site",
        ),
        (
            SITE_CONSERVATION,
            "Tree Conservation Area",
        ),
        (
            SITE_URBAN_GREEN,
            "Urban Green Space",
        ),
        (
            SITE_OTHER,
            "Other",
        ),
    ]

    name = models.CharField(
        max_length=200
    )

    site_type = models.CharField(
        max_length=40,
        choices=SITE_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    tree_species = models.CharField(
        max_length=255,
        blank=True,
        help_text="Example: Pine, Eucalyptus, Grevillea"
    )

    planting_information = models.TextField(
        blank=True,
        help_text="Information about tree planting or conservation."
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_operational = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "district",
            "name",
        ]

    def __str__(self):
        return f"{self.name} - {self.district}"
class EnvironmentalProject(models.Model):

    STATUS_PLANNED = "planned"
    STATUS_ONGOING = "ongoing"
    STATUS_COMPLETED = "completed"
    STATUS_SUSPENDED = "suspended"

    STATUS_CHOICES = [
        (STATUS_PLANNED, "Planned"),
        (STATUS_ONGOING, "Ongoing"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_SUSPENDED, "Suspended"),
    ]

    PROJECT_TREE_PLANTING = "tree_planting"
    PROJECT_FOREST_CONSERVATION = "forest_conservation"
    PROJECT_WETLAND_RESTORATION = "wetland_restoration"
    PROJECT_WASTE_REDUCTION = "waste_reduction"
    PROJECT_POLLUTION_CONTROL = "pollution_control"
    PROJECT_BIODIVERSITY = "biodiversity"
    PROJECT_CLIMATE = "climate"
    PROJECT_OTHER = "other"

    PROJECT_TYPES = [
        (
            PROJECT_TREE_PLANTING,
            "Tree Planting",
        ),
        (
            PROJECT_FOREST_CONSERVATION,
            "Forest Conservation",
        ),
        (
            PROJECT_WETLAND_RESTORATION,
            "Wetland Restoration",
        ),
        (
            PROJECT_WASTE_REDUCTION,
            "Waste Reduction",
        ),
        (
            PROJECT_POLLUTION_CONTROL,
            "Pollution Control",
        ),
        (
            PROJECT_BIODIVERSITY,
            "Biodiversity Conservation",
        ),
        (
            PROJECT_CLIMATE,
            "Climate & Environmental Restoration",
        ),
        (
            PROJECT_OTHER,
            "Other",
        ),
    ]

    name = models.CharField(
        max_length=200
    )

    project_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PLANNED
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    expected_completion_date = models.DateField(
        null=True,
        blank=True
    )

    completion_percentage = models.PositiveIntegerField(
        default=0
    )

    implementing_agency = models.CharField(
        max_length=200,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.project_code:
            import uuid

            self.project_code = (
                f"ENV-{uuid.uuid4().hex[:8].upper()}"
            )

        if self.completion_percentage > 100:
            self.completion_percentage = 100

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.project_code} - {self.name}"
        )
        
class WetlandNaturalResource(models.Model):
    RESOURCE_WETLAND = "wetland"
    RESOURCE_WETLAND_RESERVE = "wetland_reserve"
    RESOURCE_RIVER = "river"
    RESOURCE_LAKE = "lake"
    RESOURCE_FOREST = "forest"
    RESOURCE_WILDLIFE = "wildlife"
    RESOURCE_BIODIVERSITY = "biodiversity"
    RESOURCE_OTHER = "other"

    RESOURCE_TYPES = [
        (RESOURCE_WETLAND, "Wetland"),
        (RESOURCE_WETLAND_RESERVE, "Wetland Reserve"),
        (RESOURCE_RIVER, "River"),
        (RESOURCE_LAKE, "Lake"),
        (RESOURCE_FOREST, "Forest / Natural Vegetation"),
        (RESOURCE_WILDLIFE, "Wildlife / Habitat"),
        (RESOURCE_BIODIVERSITY, "Biodiversity Area"),
        (RESOURCE_OTHER, "Other Natural Resource"),
    ]

    name = models.CharField(max_length=200)

    resource_type = models.CharField(
        max_length=40,
        choices=RESOURCE_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    description = models.TextField()

    conservation_information = models.TextField(
        blank=True,
        help_text="Information about conservation, protection or responsible use."
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_protected = models.BooleanField(
        default=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["district", "name"]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class ClimateEnvironmentalInformation(models.Model):

    CATEGORY_CLIMATE = "climate"
    CATEGORY_WEATHER = "weather"
    CATEGORY_CONSERVATION = "conservation"
    CATEGORY_ADAPTATION = "adaptation"
    CATEGORY_AWARENESS = "awareness"
    CATEGORY_BIODIVERSITY = "biodiversity"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = [
        (CATEGORY_CLIMATE, "Climate Information"),
        (CATEGORY_WEATHER, "Weather & Environmental Conditions"),
        (CATEGORY_CONSERVATION, "Conservation"),
        (CATEGORY_ADAPTATION, "Climate Adaptation"),
        (CATEGORY_AWARENESS, "Environmental Awareness"),
        (CATEGORY_BIODIVERSITY, "Biodiversity"),
        (CATEGORY_OTHER, "Other"),
    ]

    title = models.CharField(
        max_length=250
    )

    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        help_text="Leave blank if the information applies nationally."
    )

    summary = models.TextField()

    content = models.TextField()

    source_organization = models.CharField(
        max_length=200,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.title
class EnvironmentalIncidentReport(models.Model):

    INCIDENT_WETLAND_DESTRUCTION = "wetland_destruction"
    INCIDENT_ILLEGAL_DUMPING = "illegal_dumping"
    INCIDENT_DEFORESTATION = "deforestation"
    INCIDENT_POLLUTION = "pollution"
    INCIDENT_CHEMICAL_SPILL = "chemical_spill"
    INCIDENT_WILDLIFE_HARM = "wildlife_harm"
    INCIDENT_LAND_DEGRADATION = "land_degradation"
    INCIDENT_BUSH_BURNING = "bush_burning"
    INCIDENT_SEWAGE_DISCHARGE = "sewage_discharge"
    INCIDENT_OTHER = "other"

    INCIDENT_TYPES = [
        (
            INCIDENT_WETLAND_DESTRUCTION,
            "Wetland Destruction"
        ),
        (
            INCIDENT_ILLEGAL_DUMPING,
            "Illegal Dumping"
        ),
        (
            INCIDENT_DEFORESTATION,
            "Deforestation / Tree Destruction"
        ),
        (
            INCIDENT_POLLUTION,
            "Environmental Pollution"
        ),
        (
            INCIDENT_CHEMICAL_SPILL,
            "Chemical Spill"
        ),
        (
            INCIDENT_WILDLIFE_HARM,
            "Wildlife / Habitat Harm"
        ),
        (
            INCIDENT_LAND_DEGRADATION,
            "Land Degradation"
        ),
        (
            INCIDENT_BUSH_BURNING,
            "Bush Burning"
        ),
        (
            INCIDENT_SEWAGE_DISCHARGE,
            "Sewage / Wastewater Discharge"
        ),
        (
            INCIDENT_OTHER,
            "Other Environmental Incident"
        ),
    ]

    URGENCY_LOW = "low"
    URGENCY_MEDIUM = "medium"
    URGENCY_HIGH = "high"
    URGENCY_EMERGENCY = "emergency"

    URGENCY_CHOICES = [
        (URGENCY_LOW, "Low"),
        (URGENCY_MEDIUM, "Medium"),
        (URGENCY_HIGH, "High"),
        (URGENCY_EMERGENCY, "Emergency"),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_INVESTIGATING = "investigating"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    incident_type = models.CharField(
        max_length=50,
        choices=INCIDENT_TYPES
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="environmental_incidents/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"ENV-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_incident_type_display()}"
        )