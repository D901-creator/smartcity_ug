
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import AccountProfile
from .forms import CitizenReportForm, OfficerReportUpdateForm
from .models import CitizenReport


CITY_ADMIN_GROUPS = (
    "City Admin",
    "City Admins",
    "System Administrator",
    "System Administrators",
)

BLOCKED_USERNAME = "admin"


def is_city_admin(user):
    """Return True for an authorized City Admin, excluding username admin."""
    if not user.is_authenticated:
        return False

    if user.get_username().casefold() == BLOCKED_USERNAME:
        return False

    return (
        user.is_superuser
        or user.groups.filter(name__in=CITY_ADMIN_GROUPS).exists()
    )


def is_officer(user):
    """Recognize officers through their profile role or Django groups."""
    if not user.is_authenticated:
        return False

    if user.get_username().casefold() == BLOCKED_USERNAME:
        return False

    profile = AccountProfile.objects.filter(user=user).first()

    return (
        user.groups.filter(name__in=["Officer", "Officers"]).exists()
        or (
            profile is not None
            and profile.role == AccountProfile.Role.OFFICER
        )
    )


# CITIZEN REPORTS

@login_required
def my_reports(request):
    reports = CitizenReport.objects.filter(
        citizen=request.user
    ).order_by("-created_at")

    return render(
        request,
        "reports/my_reports.html",
        {"reports": reports},
    )


@login_required
def create_report(request):
    if request.user.get_username().casefold() == BLOCKED_USERNAME:
        raise PermissionDenied

    if request.method == "POST":
        form = CitizenReportForm(request.POST)

        if form.is_valid():
            report = form.save(commit=False)
            report.citizen = request.user
            report.status = "submitted"
            report.save()

            messages.success(request, "Your report was submitted successfully.")

            return redirect(
                "reports:report_detail",
                report_id=report.id,
            )
    else:
        form = CitizenReportForm()

    return render(
        request,
        "reports/create_report.html",
        {"form": form},
    )


@login_required
def report_detail(request, report_id):
    report = get_object_or_404(
        CitizenReport,
        id=report_id,
        citizen=request.user,
    )

    return render(
        request,
        "reports/report_detail.html",
        {"report": report},
    )


# OFFICER AND CITY ADMIN REPORTS

@login_required
def officer_reports(request):
    user = request.user

    if not (is_officer(user) or is_city_admin(user)):
        raise PermissionDenied(
            "Only authorized officers and City Admins can access officer reports."
        )

    if is_city_admin(user):
        # Authorized City Admins can review all citizen reports.
        reports = CitizenReport.objects.all()
    else:
        # Officers can only see reports assigned to them.
        reports = CitizenReport.objects.filter(
            assigned_officer=user
        )

    reports = reports.order_by("-created_at")

    return render(
        request,
        "reports/officer_reports.html",
        {"reports": reports},
    )


@login_required
def officer_report_detail(request, report_id):
    user = request.user

    if not (is_officer(user) or is_city_admin(user)):
        raise PermissionDenied(
            "Only authorized officers and City Admins can access report details."
        )

    if is_city_admin(user):
        report_queryset = CitizenReport.objects.all()
    else:
        report_queryset = CitizenReport.objects.filter(
            assigned_officer=user
        )

    report = get_object_or_404(
        report_queryset,
        id=report_id,
    )

    if request.method == "POST":
        form = OfficerReportUpdateForm(
            request.POST,
            instance=report,
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Report updated successfully.")

            return redirect(
                "reports:officer_report_detail",
                report_id=report.id,
            )
    else:
        form = OfficerReportUpdateForm(instance=report)

    return render(
        request,
        "reports/officer_report_detail.html",
        {"report": report, "form": form},
    )
