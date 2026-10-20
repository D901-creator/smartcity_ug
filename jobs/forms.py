from django import forms

from .models import (
    JobOpportunity,
    SkillsTrainingOpportunity,
    CareerEmploymentInformation,
)


class JobOpportunityForm(forms.ModelForm):
    class Meta:
        model = JobOpportunity
        fields = [
            "title",
            "opportunity_type",
            "organization",
            "sector",
            "description",
            "requirements",
            "responsibilities",
            "location",
            "district",
            "application_process",
            "application_url",
            "contact_information",
            "salary_information",
            "posted_date",
            "closing_date",
            "status",
            "featured",
            "published",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "requirements": forms.Textarea(attrs={"rows": 4}),
            "responsibilities": forms.Textarea(attrs={"rows": 4}),
            "application_process": forms.Textarea(attrs={"rows": 4}),
            "contact_information": forms.Textarea(attrs={"rows": 3}),
        }


class SkillsTrainingOpportunityForm(forms.ModelForm):
    class Meta:
        model = SkillsTrainingOpportunity
        fields = [
            "title",
            "training_type",
            "provider",
            "description",
            "target_group",
            "requirements",
            "duration",
            "location",
            "district",
            "application_process",
            "application_url",
            "contact_information",
            "start_date",
            "closing_date",
            "status",
            "featured",
            "published",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "target_group": forms.Textarea(attrs={"rows": 3}),
            "requirements": forms.Textarea(attrs={"rows": 4}),
            "application_process": forms.Textarea(attrs={"rows": 4}),
            "contact_information": forms.Textarea(attrs={"rows": 3}),
        }


class CareerEmploymentInformationForm(
    forms.ModelForm
):
    class Meta:
        model = CareerEmploymentInformation
        fields = [
            "title",
            "information_type",
            "summary",
            "description",
            "key_points",
            "practical_steps",
            "contact_information",
            "website",
            "featured",
            "published",
        ]

        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 5}),
            "key_points": forms.Textarea(attrs={"rows": 5}),
            "practical_steps": forms.Textarea(attrs={"rows": 5}),
            "contact_information": forms.Textarea(attrs={"rows": 3}),
        }