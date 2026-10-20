from django import forms

from .models import ElectricityProblemReport,EnergyMineralRequest


class ElectricityProblemReportForm(forms.ModelForm):

    class Meta:
        model = ElectricityProblemReport

        fields = [
            "citizen_name",
            "phone_number",
            "district",
            "location",
            "problem_type",
            "description",
            "image",
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

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your district or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the exact location of the problem",
                }
            ),

            "problem_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": (
                        "Describe the electricity problem "
                        "and any important details."
                    ),
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }

        labels = {
            "citizen_name": "Your Name",
            "phone_number": "Phone Number",
            "district": "District / City",
            "location": "Problem Location",
            "problem_type": "Problem Type",
            "description": "Problem Description",
            "image": "Photo Evidence (Optional)",
        }
        
class EnergyMineralRequestForm(forms.ModelForm):

    class Meta:
        model = EnergyMineralRequest

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
                    "placeholder": "Village, town, area or specific location",
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the subject of your request",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": (
                        "Describe your request, report or "
                        "the information you need..."
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
            "citizen_name": "Full Name",
            "phone_number": "Phone Number",
            "email": "Email Address",
            "district": "District / City",
            "location": "Location",
            "request_type": "Request / Report Type",
            "subject": "Subject",
            "description": "Description",
            "attachment": "Attachment / Evidence",
        }

        help_texts = {
            "email": "Optional.",
            "location": "Optional, but recommended.",
            "attachment": (
                "Optional. You may attach supporting evidence "
                "or a relevant file."
            ),
        }