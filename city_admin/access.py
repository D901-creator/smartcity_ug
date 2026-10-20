
from functools import wraps

from django.contrib.auth.decorators import login_required


CITY_ADMIN_GROUPS = (
    "City Admin",
    "City Admins",
    "System Administrator",
    "System Administrators",
)


def is_city_admin(user):
    """
    Allow only authenticated, authorized City Admin accounts.
    Department Head accounts do not automatically qualify.
    """
    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    if user.get_username().strip().lower() == "issawamani@":
        return False

    return (
        user.is_staff
        or user.groups.filter(name__in=CITY_ADMIN_GROUPS).exists()
    )


def city_admin_required(view_func):
    """Require authentication and City Admin authorization."""

    @wraps(view_func)
    @login_required(login_url="accounts:login")
    def wrapped_view(request, *args, **kwargs):
        from django.core.exceptions import PermissionDenied

        if not is_city_admin(request.user):
            raise PermissionDenied(
                "You are not authorized to access the City Admin portal."
            )

        return view_func(request, *args, **kwargs)

    return wrapped_view
