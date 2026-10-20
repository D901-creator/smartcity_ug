from django.db import models
import uuid

class FinancialPlanningInformation(models.Model):

    INFORMATION_TYPES = [
        ("financial_planning", "Financial Planning"),
        ("financial_management", "Financial Management"),
        ("business_finance", "Business Finance"),
        ("household_finance", "Household Financial Guidance"),
        ("public_finance", "Public Financial Information"),
        ("financial_programme", "Financial Programme"),
        ("investment_guidance", "Investment Guidance"),
        ("general", "General Financial Information"),
    ]

    title = models.CharField(max_length=200)

    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    requirements = models.TextField(
        blank=True
    )

    planning_process = models.TextField(
        blank=True,
        help_text="Explain the financial planning process where applicable."
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
    
    import uuid

from django.db import models


class BusinessRegistrationInformation(models.Model):

    INFORMATION_TYPES = [
        ("registration", "Business Registration"),
        ("requirements", "Registration Requirements"),
        ("procedure", "Registration Procedure"),
        ("business_name", "Business Name Information"),
        ("licensing", "Business Licensing"),
        ("tax_information", "Business Tax Information"),
        ("compliance", "Business Compliance"),
        ("general", "General Business Information"),
    ]

    title = models.CharField(max_length=200)

    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    requirements = models.TextField(
        blank=True
    )

    registration_process = models.TextField(
        blank=True
    )

    fees_information = models.TextField(
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


class BusinessRegistrationRequest(models.Model):

    BUSINESS_TYPES = [
        ("sole_proprietorship", "Sole Proprietorship"),
        ("partnership", "Partnership"),
        ("company", "Company"),
        ("cooperative", "Cooperative"),
        ("other", "Other"),
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

    business_name = models.CharField(
        max_length=200
    )

    business_type = models.CharField(
        max_length=40,
        choices=BUSINESS_TYPES
    )

    business_location = models.CharField(
        max_length=255
    )

    business_description = models.TextField()

    proposed_activities = models.TextField(
        blank=True
    )

    supporting_information = models.TextField(
        blank=True
    )

    supporting_document = models.FileField(
        upload_to="business_registration/",
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
                f"BR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.business_name}"
    
class TradeMarketInformation(models.Model):

    INFORMATION_TYPES = [
        ("trade_services", "Trade Services"),
        ("market_information", "Market Information"),
        ("market_opportunity", "Market Opportunity"),
        ("market_facility", "Market Facility"),
        ("trade_guidance", "Trade Guidance"),
        ("trade_requirements", "Trade Requirements"),
        ("market_prices", "Market Prices & Information"),
        ("general", "General Trade Information"),
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

    process_information = models.TextField(
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


class TradeMarketRequest(models.Model):

    REQUEST_TYPES = [
        ("trade_information", "Trade Information"),
        ("market_information", "Market Information"),
        ("market_access", "Market Access"),
        ("trade_support", "Trade Support"),
        ("market_facility", "Market Facility Request"),
        ("trade_complaint", "Trade Complaint"),
        ("market_complaint", "Market Complaint"),
        ("general", "General Trade / Market Request"),
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
        blank=True
    )

    request_type = models.CharField(
        max_length=40,
        choices=REQUEST_TYPES
    )

    subject = models.CharField(
        max_length=200
    )

    description = models.TextField()

    supporting_information = models.TextField(
        blank=True
    )

    attachment = models.FileField(
        upload_to="trade_market_requests/",
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
                f"TMR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.subject}"
    
class CooperativeInformation(models.Model):

    INFORMATION_TYPES = [
        ("cooperative_services", "Cooperative Services"),
        ("registration", "Cooperative Registration"),
        ("requirements", "Cooperative Requirements"),
        ("guidance", "Cooperative Guidance"),
        ("support", "Cooperative Support"),
        ("opportunities", "Cooperative Opportunities"),
        ("programmes", "Cooperative Programmes"),
        ("finance", "Cooperative Finance"),
        ("general", "General Cooperative Information"),
    ]

    title = models.CharField(max_length=200)
    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )
    district = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255, blank=True)

    summary = models.TextField()
    description = models.TextField()

    requirements = models.TextField(blank=True)
    application_process = models.TextField(blank=True)
    support_information = models.TextField(blank=True)
    contact_information = models.TextField(blank=True)

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class CooperativeRequest(models.Model):

    REQUEST_TYPES = [
        ("registration", "Cooperative Registration"),
        ("registration_information", "Registration Information"),
        ("support", "Cooperative Support"),
        ("finance", "Cooperative Finance"),
        ("training", "Training Request"),
        ("membership", "Cooperative Membership"),
        ("market_access", "Market Access"),
        ("programme", "Cooperative Programme"),
        ("complaint", "Cooperative Complaint"),
        ("general", "General Cooperative Request"),
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

    citizen_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    district = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)

    cooperative_name = models.CharField(
        max_length=200,
        blank=True
    )

    request_type = models.CharField(
        max_length=40,
        choices=REQUEST_TYPES
    )

    subject = models.CharField(max_length=200)

    description = models.TextField()

    supporting_information = models.TextField(
        blank=True
    )

    attachment = models.FileField(
        upload_to="cooperative_requests/",
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
                f"COR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.subject}"
    
class EconomicProject(models.Model):

    PROJECT_TYPES = [
        ("business_development", "Business Development"),
        ("trade_development", "Trade Development"),
        ("cooperative_development", "Cooperative Development"),
        ("market_development", "Market Development"),
        ("industrial_development", "Industrial Development"),
        ("investment", "Investment"),
        ("employment", "Employment & Job Creation"),
        ("infrastructure", "Economic Infrastructure"),
        ("community_economic", "Community Economic Development"),
        ("other", "Other Economic Project"),
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
        max_length=50,
        choices=PROJECT_TYPES
    )

    district = models.CharField(max_length=100)

    location = models.CharField(
        max_length=255,
        blank=True
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

    partners = models.TextField(
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
        upload_to="economic_projects/",
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
    
class FundingBudgetInformation(models.Model):

    INFORMATION_TYPES = [
        ("funding_opportunity", "Funding Opportunity"),
        ("grant", "Grant"),
        ("loan", "Loan / Financing"),
        ("funding_programme", "Funding Programme"),
        ("budget_guidance", "Budgeting Guidance"),
        ("financial_guidance", "Financial Guidance"),
        ("investment_information", "Investment Information"),
        ("eligibility", "Eligibility Information"),
        ("general", "General Funding Information"),
    ]

    title = models.CharField(max_length=200)

    information_type = models.CharField(
        max_length=40,
        choices=INFORMATION_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    organization = models.CharField(
        max_length=200,
        blank=True
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

    funding_amount_information = models.TextField(
        blank=True
    )

    deadline = models.DateField(
        blank=True,
        null=True
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


class FundingBudgetRequest(models.Model):

    REQUEST_TYPES = [
        ("funding_information", "Funding Information"),
        ("grant_application", "Grant Application"),
        ("financing", "Financing Request"),
        ("business_funding", "Business Funding"),
        ("project_funding", "Project Funding"),
        ("budget_guidance", "Budget Guidance"),
        ("investment_support", "Investment Support"),
        ("general", "General Funding Request"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("under_review", "Under Review"),
        ("additional_information", "Additional Information Required"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
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
        blank=True
    )

    request_type = models.CharField(
        max_length=40,
        choices=REQUEST_TYPES
    )

    subject = models.CharField(
        max_length=200
    )

    description = models.TextField()

    requested_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True
    )

    purpose_of_funding = models.TextField(
        blank=True
    )

    supporting_information = models.TextField(
        blank=True
    )

    attachment = models.FileField(
        upload_to="funding_budget_requests/",
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
                f"FBR-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.subject}"
class EconomicFinancialRecord(models.Model):

    FINANCIAL_TYPES = [
        ("budget", "Budget"),
        ("funding", "Funding"),
        ("grant", "Grant"),
        ("loan", "Loan"),
        ("investment", "Investment"),
        ("project", "Economic Project"),
        ("expenditure", "Expenditure"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("allocated", "Allocated"),
        ("approved", "Approved"),
        ("disbursed", "Disbursed"),
        ("spent", "Spent"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(
        max_length=200
    )

    financial_type = models.CharField(
        max_length=30,
        choices=FINANCIAL_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    organization = models.CharField(
        max_length=200,
        blank=True
    )

    project_name = models.CharField(
        max_length=200,
        blank=True
    )

    financial_year = models.CharField(
        max_length=20,
        help_text="Example: 2026/2027"
    )

    allocated_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    approved_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    disbursed_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    spent_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    @property
    def remaining_amount(self):
        return (
            self.allocated_amount
            - self.spent_amount
        )

    def __str__(self):
        return (
            f"{self.title} - "
            f"{self.financial_year}"
        )