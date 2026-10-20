
from django.conf import settings
from django.db import models


class AccountProfile(models.Model):
    class Role(models.TextChoices):
        CITIZEN = "citizen", "Citizen"
        OFFICER = "officer", "Government Officer"
        DEPARTMENT_HEAD = "department_head", "Department Head"

    class VerificationStatus(models.TextChoices):
        NOT_REQUIRED = "not_required", "Not Required"
        PENDING = "pending", "Pending Verification"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="account_profile",
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    department = models.ForeignKey(
    "departments.Department",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="officer_profiles",
)
    district = models.ForeignKey(
        "locations.District",
        on_delete=models.PROTECT,
        related_name="account_profiles",
    )
    city = models.ForeignKey(
        "locations.City",
        on_delete=models.PROTECT,
        related_name="account_profiles",
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CITIZEN,
    )
    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_role_display()})"


class VerificationSubmission(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending Review"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    class AreaType(models.TextChoices):
        DISTRICT = "district", "District"
        CITY = "city", "City"

    profile = models.ForeignKey(
        AccountProfile,
        on_delete=models.CASCADE,
        related_name="verification_submissions",
    )

    # Existing verification fields
    identification_type = models.CharField(max_length=50)
    identification_number = models.CharField(max_length=100)
    identification_document = models.FileField(
        upload_to="verification/identification/",
    )
    department = models.CharField(max_length=150, blank=True)
    staff_id = models.CharField(max_length=100, blank=True)
    appointment_document = models.FileField(
        upload_to="verification/appointments/",
        blank=True,
        null=True,
    )

    # District or city information
    area_type = models.CharField(
        max_length=10,
        choices=AreaType.choices,
        default=AreaType.DISTRICT,
    )
    area_name = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )

    # Identity number and ID card images
    id_number = models.CharField(
        max_length=50,
        blank=True,
        default="",
        db_index=True,
        help_text="Enter the ID number exactly as printed on your ID.",
    )
    id_front_image = models.ImageField(
        upload_to="verification/id_front/",
        blank=True,
        null=True,
    )
    id_back_image = models.ImageField(
        upload_to="verification/id_back/",
        blank=True,
        null=True,
    )

    # Address and occupation
    occupation = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )
    county = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )
    subcounty = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )
    parish = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )
    village = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )

    # Optional image for this verification submission
    profile_image = models.ImageField(
        upload_to="verification/profile_images/",
        blank=True,
        null=True,
    )

    # Review workflow
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    review_reason = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return (
            f"{self.profile.full_name} - "
            f"{self.get_status_display()}"
        )



class AccountPreference(models.Model):
    class Theme(models.TextChoices):
        LIGHT = "light", "Default Light"
        GREEN = "green", "Green"
        BLUE = "blue", "Blue"
        DARK = "dark", "Dark"
        BLACK = "black", "Black"

    user = models.OneToOneField(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="account_preference",
    )
    theme = models.CharField(
        max_length=10,
        choices=Theme.choices,
        default=Theme.LIGHT,
    )
    in_app_notifications = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    request_updates = models.BooleanField(default=True)
    announcements = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences for {self.user}"
