
from django.urls import path
from . import views
from . import map_views
from . import database_views
from . import notification_views
from . import portal_settings_views
from . import security_audit_views
from .map_views import district_issue_map
from django.contrib.auth import views as auth_views
from locations import views as location_views
from .access import city_admin_required
app_name = "city_admin"

urlpatterns = [
    path("", views.city_admin_dashboard, name="dashboard"),
    path("users/", views.city_admin_users, name="users"),
    path(
    "users/<int:profile_id>/",
    views.city_admin_user_detail,
    name="user_detail",
),
path(
    "users/<int:profile_id>/edit/",
    views.city_admin_user_edit,
    name="user_edit",
),
path(
    "users/<int:profile_id>/status/",
    views.city_admin_toggle_user_status,
    name="user_status",
),
path(
    "verifications/",
    views.city_admin_verifications,
    name="verifications",
),
path(
    "verifications/<int:submission_id>/",
    views.city_admin_verification_review,
    name="verification_review",
),

    path(
        "departments/",
        views.city_admin_departments,
        name="departments",
    ),
    path(
        "departments/create/",
        views.city_admin_department_create,
        name="department_create",
    ),
    path(
        "ministries/create/",
        views.city_admin_ministry_create,
        name="ministry_create",
    ),
    path(
        "sectors/create/",
        views.city_admin_sector_create,
        name="sector_create",
    ),
    path(
        "department-services/create/",
        views.city_admin_service_create,
        name="department_service_create",
    ),

    path(
        "analytics/",
        views.city_admin_analytics,
        name="analytics",
    ),
    path(
        "locations/",
        location_views.locations_dashboard,
        name="locations",
    ),
    path(
        "locations/regions/create/",
        location_views.location_create_region,
        name="location_create_region",
    ),
    path(
        "locations/districts/create/",
        location_views.location_create_district,
        name="location_create_district",
    ),
    path(
        "locations/cities/create/",
        location_views.location_create_city,
        name="location_create_city",
    ),
    path(
        "locations/municipalities/create/",
        location_views.location_create_municipality,
        name="location_create_municipality",
    ),
path(
    "district-map/",
    views.district_map_generator,
    name="district_map",
),
path(
    "district-issue-map/",
    map_views.district_issue_map,
    name="district_issue_map",
),
path(
    "district-issue-map/",
    district_issue_map,
    name="district_issue_map",
),
path(
    "notifications/",
    notification_views.notification_list,
    name="notifications",
),
path(
    "notifications/<int:notification_id>/read/",
    notification_views.mark_notification_read,
    name="notification_mark_read",
),
path(
    "notifications/mark-all-read/",
    notification_views.mark_all_notifications_read,
    name="notifications_mark_all_read",
),
path(
    "database/",
    database_views.database_overview,
    name="database",
),
path(
    "users/<int:user_id>/update/",
    views.user_update,
    name="user_update",
),
path(
    "users/<int:user_id>/delete/",
    views.user_delete,
    name="user_delete",
),
path(
    "verification-applications/",
    views.city_admin_verification_applications,
    name="verification_applications",
),
   path(
    "settings/",
    portal_settings_views.system_settings,
    name="settings",
),
path(
    "portal-modules/<int:module_id>/toggle/",
    portal_settings_views.toggle_portal_module,
    name="portal_module_toggle",
),
path(
    "portal-menu/<int:item_id>/toggle/",
    portal_settings_views.toggle_portal_menu_item,
    name="portal_menu_toggle",
),
path(
    "portal-menu/<int:item_id>/delete/",
    portal_settings_views.delete_portal_menu_item,
    name="portal_menu_delete",
),
# Security monitoring and audit management
path(
    "security-audit/",
    security_audit_views.security_dashboard,
    name="security_audit",
),
path(
    "security-audit/events/",
    security_audit_views.security_events,
    name="security_events",
),
path(
    "security-audit/events/<int:event_id>/",
    security_audit_views.security_event_detail,
    name="security_event_detail",
),
path(
    "security-audit/events/<int:event_id>/review/",
    security_audit_views.update_security_event,
    name="security_event_review",
),
path(
    "security-audit/audit-trail/",
    security_audit_views.audit_trail,
    name="audit_trail",
),
path(
    "security-audit/audit-trail/export/",
    security_audit_views.export_audit_csv,
    name="audit_export",
),
path(
    "signout/",
    auth_views.LogoutView.as_view(next_page="/"),
    name="signout",
),

]
# Apply City Admin authorization to every route in this URL configuration.
# The shared login page is used for unauthenticated visitors.
for url_pattern in urlpatterns:
    if url_pattern.name != "signout":
        url_pattern.callback = city_admin_required(
            url_pattern.callback
        )