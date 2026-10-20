
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from PIL import Image

from locations.models import District, City
from .models import AccountProfile, VerificationSubmission

User = get_user_model()

MAX_UPLOAD_SIZE = 5 * 1024 * 1024
ALLOWED_IMAGE_FORMATS = {"JPEG", "PNG", "WEBP"}


def validate_image(upload, label):
    if upload.size > MAX_UPLOAD_SIZE:
        raise ValidationError(f"{label} must not exceed 5 MB.")

    try:
        upload.seek(0)
        with Image.open(upload) as image:
            if image.format not in ALLOWED_IMAGE_FORMATS:
                raise ValidationError(
                    f"{label} must be a JPEG, PNG, or WebP image."
                )
            image.verify()
    except ValidationError:
        raise
    except Exception as exc:
        raise ValidationError(f"Upload a valid {label.lower()} file.") from exc
    finally:
        upload.seek(0)


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=200,
        label="Full Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your full legal name",
        }),
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "you@example.com",
        }),
    )
    phone_number = forms.CharField(
        max_length=20,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+256...",
        }),
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.none(),
        label="District",
        empty_label="Select district",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(),
        label="City (if applicable)",
        required=False,
        empty_label="Select city",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    profile_picture = forms.ImageField(
        label="Profile Picture",
        required=False,
        help_text="Upload a profile photo (optional).",
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "accept": "image/jpeg,image/png,image/webp",
        }),
    )
    role = forms.ChoiceField(
        choices=AccountProfile.Role.choices,
        label="Register As",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Choose a username",
                "autocomplete": "username",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["district"].queryset = District.objects.order_by("name")

        district_id = (
            self.data.get("district")
            or self.initial.get("district")
        )
        if district_id and str(district_id).isdigit():
            self.fields["city"].queryset = City.objects.filter(
                district_id=district_id
            ).order_by("name")

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Create a strong password",
            "autocomplete": "new-password",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm your password",
            "autocomplete": "new-password",
        })

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                "An account with this email address already exists."
            )
        return email

    def clean_city(self):
        city = self.cleaned_data.get("city")
        district = self.cleaned_data.get("district")

        if city and district and city.district_id != district.id:
            raise ValidationError(
                "Please select a city belonging to your district."
            )
        return city

    def clean_profile_picture(self):
        image = self.cleaned_data.get("profile_picture")
        if image:
            validate_image(image, "Profile picture")
        return image

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "The passwords do not match.")

        return cleaned_data


class VerificationSubmissionForm(forms.ModelForm):
    # Existing document upload fields
    identification_document = forms.FileField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "jpg", "jpeg", "png"]
            )
        ],
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "accept": ".pdf,.jpg,.jpeg,.png",
        }),
    )

    appointment_document = forms.FileField(
        required=False,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "jpg", "jpeg", "png"]
            )
        ],
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "accept": ".pdf,.jpg,.jpeg,.png",
        }),
    )

    # Hidden legacy field, synchronized with the visible ID number.
    identification_number = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = VerificationSubmission
        fields = [
            "identification_type",
            "identification_number",
            "identification_document",
            "department",
            "staff_id",
            "appointment_document",
            "area_type",
            "area_name",
            "id_number",
            "id_front_image",
            "id_back_image",
            "occupation",
            "county",
            "subcounty",
            "parish",
            "village",
            "profile_image",
        ]
        widgets = {
            "identification_type": forms.Select(
                choices=[
                    ("national_id", "National ID"),
                    ("passport", "Passport"),
                    ("other", "Other Government-Issued ID"),
                ],
                attrs={"class": "form-select"},
            ),
            "department": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "staff_id": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "area_type": forms.Select(attrs={
                "class": "form-select",
                "id": "id_area_type",
            }),
            "area_name": forms.TextInput(attrs={
                "class": "form-control",
                "id": "id_area_name",
                "placeholder": "Enter your district or city",
            }),
            "id_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter ID number as printed on your ID",
                "autocomplete": "off",
            }),
            "id_front_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/jpeg,image/png,image/webp",
            }),
            "id_back_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/jpeg,image/png,image/webp",
            }),
            "occupation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your occupation",
            }),
            "county": forms.TextInput(attrs={
                "class": "form-control",
                "id": "id_county",
                "placeholder": "County",
            }),
            "subcounty": forms.TextInput(attrs={
                "class": "form-control",
                "id": "id_subcounty",
                "placeholder": "Subcounty",
            }),
            "parish": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Parish",
            }),
            "village": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Village",
            }),
            "profile_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/jpeg,image/png,image/webp",
            }),
        }

    def __init__(self, *args, role=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role

        self.fields["area_type"].choices = (
            VerificationSubmission.AreaType.choices
        )

        self.fields["id_front_image"].required = True
        self.fields["id_back_image"].required = True

        for name in (
            "id_number",
            "occupation",
            "area_name",
            "county",
            "subcounty",
            "parish",
            "village",
        ):
            self.fields[name].required = True

        if role == AccountProfile.Role.CITIZEN:
            self.fields.pop("department")
            self.fields.pop("staff_id")
            self.fields.pop("appointment_document")
        else:
            self.fields["department"].required = True
            self.fields["staff_id"].required = True
            self.fields["appointment_document"].required = True

        area_type = (
            self.data.get("area_type")
            or self.initial.get("area_type")
            or "district"
        )
        self.update_location_labels(area_type)

    def update_location_labels(self, area_type):
        if area_type == "city":
            self.fields["area_name"].label = "City Name"
            self.fields["county"].label = "County/Division"
            self.fields["subcounty"].label = "Subcounty/Ward"
        else:
            self.fields["area_name"].label = "District Name"
            self.fields["county"].label = "County"
            self.fields["subcounty"].label = "Subcounty"

    def clean_id_number(self):
        value = self.cleaned_data.get("id_number", "").strip()
        if not value:
            raise ValidationError("Enter your ID number.")
        if len(value) > 50:
            raise ValidationError("The ID number is too long.")
        return value

    def clean_identification_document(self):
        document = self.cleaned_data.get("identification_document")
        if document:
            if document.size > MAX_UPLOAD_SIZE:
                raise ValidationError("The file must not exceed 5 MB.")

            extension = document.name.rsplit(".", 1)[-1].lower()
            if extension in {"jpg", "jpeg", "png"}:
                validate_image(document, "Identification document")

        return document

    def clean_appointment_document(self):
        document = self.cleaned_data.get("appointment_document")
        if document:
            if document.size > MAX_UPLOAD_SIZE:
                raise ValidationError("The file must not exceed 5 MB.")

            extension = document.name.rsplit(".", 1)[-1].lower()
            if extension in {"jpg", "jpeg", "png"}:
                validate_image(document, "Appointment document")

        return document

    def clean(self):
        cleaned_data = super().clean()

        id_number = cleaned_data.get("id_number")
        if id_number:
            cleaned_data["identification_number"] = id_number

        for field_name in (
            "id_front_image",
            "id_back_image",
            "profile_image",
        ):
            image = cleaned_data.get(field_name)
            if image:
                try:
                    validate_image(image, field_name.replace("_", " "))
                except ValidationError as exc:
                    self.add_error(field_name, exc)

        return cleaned_data
