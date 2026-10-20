
from django import forms
from django.utils import timezone

from .models import CalendarEvent


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = [
            "title",
            "description",
            "category",
            "status",
            "start_time",
            "end_time",
            "location",
            "reminder_minutes",
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. Community inspection",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Event details and instructions",
            }),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "start_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Office, district or meeting location",
            }),
            "reminder_minutes": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
                "step": 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        datetime_format = "%Y-%m-%dT%H:%M"

        self.fields["start_time"].input_formats = [datetime_format]
        self.fields["end_time"].input_formats = [datetime_format]

        if timezone.is_naive(timezone.now()):
            return

        if not self.is_bound:
            for field_name in ("start_time", "end_time"):
                value = getattr(self.instance, field_name, None)

                if value:
                    self.initial[field_name] = timezone.localtime(
                        value
                    ).strftime(datetime_format)

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")

        if start and end and end <= start:
            self.add_error(
                "end_time",
                "The end time must be after the start time.",
            )

        return cleaned_data
