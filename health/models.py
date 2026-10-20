from django.db import models
from django.utils import timezone


# ============================================================
# 1. HEALTH FACILITIES
# ============================================================

class HealthFacility(models.Model):

    FACILITY_TYPES = [
        ("hospital", "Hospital"),
        ("health_centre", "Health Centre"),
        ("clinic", "Clinic"),
        ("dispensary", "Dispensary"),
        ("maternity", "Maternity Facility"),
        ("specialized", "Specialized Health Facility"),
        ("pharmacy", "Pharmacy"),
        ("laboratory", "Laboratory"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    facility_type = models.CharField(
        max_length=50,
        choices=FACILITY_TYPES
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    telephone = models.CharField(
        max_length=100,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    opening_hours = models.CharField(
        max_length=255,
        blank=True
    )

    emergency_available = models.BooleanField(
        default=False
    )

    services_information = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="health/facilities/",
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


# ============================================================
# 2. HEALTH SERVICES
# ============================================================

class HealthService(models.Model):

    SERVICE_TYPES = [
        ("outpatient", "Outpatient Services"),
        ("maternal", "Maternal Health"),
        ("child", "Child Health"),
        ("immunization", "Immunization"),
        ("laboratory", "Laboratory Services"),
        ("pharmacy", "Pharmacy Services"),
        ("dental", "Dental Services"),
        ("emergency", "Emergency Services"),
        ("community", "Community Health"),
        ("specialized", "Specialized Services"),
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

    availability_information = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="health/services/",
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


# ============================================================
# 3. MEDICINE INFORMATION
# ============================================================

class MedicineInformation(models.Model):

    AVAILABILITY_STATUS = [
        ("available", "Available"),
        ("limited", "Limited Availability"),
        ("unavailable", "Currently Unavailable"),
        ("unknown", "Availability Unknown"),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField()

    availability_status = models.CharField(
        max_length=30,
        choices=AVAILABILITY_STATUS,
        default="unknown"
    )

    facility = models.ForeignKey(
        HealthFacility,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="medicine_information"
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    last_updated = models.DateTimeField(
        default=timezone.now
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


# ============================================================
# 4. MEDICAL EQUIPMENT
# ============================================================

class MedicalEquipment(models.Model):

    STATUS_CHOICES = [
        ("available", "Available"),
        ("limited", "Limited Availability"),
        ("maintenance", "Under Maintenance"),
        ("unavailable", "Unavailable"),
        ("unknown", "Status Unknown"),
    ]

    title = models.CharField(max_length=200)

    equipment_type = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField()

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="unknown"
    )

    facility = models.ForeignKey(
        HealthFacility,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="medical_equipment"
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="health/equipment/",
        blank=True,
        null=True
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


# ============================================================
# 5. CITIZEN HEALTH REQUESTS
# ============================================================

class HealthRequest(models.Model):

    REQUEST_TYPES = [
        ("general", "General Health Request"),
        ("appointment", "Appointment Request"),
        ("referral", "Referral Inquiry"),
        ("service", "Health Service Request"),
        ("information", "Health Information Request"),
        ("facility", "Health Facility Inquiry"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("pending", "Pending"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen_name = models.CharField(
        max_length=200
    )

    citizen_email = models.EmailField(
        blank=True
    )

    citizen_phone = models.CharField(
        max_length=30,
        blank=True
    )

    request_type = models.CharField(
        max_length=50,
        choices=REQUEST_TYPES
    )

    facility = models.ForeignKey(
        HealthFacility,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="health_requests"
    )

    subject = models.CharField(
        max_length=255
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100,
        blank=True
    )

    status = models.CharField(
        max_length=30,
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
            last_request = (
                HealthRequest.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_request.id + 1
                if last_request
                else 1
            )

            self.reference_number = (
                f"HR-{next_id:08d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference_number


# ============================================================
# 6. HOSPITAL / HEALTH FACILITY REPORTS
# ============================================================

class HealthFacilityReport(models.Model):

    REPORT_TYPES = [
        ("poor_service", "Poor Service"),
        ("long_waiting", "Long Waiting Time"),
        ("medicine", "Medicine Problem"),
        ("equipment", "Medical Equipment Problem"),
        ("unavailable_service", "Unavailable Health Service"),
        ("cleanliness", "Facility Cleanliness"),
        ("water_sanitation", "Water / Sanitation Problem"),
        ("emergency", "Emergency Service Problem"),
        ("infrastructure", "Facility Infrastructure Problem"),
        ("staff_service", "Staff / Service Concern"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("pending", "Pending"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    reference_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    reporter_name = models.CharField(
        max_length=200
    )

    reporter_email = models.EmailField(
        blank=True
    )

    reporter_phone = models.CharField(
        max_length=30,
        blank=True
    )

    facility = models.ForeignKey(
        HealthFacility,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="citizen_reports"
    )

    report_type = models.CharField(
        max_length=50,
        choices=REPORT_TYPES
    )

    subject = models.CharField(
        max_length=255
    )

    description = models.TextField()

    district = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    incident_date = models.DateField(
        null=True,
        blank=True
    )

    evidence = models.ImageField(
        upload_to="health/reports/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
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

            last_report = (
                HealthFacilityReport.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_report.id + 1
                if last_report
                else 1
            )

            self.reference_number = (
                f"HFR-{next_id:08d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference_number


# ============================================================
# 7. HEALTH PROJECTS & PROGRAMMES
# ============================================================

class HealthProject(models.Model):

    PROJECT_TYPES = [
        ("facility", "Health Facility Development"),
        ("equipment", "Medical Equipment"),
        ("medicine", "Medicine Programme"),
        ("maternal", "Maternal Health"),
        ("child", "Child Health"),
        ("community", "Community Health"),
        ("infrastructure", "Health Infrastructure"),
        ("staffing", "Health Staffing Initiative"),
        ("public_health", "Public Health Programme"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("suspended", "Suspended"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(max_length=255)

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPES
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
        max_length=255,
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

    start_date = models.DateField(
        null=True,
        blank=True
    )

    expected_completion_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="planned"
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="health/projects/",
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


# ============================================================
# 8. HEALTH INFORMATION
# ============================================================

class HealthInformation(models.Model):

    INFORMATION_TYPES = [
        ("general", "General Health Information"),
        ("maternal", "Maternal Health"),
        ("child", "Child Health"),
        ("community", "Community Health"),
        ("prevention", "Preventive Health"),
        ("public_health", "Public Health"),
        ("awareness", "Health Awareness"),
        ("guidance", "Health Guidance"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    information_type = models.CharField(
        max_length=50,
        choices=INFORMATION_TYPES
    )

    summary = models.TextField()

    description = models.TextField()

    key_points = models.TextField(
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

    image = models.ImageField(
        upload_to="health/information/",
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


# ============================================================
# 9. EMERGENCY INFORMATION
# ============================================================

class HealthEmergencyInformation(models.Model):

    title = models.CharField(
        max_length=255
    )

    emergency_type = models.CharField(
        max_length=150
    )

    description = models.TextField()

    emergency_number = models.CharField(
        max_length=100,
        blank=True
    )

    facility = models.ForeignKey(
        HealthFacility,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="emergency_information"
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

    website = models.URLField(
        blank=True
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