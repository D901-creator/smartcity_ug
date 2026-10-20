 
    
from django.conf import settings
from django.db import models


class ChatMessage(models.Model):

    MESSAGE_TYPES = [
    ("text", "Text"),
    ("image", "Image"),
    ("video", "Video"),
    ("file", "File"),
    ("document", "Document"),
    ("camera", "Camera Photo"),
    ("voice", "Voice Note"),
]

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chat_messages_sent",
    )

    message = models.TextField(blank=True)

    attachment = models.FileField(
        upload_to="community_chat/%Y/%m/%d/",
        blank=True,
        null=True,
    )

    message_type = models.CharField(
        max_length=20,
        choices=MESSAGE_TYPES,
        default="text",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.sender} - {self.message[:40]}"
    
class ChatSettings(models.Model):

    THEME_CHOICES = [
        ("default", "Default"),
        ("green", "Green"),
        ("blue", "Blue"),
        ("purple", "Purple"),
        ("orange", "Orange"),
        ("dark", "Dark"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chat_settings",
    )

    theme = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        default="default",
    )

    cleared_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Chat settings - {self.user}"