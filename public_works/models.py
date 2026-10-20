from django.db import models


class RoadProblemReport(models.Model):

    PROBLEM_POTHOLE = "pothole"
    PROBLEM_DAMAGED_ROAD = "damaged_road"
    PROBLEM_IMPASSABLE_ROAD = "impassable_road"
    PROBLEM_CRACKED_ROAD = "cracked_road"
    PROBLEM_MISSING_SIGN = "missing_sign"
    PROBLEM_DAMAGED_BARRIER = "damaged_barrier"
    PROBLEM_CONSTRUCTION = "construction_problem"
    PROBLEM_OTHER = "other"

    PROBLEM_TYPES = [
        (PROBLEM_POTHOLE, "Pothole"),
        (PROBLEM_DAMAGED_ROAD, "Damaged Road"),
        (PROBLEM_IMPASSABLE_ROAD, "Impassable Road"),
        (PROBLEM_CRACKED_ROAD, "Cracked Road"),
        (PROBLEM_MISSING_SIGN, "Missing Road Sign"),
        (PROBLEM_DAMAGED_BARRIER, "Damaged Road Barrier"),
        (PROBLEM_CONSTRUCTION, "Road Construction Problem"),
        (PROBLEM_OTHER, "Other Road Problem"),
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
    STATUS_ASSIGNED = "assigned"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_ASSIGNED, "Assigned"),
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
        max_length=50,
        choices=PROBLEM_TYPES
    )

    description = models.TextField()

    district = models.CharField(max_length=100)

    road_name = models.CharField(max_length=200)

    location = models.CharField(max_length=255)

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default=URGENCY_MEDIUM
    )

    photo = models.ImageField(
        upload_to="road_problem_reports/",
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
                f"PWT-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_problem_type_display()}"
        )
class Road(models.Model):

    CLASS_LOCAL = "local"
    CLASS_DISTRICT = "district"
    CLASS_CITY = "city"
    CLASS_REGIONAL = "regional"
    CLASS_NATIONAL = "national"

    ROAD_CLASS_CHOICES = [
        (CLASS_LOCAL, "Local Road"),
        (CLASS_DISTRICT, "District Road"),
        (CLASS_CITY, "City Road"),
        (CLASS_REGIONAL, "Regional Road"),
        (CLASS_NATIONAL, "National Road"),
    ]

    CONDITION_GOOD = "good"
    CONDITION_FAIR = "fair"
    CONDITION_POOR = "poor"
    CONDITION_CRITICAL = "critical"

    CONDITION_CHOICES = [
        (CONDITION_GOOD, "Good"),
        (CONDITION_FAIR, "Fair"),
        (CONDITION_POOR, "Poor"),
        (CONDITION_CRITICAL, "Critical"),
    ]

    SURFACE_PAVED = "paved"
    SURFACE_GRAVEL = "gravel"
    SURFACE_EARTH = "earth"
    SURFACE_OTHER = "other"

    SURFACE_CHOICES = [
        (SURFACE_PAVED, "Paved / Tarmac"),
        (SURFACE_GRAVEL, "Gravel"),
        (SURFACE_EARTH, "Earth / Murram"),
        (SURFACE_OTHER, "Other"),
    ]

    name = models.CharField(
        max_length=200
    )

    road_code = models.CharField(
        max_length=50,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    start_location = models.CharField(
        max_length=255
    )

    end_location = models.CharField(
        max_length=255
    )

    road_class = models.CharField(
        max_length=30,
        choices=ROAD_CLASS_CHOICES
    )

    surface_type = models.CharField(
        max_length=30,
        choices=SURFACE_CHOICES
    )

    condition = models.CharField(
        max_length=30,
        choices=CONDITION_CHOICES,
        default=CONDITION_FAIR
    )

    length_km = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    description = models.TextField(
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
            "name"
        ]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class RoadConstructionMaintenanceProject(models.Model):

    PROJECT_CONSTRUCTION = "construction"
    PROJECT_REHABILITATION = "rehabilitation"
    PROJECT_MAINTENANCE = "maintenance"
    PROJECT_UPGRADING = "upgrading"

    PROJECT_TYPE_CHOICES = [
        (PROJECT_CONSTRUCTION, "New Road Construction"),
        (PROJECT_REHABILITATION, "Road Rehabilitation"),
        (PROJECT_MAINTENANCE, "Road Maintenance"),
        (PROJECT_UPGRADING, "Road Upgrading"),
    ]

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

    name = models.CharField(max_length=250)

    project_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    district = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    project_type = models.CharField(
        max_length=30,
        choices=PROJECT_TYPE_CHOICES
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

    contractor = models.CharField(
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
        if self.completion_percentage > 100:
            self.completion_percentage = 100

        if not self.project_code:
            import uuid
            self.project_code = (
                f"RMP-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["district", "-created_at"]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class TrafficRoadSafetyInformation(models.Model):

    CATEGORY_ROAD_SAFETY = "road_safety"
    CATEGORY_TRAFFIC_RULES = "traffic_rules"
    CATEGORY_PEDESTRIAN = "pedestrian"
    CATEGORY_ROAD_SIGNS = "road_signs"
    CATEGORY_SPEED = "speed_management"
    CATEGORY_SAFE_DRIVING = "safe_driving"
    CATEGORY_MOTORCYCLE = "motorcycle_safety"
    CATEGORY_EMERGENCY = "emergency_safety"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = [
        (CATEGORY_ROAD_SAFETY, "Road Safety"),
        (CATEGORY_TRAFFIC_RULES, "Traffic Rules"),
        (CATEGORY_PEDESTRIAN, "Pedestrian Safety"),
        (CATEGORY_ROAD_SIGNS, "Road Signs"),
        (CATEGORY_SPEED, "Speed Management"),
        (CATEGORY_SAFE_DRIVING, "Safe Driving"),
        (CATEGORY_MOTORCYCLE, "Motorcycle / Boda-Boda Safety"),
        (CATEGORY_EMERGENCY, "Emergency & Safety Information"),
        (CATEGORY_OTHER, "Other"),
    ]

    title = models.CharField(max_length=250)

    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    summary = models.TextField()

    content = models.TextField()

    safety_contact = models.CharField(
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
    
class TrafficIncidentReport(models.Model):

    INCIDENT_ACCIDENT = "accident"
    INCIDENT_COLLISION = "collision"
    INCIDENT_DANGEROUS_DRIVING = "dangerous_driving"
    INCIDENT_TRAFFIC_OBSTRUCTION = "traffic_obstruction"
    INCIDENT_BROKEN_DOWN_VEHICLE = "broken_down_vehicle"
    INCIDENT_FALLEN_OBJECT = "fallen_object"
    INCIDENT_DANGEROUS_ROAD = "dangerous_road"
    INCIDENT_TRAFFIC_SIGNAL = "traffic_signal"
    INCIDENT_OTHER = "other"

    INCIDENT_TYPES = [
        (INCIDENT_ACCIDENT, "Road Accident"),
        (INCIDENT_COLLISION, "Vehicle Collision"),
        (INCIDENT_DANGEROUS_DRIVING, "Dangerous Driving"),
        (INCIDENT_TRAFFIC_OBSTRUCTION, "Traffic Obstruction"),
        (INCIDENT_BROKEN_DOWN_VEHICLE, "Broken-down Vehicle"),
        (INCIDENT_FALLEN_OBJECT, "Fallen Object on Road"),
        (INCIDENT_DANGEROUS_ROAD, "Dangerous Road Condition"),
        (INCIDENT_TRAFFIC_SIGNAL, "Traffic Signal Problem"),
        (INCIDENT_OTHER, "Other Traffic Incident"),
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
    STATUS_ASSIGNED = "assigned"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_INVESTIGATING, "Investigating"),
        (STATUS_ASSIGNED, "Assigned"),
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

    road_name = models.CharField(
        max_length=200
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
        upload_to="traffic_incidents/",
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
                f"TIR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_incident_type_display()}"
        )
        
class ParkingFacility(models.Model):

    FACILITY_PUBLIC = "public"
    FACILITY_PRIVATE = "private"
    FACILITY_STREET = "street"
    FACILITY_MULTI_STOREY = "multi_storey"
    FACILITY_OTHER = "other"

    FACILITY_TYPES = [
        (FACILITY_PUBLIC, "Public Parking Facility"),
        (FACILITY_PRIVATE, "Private Parking Facility"),
        (FACILITY_STREET, "Street Parking"),
        (FACILITY_MULTI_STOREY, "Multi-storey Parking"),
        (FACILITY_OTHER, "Other"),
    ]

    STATUS_OPERATIONAL = "operational"
    STATUS_FULL = "full"
    STATUS_TEMPORARILY_CLOSED = "temporarily_closed"
    STATUS_CLOSED = "closed"

    STATUS_CHOICES = [
        (STATUS_OPERATIONAL, "Operational"),
        (STATUS_FULL, "Currently Full"),
        (STATUS_TEMPORARILY_CLOSED, "Temporarily Closed"),
        (STATUS_CLOSED, "Closed"),
    ]

    name = models.CharField(
        max_length=200
    )

    facility_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    facility_type = models.CharField(
        max_length=30,
        choices=FACILITY_TYPES
    )

    description = models.TextField(
        blank=True
    )

    total_spaces = models.PositiveIntegerField(
        default=0
    )

    available_spaces = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_OPERATIONAL
    )

    operating_hours = models.CharField(
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

        if not self.facility_code:
            import uuid

            self.facility_code = (
                f"PKF-{uuid.uuid4().hex[:8].upper()}"
            )

        if self.available_spaces > self.total_spaces:
            self.available_spaces = self.total_spaces

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["district", "name"]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class ParkingFee(models.Model):

    FEE_HOURLY = "hourly"
    FEE_DAILY = "daily"
    FEE_MONTHLY = "monthly"
    FEE_EVENT = "event"
    FEE_OTHER = "other"

    FEE_TYPES = [
        (FEE_HOURLY, "Hourly"),
        (FEE_DAILY, "Daily"),
        (FEE_MONTHLY, "Monthly"),
        (FEE_EVENT, "Event"),
        (FEE_OTHER, "Other"),
    ]

    name = models.CharField(
        max_length=200
    )

    facility = models.ForeignKey(
        ParkingFacility,
        on_delete=models.CASCADE,
        related_name="fees"
    )

    fee_type = models.CharField(
        max_length=20,
        choices=FEE_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    tax_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    description = models.TextField(
        blank=True
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
        ordering = ["facility", "fee_type"]

    def __str__(self):
        return (
            f"{self.name} - "
            f"{self.facility.name}"
        )

    @property
    def total_amount(self):
        return self.amount + self.tax_amount
class ParkingPayment(models.Model):

    METHOD_MOBILE_MONEY = "mobile_money"
    METHOD_BANK = "bank"
    METHOD_CARD = "card"
    METHOD_GOVERNMENT_REFERENCE = "government_reference"

    PAYMENT_METHODS = [
        (METHOD_MOBILE_MONEY, "Mobile Money"),
        (METHOD_BANK, "Bank Payment"),
        (METHOD_CARD, "Card Payment"),
        (
            METHOD_GOVERNMENT_REFERENCE,
            "Government Payment Reference"
        ),
    ]

    STATUS_PENDING = "pending"
    STATUS_PROCESSING = "processing"
    STATUS_PAID = "paid"
    STATUS_FAILED = "failed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_PAID, "Paid"),
        (STATUS_FAILED, "Failed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    payment_reference = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    vehicle_registration = models.CharField(
        max_length=30
    )

    facility = models.ForeignKey(
        ParkingFacility,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    fee = models.ForeignKey(
        ParkingFee,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHODS
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    tax_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    transaction_reference = models.CharField(
        max_length=100,
        blank=True
    )

    payment_instructions = models.TextField(
        blank=True
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.payment_reference:
            import uuid

            self.payment_reference = (
                f"PKP-{uuid.uuid4().hex[:10].upper()}"
            )

        self.total_amount = (
            self.amount + self.tax_amount
        )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.payment_reference
    
class ParkingReceipt(models.Model):

    receipt_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    payment = models.OneToOneField(
        ParkingPayment,
        on_delete=models.CASCADE,
        related_name="receipt"
    )

    issued_to = models.CharField(
        max_length=200
    )

    vehicle_registration = models.CharField(
        max_length=30
    )

    facility_name = models.CharField(
        max_length=200
    )

    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=30
    )

    issued_at = models.DateTimeField(
        auto_now_add=True
    )

    confirmation_message = models.TextField(
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.receipt_number:
            import uuid

            self.receipt_number = (
                f"PKR-{uuid.uuid4().hex[:10].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-issued_at"]

    def __str__(self):
        return self.receipt_number
class PublicWorksFacility(models.Model):

    FACILITY_OFFICE = "office"
    FACILITY_MAINTENANCE_STATION = "maintenance_station"
    FACILITY_DEPOT = "depot"
    FACILITY_WORKSHOP = "workshop"
    FACILITY_EQUIPMENT_YARD = "equipment_yard"
    FACILITY_CONSTRUCTION_FACILITY = "construction_facility"
    FACILITY_OTHER = "other"

    FACILITY_TYPES = [
        (FACILITY_OFFICE, "Public Works Office"),
        (FACILITY_MAINTENANCE_STATION, "Road Maintenance Station"),
        (FACILITY_DEPOT, "Road Maintenance Depot"),
        (FACILITY_WORKSHOP, "Engineering Workshop"),
        (FACILITY_EQUIPMENT_YARD, "Equipment Yard"),
        (FACILITY_CONSTRUCTION_FACILITY, "Construction / Maintenance Facility"),
        (FACILITY_OTHER, "Other Public Works Facility"),
    ]

    STATUS_OPERATIONAL = "operational"
    STATUS_TEMPORARILY_CLOSED = "temporarily_closed"
    STATUS_CLOSED = "closed"

    STATUS_CHOICES = [
        (STATUS_OPERATIONAL, "Operational"),
        (STATUS_TEMPORARILY_CLOSED, "Temporarily Closed"),
        (STATUS_CLOSED, "Closed"),
    ]

    name = models.CharField(max_length=200)

    facility_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    district = models.CharField(max_length=100)

    location = models.CharField(max_length=255)

    facility_type = models.CharField(
        max_length=40,
        choices=FACILITY_TYPES
    )

    description = models.TextField(blank=True)

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    operating_hours = models.CharField(
        max_length=200,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_OPERATIONAL
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.facility_code:
            import uuid

            self.facility_code = (
                f"PWF-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["district", "name"]

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class TransportInformationAdvisory(models.Model):

    CATEGORY_GENERAL = "general"
    CATEGORY_ROAD = "road"
    CATEGORY_TRAFFIC = "traffic"
    CATEGORY_SAFETY = "safety"
    CATEGORY_CONSTRUCTION = "construction"
    CATEGORY_WEATHER = "weather"
    CATEGORY_EMERGENCY = "emergency"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = [
        (CATEGORY_GENERAL, "General Transport Information"),
        (CATEGORY_ROAD, "Road Advisory"),
        (CATEGORY_TRAFFIC, "Traffic Advisory"),
        (CATEGORY_SAFETY, "Transport Safety"),
        (CATEGORY_CONSTRUCTION, "Road Construction Advisory"),
        (CATEGORY_WEATHER, "Weather / Travel Advisory"),
        (CATEGORY_EMERGENCY, "Emergency Transport Advisory"),
        (CATEGORY_OTHER, "Other"),
    ]

    PRIORITY_LOW = "low"
    PRIORITY_NORMAL = "normal"
    PRIORITY_HIGH = "high"
    PRIORITY_URGENT = "urgent"

    PRIORITY_CHOICES = [
        (PRIORITY_LOW, "Low"),
        (PRIORITY_NORMAL, "Normal"),
        (PRIORITY_HIGH, "High"),
        (PRIORITY_URGENT, "Urgent"),
    ]

    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_EXPIRED = "expired"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_EXPIRED, "Expired"),
    ]

    title = models.CharField(max_length=250)

    advisory_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_NORMAL
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    affected_location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    information = models.TextField()

    recommended_action = models.TextField(
        blank=True
    )

    source_organization = models.CharField(
        max_length=200,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PUBLISHED
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.advisory_code:
            import uuid

            self.advisory_code = (
                f"TRA-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    class Meta:
        ordering = [
            "-priority",
            "-published_at",
            "-created_at",
        ]

    def __str__(self):
        return self.title
    
class PublicWorksProject(models.Model):

    PROJECT_ROAD_CONSTRUCTION = "road_construction"
    PROJECT_ROAD_REHABILITATION = "road_rehabilitation"
    PROJECT_ROAD_MAINTENANCE = "road_maintenance"
    PROJECT_INFRASTRUCTURE = "infrastructure"
    PROJECT_DRAINAGE = "drainage"
    PROJECT_FACILITY = "facility"
    PROJECT_OTHER = "other"

    PROJECT_TYPES = [
        (
            PROJECT_ROAD_CONSTRUCTION,
            "Road Construction",
        ),
        (
            PROJECT_ROAD_REHABILITATION,
            "Road Rehabilitation",
        ),
        (
            PROJECT_ROAD_MAINTENANCE,
            "Road Maintenance",
        ),
        (
            PROJECT_INFRASTRUCTURE,
            "Infrastructure Improvement",
        ),
        (
            PROJECT_DRAINAGE,
            "Drainage / Water Infrastructure",
        ),
        (
            PROJECT_FACILITY,
            "Public Works Facility",
        ),
        (
            PROJECT_OTHER,
            "Other Public Works Project",
        ),
    ]

    STATUS_PLANNED = "planned"
    STATUS_ONGOING = "ongoing"
    STATUS_COMPLETED = "completed"
    STATUS_SUSPENDED = "suspended"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PLANNED, "Planned"),
        (STATUS_ONGOING, "Ongoing"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_SUSPENDED, "Suspended"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    name = models.CharField(
        max_length=250
    )

    project_code = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    project_type = models.CharField(
        max_length=40,
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

    completion_percentage = models.PositiveIntegerField(
        default=0
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    expected_completion_date = models.DateField(
        null=True,
        blank=True
    )

    implementing_agency = models.CharField(
        max_length=200,
        blank=True
    )

    contractor = models.CharField(
        max_length=200,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    project_budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
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
                f"PWP-{uuid.uuid4().hex[:8].upper()}"
            )

        if self.completion_percentage > 100:
            self.completion_percentage = 100

        super().save(*args, **kwargs)

    class Meta:
        ordering = [
            "district",
            "-created_at",
        ]

    def __str__(self):
        return (
            f"{self.name} - {self.district}"
        )