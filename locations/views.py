
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Region, District, City, Municipality
from .forms import (
    RegionForm,
    DistrictForm,
    CityForm,
    MunicipalityForm,
)


def locations_dashboard(request):
    """National location management dashboard."""

    search = request.GET.get("q", "").strip()

    regions = Region.objects.all()
    districts = District.objects.select_related("region").all()
    cities = City.objects.select_related("district").all()
    municipalities = Municipality.objects.select_related("district").all()

    if search:
        regions = regions.filter(name__icontains=search)
        districts = districts.filter(
            Q(name__icontains=search)
            | Q(region__name__icontains=search)
        )
        cities = cities.filter(
            Q(name__icontains=search)
            | Q(district__name__icontains=search)
        )
        municipalities = municipalities.filter(
            Q(name__icontains=search)
            | Q(district__name__icontains=search)
        )

    context = {
        "active_section": "locations",
        "search": search,
        "region_count": Region.objects.count(),
        "district_count": District.objects.count(),
        "city_count": City.objects.count(),
        "municipality_count": Municipality.objects.count(),
        "regions": regions,
        "districts": districts,
        "cities": cities,
        "municipalities": municipalities,
    }

    return render(
        request,
        "city_admin/locations.html",
        context,
    )


def _create_location(request, form_class, title):
    form = form_class(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{title} created successfully.")
        return redirect("city_admin:locations")

    return render(
        request,
        "city_admin/location_form.html",
        {
            "active_section": "locations",
            "form": form,
            "page_title": title,
        },
    )


def location_create_region(request):
    return _create_location(request, RegionForm, "Add Region")


def location_create_district(request):
    return _create_location(request, DistrictForm, "Add District")


def location_create_city(request):
    return _create_location(request, CityForm, "Add City")


def location_create_municipality(request):
    return _create_location(
        request,
        MunicipalityForm,
        "Add Municipality",
    )
