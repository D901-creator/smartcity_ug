from django import forms

from .models import CitizenRequest


class CitizenRequestForm(forms.ModelForm):

    class Meta:
        model = CitizenRequest

        fields = [
            "title",
            "description",
            "department",
            "location",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "What service or action are you requesting?",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your request...",
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
                    "placeholder": "Location, if applicable",
                }
            ),
        }