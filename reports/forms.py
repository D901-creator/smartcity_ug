from django import forms

from .models import CitizenReport


class CitizenReportForm(forms.ModelForm):

    class Meta:
        model = CitizenReport

        fields = [
            "title",
            "description",
            "department",
            "location",
            "priority",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter report title",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe the problem or issue...",
                }
            ),

            "department": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Responsible department",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Where did this happen?",
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
        
        
class OfficerReportUpdateForm(forms.ModelForm):
    class Meta:
        model = CitizenReport
        fields = ["status", "official_response"]

        widgets = {
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
            "official_response": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter the official response...",
                }
            ),
        }

        