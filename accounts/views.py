
import logging

from django.contrib import messages
from django.contrib.auth import (
    get_user_model,
    login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .forms import RegistrationForm, VerificationSubmissionForm
from .models import AccountPreference, AccountProfile, VerificationSubmission
from locations.models import City

User = get_user_model()
logger = logging.getLogger(__name__)


CITY_ADMIN_GROUPS = (
    "City Admin",
    "City Admins",
    "System Administrator",
    "System Administrators",
)


def _get_profile(user):
    """Return the user's account profile, or None if it does not exist."""
    return AccountProfile.objects.filter(user=user).first()


def _is_approved(profile):
    """Check whether an account profile has been approved."""
    return (
        profile is not None
        and profile.verification_status
        == AccountProfile.VerificationStatus.APPROVED
    )


def _is_city_admin(user):
    """
    Check whether the authenticated user is authorized as a City Admin.

    Authorization is based on superuser status or membership in one of
    the configured City Admin/System Administrator groups.
    """
    if not user.is_authenticated:
        return False

    return (
        user.is_superuser
        or user.groups.filter(name__in=CITY_ADMIN_GROUPS).exists()
    )


def _redirect_after_login(request, profile):
    """Redirect an authenticated user to the correct portal."""
    if _is_city_admin(request.user):
        return redirect("city_admin:dashboard")

    if not _is_approved(profile):
        return redirect("accounts:verification_pending")

    if profile.role == AccountProfile.Role.CITIZEN:
        return redirect("/citizen/")

    if profile.role == AccountProfile.Role.OFFICER:
        return redirect("officer:dashboard")

    if profile.role == AccountProfile.Role.DEPARTMENT_HEAD:
        return redirect("department_head:dashboard")

    return redirect("accounts:verification_pending")


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    Authenticate users through the custom account login page.

    Authorized City Admins can enter the administration portal without
    needing a citizen/officer AccountProfile.

    Other users must have an AccountProfile and follow the existing
    verification and role-based dashboard process.
    """

    # Handle users who already have an authenticated session.
    if request.user.is_authenticated:
        if _is_city_admin(request.user):
            return redirect("city_admin:dashboard")

        profile = _get_profile(request.user)

        if profile is not None and _is_approved(profile):
            return _redirect_after_login(request, profile)

        if profile is not None:
            return redirect("accounts:verification_pending")

        # An ordinary account without a profile must sign in again
        # after its invalid session is cleared.
        logout(request)

    form = AuthenticationForm(
        request=request,
        data=request.POST if request.method == "POST" else None,
    )

    if request.method == "POST" and form.is_valid():
        user = form.get_user()

        # Check administrator authorization before requiring a profile.
        if _is_city_admin(user):
            login(request, user)
            return redirect("city_admin:dashboard")

        profile = _get_profile(user)

        if profile is None:
            messages.error(
                request,
                "No account profile was found for this user. "
                "Contact the system administrator.",
            )
            return render(
                request,
                "accounts/login.html",
                {
                    "form": AuthenticationForm(request=request),
                    "next": "",
                },
            )

        login(request, user)

        if _is_approved(profile):
            return _redirect_after_login(request, profile)

        if (
            profile.verification_status
            == AccountProfile.VerificationStatus.REJECTED
        ):
            messages.warning(
                request,
                "Your verification was rejected. Review the feedback "
                "and resubmit if permitted.",
            )
        else:
            messages.info(
                request,
                "Your account is awaiting approval. You will be "
                "redirected to your dashboard after approval.",
            )

        return redirect("accounts:verification_pending")

    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
            "next": request.GET.get("next", ""),
        },
    )


@require_http_methods(["GET", "POST"])
def register(request):
    """Register an account with an initial pending verification status."""

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save(commit=False)
                    user.email = (
                        form.cleaned_data["email"].strip().lower()
                    )
                    user.save()

                    profile = AccountProfile.objects.create(
                        user=user,
                        full_name=form.cleaned_data["full_name"],
                        phone_number=form.cleaned_data["phone_number"],
                        district=form.cleaned_data["district"],
                        city=form.cleaned_data.get("city"),
                        role=form.cleaned_data["role"],
                        profile_picture=form.cleaned_data.get(
                            "profile_picture"
                        ),
                        verification_status=(
                            AccountProfile.VerificationStatus.PENDING
                        ),
                    )

                login(request, user)
                messages.success(
                    request,
                    "Registration successful. Your account is awaiting approval.",
                )
                return _redirect_after_login(request, profile)

            except Exception:
                logger.exception("Registration failed")
                messages.error(
                    request,
                    "Registration could not be completed. "
                    "Check the VS Code terminal for details and try again.",
                )
    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


@require_GET
def cities_by_district(request):
    """Return cities belonging to the selected district."""

    district_id = request.GET.get("district_id", "")

    if not district_id.isdigit():
        return JsonResponse({"cities": []})

    cities = City.objects.filter(
        district_id=district_id
    ).order_by("name")

    return JsonResponse({
        "cities": [
            {"id": city.id, "name": city.name}
            for city in cities
        ]
    })


@login_required
def verification_pending(request):
    """Display verification status and the latest submission."""

    # Administrators should go directly to their administration portal.
    if _is_city_admin(request.user):
        return redirect("city_admin:dashboard")

    profile = _get_profile(request.user)

    if profile is None:
        logout(request)
        return redirect("accounts:login")

    if _is_approved(profile):
        return _redirect_after_login(request, profile)

    latest_submission = profile.verification_submissions.first()

    return render(
        request,
        "accounts/verification_pending.html",
        {
            "profile": profile,
            "latest_submission": latest_submission,
            "has_pending_submission": (
                latest_submission is not None
                and latest_submission.status
                == VerificationSubmission.Status.PENDING
            ),
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def verification_submit(request):
    """Allow users to submit or resubmit verification where permitted."""

    if _is_city_admin(request.user):
        return redirect("city_admin:dashboard")

    profile = _get_profile(request.user)

    if profile is None:
        logout(request)
        return redirect("accounts:login")

    if _is_approved(profile):
        messages.info(request, "Your account is already approved.")
        return _redirect_after_login(request, profile)

    latest = profile.verification_submissions.first()

    if (
        latest
        and latest.status == VerificationSubmission.Status.PENDING
    ):
        messages.info(
            request,
            "Your verification is awaiting administrator review.",
        )
        return redirect("accounts:verification_pending")

    if request.method == "POST":
        form = VerificationSubmissionForm(
            request.POST,
            request.FILES,
            role=profile.role,
        )

        if form.is_valid():
            try:
                with transaction.atomic():
                    submission = form.save(commit=False)
                    submission.profile = profile
                    submission.status = (
                        VerificationSubmission.Status.PENDING
                    )
                    submission.save()

                    profile.verification_status = (
                        AccountProfile.VerificationStatus.PENDING
                    )
                    profile.save(
                        update_fields=[
                            "verification_status",
                            "updated_at",
                        ]
                    )

                messages.success(
                    request,
                    "Verification submitted successfully. Await approval.",
                )
                return redirect("accounts:verification_pending")

            except Exception:
                logger.exception("Verification submission failed")
                messages.error(
                    request,
                    "Your verification could not be submitted. "
                    "Check the VS Code terminal for details.",
                )
    else:
        form = VerificationSubmissionForm(role=profile.role)

    return render(
        request,
        "accounts/verification_submit.html",
        {
            "form": form,
            "profile": profile,
        },
    )


@login_required
@require_GET
def verification_status(request):
    """Return the current user's verification status."""

    if _is_city_admin(request.user):
        return JsonResponse({
            "status": "approved",
            "role": "city_admin",
        })

    profile = _get_profile(request.user)

    if profile is None:
        return JsonResponse(
            {"status": "missing_profile"},
            status=404,
        )

    return JsonResponse({
        "status": profile.verification_status,
        "role": profile.role,
    })


@login_required
def my_profile(request):
    """Display the authenticated user's account profile."""

    if _is_city_admin(request.user):
        return redirect("city_admin:dashboard")

    profile = _get_profile(request.user)

    if profile is None:
        return redirect("accounts:verification_pending")

    return render(
        request,
        "accounts/my_profile.html",
        {"profile": profile},
    )


@login_required
@require_http_methods(["GET", "POST"])
def settings_view(request):
    """Display and update the user's account settings and preferences."""

    if _is_city_admin(request.user):
        return redirect("city_admin:dashboard")

    profile = _get_profile(request.user)

    if profile is None:
        return redirect("accounts:verification_pending")

    preferences, _ = AccountPreference.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        phone_number = request.POST.get("phone_number", "").strip()
        theme = request.POST.get("theme", "light")

        valid_themes = AccountPreference.Theme.values

        if not full_name or not email:
            messages.error(
                request,
                "Full name and email are required.",
            )
        elif theme not in valid_themes:
            messages.error(request, "Select a valid theme.")
        elif (
            User.objects.filter(email__iexact=email)
            .exclude(pk=request.user.pk)
            .exists()
        ):
            messages.error(
                request,
                "That email address is already in use.",
            )
        else:
            request.user.email = email
            request.user.save(update_fields=["email"])

            profile.full_name = full_name
            profile.phone_number = phone_number
            profile.save()

            preferences.theme = theme
            preferences.in_app_notifications = (
                request.POST.get("in_app_notifications") == "on"
            )
            preferences.email_notifications = (
                request.POST.get("email_notifications") == "on"
            )
            preferences.request_updates = (
                request.POST.get("request_updates") == "on"
            )
            preferences.announcements = (
                request.POST.get("announcements") == "on"
            )
            preferences.save()

            messages.success(
                request,
                "Your settings have been saved.",
            )
            return redirect("accounts:settings")

    return render(
        request,
        "accounts/settings.html",
        {
            "profile": profile,
            "preferences": preferences,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    """Change the authenticated user's password."""

    if _is_city_admin(request.user):
        return redirect("city_admin:dashboard")

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was changed.")
            return redirect("accounts:settings")
    else:
        form = PasswordChangeForm(request.user)

    return render(
        request,
        "accounts/change_password.html",
        {"form": form},
    )


@require_POST
def logout_view(request):
    """Log out the current user and return to the public home page."""
    logout(request)
    return redirect("public_home")
