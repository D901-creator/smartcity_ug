from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .models import (
    SystemSettings,
    PortalConfiguration,
    PortalModule,
    PortalMenuItem,
    PortalConfigurationAudit,
)
from .forms import SystemSettingsForm
from .portal_config_forms import (
    PortalConfigurationForm,
    PortalModuleForm,
    PortalMenuItemForm,
)


PORTALS = [
    ("citizen", "Citizen Portal"),
    ("officer", "Officer Portal"),
    ("department_head", "Department Head Portal"),
    ("system_admin", "System Administrator Portal"),
]


PORTAL_STARTER_DATA = {
    "citizen": {
        "name": "Citizen Portal",
        "welcome": "Access government services and track your requests.",
        "modules": [
            ("dashboard", "Dashboard", "Citizen overview and activities."),
            ("services", "Government Services", "Browse public services."),
            ("requests", "My Requests", "Submit and track service requests."),
            ("reports", "Reports and Complaints", "Submit reports and complaints."),
            ("payments", "Payments and Bills", "View supported payments and bills."),
            ("documents", "Documents", "Access available citizen documents."),
            ("community", "Community", "Community information and engagement."),
            ("education", "Education", "Education services and learning resources."),
            ("agriculture", "Agriculture", "Agricultural services and information."),
            ("jobs", "Jobs", "View employment opportunities."),
        ],
    },
    "officer": {
        "name": "Officer Portal",
        "welcome": "Manage your assigned government service requests.",
        "modules": [
            ("dashboard", "Dashboard", "Officer work overview."),
            ("assigned_requests", "Assigned Requests", "Process assigned requests."),
            ("cases", "Cases", "Manage assigned cases."),
            ("tasks", "Tasks", "View and update work tasks."),
            ("calendar", "Calendar", "Review work schedules."),
            ("communications", "Communications", "Access official communications."),
            ("reports", "Reports", "Prepare operational reports."),
        ],
    },
    "department_head": {
        "name": "Department Head Portal",
        "welcome": "Oversee department operations and performance.",
        "modules": [
            ("dashboard", "Dashboard", "Department overview."),
            ("staff", "Staff Management", "Review department staffing."),
            ("assignments", "Assignments", "Review work assignments."),
            ("requests", "Request Oversight", "Monitor departmental requests."),
            ("performance", "Performance", "Review department performance."),
            ("reports", "Reports", "Review department reports."),
        ],
    },
    "system_admin": {
        "name": "System Administrator Portal",
        "welcome": "Manage system configuration and accountability.",
        "modules": [
            ("dashboard", "Dashboard", "System overview."),
            ("users", "User Management", "Manage platform accounts."),
            ("portals", "Portal Management", "Configure the other portals."),
            ("departments", "Departments", "Manage government departments."),
            ("locations", "Locations", "Manage national locations."),
            ("audit", "Audit and Accountability", "Review administrative activity."),
            ("security", "Security", "Review security configuration."),
            ("analytics", "Analytics", "Review system-wide indicators."),
        ],
    },
}


def require_portal_admin(user):
    """Allow only authorized administrators to change system configuration."""
    allowed_groups = [
        "City Admin",
        "City Admins",
        "System Administrator",
        "System Administrators",
    ]

    allowed = (
        user.is_authenticated
        and (
            user.is_staff
            or user.is_superuser
            or user.groups.filter(name__in=allowed_groups).exists()
        )
    )

    if not allowed:
        raise PermissionDenied(
            "You are not authorized to configure system settings."
        )


def seed_portals():
    """Create starter portal and module records without overwriting changes."""
    for key, data in PORTAL_STARTER_DATA.items():
        portal, _created = PortalConfiguration.objects.get_or_create(
            portal_key=key,
            defaults={
                "display_name": data["name"],
                "welcome_message": data["welcome"],
            },
        )

        for order, module_data in enumerate(data["modules"], start=1):
            code, name, description = module_data

            PortalModule.objects.get_or_create(
                portal=portal,
                code=code,
                defaults={
                    "name": name,
                    "description": description,
                    "is_enabled": True,
                    "display_order": order * 10,
                },
            )


def record_change(request, portal, action, details):
    PortalConfigurationAudit.objects.create(
        actor=request.user,
        portal=portal,
        action=action,
        details=details,
    )


def settings_redirect(portal_key="citizen"):
    url = reverse("city_admin:settings")
    return f"{url}?portal={portal_key}#portal-management"


