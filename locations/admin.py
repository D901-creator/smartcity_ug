
from django.contrib import admin
from .models import Region, District, City


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region")
    list_filter = ("region",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "district")
    list_filter = ("district",)
    search_fields = ("name",)
    ordering = ("name",)
