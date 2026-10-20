from django.db import models


class ElectricityServiceInformation(models.Model):

    CATEGORY_GENERAL = "general"
    CATEGORY_SUPPLY = "supply"
    CATEGORY_CONNECTION = "connection"
    CATEGORY_SAFETY = "safety"
    CATEGORY_CONTACT = "contact"
    CATEGORY_ANNOUNCEMENT = "announcement"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = [
        (CATEGORY_GENERAL, "General Electricity Information"),
        (CATEGORY_SUPPLY, "Electricity Supply"),
        (CATEGORY_CONNECTION, "Electricity Connection"),
        (CATEGORY_SAFETY, "Electricity Safety"),
        (CATEGORY_CONTACT, "Service Contacts"),
        (CATEGORY_ANNOUNCEMENT, "Electricity Announcement"),
        (CATEGORY_OTHER, "Other"),
    ]

    title = models.CharField(max_length=250)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    summary = models.TextField()

    information = models.TextField()

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    contact_email = models.EmailField(
        blank=True
    )

    source_organization = models.CharField(
        max_length=200,
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
        ordering = [
            "-is_featured",
            "-created_at"
        ]

    def __str__(self):
        return self.title
    
class ElectricityProblemReport(models.Model):

    PROBLEM_OUTAGE = "outage"
    PROBLEM_POLE = "pole"
    PROBLEM_POWER_LINE = "power_line"
    PROBLEM_TRANSFORMER = "transformer"
    PROBLEM_FIRE = "fire"
    PROBLEM_EXPOSED_WIRES = "exposed_wires"
    PROBLEM_INFRASTRUCTURE = "infrastructure"
    PROBLEM_OTHER = "other"

    PROBLEM_CHOICES = [
        (PROBLEM_OUTAGE, "Power Outage"),
        (PROBLEM_POLE, "Damaged Electricity Pole"),
        (PROBLEM_POWER_LINE, "Fallen / Damaged Power Line"),
        (PROBLEM_TRANSFORMER, "Transformer Problem"),
        (PROBLEM_FIRE, "Electrical Fire"),
        (PROBLEM_EXPOSED_WIRES, "Exposed Electrical Wires"),
        (PROBLEM_INFRASTRUCTURE, "Electricity Infrastructure Problem"),
        (PROBLEM_OTHER, "Other Electricity Problem"),
    ]

    STATUS_REPORTED = "reported"
    STATUS_RECEIVED = "received"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_REPORTED, "Reported"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    citizen_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)

    district = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    problem_type = models.CharField(
        max_length=30,
        choices=PROBLEM_CHOICES
    )

    description = models.TextField()

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_REPORTED
    )

    image = models.ImageField(
        upload_to="energy/problem_reports/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):

        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"ENE-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.get_problem_type_display()}"
        )
        
