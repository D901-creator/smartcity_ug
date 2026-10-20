from django.db import models
import uuid


class LandInformation(models.Model):
    INFORMATION_TYPES = [
        ("land_tenure", "Land Tenure"),
        ("land_title", "Land Title"),
        ("land_transfer", "Land Transfer"),
        ("lost_title", "Lost or Damaged Title"),
        ("land_search", "Land Search"),
        ("general", "General Land Information"),
    ]

    title = models.CharField(max_length=200)
    information_type = models.CharField(
        max_length=30,
        choices=INFORMATION_TYPES
    )
    summary = models.TextField()
    description = models.TextField()
    required_documents = models.TextField(
        blank=True,
        help_text="List documents or information normally required."
    )
    application_steps = models.TextField(
        blank=True,
        help_text="General steps citizens should follow."
    )
    fees_information = models.TextField(
        blank=True,
        help_text="Official fee information or a note directing citizens to verify current fees."
    )
    contact_information = models.TextField(
        blank=True
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class LandTitleApplication(models.Model):
    APPLICATION_TYPES = [
        ("new_title", "New Land Title"),
        ("transfer", "Land Title Transfer"),
        ("replacement", "Replacement of Lost/Damaged Title"),
        ("land_search", "Land Search / Land Information"),
        ("general", "General Land Title Inquiry"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("under_review", "Under Review"),
        ("additional_information", "Additional Information Required"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("completed", "Completed"),
    ]

    applicant_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    district = models.CharField(max_length=100)
    location = models.CharField(
        max_length=255,
        help_text="Village, parish, town, municipality or other location."
    )

    application_type = models.CharField(
        max_length=30,
        choices=APPLICATION_TYPES
    )

    land_reference = models.CharField(
        max_length=150,
        blank=True,
        help_text="Plot number, block number, title number or other known reference."
    )

    description = models.TextField(
        help_text="Describe the land-title service you are requesting."
    )

    supporting_information = models.TextField(
        blank=True,
        help_text="Additional information relevant to the request."
    )

    attachment = models.FileField(
        upload_to="land_title_applications/",
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
        default="submitted"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = f"LTA-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.applicant_name}"
    
class LandPropertyRequest(models.Model):

    REQUEST_TYPES = [
        ("ownership", "Land Ownership Information"),
        ("boundary", "Boundary / Property Boundary Concern"),
        ("property", "Property Information"),
        ("land_use", "Land Use Concern"),
        ("dispute", "Land / Property Dispute Inquiry"),
        ("verification", "Land / Property Verification"),
        ("general", "General Land & Property Request"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("under_review", "Under Review"),
        ("additional_information", "Additional Information Required"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
        ("rejected", "Rejected"),
    ]

    citizen_name = models.CharField(
        max_length=150
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
        help_text="Village, parish, town, municipality or other location."
    )

    request_type = models.CharField(
        max_length=30,
        choices=REQUEST_TYPES
    )

    property_reference = models.CharField(
        max_length=150,
        blank=True,
        help_text="Plot number, block number, title number or other property reference if known."
    )

    subject = models.CharField(
        max_length=200
    )

    description = models.TextField()

    supporting_information = models.TextField(
        blank=True
    )

    attachment = models.FileField(
        upload_to="land_property_requests/",
        blank=True,
        null=True
    )

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default="submitted"
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
            self.reference_number = (
                f"LPR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.subject}"
    
class HousingInformation(models.Model):

    INFORMATION_TYPES = [
        ("housing_services", "Housing Services"),
        ("housing_assistance", "Housing Assistance"),
        ("housing_programmes", "Housing Programmes"),
        ("affordable_housing", "Affordable Housing"),
        ("housing_guidance", "Housing Guidance"),
        ("housing_requirements", "Housing Requirements"),
        ("general", "General Housing Information"),
    ]

    title = models.CharField(max_length=200)

    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        help_text="Leave blank if the information applies nationally."
    )

    summary = models.CharField(
        max_length=500
    )

    description = models.TextField()

    requirements = models.TextField(
        blank=True,
        help_text="Requirements or documents citizens may need."
    )

    application_process = models.TextField(
        blank=True,
        help_text="General steps for accessing the service."
    )

    contact_information = models.TextField(
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
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
class HousingPropertyRequest(models.Model):

    REQUEST_TYPES = [
        ("housing_assistance", "Housing Assistance"),
        ("housing_information", "Housing Information Request"),
        ("housing_complaint", "Housing Complaint"),
        ("rental_concern", "Rental / Housing Concern"),
        ("property_support", "Housing / Property Support"),
        ("housing_programme", "Housing Programme Inquiry"),
        ("general", "General Housing Request"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("under_review", "Under Review"),
        ("additional_information", "Additional Information Required"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
        ("rejected", "Rejected"),
    ]

    citizen_name = models.CharField(
        max_length=150
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
        help_text="Village, parish, town, municipality or other location."
    )

    request_type = models.CharField(
        max_length=40,
        choices=REQUEST_TYPES
    )

    property_reference = models.CharField(
        max_length=150,
        blank=True,
        help_text="Property reference, plot number or other reference if known."
    )

    subject = models.CharField(
        max_length=200
    )

    description = models.TextField()

    supporting_information = models.TextField(
        blank=True
    )

    attachment = models.FileField(
        upload_to="housing_property_requests/",
        blank=True,
        null=True
    )

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default="submitted"
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
            self.reference_number = (
                f"HPR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.subject}"
    
class UrbanPlanningInformation(models.Model):

    INFORMATION_TYPES = [
        ("urban_planning", "Urban Planning"),
        ("land_use", "Land Use Planning"),
        ("zoning", "Zoning Information"),
        ("development_control", "Development Control"),
        ("physical_planning", "Physical Planning"),
        ("urban_development", "Urban Development"),
        ("planning_guidance", "Planning Guidance"),
        ("general", "General Urban Planning Information"),
    ]

    title = models.CharField(
        max_length=200
    )

    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        help_text="Leave blank if the information applies nationally."
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        help_text="City, municipality, town or other applicable location."
    )

    summary = models.CharField(
        max_length=500
    )

    description = models.TextField()

    requirements = models.TextField(
        blank=True
    )

    planning_process = models.TextField(
        blank=True,
        help_text="General process or steps citizens should follow."
    )

    important_information = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
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
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
class DevelopmentBuildingApplication(models.Model):

    APPLICATION_TYPES = [
        ("new_building", "New Building"),
        ("renovation", "Building Renovation"),
        ("extension", "Building Extension"),
        ("commercial", "Commercial Development"),
        ("residential", "Residential Development"),
        ("industrial", "Industrial Development"),
        ("change_of_use", "Change of Land / Building Use"),
        ("demolition", "Demolition"),
        ("other", "Other Development"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("under_review", "Under Review"),
        ("additional_information", "Additional Information Required"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("completed", "Completed"),
    ]

    applicant_name = models.CharField(
        max_length=150
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
        max_length=255
    )

    property_reference = models.CharField(
        max_length=150,
        blank=True,
        help_text="Plot number, block number, title number or other reference if known."
    )

    application_type = models.CharField(
        max_length=40,
        choices=APPLICATION_TYPES
    )

    project_title = models.CharField(
        max_length=200
    )

    proposed_development = models.TextField(
        help_text="Describe the proposed development."
    )

    estimated_project_value = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True
    )

    additional_information = models.TextField(
        blank=True
    )

    supporting_document = models.FileField(
        upload_to="development_building_applications/",
        blank=True,
        null=True
    )

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default="submitted"
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
            self.reference_number = (
                f"DBA-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.project_title}"
    
class LandHousingPlanningProject(models.Model):

    PROJECT_TYPES = [
        ("land_development", "Land Development"),
        ("housing", "Housing"),
        ("urban_development", "Urban Development"),
        ("physical_planning", "Physical Planning"),
        ("infrastructure", "Infrastructure Development"),
        ("community_development", "Community Development"),
        ("property_development", "Property Development"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("suspended", "Suspended"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(max_length=200)

    project_type = models.CharField(
        max_length=40,
        choices=PROJECT_TYPES
    )

    district = models.CharField(max_length=100)

    location = models.CharField(
        max_length=255,
        help_text="Town, city, municipality, ward or specific project location."
    )

    summary = models.TextField()

    description = models.TextField()

    objectives = models.TextField(
        blank=True
    )

    expected_benefits = models.TextField(
        blank=True
    )

    implementing_organization = models.CharField(
        max_length=200,
        blank=True
    )

    contact_information = models.TextField(
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
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )

    image = models.ImageField(
        upload_to="lands_planning_projects/",
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
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
class LandHousingPlanningNotice(models.Model):

    NOTICE_TYPES = [
        ("land", "Land Notice"),
        ("housing", "Housing Notice"),
        ("planning", "Planning Notice"),
        ("development", "Development Notice"),
        ("building", "Building Notice"),
        ("public", "Public Notice"),
        ("deadline", "Important Deadline"),
        ("general", "General Notice"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("normal", "Normal"),
        ("high", "High"),
        ("urgent", "Urgent"),
    ]

    title = models.CharField(max_length=200)

    notice_type = models.CharField(
        max_length=30,
        choices=NOTICE_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    content = models.TextField()

    important_date = models.DateField(
        blank=True,
        null=True
    )

    issuing_organization = models.CharField(
        max_length=200,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="normal"
    )

    image = models.ImageField(
        upload_to="lands_planning_notices/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    published_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title