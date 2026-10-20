from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import CitizenRequestForm
from .models import CitizenRequest


@login_required
def my_requests(request):

    requests = CitizenRequest.objects.filter(
        citizen=request.user
    ).order_by("-created_at")

    return render(
        request,
        "requests/my_requests.html",
        {
            "requests": requests,
        },
    )


@login_required
def create_request(request):

    if request.method == "POST":

        form = CitizenRequestForm(request.POST)

        if form.is_valid():

            citizen_request = form.save(
                commit=False
            )

            citizen_request.citizen = request.user
            citizen_request.status = "submitted"

            citizen_request.save()

            return redirect(
                "requests:request_detail",
                request_id=citizen_request.id,
            )

    else:

        form = CitizenRequestForm()

    return render(
        request,
        "requests/create_request.html",
        {
            "form": form,
        },
    )


@login_required
def request_detail(request, request_id):

    citizen_request = get_object_or_404(
        CitizenRequest,
        id=request_id,
        citizen=request.user,
    )

    return render(
        request,
        "requests/request_detail.html",
        {
            "request": citizen_request,
        },
    )