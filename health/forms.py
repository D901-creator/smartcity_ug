from django import forms

from .models import (
    HealthFacility,
    HealthService,
    MedicineInformation,
    MedicalEquipment,
    HealthRequest,
    HealthFacilityReport,
    HealthProject,
    HealthInformation,
    HealthEmergencyInformation,
)


# ============================================================
# 1. HEALTH FACILITY FORM
# ============================================================

class HealthFacilityForm(forms.ModelForm):

    class Meta:
        model = HealthFacility

        fields = [
            "title",
            "facility_type",
            "description",
            "district",
            "city",
            "location",
            "address",
            "telephone",
            "email",
            "website",
            "opening_hours",
            "emergency_available",
            "services_information",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Health facility name",
                }
            ),

            "facility_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe the health facility",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "City",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Location",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Physical address",
                }
            ),

            "telephone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Telephone number",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "opening_hours": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Monday - Sunday, 24 hours",
                }
            ),

            "services_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Services available at this facility",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


# ============================================================
# 2. HEALTH SERVICE FORM
# ============================================================

class HealthServiceForm(forms.ModelForm):

    class Meta:
        model = HealthService

        fields = [
            "title",
            "service_type",
            "summary",
            "description",
            "eligibility",
            "requirements",
            "availability_information",
            "contact_information",
            "district",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Health service name",
                }
            ),

            "service_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Short summary of the service",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Detailed description",
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Who can access this service?",
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Requirements for accessing the service",
                }
            ),

            "availability_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "When and where the service is available",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


# ============================================================
# 3. MEDICINE INFORMATION FORM
# ============================================================

class MedicineInformationForm(forms.ModelForm):

    class Meta:
        model = MedicineInformation

        fields = [
            "title",
            "category",
            "description",
            "availability_status",
            "facility",
            "district",
            "contact_information",
            "last_updated",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Medicine or medical supply name",
                }
            ),

            "category": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Medicine category",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Information about the medicine",
                }
            ),

            "availability_status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "facility": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information",
                }
            ),

            "last_updated": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


# ============================================================
# 4. MEDICAL EQUIPMENT FORM
# ============================================================

class MedicalEquipmentForm(forms.ModelForm):

    class Meta:
        model = MedicalEquipment

        fields = [
            "title",
            "equipment_type",
            "description",
            "status",
            "facility",
            "district",
            "contact_information",
            "image",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Equipment name",
                }
            ),

            "equipment_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Equipment type",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe the equipment",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "facility": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


# ============================================================
# 5. CITIZEN HEALTH REQUEST FORM
# ============================================================

class HealthRequestForm(forms.ModelForm):

    class Meta:
        model = HealthRequest

        fields = [
            "citizen_name",
            "citizen_email",
            "citizen_phone",
            "request_type",
            "facility",
            "subject",
            "description",
            "district",
        ]

        widgets = {
            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name",
                }
            ),

            "citizen_email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your email address",
                }
            ),

            "citizen_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "facility": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "What is your request about?",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": (
                        "Explain your health request clearly. "
                        "Do not include confidential medical information."
                    ),
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),
        }


# ============================================================
# 6. CITIZEN HOSPITAL / HEALTH FACILITY REPORT FORM
# ============================================================

class HealthFacilityReportForm(forms.ModelForm):

    class Meta:
        model = HealthFacilityReport

        fields = [
            "reporter_name",
            "reporter_email",
            "reporter_phone",
            "facility",
            "report_type",
            "subject",
            "description",
            "district",
            "location",
            "incident_date",
            "evidence",
        ]

        widgets = {
            "reporter_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name",
                }
            ),

            "reporter_email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your email address",
                }
            ),

            "reporter_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "facility": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "report_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short description of the issue",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 7,
                    "placeholder": (
                        "Describe what happened, where it happened, "
                        "and any useful details for review. "
                        "Do not include confidential patient information."
                    ),
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Specific location within the facility",
                }
            ),

            "incident_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "evidence": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()

        if len(description) < 10:
            raise forms.ValidationError(
                "Please provide enough information to help review the report."
            )

        return description


# ============================================================
# 7. HEALTH PROJECT FORM
# ============================================================

class HealthProjectForm(forms.ModelForm):

    class Meta:
        model = HealthProject

        fields = [
            "title",
            "project_type",
            "summary",
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
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Project or programme name",
                }
            ),

            "project_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Short project summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Detailed project description",
                }
            ),

            "objectives": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Project objectives",
                }
            ),

            "expected_benefits": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Expected benefits to citizens",
                }
            ),

            "implementing_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Implementing organization",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Project location",
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "expected_completion_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information",
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


# ============================================================
# 8. HEALTH INFORMATION FORM
# ============================================================

class HealthInformationForm(forms.ModelForm):

    class Meta:
        model = HealthInformation

        fields = [
            "title",
            "information_type",
            "summary",
            "description",
            "key_points",
            "contact_information",
            "website",
            "district",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Health information title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Short summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Detailed health information",
                }
            ),

            "key_points": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Important points or guidance",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information",
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


# ============================================================
# 9. HEALTH EMERGENCY INFORMATION FORM
# ============================================================

class HealthEmergencyInformationForm(forms.ModelForm):

    class Meta:
        model = HealthEmergencyInformation

        fields = [
            "title",
            "emergency_type",
            "description",
            "emergency_number",
            "facility",
            "district",
            "location",
            "contact_information",
            "website",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency information title",
                }
            ),

            "emergency_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency type",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Emergency information",
                }
            ),

            "emergency_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency telephone number",
                }
            ),

            "facility": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Location",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Additional contact information",
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }