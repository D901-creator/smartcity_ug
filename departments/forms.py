
from django import forms

from .models import Department, Service


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["ministry", "name", "code", "description", "is_active"]
        widgets = {
            "ministry": forms.Select(attrs={"class": "form-select"}),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Department name",
            }),
            "code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Unique department code",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "department",
            "sector",
            "name",
            "code",
            "description",
            "is_active",
        ]
        widgets = {
            "department": forms.Select(attrs={"class": "form-select"}),
            "sector": forms.Select(attrs={"class": "form-select"}),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Service name",
            }),
            "code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Unique service code",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }
