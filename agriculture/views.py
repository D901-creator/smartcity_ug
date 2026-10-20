from django.shortcuts import render

from .models import (
    FarmerProfile,
    Farm,
    MarketListing,
    BuyerRequest,
    AgriculturalProject,
    ExtensionService,
    DiseaseReport,
    Cooperative,
    AgriculturalInput,
)
from .models import (
    Fisher,
    FishingActivity,
    AquacultureFarm,
    FishProcessingFacility,
    FishMarketListing,
)
from .forms import (
    FisherForm,
    FishingActivityForm,
    AquacultureFarmForm,
    FishProcessingFacilityForm,
    FishMarketListingForm,
)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

from .forms import FarmerProfileForm, FarmForm
from .models import FarmerProfile, Farm
from django.shortcuts import render, redirect

from .forms import (  MarketMatchResponseForm, AgriculturalInputForm, ExtensionServiceForm, AgriculturalProjectForm,
    AgriculturalProgramForm, DiseaseReportForm,  IrrigationProjectForm,
    FarmerProfileForm,
    FarmForm,
    CropForm,
    CropProductionForm,
    LivestockRecordForm,
    AgriculturalProgram,
)

from .models import (FarmerProfile,
    Farm,
    Crop,
    CropProduction,
    LivestockRecord,
)
from .models import ( IrrigationProject,
    FarmerProfile,
    Farm,
    Crop,
    CropProduction,
    LivestockRecord,
    MarketListing,
    BuyerRequest,
    AgriculturalProject,
    ExtensionService,
    DiseaseReport,
    Cooperative,
    MarketMatch,
)


from .forms import (
    FarmerProfileForm,
    FarmForm,
    CropForm,
    CropProductionForm,
    LivestockRecordForm,
    MarketListingForm,
    BuyerRequestForm,
)


def home(request):

    context = {
        "stats": {
            "farmers": FarmerProfile.objects.count(),
            "farms": Farm.objects.count(),
            "market_listings": MarketListing.objects.filter(
                status="available"
            ).count(),
            "buyer_requests": BuyerRequest.objects.filter(
                status="open"
            ).count(),
            "projects": AgriculturalProject.objects.filter(
                status="active"
            ).count(),
            "extension_services": ExtensionService.objects.count(),
            "disease_reports": DiseaseReport.objects.filter(
                status__in=["reported", "assigned", "investigating"]
            ).count(),
            "cooperatives": Cooperative.objects.count(),
        },

        "market_listings": MarketListing.objects.filter(
            status="available"
        ).order_by("-created_at")[:6],

        "buyer_requests": BuyerRequest.objects.filter(
            status="open"
        ).order_by("-created_at")[:6],

        "projects": AgriculturalProject.objects.filter(
            status="active"
        ).order_by("-start_date")[:6],
    }

    return render(
        request,
        "agriculture/home.html",
        context
    )
def farmers(request):
    farmer_list = FarmerProfile.objects.all().order_by("-created_at")

    context = {
        "farmers": farmer_list,
        "total_farmers": farmer_list.count(),
    }

    return render(
        request,
        "agriculture/farmers.html",
        context
    )


def register_farmer(request):

    if request.method == "POST":

        form = FarmerProfileForm(request.POST)

        if form.is_valid():

            farmer = form.save()

            messages.success(
                request,
                f"{farmer.farmer_name} has been registered successfully."
            )

            return redirect("agriculture:farmers")

    else:
        form = FarmerProfileForm()

    return render(
        request,
        "agriculture/register_farmer.html",
        {
            "form": form
        }
    )


def farms(request):

    farm_list = Farm.objects.select_related(
        "farmer"
    ).all().order_by("-created_at")

    return render(
        request,
        "agriculture/farms.html",
        {
            "farms": farm_list,
        }
    )


def register_farm(request):

    if request.method == "POST":

        form = FarmForm(request.POST)

        if form.is_valid():

            farm = form.save()

            messages.success(
                request,
                f"{farm.farm_name} has been registered successfully."
            )

            return redirect("agriculture:farms")

    else:
        form = FarmForm()

    return render(
        request,
        "agriculture/register_farm.html",
        {
            "form": form
        }
    )
def crop_production(request):

    production = CropProduction.objects.select_related(
        "farmer",
        "farm",
        "crop"
    ).all().order_by("-id")

    return render(
        request,
        "agriculture/crop_production.html",
        {
            "production": production,
        }
    )


