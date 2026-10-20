from django import forms

from .models import WaterProblemReport,SanitationProblemReport,  EnvironmentalProblemReport,  PollutionReport


from django import forms

from .models import WaterProblemReport,DrainageWastewaterReport, EnvironmentalIncidentReport


class WaterProblemReportForm(forms.ModelForm):

    class Meta:

        model = WaterProblemReport

        fields = [
            "citizen_name",
            "phone_number",
            "problem_type",
            "description",
            "district",
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
                        "Describe the water problem in detail..."
                    ),
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
                    "placeholder": (
                        "Village, street, parish, "
                        "ward or neighbourhood"
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

            "problem_type": "Water Problem",

            "description": "Problem Description",

            "district": "District / City",

            "location": "Exact Location",

            "urgency": "Urgency Level",

            "photo": "Photo Evidence",
        }
        
        from .models import SanitationProblemReport


class SanitationProblemReportForm(forms.ModelForm):

    class Meta:

        model = SanitationProblemReport

        fields = [
            "citizen_name",
            "phone_number",
            "problem_type",
            "description",
            "district",
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
                    "placeholder": "Describe the sanitation problem...",
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
                    "placeholder": (
                        "Village, street, parish, "
                        "ward or neighbourhood"
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

            "problem_type": "Sanitation Problem",

            "description": "Problem Description",

            "district": "District / City",

            "location": "Exact Location",

            "urgency": "Urgency Level",

            "photo": "Photo Evidence",
        }
        
class EnvironmentalProblemReportForm(forms.ModelForm):

    class Meta:

        model = EnvironmentalProblemReport

        fields = [
            "citizen_name",
            "phone_number",
            "problem_type",
            "description",
            "district",
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
                        "Describe the environmental problem "
                        "in detail..."
                    ),
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
                    "placeholder": (
                        "Village, street, parish, "
                        "ward or neighbourhood"
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

            "problem_type": "Environmental Problem",

            "description": "Problem Description",

            "district": "District / City",

            "location": "Exact Location",

            "urgency": "Urgency Level",

            "photo": "Photo Evidence",
        }
        
class DrainageWastewaterReportForm(forms.ModelForm):

    class Meta:

        model = DrainageWastewaterReport

        fields = [
            "citizen_name",
            "phone_number",
            "problem_type",
            "description",
            "district",
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
                        "Describe the drainage or wastewater "
                        "problem in detail..."
                    ),
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Enter your district or city"
                    ),
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Village, street, parish, "
                        "sub-county or other location"
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
            "problem_type": "Problem Type",
            "description": "Problem Description",
            "district": "District / City",
            "location": "Exact Location",
            "urgency": "Urgency Level",
            "photo": "Photo Evidence",
        }
        
class PollutionReportForm(forms.ModelForm):

    class Meta:
        model = PollutionReport

        fields = [
            "citizen_name",
            "phone_number",
            "pollution_type",
            "description",
            "district",
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

            "pollution_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": (
                        "Describe the pollution problem "
                        "in detail..."
                    ),
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Enter your district or city"
                    ),
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Village, street, parish, "
                        "sub-county or other location"
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
            "pollution_type": "Pollution Type",
            "description": "Pollution Description",
            "district": "District / City",
            "location": "Exact Location",
            "urgency": "Urgency Level",
            "photo": "Photo Evidence",
        }
        
class EnvironmentalIncidentReportForm(forms.ModelForm):

    class Meta:
        model = EnvironmentalIncidentReport

        fields = [
            "citizen_name",
            "phone_number",
            "incident_type",
            "description",
            "district",
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
                        "Describe the environmental incident "
                        "and what you observed..."
                    ),
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
                    "placeholder": (
                        "Village, street, parish, "
                        "sub-county or other location"
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
            "location": "Exact Location",
            "urgency": "Urgency Level",
            "photo": "Photo Evidence",
        }