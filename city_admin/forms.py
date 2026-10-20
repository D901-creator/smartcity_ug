
from django import forms
from django.contrib.auth.models import User
from .models import SystemSettings

from accounts.models import AccountProfile
from departments.models import Ministry, Department, Sector, Service

from django import forms

from accounts.models import VerificationSubmission

class AdminUserEditForm(forms.ModelForm):
    email = forms.EmailField(required=False, max_length=254)

    class Meta:
        model = AccountProfile
        fields = [
            "full_name",
            "phone_number",
            "role",
            "department",
            "district",
            "city",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "role": forms.Select(attrs={
                "class": "form-select",
            }),
            "department": forms.Select(attrs={
                "class": "form-select",
            }),
            "district": forms.Select(attrs={
                "class": "form-select",
            }),
            "city": forms.Select(attrs={
                "class": "form-select",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
        })

        if self.instance and self.instance.pk:
            self.fields["email"].initial = self.instance.user.email

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()

        if email:
            duplicate = User.objects.filter(
                email__iexact=email
            ).exclude(pk=self.instance.user_id)

            if duplicate.exists():
                raise forms.ValidationError(
                    "This email address is already in use."
                )

        return email

    def save(self, commit=True):
        profile = super().save(commit=commit)

        if commit:
            user = profile.user
            user.email = self.cleaned_data["email"]
            user.save(update_fields=["email"])

        return profile



class VerificationReviewForm(forms.Form):
    decision = forms.ChoiceField(
        choices=[
            ("approved", "Approve verification"),
            ("rejected", "Reject verification"),
        ],
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    review_reason = forms.CharField(
        required=False,
        max_length=3000,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Explain the decision or any missing information.",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        decision = cleaned_data.get("decision")
        reason = (cleaned_data.get("review_reason") or "").strip()

        if decision == "rejected" and not reason:
            self.add_error(
                "review_reason",
                "A reason is required when rejecting a verification.",
            )

        cleaned_data["review_reason"] = reason
        return cleaned_data


class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = ["name", "code", "is_active"]


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "ministry",
            "name",
            "code",
            "description",
            "is_active",
        ]


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ["name", "description", "is_active"]


class DepartmentServiceForm(forms.ModelForm):
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


class SystemSettingsForm(forms.ModelForm):
    class Meta:
        model = SystemSettings

        fields = [
            "site_name",
            "support_email",
            "support_phone",
            "allow_public_registration",
            "require_government_verification",
            "default_theme",
            "announcement_enabled",
            "announcement_title",
            "announcement_message",
            "maintenance_mode",
            "maintenance_message",
        ]

        widgets = {
            "site_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "support_email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "support_phone": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "default_theme": forms.Select(
                attrs={"class": "form-select"}
            ),
            "announcement_title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "announcement_message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            "maintenance_message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }

