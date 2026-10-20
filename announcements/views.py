from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from accounts.models import AccountProfile
from .models import DepartmentAnnouncement


def department_head_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        try:
            profile = request.user.account_profile
        except AccountProfile.DoesNotExist:
            messages.error(request, "Department Head access required.")
            return redirect("department_head:login")

        if profile.role != "department_head":
            messages.error(request, "Access denied.")
            return redirect("department_head:login")

        if not profile.department_id:
            messages.error(request, "Your account has no department assigned.")
            return redirect("department_head:dashboard")

        request.department_head_profile = profile
        return view_func(request, *args, **kwargs)

    return wrapper


@department_head_required
def announcement_list(request):
    announcements = DepartmentAnnouncement.objects.filter(
        department=request.department_head_profile.department
    )

    return render(
        request,
        "announcements/list.html",
        {
            "page_title": "Department Announcements",
            "announcements": announcements,
        },
    )


@department_head_required
def announcement_create(request):
    profile = request.department_head_profile

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        message = request.POST.get("message", "").strip()
        action = request.POST.get("action", "draft")
        expires_at_value = request.POST.get("expires_at", "").strip()

        if not title or not message:
            messages.error(request, "Title and message are required.")
        elif action not in ["draft", "publish"]:
            messages.error(request, "Invalid announcement action.")
        else:
            expires_at = None

            if expires_at_value:
                from datetime import datetime

                try:
                    expires_at = timezone.make_aware(
                        datetime.strptime(expires_at_value, "%Y-%m-%dT%H:%M")
                    )
                except ValueError:
                    messages.error(request, "Enter a valid expiry date and time.")
                    return render(
                        request,
                        "announcements/create.html",
                        {"page_title": "Create Announcement"},
                    )

                if expires_at <= timezone.now():
                    messages.error(request, "Expiry must be in the future.")
                    return render(
                        request,
                        "announcements/create.html",
                        {"page_title": "Create Announcement"},
                    )

            status = (
                DepartmentAnnouncement.Status.PUBLISHED
                if action == "publish"
                else DepartmentAnnouncement.Status.DRAFT
            )

            announcement = DepartmentAnnouncement.objects.create(
                title=title,
                message=message,
                department=profile.department,
                created_by=request.user,
                status=status,
                published_at=timezone.now() if action == "publish" else None,
                expires_at=expires_at,
            )

            messages.success(request, "Announcement saved successfully.")
            return redirect("announcements:list")

    return render(
        request,
        "announcements/create.html",
        {"page_title": "Create Announcement"},
    )


@department_head_required
def announcement_archive(request, announcement_id):
    if request.method != "POST":
        return redirect("announcements:list")

    announcement = get_object_or_404(
        DepartmentAnnouncement,
        pk=announcement_id,
        department=request.department_head_profile.department,
    )

    announcement.status = DepartmentAnnouncement.Status.ARCHIVED
    announcement.save(update_fields=["status", "updated_at"])

    messages.success(request, "Announcement archived.")
    return redirect("announcements:list")