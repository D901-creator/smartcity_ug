
from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import AccountProfile
from .forms import DepartmentForm, ServiceForm
from .models import Department, Service


CITY_ADMIN_GROUPS = (
    "City Admin",
    "City Admins",
    "System Administrator",
    "System Administrators",
)

BLOCKED_USERNAME = "admin"


def is_city_admin(user):
    """Check explicit City Admin access, excluding the username admin."""
    if not user.is_authenticated:
        return False

    if user.get_username().casefold() == BLOCKED_USERNAME:
        return False

    return (
        user.is_superuser
        or user.groups.filter(name__in=CITY_ADMIN_GROUPS).exists()
    )


def has_profile_role(user, role):
    """Check a user's application-level AccountProfile role."""
    profile = AccountProfile.objects.filter(user=user).first()

    return profile is not None and profile.role == role


def is_department_head(user):
    """Recognize department heads through their profile or groups."""
    if not user.is_authenticated:
        return False

    if user.get_username().casefold() == BLOCKED_USERNAME:
        return False

    return (
        user.groups.filter(
            name__in=["Department Head", "Department Heads"]
        ).exists()
        or has_profile_role(
            user,
            AccountProfile.Role.DEPARTMENT_HEAD,
        )
    )


def is_officer(user):
    """Recognize officers through their profile or groups."""
    if not user.is_authenticated:
        return False

    if user.get_username().casefold() == BLOCKED_USERNAME:
        return False

    return (
        user.groups.filter(
            name__in=["Officer", "Officers"]
        ).exists()
        or has_profile_role(
            user,
            AccountProfile.Role.OFFICER,
        )
    )


# PUBLIC SERVICE DIRECTORY

def service_directory(request):
    services = Service.objects.filter(
        is_active=True,
        department__is_active=True,
    ).select_related(
        "department",
        "sector",
        "department__ministry",
    )

    search_query = request.GET.get("q", "").strip()
    selected_sector = request.GET.get("sector", "").strip()

    if search_query:
        services = services.filter(
            Q(name__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(department__name__icontains=search_query)
        )

    if selected_sector.isdigit():
        services = services.filter(
            sector_id=int(selected_sector)
        )

    sectors = Service.objects.filter(
        is_active=True,
        department__is_active=True,
        sector__is_active=True,
    ).values(
        "sector_id",
        "sector__name",
    ).distinct().order_by("sector__name")

    return render(
        request,
        "departments/service_directory.html",
        {
            "services": services,
            "sectors": sectors,
            "search_query": search_query,
            "selected_sector": selected_sector,
        },
    )


def service_detail(request, service_id):
    service = get_object_or_404(
        Service.objects.select_related(
            "department",
            "sector",
            "department__ministry",
        ),
        pk=service_id,
        is_active=True,
        department__is_active=True,
    )

    return render(
        request,
        "departments/service_detail.html",
        {"service": service},
    )


# DEPARTMENT HEAD DASHBOARD

@login_required
def department_services_dashboard(request):
    user = request.user

    if not (is_department_head(user) or is_city_admin(user)):
        raise PermissionDenied(
            "Only authorized Department Heads and City Admins can access this dashboard."
        )

    return render(
        request,
        "departments/department_services_dashboard.html",
    )


# DEPARTMENT AND SERVICE MANAGEMENT ACCESS

def department_management_required(view_func):
    """Require an officer, department head, or authorized City Admin."""

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user

        if not (
            is_officer(user)
            or is_department_head(user)
            or is_city_admin(user)
        ):
            raise PermissionDenied(
                "You are not authorized to manage departments or services."
            )

        return view_func(request, *args, **kwargs)

    return login_required(wrapper)


# DEPARTMENT MANAGEMENT

@department_management_required
def manage_departments(request):
    departments = Department.objects.select_related(
        "ministry"
    ).order_by("name")

    return render(
        request,
        "departments/manage_departments.html",
        {"departments": departments},
    )


@department_management_required
def department_add(request):
    form = DepartmentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Department created successfully.")
        return redirect("departments:manage_departments")

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form,
            "page_title": "Add Department",
        },
    )


@department_management_required
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(
        request.POST or None,
        instance=department,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Department updated successfully.")
        return redirect("departments:manage_departments")

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form,
            "page_title": "Edit Department",
            "department": department,
        },
    )


# SERVICE CONFIGURATION

@department_management_required
def manage_services(request):
    services = Service.objects.select_related(
        "department",
        "sector",
    ).order_by("name")

    return render(
        request,
        "departments/manage_services.html",
        {"services": services},
    )


@department_management_required
def service_add(request):
    form = ServiceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Service created successfully.")
        return redirect("departments:manage_services")

    return render(
        request,
        "departments/service_form.html",
        {
            "form": form,
            "page_title": "Add Service",
        },
    )


@department_management_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(
        request.POST or None,
        instance=service,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Service updated successfully.")
        return redirect("departments:manage_services")

    return render(
        request,
        "departments/service_form.html",
        {
            "form": form,
            "page_title": "Edit Service",
            "service": service,
        },
    )
