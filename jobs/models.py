
from django.db import models


class JobOpportunity(models.Model):

    EMPLOYMENT_TYPES = [
        ("full_time", "Full-time"),
        ("part_time", "Part-time"),
        ("contract", "Contract"),
        ("temporary", "Temporary"),
        ("internship", "Internship"),
        ("apprenticeship", "Apprenticeship"),
        ("volunteer", "Volunteer"),
        ("remote", "Remote"),
    ]

    STATUS_CHOICES = [
        ("open", "Open"),
        ("closing_soon", "Closing Soon"),
        ("closed", "Closed"),
    ]

    SECTOR_CHOICES = [
        ("government", "Government"),
        ("health", "Health"),
        ("education", "Education"),
        ("agriculture", "Agriculture"),
        ("ict", "ICT & Technology"),
        ("finance", "Finance"),
        ("construction", "Construction"),
        ("transport", "Transport"),
        ("tourism", "Tourism & Wildlife"),
        ("trade", "Business & Trade"),
        ("energy", "Energy & Minerals"),
        ("security", "Security"),
        ("manufacturing", "Manufacturing"),
        ("ngo", "NGO / Development"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=255)

    organization = models.CharField(max_length=255)

    employment_type = models.CharField(
        max_length=30,
        choices=EMPLOYMENT_TYPES
    )

    sector = models.CharField(
        max_length=50,
        choices=SECTOR_CHOICES
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

    requirements = models.TextField(
        blank=True
    )

    responsibilities = models.TextField(
        blank=True
    )

    salary_information = models.CharField(
        max_length=255,
        blank=True
    )

    application_process = models.TextField(
        blank=True
    )

    application_url = models.URLField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    deadline = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    image = models.ImageField(
        upload_to="jobs/",
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
        return f"{self.title} - {self.organization}"


class SkillsOpportunity(models.Model):

    OPPORTUNITY_TYPES = [
        ("training", "Skills Training"),
        ("vocational", "Vocational Training"),
        ("digital", "Digital Skills"),
        ("entrepreneurship", "Entrepreneurship"),
        ("graduate", "Graduate Programme"),
        ("internship", "Internship"),
        ("apprenticeship", "Apprenticeship"),
        ("career", "Career Development"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("open", "Open"),
        ("ongoing", "Ongoing"),
        ("closed", "Closed"),
    ]

    title = models.CharField(
        max_length=255
    )

    organization = models.CharField(
        max_length=255
    )

    opportunity_type = models.CharField(
        max_length=40,
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

    target_group = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    benefits = models.TextField(
        blank=True
    )

    application_process = models.TextField(
        blank=True
    )

    application_url = models.URLField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    closing_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    image = models.ImageField(
        upload_to="jobs/skills/",
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


class EmploymentInformation(models.Model):

    INFORMATION_TYPES = [
        ("career", "Career Guidance"),
        ("cv", "CV & Resume"),
        ("interview", "Interview Preparation"),
        ("job_search", "Job Search"),
        ("workplace", "Workplace Information"),
        ("rights", "Employment Rights"),
        ("responsibilities", "Employment Responsibilities"),
        ("labour", "Labour Information"),
        ("skills", "Skills Development"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )

    summary = models.TextField()

    content = models.TextField()

    key_points = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
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
