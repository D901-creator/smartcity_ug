from django.shortcuts import render

# Create your views here.

from datetime import date, datetime, time, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import CalendarEventForm
from .models import CalendarEvent


def _parse_month(value):
    try:
        parsed = datetime.strptime(value, "%Y-%m")
        return date(parsed.year, parsed.month, 1)
    except (ValueError, TypeError):
        today = timezone.localdate()
        return date(today.year, today.month, 1)


def _month_bounds(month_date):
    start = timezone.make_aware(
        datetime.combine(month_date, time.min)
    )

    if month_date.month == 12:
        next_month = date(month_date.year + 1, 1, 1)
    else:
        next_month = date(month_date.year, month_date.month + 1, 1)

    end = timezone.make_aware(
        datetime.combine(next_month, time.min)
    )

    return start, end



import calendar
from datetime import date, datetime, time, timedelta

from django.utils import timezone


def calendar_view(request):
    month_value = request.GET.get("month", "")

    try:
        parsed = datetime.strptime(month_value, "%Y-%m")
        month = date(parsed.year, parsed.month, 1)
    except (ValueError, TypeError):
        today = timezone.localdate()
        month = date(today.year, today.month, 1)

    if month.month == 12:
        next_month_date = date(month.year + 1, 1, 1)
    else:
        next_month_date = date(month.year, month.month + 1, 1)

    previous_month_date = (
        date(month.year - 1, 12, 1)
        if month.month == 1
        else date(month.year, month.month - 1, 1)
    )

    month_start = timezone.make_aware(
        datetime.combine(month, time.min)
    )
    month_end = timezone.make_aware(
        datetime.combine(next_month_date, time.min)
    )

    events = list(
        CalendarEvent.objects.filter(
            created_by=request.user,
            start_time__lt=month_end,
            end_time__gte=month_start,
        ).order_by("start_time")
    )

    events_by_day = {}

    for event in events:
        first_day = max(event.start_time.date(), month)
        last_day = min(
            event.end_time.date(),
            next_month_date - timedelta(days=1),
        )

        current_day = first_day
        while current_day <= last_day:
            events_by_day.setdefault(current_day.day, []).append(event)
            current_day += timedelta(days=1)

    month_calendar = calendar.Calendar(firstweekday=0)
    weeks = month_calendar.monthdatescalendar(month.year, month.month)
    calendar_cells = []

    for week in weeks:
        for day in week:
            if day.month == month.month:
                calendar_cells.append({
                    "date": day,
                    "events": events_by_day.get(day.day, []),
                })
            else:
                calendar_cells.append({
                    "date": None,
                    "events": [],
                })

    context = {
        "month": month,
        "month_label": month.strftime("%B %Y"),
        "calendar_cells": calendar_cells,
        "events": events,
        "today": timezone.localdate(),
        "previous_month": previous_month_date.strftime("%Y-%m"),
        "next_month": next_month_date.strftime("%Y-%m"),
        "event_count": len(events),
        "upcoming_events": [
            event for event in events
            if event.start_time >= timezone.now()
        ][:5],
    }

    return render(request, "calendar_app/calendar.html", context)

@login_required
def create_event(request):
    if request.method == "POST":
        form = CalendarEventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user

            try:
                event.full_clean()
                event.save()
            except ValidationError as exc:
                form.add_error(None, exc)

            if event.pk:
                messages.success(request, "Calendar event created.")
                return redirect("calendar_app:calendar")
    else:
        form = CalendarEventForm()

    return render(
        request,
        "calendar_app/event_form.html",
        {"form": form, "page_title": "Create event"},
    )


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(
        CalendarEvent,
        pk=event_id,
        created_by=request.user,
    )

    return render(
        request,
        "calendar_app/event_detail.html",
        {"event": event},
    )


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(
        CalendarEvent,
        pk=event_id,
        created_by=request.user,
    )

    if request.method == "POST":
        form = CalendarEventForm(request.POST, instance=event)

        if form.is_valid():
            try:
                updated_event = form.save(commit=False)
                updated_event.full_clean()
                updated_event.save()
            except ValidationError as exc:
                form.add_error(None, exc)
            else:
                messages.success(request, "Calendar event updated.")
                return redirect("calendar_app:event_detail", event_id=event.pk)
    else:
        form = CalendarEventForm(instance=event)

    return render(
        request,
        "calendar_app/event_form.html",
        {"form": form, "page_title": "Edit event"},
    )


@login_required
@require_POST
def delete_event(request, event_id):
    event = get_object_or_404(
        CalendarEvent,
        pk=event_id,
        created_by=request.user,
    )

    event.delete()
    messages.success(request, "Calendar event deleted.")

    return redirect("calendar_app:calendar")
