from django import forms

from .models import (SecurityIncidentReport,EmergencySafetyInformation, 
                     CommunitySafetyProgramme, SecurityAdvisory,
 MissingPersonCommunityNotice,SecurityFacilityContact,SecurityReportRequest,
)
class SecurityIncidentReportForm(forms.ModelForm):

    class Meta:
        model = SecurityIncidentReport

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "incident_type",
            "description",
            "attachment",
        ]

        widgets = {
            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your full name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@email.com",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your district or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Where did the incident occur?",
                }
            ),

            "incident_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": (
                        "Describe what happened, including "
                        "any important details."
                    ),
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

        labels = {
            "citizen_name": "Your Full Name",
            "phone_number": "Phone Number",
            "email": "Email Address",
            "district": "District / City",
            "location": "Incident Location",
            "incident_type": "Incident Type",
            "description": "Incident Description",
            "attachment": "Supporting File / Image",
        }
        
class EmergencySafetyInformationForm(forms.ModelForm):

    class Meta:
        model = EmergencySafetyInformation

        fields = [
            "title",
            "category",
            "district",
            "summary",
            "information",
            "emergency_number",
            "contact_name",
            "contact_organization",
            "address",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Information title",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District / City",
                }
            ),

            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short summary",
                }
            ),

            "information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Enter the safety information...",
                }
            ),

            "emergency_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency contact number",
                }
            ),

            "contact_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contact person",
                }
            ),

            "contact_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Organization",
                }
            ),

            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Physical address",
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
        
class CommunitySafetyProgrammeForm(forms.ModelForm):

    class Meta:
        model = CommunitySafetyProgramme

        fields = [
            "title",
            "programme_type",
            "district",
            "location",
            "summary",
            "description",
            "objectives",
            "participating_organization",
            "contact_information",
            "start_date",
            "end_date",
            "status",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Programme title",
                }
            ),

            "programme_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District / City",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Programme location",
                }
            ),

            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short programme summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe the programme...",
                }
            ),

            "objectives": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Programme objectives...",
                }
            ),

            "participating_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Organization responsible",
                }
            ),

            "contact_information": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone, email or other contact",
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "end_date": forms.DateInput(
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
class SecurityAdvisoryForm(forms.ModelForm):

    class Meta:
        model = SecurityAdvisory

        fields = [
            "title",
            "advisory_type",
            "district",
            "location",
            "summary",
            "message",
            "recommended_action",
            "issuing_organization",
            "contact_information",
            "priority",
            "image",
            "start_date",
            "end_date",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Advisory title"
                }
            ),

            "advisory_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District / City"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Specific location, if applicable"
                }
            ),

            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short advisory summary"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Enter the full security advisory..."
                }
            ),

            "recommended_action": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "What should citizens do?"
                }
            ),

            "issuing_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Issuing organization"
                }
            ),

            "contact_information": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone, email or other contact"
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "start_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "end_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }
        
class MissingPersonCommunityNoticeForm(forms.ModelForm):

    class Meta:
        model = MissingPersonCommunityNotice

        fields = [
            "title",
            "notice_type",
            "district",
            "location",
            "summary",
            "description",
            "person_name",
            "age",
            "gender",
            "physical_description",
            "last_seen_location",
            "last_seen_date",
            "contact_information",
            "issuing_organization",
            "image",
            "status",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Notice title"
                }
            ),

            "notice_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District / City"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Relevant location"
                }
            ),

            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short notice summary"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Enter the full notice..."
                }
            ),

            "person_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Full name, if applicable"
                }
            ),

            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Age"
                }
            ),

            "gender": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Gender"
                }
            ),

            "physical_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Physical description or identifying information"
                }
            ),

            "last_seen_location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Where was the person last seen?"
                }
            ),

            "last_seen_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "contact_information": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone, email or other contact"
                }
            ),

            "issuing_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Issuing organization"
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }
class SecurityFacilityContactForm(forms.ModelForm):

    class Meta:
        model = SecurityFacilityContact

        fields = [
            "name",
            "facility_type",
            "district",
            "city",
            "location",
            "address",
            "description",
            "phone_number",
            "emergency_number",
            "email",
            "website",
            "operating_hours",
            "contact_person",
            "image",
            "is_emergency_facility",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Facility name"
                }
            ),

            "facility_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District"
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "City / Municipality"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Location"
                }
            ),

            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Physical address"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe the facility and services..."
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "General phone number"
                }
            ),

            "emergency_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Emergency contact number"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address"
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com"
                }
            ),

            "operating_hours": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 24 hours / Monday-Friday 8:00-17:00"
                }
            ),

            "contact_person": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contact person"
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "is_emergency_facility": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }
        
class SecurityReportRequestForm(forms.ModelForm):

    class Meta:
        model = SecurityReportRequest

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "request_type",
            "subject",
            "description",
            "attachment",
        ]

        widgets = {

            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your full name"
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@email.com"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District / City"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Specific location, if applicable"
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "What is your request about?"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": (
                        "Describe your security request or concern "
                        "in detail..."
                    )
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }

        labels = {
            "citizen_name": "Your Full Name",
            "phone_number": "Phone Number",
            "email": "Email Address",
            "district": "District / City",
            "location": "Location",
            "request_type": "Request Type",
            "subject": "Subject",
            "description": "Description",
            "attachment": "Supporting File / Image",
        }