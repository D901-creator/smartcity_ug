
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="districts",
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text="Latitude of the district's representative map point.",
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text="Longitude of the district's representative map point.",
    )

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "region"],
                name="unique_district_per_region",
            )
        ]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    district = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        related_name="cities",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        related_name="municipalities",
    )

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "district"],
                name="unique_municipality_per_district",
            )
        ]

    def __str__(self):
        return self.name
