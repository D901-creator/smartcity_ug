from django import forms

from .models import (
    EducationInstitution,
    EducationRequest,
    EducationProgramme,
    ScholarshipOpportunity,
    TeacherService,
    AdministratorService,
    EducationFunding,
    ExaminationInformation,
    EducationService,
    GovernmentEducationProgramme,
    EducationApplication,
    EducationProject,
    EducationNotice,
    EducationProblemReport,
    EducationInformation,
    LearningResource,
)


# ============================================================
# COMMON FORM STYLING
# ============================================================

class EducationFormMixin:

    def apply_bootstrap(self):
        for field in self.fields.values():

            existing_class = field.widget.attrs.get("class", "")

            field.widget.attrs["class"] = (
                f"{existing_class} form-control".strip()
            )

            if isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = (
                    f"{existing_class} form-select".strip()
                )

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = (
                    f"{existing_class} form-check-input".strip()
                )

            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs["class"] = (
                    f"{existing_class} form-control".strip()
                )


# ============================================================
# 1. EDUCATION INSTITUTION
# ============================================================

class EducationInstitutionForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationInstitution

        fields = [
            "name",
            "institution_type",
            "ownership",
            "district",
            "location",
            "phone_number",
            "email",
            "website",
            "description",
            "programs",
            "opening_hours",
            "is_active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter institution name"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "Enter district"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "Enter location"
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "Enter telephone number"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter email address"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Describe the institution"
                }
            ),

            "programs": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "List programmes or services"
                }
            ),

            "opening_hours": forms.TextInput(
                attrs={
                    "placeholder": "Example: Monday - Friday, 8:00 AM - 5:00 PM"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 2. EDUCATION REQUEST
# ============================================================

class EducationRequestForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationRequest

        fields = [
            "request_type",
            "citizen_name",
            "citizen_phone",
            "citizen_district",
            "institution",
            "description",
        ]

        widgets = {

            "citizen_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name"
                }
            ),

            "citizen_phone": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number"
                }
            ),

            "citizen_district": forms.TextInput(
                attrs={
                    "placeholder": "Enter your district"
                }
            ),

            "institution": forms.Select(
                attrs={}
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe your request"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["institution"].queryset = (
            EducationInstitution.objects.filter(
                is_active=True
            ).order_by("name")
        )

        self.apply_bootstrap()


# ============================================================
# 3. EDUCATION PROGRAMMES & COURSES
# ============================================================

class EducationProgrammeForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationProgramme

        fields = [
            "title",
            "programme_type",
            "institution",
            "description",
            "requirements",
            "duration",
            "location",
            "district",
            "application_process",
            "application_url",
            "contact_information",
            "start_date",
            "closing_date",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Programme or course title"
                }
            ),

            "institution": forms.Select(),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the programme"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Enter admission or programme requirements"
                }
            ),

            "duration": forms.TextInput(
                attrs={
                    "placeholder": "Example: 2 years"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "Programme location"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Explain how to apply"
                }
            ),

            "application_url": forms.URLInput(
                attrs={
                    "placeholder": "Official application website"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Phone, email or office contact"
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "closing_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["institution"].queryset = (
            EducationInstitution.objects.filter(
                is_active=True
            ).order_by("name")
        )

        self.apply_bootstrap()


# ============================================================
# 4. SCHOLARSHIPS & BURSARIES
# ============================================================

class ScholarshipOpportunityForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = ScholarshipOpportunity

        fields = [
            "title",
            "opportunity_type",
            "provider",
            "description",
            "eligibility",
            "requirements",
            "target_group",
            "funding_information",
            "application_process",
            "application_url",
            "contact_information",
            "district",
            "opening_date",
            "closing_date",
            "status",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Scholarship or bursary title"
                }
            ),

            "provider": forms.TextInput(
                attrs={
                    "placeholder": "Scholarship provider"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the opportunity"
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Who is eligible?"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Application requirements"
                }
            ),

            "target_group": forms.TextInput(
                attrs={
                    "placeholder": "Example: Secondary students"
                }
            ),

            "funding_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Explain the financial support"
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Explain how to apply"
                }
            ),

            "application_url": forms.URLInput(
                attrs={
                    "placeholder": "Official application link"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "opening_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "closing_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 5. TEACHERS' SERVICES
# ============================================================

class TeacherServiceForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = TeacherService

        fields = [
            "title",
            "service_type",
            "description",
            "eligibility",
            "requirements",
            "access_information",
            "application_process",
            "application_url",
            "contact_information",
            "provider",
            "district",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Teacher service title"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the teacher service"
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Who can access this service?"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Service requirements"
                }
            ),

            "access_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Explain how teachers can access this service"
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Application procedure"
                }
            ),

            "application_url": forms.URLInput(
                attrs={
                    "placeholder": "Official website or application link"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "provider": forms.TextInput(
                attrs={
                    "placeholder": "Service provider"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 6. SCHOOL ADMINISTRATORS' SERVICES
# ============================================================

class AdministratorServiceForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = AdministratorService

        fields = [
            "title",
            "service_type",
            "description",
            "eligibility",
            "requirements",
            "access_information",
            "application_process",
            "application_url",
            "contact_information",
            "provider",
            "district",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Administrator service title"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the service"
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Who can access this service?"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Service requirements"
                }
            ),

            "access_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "How administrators can access the service"
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Application process"
                }
            ),

            "application_url": forms.URLInput(
                attrs={
                    "placeholder": "Official website or application link"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "provider": forms.TextInput(
                attrs={
                    "placeholder": "Service provider"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 7. EDUCATION FUNDING
# ============================================================

class EducationFundingForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationFunding

        fields = [
            "title",
            "funding_type",
            "provider",
            "description",
            "eligibility",
            "requirements",
            "funding_information",
            "application_process",
            "application_url",
            "contact_information",
            "target_group",
            "district",
            "opening_date",
            "closing_date",
            "status",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Education funding title"
                }
            ),

            "provider": forms.TextInput(
                attrs={
                    "placeholder": "Funding provider"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the funding"
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Eligibility criteria"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Requirements"
                }
            ),

            "funding_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Funding details"
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "How to apply"
                }
            ),

            "application_url": forms.URLInput(
                attrs={
                    "placeholder": "Official application website"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "target_group": forms.TextInput(
                attrs={
                    "placeholder": "Target group"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "opening_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "closing_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 8. EXAMINATIONS & ACADEMIC INFORMATION
# ============================================================

class ExaminationInformationForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = ExaminationInformation

        fields = [
            "title",
            "information_type",
            "description",
            "requirements",
            "access_information",
            "important_dates",
            "contact_information",
            "website",
            "district",
            "published_date",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Examination information title"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the examination information"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Examination requirements"
                }
            ),

            "access_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Explain how citizens can access this information"
                }
            ),

            "important_dates": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Important examination dates"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "placeholder": "Official website"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "published_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 9. EDUCATION SERVICES & REQUIREMENTS
# ============================================================

class EducationServiceForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationService

        fields = [
            "title",
            "service_type",
            "summary",
            "description",
            "eligibility",
            "requirements",
            "application_process",
            "access_information",
            "required_documents",
            "contact_information",
            "website",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Education service title"
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Short summary"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the service"
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Eligibility"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Requirements"
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Application process"
                }
            ),

            "access_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "How citizens can access this service"
                }
            ),

            "required_documents": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Required documents"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "placeholder": "Official website"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 10. GOVERNMENT EDUCATION PROGRAMMES
# ============================================================

class GovernmentEducationProgrammeForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = GovernmentEducationProgramme

        fields = [
            "title",
            "programme_type",
            "description",
            "objectives",
            "target_group",
            "eligibility",
            "requirements",
            "registration_information",
            "registration_process",
            "registration_url",
            "contact_information",
            "implementing_organization",
            "district",
            "start_date",
            "closing_date",
            "status",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Government education programme"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the programme"
                }
            ),

            "objectives": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Programme objectives"
                }
            ),

            "target_group": forms.TextInput(
                attrs={
                    "placeholder": "Who is the programme for?"
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Eligibility requirements"
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Required documents or conditions"
                }
            ),

            "registration_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Registration information"
                }
            ),

            "registration_process": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Explain how citizens register"
                }
            ),

            "registration_url": forms.URLInput(
                attrs={
                    "placeholder": "Official registration website"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "implementing_organization": forms.TextInput(
                attrs={
                    "placeholder": "Implementing organization"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "closing_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 11. EDUCATION APPLICATIONS
# ============================================================

class EducationApplicationForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = EducationApplication

        fields = [
            "applicant_name",
            "applicant_phone",
            "applicant_email",
            "applicant_district",
            "application_type",
            "institution",
            "programme",
            "subject",
            "description",
        ]

        widgets = {

            "applicant_name": forms.TextInput(
                attrs={
                    "placeholder": "Applicant full name"
                }
            ),

            "applicant_phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone number"
                }
            ),

            "applicant_email": forms.EmailInput(
                attrs={
                    "placeholder": "Email address"
                }
            ),

            "applicant_district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "institution": forms.Select(),

            "programme": forms.Select(),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "Application subject"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe your application"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["institution"].queryset = (
            EducationInstitution.objects.filter(
                is_active=True
            ).order_by("name")
        )

        self.fields["programme"].queryset = (
            EducationProgramme.objects.filter(
                is_published=True
            ).order_by("title")
        )

        self.apply_bootstrap()


# ============================================================
# 12. EDUCATION PROJECTS & INFRASTRUCTURE
# ============================================================

class EducationProjectForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationProject

        fields = [
            "title",
            "project_type",
            "description",
            "objectives",
            "expected_benefits",
            "implementing_organization",
            "district",
            "location",
            "start_date",
            "expected_completion_date",
            "status",
            "contact_information",
            "website",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Education project title"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe the project"
                }
            ),

            "objectives": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Project objectives"
                }
            ),

            "expected_benefits": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Expected benefits"
                }
            ),

            "implementing_organization": forms.TextInput(
                attrs={
                    "placeholder": "Implementing organization"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "Project location"
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "expected_completion_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "placeholder": "Project website"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 13. EDUCATION UPDATES & NOTICES
# ============================================================

class EducationNoticeForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = EducationNotice

        fields = [
            "title",
            "notice_type",
            "summary",
            "content",
            "important_date",
            "district",
            "contact_information",
            "website",
            "published_date",
            "is_important",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Notice title"
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Short notice summary"
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "rows": 7,
                    "placeholder": "Full notice content"
                }
            ),

            "important_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "placeholder": "Official website"
                }
            ),

            "published_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


# ============================================================
# 14. EDUCATION PROBLEM REPORT
# ============================================================

class EducationProblemReportForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = EducationProblemReport

        fields = [
            "reporter_name",
            "reporter_phone",
            "reporter_email",
            "report_type",
            "institution",
            "subject",
            "description",
            "district",
            "location",
            "incident_date",
        ]

        widgets = {

            "reporter_name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name"
                }
            ),

            "reporter_phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone number"
                }
            ),

            "reporter_email": forms.EmailInput(
                attrs={
                    "placeholder": "Email address"
                }
            ),

            "institution": forms.Select(),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "Briefly describe the problem"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Provide details about the education problem"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "Location of the problem"
                }
            ),

            "incident_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["institution"].queryset = (
            EducationInstitution.objects.filter(
                is_active=True
            ).order_by("name")
        )

        self.apply_bootstrap()


# ============================================================
# 15. EDUCATION INFORMATION & GUIDANCE
# ============================================================

class EducationInformationForm(
    EducationFormMixin,
    forms.ModelForm
):

    class Meta:
        model = EducationInformation

        fields = [
            "title",
            "information_type",
            "summary",
            "description",
            "key_points",
            "practical_steps",
            "contact_information",
            "website",
            "district",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Information title"
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Short summary"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Detailed information"
                }
            ),

            "key_points": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Important points"
                }
            ),

            "practical_steps": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Practical steps citizens can follow"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "placeholder": "Official website"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "placeholder": "District"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()
        
class LearningResourceForm(EducationFormMixin, forms.ModelForm):

    class Meta:
        model = LearningResource

        fields = [
            "title",
            "education_level",
            "class_level",
            "subject",
            "topic",
            "resource_type",
            "description",
            "learning_objectives",
            "access_type",
            "resource_url",
            "download_file",
            "source_organization",
            "language",
            "publication_year",
            "access_instructions",
            "thumbnail",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Describe what this learning resource contains..."
            }),

            "learning_objectives": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "What should the learner understand or achieve?"
            }),

            "access_instructions": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Explain how learners can access and use this resource..."
            }),

            "class_level": forms.TextInput(attrs={
                "placeholder": "For example P1, P5, P7, S1, S4, S6"
            }),

            "subject": forms.TextInput(attrs={
                "placeholder": "For example Mathematics, Science, English"
            }),

            "topic": forms.TextInput(attrs={
                "placeholder": "For example Fractions, Living Things, Grammar"
            }),

            "resource_url": forms.URLInput(attrs={
                "placeholder": "https://..."
            }),

            "publication_year": forms.NumberInput(attrs={
                "placeholder": "For example 2026"
            }),
        }
        
        