def register_crop_production(request):

    if request.method == "POST":

        form = CropProductionForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Crop production record added successfully."
            )

            return redirect(
                "agriculture:crop_production"
            )

    else:

        form = CropProductionForm()

    return render(
        request,
        "agriculture/register_crop_production.html",
        {
            "form": form,
        }
    )


def livestock(request):

    livestock_records = LivestockRecord.objects.select_related(
        "farmer"
    ).all().order_by("-id")

    return render(
        request,
        "agriculture/livestock.html",
        {
            "livestock_records": livestock_records,
        }
    )


def register_livestock(request):

    if request.method == "POST":

        form = LivestockRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Livestock record added successfully."
            )

            return redirect(
                "agriculture:livestock"
            )

    else:

        form = LivestockRecordForm()

    return render(
        request,
        "agriculture/register_livestock.html",
        {
            "form": form,
        }
    ) 

def market(request):
    listings = MarketListing.objects.filter(
        status="available"
    ).order_by("-created_at")

    buyer_requests = BuyerRequest.objects.filter(
        status="open"
    ).order_by("-created_at")

    context = {
        "listings": listings,
        "buyer_requests": buyer_requests,
    }

    return render(request, "agriculture/market.html", context)


def create_market_listing(request):
    if request.method == "POST":
        form = MarketListingForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Agricultural product successfully listed in the market."
            )
            return redirect("agriculture:market")

    else:
        form = MarketListingForm()

    return render(
        request,
        "agriculture/create_market_listing.html",
        {"form": form}
    )
def calculate_match_score(buyer_request, listing):
    score = 0

    product_match = False
    quantity_match = False
    district_match = False
    price_match = False

    # 1. PRODUCT MATCH
    requested_product = buyer_request.product_required.lower().strip()
    listed_product = listing.product_name.lower().strip()

    if requested_product == listed_product:
        score += 40
        product_match = True

    elif requested_product in listed_product or listed_product in requested_product:
        score += 30
        product_match = True

    # 2. QUANTITY MATCH
    if listing.quantity >= buyer_request.quantity_required:
        score += 25
        quantity_match = True

    # 3. DISTRICT MATCH
    if (
        buyer_request.district
        and listing.district
        and buyer_request.district.lower().strip()
        == listing.district.lower().strip()
    ):
        score += 20
        district_match = True

    # 4. PRICE MATCH
    if (
        listing.price_per_unit is not None
        and buyer_request.maximum_price is not None
        and listing.price_per_unit <= buyer_request.maximum_price
    ):
        score += 15
        price_match = True

    return {
        "score": score,
        "product": product_match,
        "quantity": quantity_match,
        "district": district_match,
        "price": price_match,
    }
def generate_matches_for_request(buyer_request):
    listings = MarketListing.objects.filter(
        status="available"
    )

    for listing in listings:

        result = calculate_match_score(
            buyer_request,
            listing
        )

        # Only create a match when the product matches
        if result["product"]:

            MarketMatch.objects.update_or_create(
                buyer_request=buyer_request,
                market_listing=listing,
                defaults={
                    "match_score": result["score"],
                    "matched_product": result["product"],
                    "matched_quantity": result["quantity"],
                    "matched_district": result["district"],
                    "matched_price": result["price"],
                }
            )
def matches(request):
    matches = MarketMatch.objects.select_related(
        "buyer_request",
        "market_listing",
        "market_listing__farmer",
    ).filter(
        match_score__gte=40
    ).order_by(
        "-match_score",
        "-created_at"
    )

    context = {
        "matches": matches,
    }

    return render(
        request,
        "agriculture/matches.html",
        context
    )
def match_detail(request, match_id):

    match = get_object_or_404(
        MarketMatch.objects.select_related(
            "buyer_request",
            "market_listing",
            "market_listing__farmer",
        ),
        id=match_id
    )

    return render(
        request,
        "agriculture/match_detail.html",
        {
            "match": match,
        }
    )
