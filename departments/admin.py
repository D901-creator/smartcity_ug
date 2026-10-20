
from django.contrib import admin
from .models import Ministry, Department, Sector
from .models import Ministry, Department, Sector, Service

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "code")
    list_editable = ("is_active",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "ministry", "is_active")
    list_filter = ("is_active", "ministry")
    search_fields = ("name", "code", "description")
    list_editable = ("is_active",)


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    list_editable = ("is_active",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "department",
        "sector",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "department", "sector")
    search_fields = ("name", "code", "description")
    list_editable = ("is_active",)
