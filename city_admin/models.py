from django.db import models
from django.conf import settings


class SystemSettings(models.Model):
    """Configurable settings for the Smart City Uganda platform."""

    THEME_CHOICES = [
        ("light", "Default Light"),
        ("green", "Green"),
        ("blue", "Blue"),
        ("dark", "Dark"),
        ("black", "Black"),
    ]

    site_name = models.CharField(
        max_length=150,
        default="Smart City Uganda",
    )

    support_email = models.EmailField(
        blank=True,
        default="",
    )

    support_phone = models.CharField(
        max_length=30,
        blank=True,
        default="",
    )

    allow_public_registration = models.BooleanField(default=True)

    require_government_verification = models.BooleanField(default=True)

    default_theme = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        default="light",
    )

    announcement_enabled = models.BooleanField(default=False)

    announcement_title = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )

    announcement_message = models.TextField(
        blank=True,
        default="",
    )

    maintenance_mode = models.BooleanField(default=False)

    maintenance_message = models.TextField(
        default=(
            "Smart City Uganda is undergoing scheduled maintenance. "
            "Please try again later."
        ),
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "System Settings"
        verbose_name_plural = "System Settings"

    def __str__(self):
        return self.site_name

    @classmethod
    def load(cls):
        """Return the single settings record used by the admin portal."""
        settings, _created = cls.objects.get_or_create(
            pk=1,
            defaults={"site_name": "Smart City Uganda"},
        )
        return settings
    
    
class PortalConfiguration(models.Model):
    PORTAL_CHOICES = [
        ("citizen", "Citizen Portal"),
        ("officer", "Officer Portal"),
        ("department_head", "Department Head Portal"),
        ("system_admin", "System Administrator Portal"),
    ]

    portal_key = models.CharField(
        max_length=30,
        choices=PORTAL_CHOICES,
        unique=True,
    )
    display_name = models.CharField(max_length=120)
    welcome_message = models.CharField(max_length=250, blank=True)
    is_enabled = models.BooleanField(default=True)
    maintenance_enabled = models.BooleanField(default=False)
    maintenance_message = models.TextField(
        blank=True,
        default="This portal is temporarily unavailable for maintenance.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["portal_key"]

    def __str__(self):
        return self.display_name


class PortalModule(models.Model):
    portal = models.ForeignKey(
        PortalConfiguration,
        on_delete=models.CASCADE,
        related_name="modules",
    )
    code = models.SlugField(max_length=80)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    is_enabled = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["portal", "code"],
                name="unique_portal_module_code",
            ),
        ]

    def __str__(self):
        return f"{self.portal.display_name} — {self.name}"


class PortalMenuItem(models.Model):
    portal = models.ForeignKey(
        PortalConfiguration,
        on_delete=models.CASCADE,
        related_name="menu_items",
    )
    key = models.SlugField(max_length=80)
    label = models.CharField(max_length=120)
    icon = models.CharField(max_length=80, default="bi-grid")
    url_name = models.CharField(max_length=150, blank=True)
    is_visible = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "label"]
        constraints = [
            models.UniqueConstraint(
                fields=["portal", "key"],
                name="unique_portal_menu_key",
            ),
        ]

    def __str__(self):
        return f"{self.portal.display_name} — {self.label}"


class PortalConfigurationAudit(models.Model):
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="portal_configuration_audits",
    )
    portal = models.ForeignKey(
        PortalConfiguration,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_entries",
    )
    action = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.action} — {self.created_at:%Y-%m-%d %H:%M}"


class SecurityEvent(models.Model):
    SEVERITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("investigating", "Investigating"),
        ("resolved", "Resolved"),
        ("dismissed", "Dismissed"),
    ]

    EVENT_TYPE_CHOICES = [
        ("failed_login", "Failed Login"),
        ("access_denied", "Access Denied"),
        ("suspicious_request", "Suspicious Request"),
        ("account_change", "Account Change"),
        ("permission_change", "Permission Change"),
        ("configuration_change", "Configuration Change"),
        ("other", "Other"),
    ]

    event_type = models.CharField(
        max_length=40,
        choices=EVENT_TYPE_CHOICES,
        default="other",
        db_index=True,
    )
    severity = models.CharField(
        max_length=10,
        choices=SEVERITY_CHOICES,
        default="medium",
        db_index=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        db_index=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="city_admin_security_events",
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )
    request_path = models.CharField(max_length=500, blank=True)
    summary = models.CharField(max_length=250)
    details = models.TextField(blank=True)

    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_city_admin_security_events",
    )
    review_notes = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Security Event"
        verbose_name_plural = "Security Events"

    def __str__(self):
        return f"{self.get_severity_display()} — {self.summary}"