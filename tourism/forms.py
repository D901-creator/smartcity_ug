from django import forms

from .models import( TourismDestination,CulturalHeritageSite,TourismService

,TourismEvent,
    WildlifeConservationInformation,
    TourismProjectOpportunity,
)
class TourismDestinationForm(forms.ModelForm):

    class Meta:
        model = TourismDestination

        fields = [
            "title",
            "destination_type",
            "district",
            "location",
            "summary",
            "description",
            "attractions",
            "activities",
            "visitor_information",
            "opening_information",
            "contact_information",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Short summary of the destination"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Detailed description"
                }
            ),

            "attractions": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Main attractions"
                }
            ),

            "activities": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Activities visitors can undertake"
                }
            ),

            "visitor_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Important visitor information"
                }
            ),

            "opening_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Opening hours or visiting information"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),
        }
        
class TourismServiceForm(forms.ModelForm):

    class Meta:
        model = TourismService

        fields = [
            "title",
            "service_type",
            "district",
            "location",
            "summary",
            "description",
            "services_offered",
            "facilities",
            "contact_information",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Short summary of this tourism service"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Detailed description"
                }
            ),

            "services_offered": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Services offered"
                }
            ),

            "facilities": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Facilities available"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),
        }


class CulturalHeritageSiteForm(forms.ModelForm):

    class Meta:
        model = CulturalHeritageSite

        fields = [
            "title",
            "site_type",
            "district",
            "location",
            "summary",
            "description",
            "historical_information",
            "cultural_significance",
            "visitor_information",
            "activities",
            "contact_information",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Short summary of the heritage site"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Detailed description"
                }
            ),

            "historical_information": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Historical information"
                }
            ),

            "cultural_significance": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Cultural significance"
                }
            ),

            "visitor_information": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Visitor information"
                }
            ),

            "activities": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Activities available"
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Contact information"
                }
            ),
        }
        
class TourismEventForm(forms.ModelForm):

    class Meta:
        model = TourismEvent

        fields = [
            "title",
            "event_type",
            "district",
            "location",
            "summary",
            "description",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "organizer",
            "contact_information",
            "website",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "start_time": forms.TimeInput(
                attrs={"type": "time"}
            ),

            "end_time": forms.TimeInput(
                attrs={"type": "time"}
            ),

            "summary": forms.Textarea(
                attrs={"rows": 3}
            ),

            "description": forms.Textarea(
                attrs={"rows": 6}
            ),

            "contact_information": forms.Textarea(
                attrs={"rows": 3}
            ),
        }


class WildlifeConservationInformationForm(forms.ModelForm):

    class Meta:
        model = WildlifeConservationInformation

        fields = [
            "title",
            "conservation_type",
            "district",
            "location",
            "summary",
            "description",
            "wildlife_information",
            "conservation_actions",
            "community_information",
            "important_information",
            "contact_information",
            "website",
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

            "wildlife_information": forms.Textarea(
                attrs={"rows": 5}
            ),

            "conservation_actions": forms.Textarea(
                attrs={"rows": 5}
            ),

            "community_information": forms.Textarea(
                attrs={"rows": 4}
            ),

            "important_information": forms.Textarea(
                attrs={"rows": 4}
            ),

            "contact_information": forms.Textarea(
                attrs={"rows": 3}
            ),
        }


class TourismProjectOpportunityForm(forms.ModelForm):

    class Meta:
        model = TourismProjectOpportunity

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
            "summary": forms.Textarea(
                attrs={"rows": 3}
            ),

            "description": forms.Textarea(
                attrs={"rows": 6}
            ),

            "objectives": forms.Textarea(
                attrs={"rows": 4}
            ),

            "benefits": forms.Textarea(
                attrs={"rows": 4}
            ),

            "requirements": forms.Textarea(
                attrs={"rows": 4}
            ),

            "contact_information": forms.Textarea(
                attrs={"rows": 3}
            ),

            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "closing_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }