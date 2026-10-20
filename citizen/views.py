
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from accounts.models import AccountProfile


@login_required
def dashboard(request):
    profile = (
        AccountProfile.objects
        .filter(user=request.user)
        .select_related("district", "city")
        .first()
    )

    # Accounts without a profile must complete the account workflow.
    if profile is None:
        return redirect("accounts:verification_pending")

    # Unapproved accounts must not access the Citizen Portal.
    if (
        profile.verification_status
        != AccountProfile.VerificationStatus.APPROVED
    ):
        return redirect("accounts:verification_pending")

    # Only approved citizen accounts may access this dashboard.
    if profile.role != AccountProfile.Role.CITIZEN:
        raise PermissionDenied(
            "This dashboard is available to approved citizen accounts only."
        )

    # Reuse the existing dashboard view and its existing template.
    from dashboard.views import home

    return home(request)
