from django import forms

from .models import RoadProblemReport, TrafficIncidentReport


class RoadProblemReportForm(forms.ModelForm):

    class Meta:
        model = RoadProblemReport

        fields = [
            "citizen_name",
            "phone_number",
            "problem_type",
            "description",
            "district",
            "road_name",
            "location",
            "urgency",
            "photo",
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
                        "Describe the road problem clearly..."
                    ),
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district or city",
                }
            ),

            "road_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter road name",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Village, street, parish, "
                        "town or nearby landmark"
                    ),
                }
            ),

            "urgency": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }

        labels = {
            "citizen_name": "Your Name",
            "phone_number": "Phone Number",
            "problem_type": "Road Problem Type",
            "description": "Problem Description",
            "district": "District / City",
            "road_name": "Road Name",
            "location": "Exact Location",
            "urgency": "Urgency Level",
            "photo": "Photo Evidence",
        }
class TrafficIncidentReportForm(forms.ModelForm):

    class Meta:
        model = TrafficIncidentReport

        fields = [
            "citizen_name",
            "phone_number",
            "incident_type",
            "description",
            "district",
            "road_name",
            "location",
            "urgency",
            "photo",
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
                        "Describe what happened and provide "
                        "as much useful information as possible..."
                    ),
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district or city",
                }
            ),

            "road_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter road name",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Street, village, trading centre, "
                        "landmark or nearby location"
                    ),
                }
            ),

            "urgency": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }

        labels = {
            "citizen_name": "Your Name",
            "phone_number": "Phone Number",
            "incident_type": "Incident Type",
            "description": "Incident Description",
            "district": "District / City",
            "road_name": "Road Name",
            "location": "Exact Location",
            "urgency": "Urgency Level",
            "photo": "Photo Evidence",
        }