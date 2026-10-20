from django.db import models


# ============================================================
# 1. EDUCATION INSTITUTIONS
# ============================================================

class EducationInstitution(models.Model):

    INSTITUTION_TYPES = [
        ("primary", "Primary School"),
        ("secondary", "Secondary School"),
        ("tveta", "TVET Institution"),
        ("university", "University"),
        ("college", "College"),
        ("vocational", "Vocational Institution"),
        ("special_needs", "Special Needs Institution"),
        ("other", "Other"),
    ]

    OWNERSHIP_CHOICES = [
        ("government", "Government"),
        ("private", "Private"),
        ("community", "Community"),
        ("other", "Other"),
    ]

    name = models.CharField(
        max_length=250
    )

    institution_type = models.CharField(
        max_length=50,
        choices=INSTITUTION_TYPES
    )

    ownership = models.CharField(
        max_length=30,
        choices=OWNERSHIP_CHOICES,
        default="government"
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    programs = models.TextField(
        blank=True,
        help_text="Separate programs/services using commas."
    )

    opening_hours = models.CharField(
        max_length=200,
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
        ordering = ["name"]

    def __str__(self):
        return self.name


# ============================================================
# 2. EDUCATION REQUESTS
# ============================================================

class EducationRequest(models.Model):

    REQUEST_TYPES = [
        ("information", "Education Information"),
        ("admission", "Admission Inquiry"),
        ("institution", "Institution Inquiry"),
        ("complaint", "Education Complaint"),
        ("scholarship", "Scholarship Inquiry"),
        ("teacher", "Teacher / Staff Inquiry"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("in_progress", "In Progress"),
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
    ]

    request_type = models.CharField(
        max_length=40,
        choices=REQUEST_TYPES
    )

    citizen_name = models.CharField(
        max_length=200
    )

    citizen_phone = models.CharField(
        max_length=30,
        blank=True
    )

    citizen_district = models.CharField(
        max_length=100,
        blank=True
    )

    institution = models.ForeignKey(
        EducationInstitution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="education_requests"
    )

    description = models.TextField()

    reference_number = models.CharField(
        max_length=60,
        unique=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="submitted"
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.reference_number} - {self.citizen_name}"


# ============================================================
# 3. EDUCATION PROGRAMMES & COURSES
# ============================================================

class EducationProgramme(models.Model):

    PROGRAMME_TYPES = [
        ("primary", "Primary Education"),
        ("secondary", "Secondary Education"),
        ("certificate", "Certificate"),
        ("diploma", "Diploma"),
        ("degree", "Degree"),
        ("postgraduate", "Postgraduate"),
        ("vocational", "Vocational Training"),
        ("technical", "Technical Programme"),
        ("short_course", "Short Course"),
        ("skills", "Skills Development"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    programme_type = models.CharField(
        max_length=50,
        choices=PROGRAMME_TYPES
    )

    institution = models.ForeignKey(
        EducationInstitution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="education_programmes"
    )

    description = models.TextField()

    requirements = models.TextField(
        blank=True
    )

    duration = models.CharField(
        max_length=150,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    district = models.CharField(
        max_length=100,
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
# 4. SCHOLARSHIPS, BURSARIES & STUDENT OPPORTUNITIES
# ============================================================

class ScholarshipOpportunity(models.Model):

    OPPORTUNITY_TYPES = [
        ("scholarship", "Scholarship"),
        ("bursary", "Bursary"),
        ("grant", "Education Grant"),
        ("student_support", "Student Support"),
        ("loan", "Education Loan"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("open", "Open"),
        ("upcoming", "Upcoming"),
        ("closed", "Closed"),
        ("completed", "Completed"),
    ]

    title = models.CharField(
        max_length=255
    )

    opportunity_type = models.CharField(
        max_length=50,
        choices=OPPORTUNITY_TYPES
    )

    provider = models.CharField(
        max_length=255
    )

    description = models.TextField()

    eligibility = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    target_group = models.CharField(
        max_length=255,
        blank=True
    )

    funding_information = models.TextField(
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

    district = models.CharField(
        max_length=100,
        blank=True
    )

    opening_date = models.DateField(
        null=True,
        blank=True
    )

    closing_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="open"
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
# 5. TEACHERS' SERVICES
# ============================================================

class TeacherService(models.Model):

    SERVICE_TYPES = [
        ("training", "Teacher Training"),
        ("professional_development", "Professional Development"),
        ("teaching_resources", "Teaching Resources"),
        ("career", "Teacher Career Services"),
        ("opportunity", "Teacher Opportunities"),
        ("registration", "Teacher Registration"),
        ("guidance", "Teacher Guidance"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_TYPES
    )

    description = models.TextField()

    eligibility = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    access_information = models.TextField(
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

    provider = models.CharField(
        max_length=255,
        blank=True
    )

    district = models.CharField(
        max_length=100,
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
        ordering = ["title"]

    def __str__(self):
        return self.title


# ============================================================
# 6. SCHOOL ADMINISTRATORS' SERVICES
# ============================================================

class AdministratorService(models.Model):

    SERVICE_TYPES = [
        ("school_management", "School Management"),
        ("administration", "Administrative Service"),
        ("reporting", "Education Reporting"),
        ("school_improvement", "School Improvement"),
        ("planning", "Education Planning"),
        ("training", "Administrator Training"),
        ("guidance", "Administrative Guidance"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_TYPES
    )

    description = models.TextField()

    eligibility = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    access_information = models.TextField(
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

    provider = models.CharField(
        max_length=255,
        blank=True
    )

    district = models.CharField(
        max_length=100,
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
        ordering = ["title"]

    def __str__(self):
        return self.title


# ============================================================
# 7. EDUCATION FUNDING
# ============================================================

class EducationFunding(models.Model):

    FUNDING_TYPES = [
        ("government", "Government Funding"),
        ("school", "School Funding"),
        ("student", "Student Financial Support"),
        ("scholarship", "Scholarship Funding"),
        ("bursary", "Bursary Funding"),
        ("grant", "Education Grant"),
        ("loan", "Education Loan"),
        ("infrastructure", "Infrastructure Funding"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("available", "Available"),
        ("open", "Open for Application"),
        ("upcoming", "Upcoming"),
        ("closed", "Closed"),
        ("completed", "Completed"),
    ]

    title = models.CharField(
        max_length=255
    )

    funding_type = models.CharField(
        max_length=50,
        choices=FUNDING_TYPES
    )

    provider = models.CharField(
        max_length=255
    )

    description = models.TextField()

    eligibility = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    funding_information = models.TextField(
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

    target_group = models.CharField(
        max_length=255,
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    opening_date = models.DateField(
        null=True,
        blank=True
    )

    closing_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="available"
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
# 8. EXAMINATIONS & ACADEMIC INFORMATION
# ============================================================

class ExaminationInformation(models.Model):

    INFORMATION_TYPES = [
        ("registration", "Examination Registration"),
        ("timetable", "Examination Timetable"),
        ("results", "Examination Results"),
        ("requirements", "Examination Requirements"),
        ("guidance", "Examination Guidance"),
        ("academic_calendar", "Academic Calendar"),
        ("notice", "Examination Notice"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    information_type = models.CharField(
        max_length=50,
        choices=INFORMATION_TYPES
    )

    description = models.TextField()

    requirements = models.TextField(
        blank=True
    )

    access_information = models.TextField(
        blank=True
    )

    important_dates = models.TextField(
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

    published_date = models.DateField(
        null=True,
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


# ============================================================
# 9. EDUCATION SERVICES & REQUIREMENTS
# ============================================================

class EducationService(models.Model):

    SERVICE_TYPES = [
        ("admission", "Admission"),
        ("registration", "Registration"),
        ("transfer", "School Transfer"),
        ("certification", "Certification"),
        ("student_service", "Student Service"),
        ("teacher_service", "Teacher Service"),
        ("institution_service", "Institution Service"),
        ("guidance", "Education Guidance"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

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

    access_information = models.TextField(
        blank=True
    )

    required_documents = models.TextField(
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


# ============================================================
# 10. GOVERNMENT EDUCATION PROGRAMMES
# ============================================================

class GovernmentEducationProgramme(models.Model):

    PROGRAMME_TYPES = [
        ("student", "Student Programme"),
        ("teacher", "Teacher Programme"),
        ("school", "School Programme"),
        ("skills", "Skills Development Programme"),
        ("infrastructure", "Education Infrastructure Programme"),
        ("funding", "Education Funding Programme"),
        ("community", "Community Education Programme"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("open", "Open"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("closed", "Closed"),
    ]

    title = models.CharField(
        max_length=255
    )

    programme_type = models.CharField(
        max_length=50,
        choices=PROGRAMME_TYPES
    )

    description = models.TextField()

    objectives = models.TextField(
        blank=True
    )

    target_group = models.CharField(
        max_length=255,
        blank=True
    )

    eligibility = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    registration_information = models.TextField(
        blank=True
    )

    registration_process = models.TextField(
        blank=True
    )

    registration_url = models.URLField(
        blank=True
    )

    contact_information = models.TextField(
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

    start_date = models.DateField(
        null=True,
        blank=True
    )

    closing_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="planned"
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
# 11. EDUCATION REGISTRATION & APPLICATIONS
# ============================================================

class EducationApplication(models.Model):

    APPLICATION_TYPES = [
        ("admission", "Admission"),
        ("programme", "Programme Registration"),
        ("scholarship", "Scholarship Application"),
        ("bursary", "Bursary Application"),
        ("funding", "Education Funding"),
        ("government_programme", "Government Programme"),
        ("teacher_service", "Teacher Service"),
        ("administrator_service", "Administrator Service"),
        ("education_service", "Education Service"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("received", "Received"),
        ("under_review", "Under Review"),
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    reference_number = models.CharField(
        max_length=60,
        unique=True
    )

    applicant_name = models.CharField(
        max_length=200
    )

    applicant_phone = models.CharField(
        max_length=30,
        blank=True
    )

    applicant_email = models.EmailField(
        blank=True
    )

    applicant_district = models.CharField(
        max_length=100,
        blank=True
    )

    application_type = models.CharField(
        max_length=50,
        choices=APPLICATION_TYPES
    )

    institution = models.ForeignKey(
        EducationInstitution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="education_applications"
    )

    programme = models.ForeignKey(
        EducationProgramme,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="applications"
    )

    subject = models.CharField(
        max_length=255
    )

    description = models.TextField()

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="submitted"
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.reference_number} - {self.applicant_name}"


# ============================================================
# 12. EDUCATION PROJECTS & INFRASTRUCTURE
# ============================================================

class EducationProject(models.Model):

    PROJECT_TYPES = [
        ("school", "School Development"),
        ("classroom", "Classroom Construction"),
        ("laboratory", "Laboratory"),
        ("library", "Library"),
        ("ict", "ICT Infrastructure"),
        ("water_sanitation", "Water & Sanitation"),
        ("accessibility", "Accessibility Infrastructure"),
        ("equipment", "Education Equipment"),
        ("teacher_housing", "Teacher Housing"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("suspended", "Suspended"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(
        max_length=255
    )

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPES
    )

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
# 13. EDUCATION UPDATES & NOTICES
# ============================================================

class EducationNotice(models.Model):

    NOTICE_TYPES = [
        ("general", "General Education Notice"),
        ("examination", "Examination Notice"),
        ("registration", "Registration Notice"),
        ("scholarship", "Scholarship Notice"),
        ("programme", "Programme Notice"),
        ("teacher", "Teacher Notice"),
        ("administrator", "Administrator Notice"),
        ("school", "School Notice"),
        ("deadline", "Deadline Notice"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    notice_type = models.CharField(
        max_length=50,
        choices=NOTICE_TYPES
    )

    summary = models.TextField()

    content = models.TextField()

    important_date = models.DateField(
        null=True,
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    published_date = models.DateField(
        null=True,
        blank=True
    )

    is_important = models.BooleanField(
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
# 14. CITIZEN EDUCATION PROBLEM REPORTS
# ============================================================

class EducationProblemReport(models.Model):

    REPORT_TYPES = [
        ("infrastructure", "Infrastructure Problem"),
        ("classroom", "Classroom Problem"),
        ("water_sanitation", "Water / Sanitation Problem"),
        ("learning_materials", "Learning Materials Problem"),
        ("ict", "ICT Problem"),
        ("accessibility", "Accessibility Problem"),
        ("service_delivery", "Education Service Concern"),
        ("facility", "School Facility Problem"),
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
        max_length=60,
        unique=True
    )

    reporter_name = models.CharField(
        max_length=200
    )

    reporter_phone = models.CharField(
        max_length=30,
        blank=True
    )

    reporter_email = models.EmailField(
        blank=True
    )

    report_type = models.CharField(
        max_length=50,
        choices=REPORT_TYPES
    )

    institution = models.ForeignKey(
        EducationInstitution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="problem_reports"
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

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="submitted"
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.reference_number} - {self.subject}"


# ============================================================
# 15. EDUCATION INFORMATION & GUIDANCE
# ============================================================

class EducationInformation(models.Model):

    INFORMATION_TYPES = [
        ("student", "Student Guidance"),
        ("parent", "Parent Guidance"),
        ("teacher", "Teacher Guidance"),
        ("administrator", "Administrator Guidance"),
        ("career", "Career Guidance"),
        ("admission", "Admission Guidance"),
        ("learning", "Learning Guidance"),
        ("education_service", "Education Service Guidance"),
        ("general", "General Education Information"),
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

    practical_steps = models.TextField(
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
# 16. EDUCATION STATISTICS & REPORTS
# ============================================================

class EducationStatistic(models.Model):

    STATISTIC_TYPES = [
        ("institutions", "Education Institutions"),
        ("primary", "Primary Schools"),
        ("secondary", "Secondary Schools"),
        ("tvet", "TVET Institutions"),
        ("universities", "Universities"),
        ("colleges", "Colleges"),
        ("vocational", "Vocational Institutions"),
        ("special_needs", "Special Needs Institutions"),
        ("teachers", "Teachers"),
        ("students", "Students"),
        ("programmes", "Education Programmes"),
        ("projects", "Education Projects"),
        ("funding", "Education Funding"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=255
    )

    statistic_type = models.CharField(
        max_length=50,
        choices=STATISTIC_TYPES
    )

    value = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=100,
        blank=True
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    source = models.CharField(
        max_length=255,
        blank=True
    )

    source_url = models.URLField(
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
        ordering = ["-year", "title"]

    def __str__(self):
        return self.title
    
class LearningResource(models.Model):

    EDUCATION_LEVEL_CHOICES = [
        ("primary", "Primary School"),
        ("secondary", "Secondary School"),
        ("tvet", "TVET / Vocational"),
        ("tertiary", "University / Tertiary"),
        ("teacher", "Teacher Resources"),
        ("general", "General Learning"),
    ]

    PRIMARY_CLASS_CHOICES = [
        ("p1", "Primary 1"),
        ("p2", "Primary 2"),
        ("p3", "Primary 3"),
        ("p4", "Primary 4"),
        ("p5", "Primary 5"),
        ("p6", "Primary 6"),
        ("p7", "Primary 7"),
    ]

    SECONDARY_CLASS_CHOICES = [
        ("s1", "Senior 1"),
        ("s2", "Senior 2"),
        ("s3", "Senior 3"),
        ("s4", "Senior 4"),
        ("s5", "Senior 5"),
        ("s6", "Senior 6"),
    ]

    RESOURCE_TYPE_CHOICES = [
        ("notes", "Notes"),
        ("textbook", "Textbook / Book"),
        ("exercise", "Exercises"),
        ("revision", "Revision Materials"),
        ("past_paper", "Past Paper"),
        ("answer_guide", "Answer Guide"),
        ("lesson", "Lesson Material"),
        ("video", "Educational Video"),
        ("audio", "Educational Audio"),
        ("course", "Course Material"),
        ("research", "Research Material"),
        ("library", "Digital Library"),
        ("website", "Learning Website"),
        ("other", "Other"),
    ]

    ACCESS_TYPE_CHOICES = [
        ("online", "Access Online"),
        ("download", "Download"),
        ("both", "Online and Download"),
        ("physical", "Physical Location"),
        ("external", "External Learning Platform"),
    ]

    LANGUAGE_CHOICES = [
        ("english", "English"),
        ("luganda", "Luganda"),
        ("swahili", "Swahili"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=300
    )

    education_level = models.CharField(
        max_length=30,
        choices=EDUCATION_LEVEL_CHOICES
    )

    class_level = models.CharField(
        max_length=20,
        blank=True,
        help_text="For example P1, P7, S1, S4 or S6."
    )

    subject = models.CharField(
        max_length=150,
        blank=True
    )

    topic = models.CharField(
        max_length=250,
        blank=True
    )

    resource_type = models.CharField(
        max_length=40,
        choices=RESOURCE_TYPE_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    learning_objectives = models.TextField(
        blank=True,
        help_text="What the learner should understand or achieve."
    )

    access_type = models.CharField(
        max_length=30,
        choices=ACCESS_TYPE_CHOICES,
        default="online"
    )

    resource_url = models.URLField(
        blank=True,
        help_text="Official or legitimate online learning resource URL."
    )

    download_file = models.FileField(
        upload_to="education/learning_resources/",
        blank=True,
        null=True
    )

    source_organization = models.CharField(
        max_length=250,
        blank=True,
        help_text="Organization, institution or platform providing the resource."
    )

    language = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES,
        default="english"
    )

    publication_year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    access_instructions = models.TextField(
        blank=True,
        help_text="Explain to learners how they can access or use this resource."
    )

    thumbnail = models.ImageField(
        upload_to="education/learning_resources/thumbnails/",
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
        ordering = ["-is_featured", "-created_at"]
        verbose_name = "Learning Resource"
        verbose_name_plural = "Learning Resources"

    def __str__(self):
        return self.title