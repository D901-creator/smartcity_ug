from django import forms

from .models import (
    PortalConfiguration,
    PortalModule,
    PortalMenuItem,
)


class PortalConfigurationForm(forms.ModelForm):
    class Meta:
        model = PortalConfiguration
        fields = [
            "display_name",
            "welcome_message",
            "is_enabled",
            "maintenance_enabled",
            "maintenance_message",
        ]
        widgets = {
            "display_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "welcome_message": forms.Textarea(
                attrs={"class": "form-control", "rows": 2}
            ),
            "maintenance_message": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "is_enabled": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "maintenance_enabled": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


class PortalModuleForm(forms.ModelForm):
    class Meta:
        model = PortalModule
        fields = [
            "code",
            "name",
            "description",
            "is_enabled",
            "display_order",
        ]
        widgets = {
            "code": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 2}
            ),
            "is_enabled": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
        }


class PortalMenuItemForm(forms.ModelForm):
    class Meta:
        model = PortalMenuItem
        fields = [
            "key",
            "label",
            "icon",
            "url_name",
            "is_visible",
            "display_order",
        ]
        widgets = {
            "key": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "label": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "icon": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "url_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "is_visible": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "display_order": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
        }