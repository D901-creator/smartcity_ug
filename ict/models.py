from django.db import models


class ICTService(models.Model):

    SERVICE_TYPES = [
        ("digital_government", "Digital Government"),
        ("ict_service", "ICT Service"),
        ("e_government", "E-Government"),
        ("connectivity", "Internet & Connectivity"),
        ("digital_literacy", "Digital Literacy"),
        ("ict_support", "ICT Support"),
        ("technology", "Technology Information"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_TYPES
    )

    summary = models.TextField()

    description = models.TextField()

    eligibility = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    application_process = models.TextField(
        blank=True
    )

    fees_information = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    image = models.ImageField(
        upload_to="ict_services/",
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
        ordering = ["title"]

    def __str__(self):
        return self.title
    
    
class ICTInfrastructure(models.Model):

    INFRASTRUCTURE_TYPES = [
        ("internet", "Internet Connectivity"),
        ("telecommunication", "Telecommunication"),
        ("data_centre", "Data Centre"),
        ("ict_centre", "ICT Centre"),
        ("network", "Network Infrastructure"),
        ("digital_access", "Digital Access Point"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    infrastructure_type = models.CharField(
        max_length=50,
        choices=INFRASTRUCTURE_TYPES
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

    description = models.TextField()

    services_available = models.TextField(
        blank=True
    )

    coverage_information = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="ict_infrastructure/",
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
        ordering = ["title"]

    def __str__(self):
        return self.title


class ICTInnovation(models.Model):

    INNOVATION_TYPES = [
        ("technology", "Technology Innovation"),
        ("startup", "ICT Startup"),
        ("digital_solution", "Digital Solution"),
        ("research", "ICT Research"),
        ("innovation_hub", "Innovation Hub"),
        ("digital_transformation", "Digital Transformation"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    innovation_type = models.CharField(
        max_length=50,
        choices=INNOVATION_TYPES
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

    description = models.TextField()

    objectives = models.TextField(
        blank=True
    )

    target_group = models.TextField(
        blank=True
    )

    benefits = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="ict_innovations/",
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
        ordering = ["title"]

    def __str__(self):
        return self.title


class ICTOpportunity(models.Model):

    OPPORTUNITY_TYPES = [
        ("training", "ICT Training"),
        ("innovation", "Innovation Opportunity"),
        ("startup", "Startup Opportunity"),
        ("investment", "ICT Investment"),
        ("project", "ICT Project"),
        ("partnership", "Partnership"),
        ("grant", "Grant Opportunity"),
        ("competition", "Technology Competition"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("open", "Open"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("closed", "Closed"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(max_length=200)

    opportunity_type = models.CharField(
        max_length=50,
        choices=OPPORTUNITY_TYPES
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

    description = models.TextField()

    objectives = models.TextField(
        blank=True
    )

    benefits = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    application_process = models.TextField(
        blank=True
    )

    implementing_organization = models.CharField(
        max_length=200,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    closing_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )

    image = models.ImageField(
        upload_to="ict_opportunities/",
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
    
class NationalGuidanceInformation(models.Model):
    INFORMATION_TYPES = [
        ("national_guidance", "National Guidance"),
        ("civic_education", "Civic Education"),
        ("citizenship", "Citizenship"),
        ("rights_responsibilities", "Rights & Responsibilities"),
        ("national_programme", "National Programme"),
        ("public_awareness", "Public Awareness"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    information_type = models.CharField(
        max_length=50,
        choices=INFORMATION_TYPES
    )

    summary = models.TextField()

    description = models.TextField()

    key_points = models.TextField(blank=True)

    citizen_responsibilities = models.TextField(blank=True)

    related_information = models.TextField(blank=True)

    contact_information = models.TextField(blank=True)

    website = models.URLField(blank=True)

    district = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="national_guidance/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=False)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class CivicProgramme(models.Model):
    PROGRAMME_TYPES = [
        ("national_programme", "National Programme"),
        ("community_programme", "Community Programme"),
        ("civic_programme", "Civic Programme"),
        ("awareness_campaign", "Awareness Campaign"),
        ("public_initiative", "Public Initiative"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("closed", "Closed"),
    ]

    title = models.CharField(max_length=200)

    programme_type = models.CharField(
        max_length=50,
        choices=PROGRAMME_TYPES
    )

    summary = models.TextField()

    description = models.TextField()

    objectives = models.TextField(blank=True)

    target_group = models.TextField(blank=True)

    benefits = models.TextField(blank=True)

    implementing_organization = models.CharField(
        max_length=200,
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(blank=True)

    start_date = models.DateField(
        blank=True,
        null=True
    )

    end_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )

    image = models.ImageField(
        upload_to="civic_programmes/",
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