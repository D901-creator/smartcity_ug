from django import forms

from .models import (ICTService, ICTOpportunity,ICTInfrastructure,ICTInnovation,NationalGuidanceInformation,
    CivicProgramme,)


class ICTServiceForm(forms.ModelForm):

    class Meta:
        model = ICTService

        fields = [
            "title",
            "service_type",
            "summary",
            "description",
            "eligibility",
            "requirements",
            "application_process",
            "fees_information",
            "contact_information",
            "website",
            "district",
            "location",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "summary": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "rows": 5
                }
            ),

            "fees_information": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),
        }
        
class ICTInfrastructureForm(forms.ModelForm):

    class Meta:
        model = ICTInfrastructure

        fields = [
            "title",
            "infrastructure_type",
            "district",
            "location",
            "summary",
            "description",
            "services_available",
            "coverage_information",
            "contact_information",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 5}),
            "services_available": forms.Textarea(attrs={"rows": 4}),
            "coverage_information": forms.Textarea(attrs={"rows": 4}),
            "contact_information": forms.Textarea(attrs={"rows": 3}),
        }


class ICTInnovationForm(forms.ModelForm):

    class Meta:
        model = ICTInnovation

        fields = [
            "title",
            "innovation_type",
            "district",
            "location",
            "summary",
            "description",
            "objectives",
            "target_group",
            "benefits",
            "contact_information",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 5}),
            "objectives": forms.Textarea(attrs={"rows": 4}),
            "target_group": forms.Textarea(attrs={"rows": 3}),
            "benefits": forms.Textarea(attrs={"rows": 4}),
            "contact_information": forms.Textarea(attrs={"rows": 3}),
        }


class ICTOpportunityForm(forms.ModelForm):

    class Meta:
        model = ICTOpportunity

        fields = [
            "title",
            "opportunity_type",
            "district",
            "location",
            "summary",
            "description",
            "objectives",
            "benefits",
            "requirements",
            "application_process",
            "implementing_organization",
            "contact_information",
            "website",
            "start_date",
            "closing_date",
            "status",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 5}),
            "objectives": forms.Textarea(attrs={"rows": 4}),
            "benefits": forms.Textarea(attrs={"rows": 4}),
            "requirements": forms.Textarea(attrs={"rows": 4}),
            "application_process": forms.Textarea(attrs={"rows": 5}),
            "contact_information": forms.Textarea(attrs={"rows": 3}),
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "closing_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
        
class NationalGuidanceInformationForm(forms.ModelForm):

    class Meta:
        model = NationalGuidanceInformation

        fields = [
            "title",
            "information_type",
            "summary",
            "description",
            "key_points",
            "citizen_responsibilities",
            "related_information",
            "contact_information",
            "website",
            "district",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(
                attrs={"rows": 3}
            ),
            "description": forms.Textarea(
                attrs={"rows": 6}
            ),
            "key_points": forms.Textarea(
                attrs={"rows": 5}
            ),
            "citizen_responsibilities": forms.Textarea(
                attrs={"rows": 5}
            ),
            "related_information": forms.Textarea(
                attrs={"rows": 4}
            ),
            "contact_information": forms.Textarea(
                attrs={"rows": 3}
            ),
        }


class CivicProgrammeForm(forms.ModelForm):

    class Meta:
        model = CivicProgramme

        fields = [
            "title",
            "programme_type",
            "summary",
            "description",
            "objectives",
            "target_group",
            "benefits",
            "implementing_organization",
            "district",
            "location",
            "contact_information",
            "website",
            "start_date",
            "end_date",
            "status",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(
                attrs={"rows": 3}
            ),
            "description": forms.Textarea(
                attrs={"rows": 6}
            ),
            "objectives": forms.Textarea(
                attrs={"rows": 4}
            ),
            "target_group": forms.Textarea(
                attrs={"rows": 3}
            ),
            "benefits": forms.Textarea(
                attrs={"rows": 4}
            ),
            "contact_information": forms.Textarea(
                attrs={"rows": 3}
            ),
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }