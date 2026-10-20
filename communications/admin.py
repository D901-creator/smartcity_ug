from django.contrib import admin
from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):

    list_display = (
        "sender",
        "message_type",
        "created_at",
        "is_deleted",
    )

    list_filter = (
        "message_type",
        "is_deleted",
        "created_at",
    )

    search_fields = (
        "sender__username",
        "message",
    )

    readonly_fields = (
        "created_at",
    )