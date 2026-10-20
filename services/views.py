from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import GovernmentService, ServiceRequest


def service_list(request):

    services = GovernmentService.objects.filter(
        is_active=True
    )

    search = request.GET.get("search", "").strip()

    category = request.GET.get(
        "category",
        ""
    ).strip()

    if search:
        services = services.filter(
            name__icontains=search
        ) | services.filter(
            short_description__icontains=search
        )

    if category:
        services = services.filter(
            category=category
        )

    categories = GovernmentService.CATEGORY_CHOICES

    context = {
        "services": services,
        "categories": categories,
        "search": search,
        "selected_category": category,
    }

    return render(
        request,
        "services/service_list.html",
        context
    )


def service_detail(request, service_id):

    service = get_object_or_404(
        GovernmentService,
        id=service_id,
        is_active=True
    )

    required_information = []

    if service.required_information:

        required_information = [
            item.strip()
            for item in service.required_information.split(",")
            if item.strip()
        ]

    context = {
        "service": service,
        "required_information": required_information,
    }

    return render(
        request,
        "services/service_detail.html",
        context
    )


def service_request(request, service_id):

    service = get_object_or_404(
        GovernmentService,
        id=service_id,
        is_active=True
    )

    if request.method == "POST":

        citizen_name = request.POST.get(
            "citizen_name",
            "Guest Citizen"
        ).strip()

        citizen_phone = request.POST.get(
            "citizen_phone",
            ""
        ).strip()

        citizen_district = request.POST.get(
            "citizen_district",
            "Kampala"
        ).strip()

        description = request.POST.get(
            "description",
            ""
        ).strip()

        if not description:

            context = {
                "service": service,
                "error": "Please describe the service you need.",
            }

            return render(
                request,
                "services/service_request.html",
                context
            )

        reference_number = (
            f"SCU-{timezone.now().strftime('%Y%m%d')}-"
            f"{timezone.now().strftime('%H%M%S%f')[-6:]}"
        )

        ServiceRequest.objects.create(
            service=service,
            citizen_name=citizen_name,
            citizen_phone=citizen_phone,
            citizen_district=citizen_district,
            description=description,
            reference_number=reference_number,
        )

        return redirect(
            "services:request_success",
            reference_number=reference_number
        )

    context = {
        "service": service,
    }

    return render(
        request,
        "services/service_request.html",
        context
    )


def request_success(request, reference_number):

    service_request_object = get_object_or_404(
        ServiceRequest,
        reference_number=reference_number
    )

    context = {
        "service_request": service_request_object
    }

    return render(
        request,
        "services/request_success.html",
        context
    )