
from django.contrib import admin

from .models import (
    CitizenRequest,
    RequestReply,
    RequestStatusHistory,
)


class RequestReplyInline(admin.TabularInline):
    model = RequestReply
    extra = 0
    readonly_fields = ("created_at",)


class RequestStatusHistoryInline(admin.TabularInline):
    model = RequestStatusHistory
    extra = 0
    readonly_fields = ("changed_at",)


@admin.register(CitizenRequest)
class CitizenRequestAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "subject",
        "department",
        "status",
        "priority",
        "assigned_officer",
        "created_at",
    )
    list_filter = ("status", "priority", "department")
    search_fields = (
        "subject",
        "description",
        "department",
        "citizen__username",
    )
    readonly_fields = ("reference", "created_at", "updated_at")
    inlines = [RequestReplyInline, RequestStatusHistoryInline]


@admin.register(RequestReply)
class RequestReplyAdmin(admin.ModelAdmin):
    list_display = ("request", "sender", "sender_type", "created_at")
    list_filter = ("sender_type", "created_at")
    search_fields = ("message", "request__subject")


@admin.register(RequestStatusHistory)
class RequestStatusHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "request",
        "previous_status",
        "new_status",
        "changed_by",
        "changed_at",
    )
    list_filter = ("new_status", "changed_at")
