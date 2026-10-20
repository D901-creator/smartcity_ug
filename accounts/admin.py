from django.contrib import admin, messages
from django.db import transaction
from django.utils import timezone

from .models import AccountProfile, VerificationSubmission


@admin.register(AccountProfile)
class AccountProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "role",
        "district",
        "city",
        "verification_status",
    )
    list_filter = ("role", "district", "verification_status")
    search_fields = ("full_name", "user__username", "user__email")
    readonly_fields = ("created_at", "updated_at")


@admin.register(VerificationSubmission)
class VerificationSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "identification_type",
        "status",
        "submitted_at",
        "reviewed_at",
    )
    list_filter = ("status", "identification_type")
    search_fields = (
        "profile__full_name",
        "profile__user__username",
        "profile__user__email",
        "identification_number",
        "staff_id",
    )
    readonly_fields = ("submitted_at", "reviewed_at")
    actions = ("approve_verifications", "reject_verifications")

    @admin.action(description="Approve selected verification submissions")
    def approve_verifications(self, request, queryset):
        approved_count = 0

        with transaction.atomic():
            for submission in queryset.select_related("profile"):
                submission.status = VerificationSubmission.Status.APPROVED
                submission.reviewed_at = timezone.now()
                submission.save(update_fields=["status", "reviewed_at"])

                profile = submission.profile
                profile.verification_status = (
                    AccountProfile.VerificationStatus.APPROVED
                )
                profile.save(update_fields=["verification_status", "updated_at"])
                approved_count += 1

        self.message_user(
            request,
            f"Approved {approved_count} verification submission(s).",
            messages.SUCCESS,
        )

    @admin.action(description="Reject selected verification submissions")
    def reject_verifications(self, request, queryset):
        rejected_count = 0

        with transaction.atomic():
            for submission in queryset.select_related("profile"):
                submission.status = VerificationSubmission.Status.REJECTED
                submission.reviewed_at = timezone.now()
                submission.save(update_fields=["status", "reviewed_at"])

                profile = submission.profile
                profile.verification_status = (
                    AccountProfile.VerificationStatus.REJECTED
                )
                profile.save(update_fields=["verification_status", "updated_at"])
                rejected_count += 1

        self.message_user(
            request,
            f"Rejected {rejected_count} verification submission(s).",
            messages.WARNING,
        )