class EnergyServiceInformation(models.Model):

    CATEGORY_GENERAL = "general"
    CATEGORY_CLEAN_ENERGY = "clean_energy"
    CATEGORY_ENERGY_EFFICIENCY = "efficiency"
    CATEGORY_RENEWABLE = "renewable"
    CATEGORY_SAFETY = "safety"
    CATEGORY_CONSERVATION = "conservation"
    CATEGORY_ANNOUNCEMENT = "announcement"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = [
        (CATEGORY_GENERAL, "General Energy Information"),
        (CATEGORY_CLEAN_ENERGY, "Clean Energy"),
        (CATEGORY_ENERGY_EFFICIENCY, "Energy Efficiency"),
        (CATEGORY_RENEWABLE, "Renewable Energy"),
        (CATEGORY_SAFETY, "Energy Safety"),
        (CATEGORY_CONSERVATION, "Energy Conservation"),
        (CATEGORY_ANNOUNCEMENT, "Energy Announcement"),
        (CATEGORY_OTHER, "Other"),
    ]

    title = models.CharField(max_length=250)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    summary = models.TextField()

    information = models.TextField()

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    contact_email = models.EmailField(
        blank=True
    )

    source_organization = models.CharField(
        max_length=200,
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
        ordering = [
            "-is_featured",
            "-created_at"
        ]

    def __str__(self):
        return self.title
    
class EnergyProject(models.Model):

    TYPE_ELECTRICITY = "electricity"
    TYPE_TRANSMISSION = "transmission"
    TYPE_DISTRIBUTION = "distribution"
    TYPE_RURAL_ELECTRIFICATION = "rural_electrification"
    TYPE_RENEWABLE = "renewable"
    TYPE_CLEAN_ENERGY = "clean_energy"
    TYPE_OTHER = "other"

    PROJECT_TYPE_CHOICES = [
        (TYPE_ELECTRICITY, "Electricity Project"),
        (TYPE_TRANSMISSION, "Electricity Transmission"),
        (TYPE_DISTRIBUTION, "Electricity Distribution"),
        (
            TYPE_RURAL_ELECTRIFICATION,
            "Rural Electrification",
        ),
        (TYPE_RENEWABLE, "Renewable Energy"),
        (TYPE_CLEAN_ENERGY, "Clean Energy"),
        (TYPE_OTHER, "Other Energy Project"),
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

    project_type = models.CharField(
        max_length=40,
        choices=PROJECT_TYPE_CHOICES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField()

    implementing_organization = models.CharField(
        max_length=250,
        blank=True
    )

    contractor = models.CharField(
        max_length=250,
        blank=True
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    expected_completion_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_PLANNED
    )

    project_image = models.ImageField(
        upload_to="energy/projects/",
        blank=True,
        null=True
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
        ordering = [
            "-is_featured",
            "-created_at"
        ]

    def __str__(self):
        return self.name
    
class MineralResourceInformation(models.Model):

    TYPE_GOLD = "gold"
    TYPE_COPPER = "copper"
    TYPE_COBALT = "cobalt"
    TYPE_IRON = "iron"
    TYPE_LIMESTONE = "limestone"
    TYPE_SALT = "salt"
    TYPE_TIN = "tin"
    TYPE_TUNGSTEN = "tungsten"
    TYPE_MARBLE = "marble"
    TYPE_OTHER = "other"

    MINERAL_TYPE_CHOICES = [
        (TYPE_GOLD, "Gold"),
        (TYPE_COPPER, "Copper"),
        (TYPE_COBALT, "Cobalt"),
        (TYPE_IRON, "Iron Ore"),
        (TYPE_LIMESTONE, "Limestone"),
        (TYPE_SALT, "Salt"),
        (TYPE_TIN, "Tin"),
        (TYPE_TUNGSTEN, "Tungsten"),
        (TYPE_MARBLE, "Marble"),
        (TYPE_OTHER, "Other Mineral"),
    ]

    name = models.CharField(
        max_length=200
    )

    mineral_type = models.CharField(
        max_length=30,
        choices=MINERAL_TYPE_CHOICES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField()

    uses = models.TextField(
        blank=True
    )

    development_information = models.TextField(
        blank=True
    )

    source_organization = models.CharField(
        max_length=250,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    contact_email = models.EmailField(
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
        ordering = [
            "-is_featured",
            "-created_at"
        ]

    def __str__(self):
        return self.name
    
class MiningDevelopmentInformation(models.Model):

    ACTIVITY_EXPLORATION = "exploration"
    ACTIVITY_EXTRACTION = "extraction"
    ACTIVITY_PROCESSING = "processing"
    ACTIVITY_DEVELOPMENT = "development"
    ACTIVITY_COMMUNITY = "community"
    ACTIVITY_OTHER = "other"

    ACTIVITY_CHOICES = [
        (ACTIVITY_EXPLORATION, "Mineral Exploration"),
        (ACTIVITY_EXTRACTION, "Mineral Extraction"),
        (ACTIVITY_PROCESSING, "Mineral Processing"),
        (ACTIVITY_DEVELOPMENT, "Mineral Development"),
        (ACTIVITY_COMMUNITY, "Community Development"),
        (ACTIVITY_OTHER, "Other Mining Activity"),
    ]

    STATUS_PLANNED = "planned"
    STATUS_ACTIVE = "active"
    STATUS_COMPLETED = "completed"
    STATUS_SUSPENDED = "suspended"
    STATUS_CLOSED = "closed"

    STATUS_CHOICES = [
        (STATUS_PLANNED, "Planned"),
        (STATUS_ACTIVE, "Active"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_SUSPENDED, "Suspended"),
        (STATUS_CLOSED, "Closed"),
    ]

    title = models.CharField(
        max_length=250
    )

    activity_type = models.CharField(
        max_length=30,
        choices=ACTIVITY_CHOICES
    )

    mineral = models.CharField(
        max_length=150,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField()

    development_information = models.TextField(
        blank=True
    )

    community_information = models.TextField(
        blank=True
    )

    environmental_information = models.TextField(
        blank=True
    )

    responsible_organization = models.CharField(
        max_length=250,
        blank=True
    )

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    contact_email = models.EmailField(
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_PLANNED
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
        ordering = [
            "-is_featured",
            "-created_at"
        ]

    def __str__(self):
        return self.title
    
class EnergyMineralRequest(models.Model):

    TYPE_ELECTRICITY_SERVICE = "electricity_service"
    TYPE_ENERGY_INFORMATION = "energy_information"
    TYPE_ENERGY_PROJECT = "energy_project"
    TYPE_MINERAL_INFORMATION = "mineral_information"
    TYPE_MINING_REPORT = "mining_report"
    TYPE_OTHER = "other"

    REQUEST_TYPE_CHOICES = [
        (
            TYPE_ELECTRICITY_SERVICE,
            "Electricity Service Request",
        ),
        (
            TYPE_ENERGY_INFORMATION,
            "Energy Information Request",
        ),
        (
            TYPE_ENERGY_PROJECT,
            "Energy Project Inquiry",
        ),
        (
            TYPE_MINERAL_INFORMATION,
            "Mineral Information Request",
        ),
        (
            TYPE_MINING_REPORT,
            "Mining / Mineral Development Report",
        ),
        (
            TYPE_OTHER,
            "Other Energy / Mineral Request",
        ),
    ]

    STATUS_SUBMITTED = "submitted"
    STATUS_RECEIVED = "received"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_RECEIVED, "Received"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_REJECTED, "Rejected"),
    ]

    citizen_name = models.CharField(
        max_length=200
    )

    phone_number = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    request_type = models.CharField(
        max_length=40,
        choices=REQUEST_TYPE_CHOICES
    )

    subject = models.CharField(
        max_length=250
    )

    description = models.TextField()

    attachment = models.FileField(
        upload_to="energy/requests/",
        blank=True,
        null=True
    )

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
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

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):

        if not self.reference_number:
            import uuid

            self.reference_number = (
                f"EMR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.reference_number} - "
            f"{self.subject}"
        )