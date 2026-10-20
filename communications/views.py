from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from django.utils import timezone
from .models import ChatMessage, ChatSettings

# =========================================================
# COMMUNITY CHAT PAGE
# =========================================================

@login_required
def chat(request):
    messages = (
        ChatMessage.objects
        .filter(is_deleted=False)
        .select_related("sender")
    )

    return render(
        request,
        "communications/chat.html",
        {
            "messages": messages,
        },
    )


# =========================================================
# SEND MESSAGE
# =========================================================

@login_required
@require_POST
def send_message(request):

    message_text = request.POST.get(
        "message",
        ""
    ).strip()

    attachment = request.FILES.get(
        "attachment"
    )

    # Prevent empty messages
    if not message_text and not attachment:

        return JsonResponse(
            {
                "success": False,
                "error": "Message cannot be empty.",
            },
            status=400,
        )

    # Default message type
    message_type = "text"

    # Detect attachment type
    if attachment:

        content_type = (
            attachment.content_type
            or ""
        ).lower()

        if content_type.startswith(
            "image/"
        ):

            message_type = "image"

        elif content_type.startswith(
            "video/"
        ):

            message_type = "video"

        elif content_type.startswith(
            "audio/"
        ):

            message_type = "voice"

        elif (
            content_type == "application/pdf"
        ):

            message_type = "document"

        elif (
            content_type.startswith(
                "application/msword"
            )
            or content_type.startswith(
                "application/vnd.openxmlformats"
            )
            or content_type.startswith(
                "application/vnd.ms-excel"
            )
            or content_type.startswith(
                "application/vnd.ms-powerpoint"
            )
            or content_type.startswith(
                "text/"
            )
        ):

            message_type = "document"

        else:

            message_type = "file"

    # Create database message
    new_message = ChatMessage.objects.create(
        sender=request.user,
        message=message_text,
        attachment=attachment,
        message_type=message_type,
    )

    # Sender name
    sender_name = (
        new_message.sender.get_full_name()
        or new_message.sender.username
    )

    # Attachment URL
    attachment_url = None

    if new_message.attachment:

        attachment_url = (
            new_message.attachment.url
        )

    return JsonResponse(
        {
            "success": True,

            "message": {
                "id": new_message.id,

                "sender": sender_name,

                "message":
                    new_message.message,

                "message_type":
                    new_message.message_type,

                "attachment":
                    attachment_url,

                "created_at":
                    new_message.created_at.strftime(
                        "%I:%M %p"
                    ),

                "is_mine": True,

                # Prepared for future
                # read/unread functionality.
                "is_read": False,
            },
        }
    )


# =========================================================
# GET MESSAGES
# =========================================================

@login_required
def message_list(request):

    messages = (
        ChatMessage.objects
        .filter(is_deleted=False)
        .select_related("sender")
        .order_by("created_at")
    )

    data = []

    for message in messages:

        sender_name = (
            message.sender.get_full_name()
            or message.sender.username
        )

        attachment_url = None

        if message.attachment:

            attachment_url = (
                message.attachment.url
            )

        data.append(
            {
                "id": message.id,

                "sender":
                    sender_name,

                "message":
                    message.message,

                "message_type":
                    message.message_type,

                "attachment":
                    attachment_url,

                "created_at":
                    message.created_at.strftime(
                        "%I:%M %p"
                    ),

                "is_mine":
                    message.sender_id
                    == request.user.id,

                # Prepared for future
                # read/unread functionality.
                "is_read": False,
            }
        )

    return JsonResponse(
        {
            "messages": data,
        }
    )


# =========================================================
# ONLINE USERS
# =========================================================

@login_required
def online_users(request):

    User = get_user_model()

    count = (
        User.objects
        .filter(is_active=True)
        .count()
    )

    return JsonResponse(
        {
            "online": count,
        }
    )
    
@login_required
@require_POST
def delete_message(request, message_id):

    try:
        message = ChatMessage.objects.get(
            id=message_id,
            sender=request.user,
        )

    except ChatMessage.DoesNotExist:

        return JsonResponse(
            {
                "success": False,
                "error": "Message not found or you are not allowed to delete it.",
            },
            status=404,
        )

    message.is_deleted = True
    message.save(update_fields=["is_deleted"])

    return JsonResponse(
        {
            "success": True,
            "message_id": message.id,
        }
    )
@login_required
def chat_settings(request):

    settings_obj, created = ChatSettings.objects.get_or_create(
        user=request.user
    )

    return JsonResponse(
        {
            "success": True,
            "theme": settings_obj.theme,
        }
    )


@login_required
@require_POST
def update_chat_settings(request):

    theme = request.POST.get(
        "theme",
        "default"
    ).strip().lower()

    valid_themes = {
        choice[0]
        for choice in ChatSettings.THEME_CHOICES
    }

    if theme not in valid_themes:

        return JsonResponse(
            {
                "success": False,
                "error": "Invalid chat theme.",
            },
            status=400,
        )

    settings_obj, created = ChatSettings.objects.get_or_create(
        user=request.user
    )

    settings_obj.theme = theme
    settings_obj.save()

    return JsonResponse(
        {
            "success": True,
            "theme": settings_obj.theme,
        }
    )


@login_required
@require_POST
def clear_chat(request):

    settings_obj, created = ChatSettings.objects.get_or_create(
        user=request.user
    )

    settings_obj.cleared_at = timezone.now()
    settings_obj.save()

    return JsonResponse(
        {
            "success": True,
        }
    ) 