def respond_to_match(request, match_id):

    match = get_object_or_404(
        MarketMatch,
        id=match_id
    )

    if request.method == "POST":

        form = MarketMatchResponseForm(
            request.POST,
            instance=match
        )

        if form.is_valid():

            updated_match = form.save()

            if updated_match.status == "contacted":
                updated_match.contacted_at = timezone.now()

            elif updated_match.status == "accepted":
                updated_match.accepted_at = timezone.now()

            elif updated_match.status == "completed":
                updated_match.completed_at = timezone.now()

            updated_match.save()

            messages.success(
                request,
                "Match response successfully updated."
            )

            return redirect(
                "agriculture:match_detail",
                match_id=match.id
            )

    else:

        form = MarketMatchResponseForm(
            instance=match
        )

    return render(
        request,
        "agriculture/respond_to_match.html",
        {
            "form": form,
            "match": match,
        }
    )

def create_buyer_request(request):
    if request.method == "POST":

        form = BuyerRequestForm(request.POST)

        if form.is_valid():

            buyer_request = form.save()

            generate_matches_for_request(
                buyer_request
            )

            messages.success(
                request,
                "Buyer request submitted and matching farmers have been identified."
            )

            return redirect(
                "agriculture:matches",
            )

    else:
        form = BuyerRequestForm()

    return render(
        request,
        "agriculture/create_buyer_request.html",
        {"form": form}
    )
    
def agricultural_inputs(request):

    inputs = AgriculturalInput.objects.filter(
        is_available=True
    ).order_by("name")

    context = {
        "inputs": inputs,
    }

    return render(
        request,
        "agriculture/agricultural_inputs.html",
        context
    )
def create_agricultural_input(request):

    if request.method == "POST":

        form = AgriculturalInputForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Agricultural input successfully added."
            )

            return redirect(
                "agriculture:agricultural_inputs"
            )

    else:

        form = AgriculturalInputForm()

    return render(
        request,
        "agriculture/create_agricultural_input.html",
        {
            "form": form
        }
    )
def extension_services(request):

    services = ExtensionService.objects.all().order_by(
        "scheduled_date"
    )

    context = {
        "services": services,
    }

    return render(
        request,
        "agriculture/extension_services.html",
        context
    )
def create_extension_service(request):

    if request.method == "POST":

        form = ExtensionServiceForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Extension service successfully scheduled."
            )

            return redirect(
                "agriculture:extension_services"
            )

    else:

        form = ExtensionServiceForm()

    return render(
        request,
        "agriculture/create_extension_service.html",
        {
            "form": form
        }
    )
    
def agricultural_projects(request):
    projects = AgriculturalProject.objects.all().order_by("-start_date")

    context = {
        "projects": projects,
    }

    return render(
        request,
        "agriculture/agricultural_projects.html",
        context
    )


def create_agricultural_project(request):
    if request.method == "POST":
        form = AgriculturalProjectForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Agricultural project successfully added."
            )

            return redirect(
                "agriculture:agricultural_projects"
            )
    else:
        form = AgriculturalProjectForm()

    return render(
        request,
        "agriculture/create_agricultural_project.html",
        {"form": form}
    )
    
def agricultural_programs(request):
    programs = AgriculturalProgram.objects.all().order_by(
        "-application_open"
    )

    context = {
        "programs": programs,
    }

    return render(
        request,
        "agriculture/agricultural_programs.html",
        context
    )


def create_agricultural_program(request):
    if request.method == "POST":
        form = AgriculturalProgramForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Agricultural programme successfully added."
            )

            return redirect(
                "agriculture:agricultural_programs"
            )
    else:
        form = AgriculturalProgramForm()

    return render(
        request,
        "agriculture/create_agricultural_program.html",
        {"form": form}
    )
def disease_reports(request):
    reports = DiseaseReport.objects.all().order_by("-created_at")

    context = {
        "reports": reports,
    }

    return render(
        request,
        "agriculture/disease_reports.html",
        context
    )
def create_disease_report(request):
    if request.method == "POST":
        form = DiseaseReportForm(request.POST)

        if form.is_valid():
            report = form.save()

            messages.success(
                request,
                "Disease report successfully submitted."
            )

            return redirect(
                "agriculture:disease_reports"
            )
    else:
        form = DiseaseReportForm()

    return render(
        request,
        "agriculture/create_disease_report.html",
        {"form": form}
    )
def irrigation_projects(request):
    projects = IrrigationProject.objects.all().order_by(
        "district",
        "name"
    )

    context = {
        "projects": projects,
    }

    return render(
        request,
        "agriculture/irrigation_projects.html",
        context
    )
