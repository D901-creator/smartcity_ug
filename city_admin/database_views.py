
import os

from django.apps import apps
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import DatabaseError, connection
from django.shortcuts import render


def city_admin_access_required(user):
    """Allow only authorized City Admin or system administrator accounts."""
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.is_staff
            or user.groups.filter(
                name__in=[
                    "City Admin",
                    "City Admins",
                    "System Administrator",
                    "System Administrators",
                ]
            ).exists()
        )
    )


@login_required
def database_overview(request):
    """Display database information to authorized administrators only."""

    # Temporary debugging: inspect the account used by the browser.
    print("\n===== DATABASE ACCESS DEBUG =====")
    print("Username:", request.user.get_username())
    print("Authenticated:", request.user.is_authenticated)
    print("Staff:", request.user.is_staff)
    print("Superuser:", request.user.is_superuser)
    print(
        "Groups:",
        list(request.user.groups.values_list("name", flat=True)),
    )

    has_access = city_admin_access_required(request.user)
    print("Permission result:", has_access)
    print("=================================\n")

    # Protect database information from unauthorized users.
    if not has_access:
        raise PermissionDenied(
            "Only authorized city administrators can access database information."
        )

    # Read the configured database settings.
    database_config = settings.DATABASES.get("default", {})
    database_engine = database_config.get("ENGINE", "")
    database_name = database_config.get("NAME", "")
    is_sqlite = "sqlite3" in database_engine.lower()

    database_path = ""
    database_size = None
    connection_status = "Disconnected"
    connection_error = ""
    tables = []
    total_records = 0
    total_tables = 0

    # Resolve the SQLite database file path when applicable.
    if is_sqlite and database_name:
        database_path = os.path.abspath(str(database_name))

    try:
        # Use Django's configured database connection.
        connection.ensure_connection()
        connection_status = "Connected"

        with connection.cursor() as cursor:
            existing_tables = set(
                connection.introspection.table_names(cursor)
            )

            total_tables = len(existing_tables)

            # Collect information about Django models whose tables exist.
            for model in apps.get_models():
                table_name = model._meta.db_table

                if table_name not in existing_tables:
                    continue

                try:
                    record_count = model._base_manager.count()
                except (DatabaseError, ValueError):
                    record_count = None

                if record_count is not None:
                    total_records += record_count

                tables.append(
                    {
                        "app_label": model._meta.app_label,
                        "model_name": model._meta.verbose_name.title(),
                        "table_name": table_name,
                        "record_count": record_count,
                    }
                )

        tables.sort(
            key=lambda item: (
                item["app_label"].lower(),
                item["model_name"].lower(),
            )
        )

        # Read the database file size when using accessible SQLite storage.
        if is_sqlite and os.path.isfile(database_path):
            database_size = os.path.getsize(database_path)

    except DatabaseError:
        connection_status = "Connection error"
        connection_error = (
            "Django could not inspect the database. "
            "Check the database configuration and migrations."
        )

    except (OSError, ValueError):
        connection_error = (
            "The database file information could not be read."
        )

    context = {
        "active_section": "database",
        "database_engine": database_engine,
        "database_name": database_name,
        "database_path": database_path,
        "database_size": database_size,
        "is_sqlite": is_sqlite,
        "connection_status": connection_status,
        "connection_error": connection_error,
        "tables": tables,
        "total_tables": total_tables,
        "total_records": total_records,
    }

    return render(
        request,
        "city_admin/database.html",
        context,
    )