@login_required
@require_http_methods(["GET", "POST"])
def system_settings(request):
    require_portal_admin(request.user)

    seed_portals()

    system_settings_obj = SystemSettings.load()

    portal_key = (
        request.POST.get("portal_key")
        or request.GET.get("portal", "citizen")
    )

    valid_portal_keys = {key for key, _label in PORTALS}

    if portal_key not in valid_portal_keys:
        portal_key = "citizen"

    portal = get_object_or_404(
        PortalConfiguration,
        portal_key=portal_key,
    )

    action = request.POST.get("action", "").strip()

    system_form = SystemSettingsForm(instance=system_settings_obj)
    portal_form = PortalConfigurationForm(instance=portal)
    module_form = PortalModuleForm()
    menu_form = PortalMenuItemForm()

    if request.method == "POST":

        # Save the general system settings.
        if action == "save_system_settings":
            system_form = SystemSettingsForm(
                request.POST,
                instance=system_settings_obj,
            )

            if system_form.is_valid():
                system_form.save()
                messages.success(
                    request,
                    "General system settings saved successfully.",
                )
                return redirect(settings_redirect(portal_key))

            messages.error(
                request,
                "Please correct the errors in the general settings form.",
            )

        # Save settings for the selected portal.
        elif action == "save_portal":
            portal_form = PortalConfigurationForm(
                request.POST,
                instance=portal,
            )

            if portal_form.is_valid():
                with transaction.atomic():
                    updated_portal = portal_form.save()
                    record_change(
                        request,
                        updated_portal,
                        "portal_updated",
                        (
                            "Updated portal information, enabled status "
                            "or maintenance configuration."
                        ),
                    )

                messages.success(
                    request,
                    "Portal configuration saved successfully.",
                )
                return redirect(settings_redirect(portal_key))

            messages.error(
                request,
                "Please correct the errors in the portal form.",
            )

        # Add a module to the selected portal.
        elif action == "add_module":
            module_form = PortalModuleForm(request.POST)

            if module_form.is_valid():
                module = module_form.save(commit=False)
                module.portal = portal

                try:
                    with transaction.atomic():
                        module.save()
                        record_change(
                            request,
                            portal,
                            "module_created",
                            f"Created module '{module.name}' ({module.code}).",
                        )

                    messages.success(request, "Portal module added.")
                    return redirect(settings_redirect(portal_key))

                except Exception:
                    module_form.add_error(
                        "code",
                        "This module code may already exist for this portal.",
                    )

            messages.error(
                request,
                "The module could not be added. Check the fields below.",
            )

        # Add a menu item to the selected portal.
        elif action == "add_menu":
            menu_form = PortalMenuItemForm(request.POST)

            if menu_form.is_valid():
                menu_item = menu_form.save(commit=False)
                menu_item.portal = portal

                try:
                    with transaction.atomic():
                        menu_item.save()
                        record_change(
                            request,
                            portal,
                            "menu_created",
                            (
                                f"Created menu item '{menu_item.label}' "
                                f"({menu_item.key})."
                            ),
                        )

                    messages.success(request, "Portal menu item added.")
                    return redirect(settings_redirect(portal_key))

                except Exception:
                    menu_form.add_error(
                        "key",
                        "This menu key may already exist for this portal.",
                    )

            messages.error(
                request,
                "The menu item could not be added. Check the fields below.",
            )

        else:
            messages.error(request, "Unknown settings action.")

    context = {
        "active_section": "settings",
        "system_settings": system_settings_obj,
        "system_form": system_form,
        "portals": PORTALS,
        "selected_portal": portal,
        "portal_form": portal_form,
        "module_form": module_form,
        "menu_form": menu_form,
        "modules": portal.modules.all(),
        "menu_items": portal.menu_items.all(),
        "audit_entries": portal.audit_entries.select_related("actor")[:20],
    }

    return render(
        request,
        "city_admin/settings.html",
        context,
    )


@login_required
@require_http_methods(["POST"])
def toggle_portal_module(request, module_id):
    require_portal_admin(request.user)

    module = get_object_or_404(
        PortalModule.objects.select_related("portal"),
        pk=module_id,
    )

    module.is_enabled = not module.is_enabled
    module.save(update_fields=["is_enabled"])

    record_change(
        request,
        module.portal,
        "module_toggled",
        f"Module '{module.name}' enabled={module.is_enabled}.",
    )

    messages.success(
        request,
        f"Module '{module.name}' updated.",
    )

    return redirect(settings_redirect(module.portal.portal_key))


@login_required
@require_http_methods(["POST"])
def toggle_portal_menu_item(request, item_id):
    require_portal_admin(request.user)

    item = get_object_or_404(
        PortalMenuItem.objects.select_related("portal"),
        pk=item_id,
    )

    item.is_visible = not item.is_visible
    item.save(update_fields=["is_visible"])

    record_change(
        request,
        item.portal,
        "menu_visibility_toggled",
        f"Menu item '{item.label}' visible={item.is_visible}.",
    )

    messages.success(
        request,
        f"Menu item '{item.label}' visibility updated.",
    )

    return redirect(settings_redirect(item.portal.portal_key))


@login_required
@require_http_methods(["POST"])
def delete_portal_menu_item(request, item_id):
    require_portal_admin(request.user)

    item = get_object_or_404(
        PortalMenuItem.objects.select_related("portal"),
        pk=item_id,
    )

    portal = item.portal
    label = item.label

    record_change(
        request,
        portal,
        "menu_deleted",
        f"Deleted menu item '{label}'.",
    )

    item.delete()

    messages.success(request, f"Menu item '{label}' deleted.")

    return redirect(settings_redirect(portal.portal_key))