def create_irrigation_project(request):
    if request.method == "POST":
        form = IrrigationProjectForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Irrigation project successfully added."
            )

            return redirect(
                "agriculture:irrigation_projects"
            )
    else:
        form = IrrigationProjectForm()

    return render(
        request,
        "agriculture/create_irrigation_project.html",
        {"form": form}
    )
def cooperatives(request):
    cooperatives_list = Cooperative.objects.all().order_by(
        "district",
        "name"
    )

    context = {
        "cooperatives": cooperatives_list,
    }

    return render(
        request,
        "agriculture/cooperatives.html",
        context
    )
    
def agricultural_statistics(request):
    context = {
        # ============================================================
        # GENERAL AGRICULTURE STATISTICS
        # ============================================================

        "farmers_count": FarmerProfile.objects.count(),

        "farms_count": Farm.objects.count(),

        "crop_production_count": CropProduction.objects.count(),

        "livestock_count": LivestockRecord.objects.count(),

        "market_listings_count": MarketListing.objects.filter(
            status="available"
        ).count(),

        "buyer_requests_count": BuyerRequest.objects.filter(
            status="open"
        ).count(),

        "cooperatives_count": Cooperative.objects.count(),

        "projects_count": AgriculturalProject.objects.filter(
            status="active"
        ).count(),

        "disease_reports_count": DiseaseReport.objects.filter(
            status__in=[
                "reported",
                "assigned",
                "investigating"
            ]
        ).count(),

        "irrigation_projects_count": IrrigationProject.objects.count(),


        # ============================================================
        # PHASE 3 — FISHING & FISHERIES STATISTICS
        # ============================================================

        "fishers_count": Fisher.objects.count(),

        "fishing_activities_count": FishingActivity.objects.count(),

        "aquaculture_farms_count": AquacultureFarm.objects.count(),

        "fish_processing_facilities_count": (
            FishProcessingFacility.objects.count()
        ),

        "fish_market_listings_count": FishMarketListing.objects.filter(
            status="available"
        ).count(),
    }

    return render(
        request,
        "agriculture/agricultural_statistics.html",
        context
    )
    
    # ============================================================
# PHASE 3 — FISHING & FISHERIES VIEWS
# ============================================================


def fishing_fishers(request):
    """
    Fisher Registration & Records
    """

    if request.method == "POST":
        form = FisherForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("agriculture:fishing_fishers")

    else:
        form = FisherForm()

    fishers = Fisher.objects.all()

    context = {
        "form": form,
        "fishers": fishers,
        "active": "agriculture",
    }

    return render(
        request,
        "agriculture/fishing/fishers.html",
        context,
    )


def capture_fisheries(request):
    """
    Capture Fisheries
    """

    if request.method == "POST":
        form = FishingActivityForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("agriculture:capture_fisheries")

    else:
        form = FishingActivityForm()

    activities = (
        FishingActivity.objects
        .select_related("fisher")
        .all()
    )

    context = {
        "form": form,
        "activities": activities,
        "active": "agriculture",
    }

    return render(
        request,
        "agriculture/fishing/capture_fisheries.html",
        context,
    )


def aquaculture(request):
    """
    Aquaculture / Fish Farming
    """

    if request.method == "POST":
        form = AquacultureFarmForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("agriculture:aquaculture")

    else:
        form = AquacultureFarmForm()

    farms = AquacultureFarm.objects.all()

    context = {
        "form": form,
        "farms": farms,
        "active": "agriculture",
    }

    return render(
        request,
        "agriculture/fishing/aquaculture.html",
        context,
    )


def fish_processing(request):
    """
    Fish Processing & Value Addition
    """

    if request.method == "POST":
        form = FishProcessingFacilityForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("agriculture:fish_processing")

    else:
        form = FishProcessingFacilityForm()

    facilities = FishProcessingFacility.objects.all()

    context = {
        "form": form,
        "facilities": facilities,
        "active": "agriculture",
    }

    return render(
        request,
        "agriculture/fishing/fish_processing.html",
        context,
    )


def fish_marketing(request):
    """
    Fish Marketing & Trade
    """

    if request.method == "POST":
        form = FishMarketListingForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("agriculture:fish_marketing")

    else:
        form = FishMarketListingForm()

    listings = FishMarketListing.objects.all()

    context = {
        "form": form,
        "listings": listings,
        "active": "agriculture",
    }

    return render(
        request,
        "agriculture/fishing/fish_marketing.html",
        context,
    )