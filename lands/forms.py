from django import forms
from .models import( LandTitleApplication, LandPropertyRequest, 
                    DevelopmentBuildingApplication,
                    
                    UrbanPlanningInformation,  HousingInformation,HousingPropertyRequest
)

class LandTitleApplicationForm(forms.ModelForm):

    class Meta:
        model = LandTitleApplication

        fields = [
            "applicant_name",
            "phone_number",
            "email",
            "district",
            "location",
            "application_type",
            "land_reference",
            "description",
            "supporting_information",
            "attachment",
        ]

        widgets = {
            "applicant_name": forms.TextInput(
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
                    "placeholder": "Enter district or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Village, parish, town or municipality",
                }
            ),

            "application_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "land_reference": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Plot / Block / Title number if known",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe what you need help with...",
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Add any additional information...",
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        
class LandPropertyRequestForm(forms.ModelForm):

    class Meta:
        model = LandPropertyRequest

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "request_type",
            "property_reference",
            "subject",
            "description",
            "supporting_information",
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
                    "placeholder": "Enter district or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Village, parish, town or municipality",
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "property_reference": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Plot / Block / Title number if known",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Brief subject of your request",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Explain your land or property request...",
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Add any additional information...",
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        
class HousingInformationForm(forms.ModelForm):

    class Meta:
        model = HousingInformation

        fields = [
            "title",
            "information_type",
            "district",
            "summary",
            "description",
            "requirements",
            "application_process",
            "contact_information",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Housing information title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe the housing service or information.",
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "List requirements or documents.",
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Explain the general application or access process.",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information.",
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
        
class HousingPropertyRequestForm(forms.ModelForm):

    class Meta:
        model = HousingPropertyRequest

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "request_type",
            "property_reference",
            "subject",
            "description",
            "supporting_information",
            "attachment",
        ]

        widgets = {
            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name",
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
                    "placeholder": "your@email.com",
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
                    "placeholder": "Village, parish, town or municipality",
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "property_reference": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Plot number or property reference if known",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Brief subject of your request",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Explain your housing or property request...",
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Add any additional information...",
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        
class UrbanPlanningInformationForm(forms.ModelForm):

    class Meta:
        model = UrbanPlanningInformation

        fields = [
            "title",
            "information_type",
            "district",
            "location",
            "summary",
            "description",
            "requirements",
            "planning_process",
            "important_information",
            "contact_information",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Urban planning information title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
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
                    "placeholder": "City, municipality or town",
                }
            ),

            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe the planning information...",
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Planning requirements or documents...",
                }
            ),

            "planning_process": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Explain the general planning process...",
                }
            ),

            "important_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Important information citizens should know...",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Contact information...",
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
class DevelopmentBuildingApplicationForm(forms.ModelForm):

    class Meta:
        model = DevelopmentBuildingApplication

        fields = [
            "applicant_name",
            "phone_number",
            "email",
            "district",
            "location",
            "property_reference",
            "application_type",
            "project_title",
            "proposed_development",
            "estimated_project_value",
            "additional_information",
            "supporting_document",
        ]

        widgets = {
            "applicant_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Applicant full name",
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
                    "placeholder": "your@email.com",
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
                    "placeholder": "Location of proposed development",
                }
            ),

            "property_reference": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Plot / block / title reference if known",
                }
            ),

            "application_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "project_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Name or title of the proposed project",
                }
            ),

            "proposed_development": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Describe the proposed development...",
                }
            ),

            "estimated_project_value": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Estimated value",
                    "step": "0.01",
                }
            ),

            "additional_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Any additional information...",
                }
            ),

            "supporting_document": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }