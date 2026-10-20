from django.shortcuts import render,redirect
from django.db.models import Q

import json
from .forms import EconomicFinancialExcelImportForm
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter

from django.http import HttpResponse
from django.db.models import Count, Sum
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from .models import (
    FinancialPlanningInformation,
    BusinessRegistrationInformation,EconomicFinancialRecord,
    BusinessRegistrationRequest,
     TradeMarketInformation,EconomicProject,FundingBudgetInformation,
FundingBudgetRequest,
    TradeMarketRequest,CooperativeInformation,
    CooperativeRequest,
)
from django.db.models import Count, Sum
from django.shortcuts import render

from .forms import BusinessRegistrationRequestForm,TradeMarketRequestForm,CooperativeRequestForm,FundingBudgetRequestForm
from .models import FinancialPlanningInformation

def home(request):
    services = [
        {
            "name": "Financial Planning",
            "icon": "bi-wallet2",
            "description": "Access financial planning information, guidance and related economic services.",
            "url": "economic_development:financial_planning",
            "color": "primary",
        },
        {
            "name": "Business Registration",
            "icon": "bi-shop",
            "description": "Access business registration information, requirements and related services.",
            "url": "economic_development:business_registration",
            "color": "success",
        },
        {
            "name": "Trade & Markets",
            "icon": "bi-cart3",
            "description": "Access trade, market and business opportunity information.",
           "url": "economic_development:trade_markets",
            "color": "warning",
        },
        {
            "name": "Cooperatives",
            "icon": "bi-people",
            "description": "Access cooperative information, support services and opportunities.",
              "url": "economic_development:cooperatives",
            "color": "info",
        },
        {
            "name": "Economic Projects",
            "icon": "bi-kanban",
            "description": "Explore economic development projects and related opportunities.",
           "url": "economic_development:economic_projects",
            "color": "secondary",
        },
        {
            "name": "Funding & Budgeting",
            "icon": "bi-cash-stack",
            "description": "Access funding opportunities, budgeting information and related services.",
           "url": "economic_development:funding_budget",
            "color": "success",
        },
        {
            "name": "Economic Reports",
            "icon": "bi-bar-chart-line",
            "description": "View economic reports, statistics and published economic information.",
            "url": None,
            "color": "dark",
        },
    ]

    return render(
        request,
        "economic_development/home.html",
        {
            "services": services,
        },
    )
    
def financial_planning(request):
    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()

    financial_information = FinancialPlanningInformation.objects.filter(
        is_published=True
    )

    if search:
        financial_information = financial_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(important_information__icontains=search)
        )

    if information_type:
        financial_information = financial_information.filter(
            information_type=information_type
        )

    context = {
        "financial_information": financial_information,
        "information_types": FinancialPlanningInformation.INFORMATION_TYPES,
        "search": search,
        "selected_type": information_type,
    }

    return render(
        request,
        "economic_development/financial_planning.html",
        context
    )


def financial_planning_detail(request, information_id):
    information = get_object_or_404(
        FinancialPlanningInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "economic_development/financial_planning_detail.html",
        {
            "information": information,
        }
    )
    
def business_registration(request):

    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()

    registration_information = (
        BusinessRegistrationInformation.objects.filter(
            is_published=True
        )
    )

    if search:
        registration_information = registration_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(requirements__icontains=search)
        )

    if information_type:
        registration_information = registration_information.filter(
            information_type=information_type
        )

    context = {
        "registration_information": registration_information,
        "information_types": (
            BusinessRegistrationInformation.INFORMATION_TYPES
        ),
        "search": search,
        "selected_type": information_type,
    }

    return render(
        request,
        "economic_development/business_registration.html",
        context
    )


def business_registration_detail(request, information_id):

    information = get_object_or_404(
        BusinessRegistrationInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "economic_development/business_registration_detail.html",
        {
            "information": information,
        }
    )


def business_registration_apply(request):

    if request.method == "POST":

        form = BusinessRegistrationRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            registration_request = form.save()

            messages.success(
                request,
                "Your business registration request has been submitted successfully."
            )

            return redirect(
                "economic_development:business_registration_success",
                request_id=registration_request.id
            )

    else:

        form = BusinessRegistrationRequestForm()

    return render(
        request,
        "economic_development/business_registration_apply.html",
        {
            "form": form,
        }
    )


def business_registration_success(request, request_id):

    registration_request = get_object_or_404(
        BusinessRegistrationRequest,
        id=request_id
    )

    return render(
        request,
        "economic_development/business_registration_success.html",
        {
            "registration_request": registration_request,
        }
    )
    
def trade_markets(request):

    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    trade_information = TradeMarketInformation.objects.filter(
        is_published=True
    )

    if search:
        trade_information = trade_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(requirements__icontains=search)
        )

    if information_type:
        trade_information = trade_information.filter(
            information_type=information_type
        )

    if district:
        trade_information = trade_information.filter(
            district__icontains=district
        )

    context = {
        "trade_information": trade_information,
        "information_types": TradeMarketInformation.INFORMATION_TYPES,
        "search": search,
        "selected_type": information_type,
        "selected_district": district,
    }

    return render(
        request,
        "economic_development/trade_markets.html",
        context
    )


def trade_market_detail(request, information_id):

    information = get_object_or_404(
        TradeMarketInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "economic_development/trade_market_detail.html",
        {
            "information": information,
        }
    )


def trade_market_request_create(request):

    if request.method == "POST":

        form = TradeMarketRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            trade_request = form.save()

            messages.success(
                request,
                "Your trade and market request has been submitted successfully."
            )

            return redirect(
                "economic_development:trade_market_request_success",
                request_id=trade_request.id
            )

    else:

        form = TradeMarketRequestForm()

    return render(
        request,
        "economic_development/trade_market_request_form.html",
        {
            "form": form,
        }
    )


def trade_market_request_success(request, request_id):

    trade_request = get_object_or_404(
        TradeMarketRequest,
        id=request_id
    )

    return render(
        request,
        "economic_development/trade_market_request_success.html",
        {
            "trade_request": trade_request,
        }
    )
    
def cooperatives(request):

    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    cooperative_information = CooperativeInformation.objects.filter(
        is_published=True
    )

    if search:
        cooperative_information = cooperative_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(requirements__icontains=search)
        )

    if information_type:
        cooperative_information = cooperative_information.filter(
            information_type=information_type
        )

    if district:
        cooperative_information = cooperative_information.filter(
            district__icontains=district
        )

    context = {
        "cooperative_information": cooperative_information,
        "information_types": CooperativeInformation.INFORMATION_TYPES,
        "search": search,
        "selected_type": information_type,
        "selected_district": district,
    }

    return render(
        request,
        "economic_development/cooperatives.html",
        context
    )


def cooperative_detail(request, information_id):

    information = get_object_or_404(
        CooperativeInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "economic_development/cooperative_detail.html",
        {
            "information": information
        }
    )


def cooperative_request_create(request):

    if request.method == "POST":

        form = CooperativeRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            cooperative_request = form.save()

            messages.success(
                request,
                "Your cooperative request has been submitted successfully."
            )

            return redirect(
                "economic_development:cooperative_request_success",
                request_id=cooperative_request.id
            )

    else:
        form = CooperativeRequestForm()

    return render(
        request,
        "economic_development/cooperative_request_form.html",
        {
            "form": form
        }
    )


def cooperative_request_success(request, request_id):

    cooperative_request = get_object_or_404(
        CooperativeRequest,
        id=request_id
    )

    return render(
        request,
        "economic_development/cooperative_request_success.html",
        {
            "cooperative_request": cooperative_request
        }
    )
    
def economic_projects(request):

    search = request.GET.get("search", "").strip()
    project_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()
    status = request.GET.get("status", "").strip()

    projects = EconomicProject.objects.filter(
        is_published=True
    )

    if search:
        projects = projects.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
            | Q(implementing_organization__icontains=search)
        )

    if project_type:
        projects = projects.filter(
            project_type=project_type
        )

    if district:
        projects = projects.filter(
            district__icontains=district
        )

    if status:
        projects = projects.filter(
            status=status
        )

    context = {
        "projects": projects,

        "project_types": EconomicProject.PROJECT_TYPES,

        "statuses": EconomicProject.STATUS_CHOICES,

        "search": search,

        "selected_type": project_type,

        "selected_district": district,

        "selected_status": status,
    }

    return render(
        request,
        "economic_development/economic_projects.html",
        context
    )


def economic_project_detail(request, project_id):

    project = get_object_or_404(
        EconomicProject,
        id=project_id,
        is_published=True
    )

    return render(
        request,
        "economic_development/economic_project_detail.html",
        {
            "project": project
        }
    )
def funding_budget(request):

    search = request.GET.get("search", "").strip()
    information_type = request.GET.get("type", "").strip()
    district = request.GET.get("district", "").strip()

    funding_information = FundingBudgetInformation.objects.filter(
        is_published=True
    )

    if search:
        funding_information = funding_information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(organization__icontains=search)
            | Q(district__icontains=search)
            | Q(eligibility__icontains=search)
            | Q(requirements__icontains=search)
        )

    if information_type:
        funding_information = funding_information.filter(
            information_type=information_type
        )

    if district:
        funding_information = funding_information.filter(
            district__icontains=district
        )

    context = {
        "funding_information": funding_information,
        "information_types": FundingBudgetInformation.INFORMATION_TYPES,
        "search": search,
        "selected_type": information_type,
        "selected_district": district,
    }

    return render(
        request,
        "economic_development/funding_budget.html",
        context
    )


def funding_budget_detail(request, information_id):

    information = get_object_or_404(
        FundingBudgetInformation,
        id=information_id,
        is_published=True
    )

    return render(
        request,
        "economic_development/funding_budget_detail.html",
        {
            "information": information
        }
    )


def funding_budget_request_create(request):

    if request.method == "POST":

        form = FundingBudgetRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            funding_request = form.save()

            messages.success(
                request,
                "Your funding and budgeting request has been submitted successfully."
            )

            return redirect(
                "economic_development:funding_budget_request_success",
                request_id=funding_request.id
            )

    else:
        form = FundingBudgetRequestForm()

    return render(
        request,
        "economic_development/funding_budget_request_form.html",
        {
            "form": form
        }
    )


def funding_budget_request_success(request, request_id):

    funding_request = get_object_or_404(
        FundingBudgetRequest,
        id=request_id
    )

    return render(
        request,
        "economic_development/funding_budget_request_success.html",
        {
            "funding_request": funding_request
        }
    )
def economic_reports(request):
    """
    Citizen-facing Economic Development Reports.

    All statistics are calculated from the existing
    Economic Development database records.
    """

    # =========================================================
    # 1. BASIC COUNTS
    # =========================================================

    business_registration_count = (
        BusinessRegistrationRequest.objects.count()
    )

    trade_market_request_count = (
        TradeMarketRequest.objects.count()
    )

    cooperative_request_count = (
        CooperativeRequest.objects.count()
    )

    economic_project_count = (
        EconomicProject.objects
        .filter(is_published=True)
        .count()
    )

    funding_request_count = (
        FundingBudgetRequest.objects.count()
    )

    # =========================================================
    # 2. TOTAL FUNDING REQUESTED
    # =========================================================

    total_requested_funding = (
        FundingBudgetRequest.objects
        .exclude(requested_amount__isnull=True)
        .aggregate(
            total=Sum("requested_amount")
        )["total"]
        or 0
    )

    # =========================================================
    # 3. ECONOMIC PROJECT STATUS
    # =========================================================

    project_status_counts = list(
        EconomicProject.objects
        .filter(is_published=True)
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    # =========================================================
    # 4. ECONOMIC PROJECT TYPE
    # =========================================================

    project_type_counts = list(
        EconomicProject.objects
        .filter(is_published=True)
        .values("project_type")
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    # =========================================================
    # 5. BUSINESS REGISTRATION STATUS
    # =========================================================

    business_status_counts = list(
        BusinessRegistrationRequest.objects
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    # =========================================================
    # 6. TRADE & MARKET STATUS
    # =========================================================

    trade_status_counts = list(
        TradeMarketRequest.objects
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    # =========================================================
    # 7. COOPERATIVE STATUS
    # =========================================================

    cooperative_status_counts = list(
        CooperativeRequest.objects
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    # =========================================================
    # 8. FUNDING REQUEST STATUS
    # =========================================================

    funding_status_counts = list(
        FundingBudgetRequest.objects
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    # =========================================================
    # 9. FINANCIAL RECORDS
    # =========================================================

    financial_records = EconomicFinancialRecord.objects.all()

    # ---------------------------------------------------------
    # Total Allocated
    # ---------------------------------------------------------

    total_allocated = (
        financial_records.aggregate(
            total=Sum("allocated_amount")
        )["total"]
        or 0
    )

    # ---------------------------------------------------------
    # Total Approved
    # ---------------------------------------------------------

    total_approved = (
        financial_records.aggregate(
            total=Sum("approved_amount")
        )["total"]
        or 0
    )

    # ---------------------------------------------------------
    # Total Disbursed
    # ---------------------------------------------------------

    total_disbursed = (
        financial_records.aggregate(
            total=Sum("disbursed_amount")
        )["total"]
        or 0
    )

    # ---------------------------------------------------------
    # Total Spent
    # ---------------------------------------------------------

    total_spent = (
        financial_records.aggregate(
            total=Sum("spent_amount")
        )["total"]
        or 0
    )

    # ---------------------------------------------------------
    # Remaining Funds
    # ---------------------------------------------------------

    total_remaining = (
        total_allocated - total_spent
    )

    # =========================================================
    # 10. FINANCIAL STATUS
    # =========================================================

    financial_status_counts = list(
        EconomicFinancialRecord.objects
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    # =========================================================
    # 11. FINANCIAL TYPE
    # =========================================================

    financial_type_counts = list(
        EconomicFinancialRecord.objects
        .values("financial_type")
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    # =========================================================
    # 12. FINANCIAL DISTRICT TOTALS
    # =========================================================

    financial_district_totals = list(
        EconomicFinancialRecord.objects
        .values("district")
        .annotate(
            allocated=Sum("allocated_amount"),
            approved=Sum("approved_amount"),
            disbursed=Sum("disbursed_amount"),
            spent=Sum("spent_amount"),
        )
        .order_by("district")
    )

    # =========================================================
    # 13. PROJECT CHART DATA
    # =========================================================

    project_type_labels = [
        item["project_type"]
        .replace("_", " ")
        .title()
        for item in project_type_counts
    ]

    project_type_values = [
        item["total"]
        for item in project_type_counts
    ]

    project_status_labels = [
        item["status"]
        .replace("_", " ")
        .title()
        for item in project_status_counts
    ]

    project_status_values = [
        item["total"]
        for item in project_status_counts
    ]

    # =========================================================
    # 14. BUSINESS CHART DATA
    # =========================================================

    business_status_labels = [
        item["status"]
        .replace("_", " ")
        .title()
        for item in business_status_counts
    ]

    business_status_values = [
        item["total"]
        for item in business_status_counts
    ]

    # =========================================================
    # 15. TRADE CHART DATA
    # =========================================================

    trade_status_labels = [
        item["status"]
        .replace("_", " ")
        .title()
        for item in trade_status_counts
    ]

    trade_status_values = [
        item["total"]
        for item in trade_status_counts
    ]

    # =========================================================
    # 16. COOPERATIVE CHART DATA
    # =========================================================

    cooperative_status_labels = [
        item["status"]
        .replace("_", " ")
        .title()
        for item in cooperative_status_counts
    ]

    cooperative_status_values = [
        item["total"]
        for item in cooperative_status_counts
    ]

    # =========================================================
    # 17. FUNDING CHART DATA
    # =========================================================

    funding_status_labels = [
        item["status"]
        .replace("_", " ")
        .title()
        for item in funding_status_counts
    ]

    funding_status_values = [
        item["total"]
        for item in funding_status_counts
    ]

    # =========================================================
    # 18. FINANCIAL CHART DATA
    # =========================================================

    financial_status_labels = [
        item["status"]
        .replace("_", " ")
        .title()
        for item in financial_status_counts
    ]

    financial_status_values = [
        item["total"]
        for item in financial_status_counts
    ]

    financial_type_labels = [
        item["financial_type"]
        .replace("_", " ")
        .title()
        for item in financial_type_counts
    ]

    financial_type_values = [
        item["total"]
        for item in financial_type_counts
    ]

    # =========================================================
    # 19. FINANCIAL DISTRICT CHART DATA
    # =========================================================

    financial_district_labels = [
        item["district"]
        for item in financial_district_totals
    ]

    financial_allocated_values = [
        float(item["allocated"] or 0)
        for item in financial_district_totals
    ]

    financial_approved_values = [
        float(item["approved"] or 0)
        for item in financial_district_totals
    ]

    financial_disbursed_values = [
        float(item["disbursed"] or 0)
        for item in financial_district_totals
    ]

    financial_spent_values = [
        float(item["spent"] or 0)
        for item in financial_district_totals
    ]

    # =========================================================
    # 20. CONTEXT
    # =========================================================

    context = {

        # -----------------------------------------------------
        # Basic counts
        # -----------------------------------------------------

        "business_registration_count":
            business_registration_count,

        "trade_market_request_count":
            trade_market_request_count,

        "cooperative_request_count":
            cooperative_request_count,

        "economic_project_count":
            economic_project_count,

        "funding_request_count":
            funding_request_count,

        # -----------------------------------------------------
        # Funding
        # -----------------------------------------------------

        "total_requested_funding":
            total_requested_funding,

        # -----------------------------------------------------
        # Project reports
        # -----------------------------------------------------

        "project_status_counts":
            project_status_counts,

        "project_type_counts":
            project_type_counts,

        # -----------------------------------------------------
        # Business reports
        # -----------------------------------------------------

        "business_status_counts":
            business_status_counts,

        # -----------------------------------------------------
        # Trade reports
        # -----------------------------------------------------

        "trade_status_counts":
            trade_status_counts,

        # -----------------------------------------------------
        # Cooperative reports
        # -----------------------------------------------------

        "cooperative_status_counts":
            cooperative_status_counts,

        # -----------------------------------------------------
        # Funding reports
        # -----------------------------------------------------

        "funding_status_counts":
            funding_status_counts,

        # -----------------------------------------------------
        # Financial reporting
        # -----------------------------------------------------

        "financial_records":
            financial_records,

        "total_allocated":
            total_allocated,

        "total_approved":
            total_approved,

        "total_disbursed":
            total_disbursed,

        "total_spent":
            total_spent,

        "total_remaining":
            total_remaining,

        "financial_status_counts":
            financial_status_counts,

        "financial_type_counts":
            financial_type_counts,

        "financial_district_totals":
            financial_district_totals,

        # -----------------------------------------------------
        # Project chart data
        # -----------------------------------------------------

        "project_type_labels":
            json.dumps(project_type_labels),

        "project_type_values":
            json.dumps(project_type_values),

        "project_status_labels":
            json.dumps(project_status_labels),

        "project_status_values":
            json.dumps(project_status_values),

        # -----------------------------------------------------
        # Business chart data
        # -----------------------------------------------------

        "business_status_labels":
            json.dumps(business_status_labels),

        "business_status_values":
            json.dumps(business_status_values),

        # -----------------------------------------------------
        # Trade chart data
        # -----------------------------------------------------

        "trade_status_labels":
            json.dumps(trade_status_labels),

        "trade_status_values":
            json.dumps(trade_status_values),

        # -----------------------------------------------------
        # Cooperative chart data
        # -----------------------------------------------------

        "cooperative_status_labels":
            json.dumps(cooperative_status_labels),

        "cooperative_status_values":
            json.dumps(cooperative_status_values),

        # -----------------------------------------------------
        # Funding chart data
        # -----------------------------------------------------

        "funding_status_labels":
            json.dumps(funding_status_labels),

        "funding_status_values":
            json.dumps(funding_status_values),

        # -----------------------------------------------------
        # Financial chart data
        # -----------------------------------------------------

        "financial_status_labels":
            json.dumps(financial_status_labels),

        "financial_status_values":
            json.dumps(financial_status_values),

        "financial_type_labels":
            json.dumps(financial_type_labels),

        "financial_type_values":
            json.dumps(financial_type_values),

        # -----------------------------------------------------
        # District financial chart data
        # -----------------------------------------------------

        "financial_district_labels":
            json.dumps(financial_district_labels),

        "financial_allocated_values":
            json.dumps(financial_allocated_values),

        "financial_approved_values":
            json.dumps(financial_approved_values),

        "financial_disbursed_values":
            json.dumps(financial_disbursed_values),

        "financial_spent_values":
            json.dumps(financial_spent_values),
    }

    # =========================================================
    # 21. RENDER REPORT PAGE
    # =========================================================

    return render(
        request,
        "economic_development/economic_reports.html",
        context
    )
def economic_reports_excel(request):
    """
    Generate an Excel Economic Development Report.

    The report is generated from the existing
    Economic Development database records.
    """

    # =========================================================
    # CREATE WORKBOOK
    # =========================================================

    workbook = Workbook()

    # Remove default worksheet
    summary_sheet = workbook.active
    summary_sheet.title = "Executive Summary"

    # =========================================================
    # COMMON STYLES
    # =========================================================

    title_font = Font(
        bold=True,
        size=16
    )

    header_font = Font(
        bold=True
    )

    section_font = Font(
        bold=True,
        size=13
    )

    center_alignment = Alignment(
        horizontal="center",
        vertical="center"
    )

    # =========================================================
    # 1. EXECUTIVE SUMMARY
    # =========================================================

    summary_sheet["A1"] = "SMART CITY UGANDA"
    summary_sheet["A1"].font = title_font

    summary_sheet["A2"] = (
        "Economic Development — Financial & Activity Report"
    )

    summary_sheet["A4"] = "Report Indicator"
    summary_sheet["B4"] = "Value"

    summary_sheet["A4"].font = header_font
    summary_sheet["B4"].font = header_font

    # ---------------------------------------------------------
    # Basic counts
    # ---------------------------------------------------------

    business_registration_count = (
        BusinessRegistrationRequest.objects.count()
    )

    trade_market_request_count = (
        TradeMarketRequest.objects.count()
    )

    cooperative_request_count = (
        CooperativeRequest.objects.count()
    )

    economic_project_count = (
        EconomicProject.objects
        .filter(is_published=True)
        .count()
    )

    funding_request_count = (
        FundingBudgetRequest.objects.count()
    )

    # ---------------------------------------------------------
    # Funding requested
    # ---------------------------------------------------------

    total_requested_funding = (
        FundingBudgetRequest.objects
        .exclude(requested_amount__isnull=True)
        .aggregate(
            total=Sum("requested_amount")
        )["total"]
        or 0
    )

    # ---------------------------------------------------------
    # Financial records
    # ---------------------------------------------------------

    financial_records = EconomicFinancialRecord.objects.all()

    total_allocated = (
        financial_records.aggregate(
            total=Sum("allocated_amount")
        )["total"]
        or 0
    )

    total_approved = (
        financial_records.aggregate(
            total=Sum("approved_amount")
        )["total"]
        or 0
    )

    total_disbursed = (
        financial_records.aggregate(
            total=Sum("disbursed_amount")
        )["total"]
        or 0
    )

    total_spent = (
        financial_records.aggregate(
            total=Sum("spent_amount")
        )["total"]
        or 0
    )

    total_remaining = (
        total_allocated - total_spent
    )

    # =========================================================
    # SUMMARY DATA
    # =========================================================

    summary_data = [
        (
            "Business Registration Requests",
            business_registration_count
        ),
        (
            "Trade & Market Requests",
            trade_market_request_count
        ),
        (
            "Cooperative Requests",
            cooperative_request_count
        ),
        (
            "Economic Projects",
            economic_project_count
        ),
        (
            "Funding Requests",
            funding_request_count
        ),
        (
            "Total Funding Requested",
            float(total_requested_funding)
        ),
        (
            "Total Allocated",
            float(total_allocated)
        ),
        (
            "Total Approved",
            float(total_approved)
        ),
        (
            "Total Disbursed",
            float(total_disbursed)
        ),
        (
            "Total Spent",
            float(total_spent)
        ),
        (
            "Remaining Allocated Funds",
            float(total_remaining)
        ),
    ]

    row = 5

    for label, value in summary_data:
        summary_sheet.cell(
            row=row,
            column=1,
            value=label
        )

        summary_sheet.cell(
            row=row,
            column=2,
            value=value
        )

        row += 1

    # =========================================================
    # 2. ECONOMIC PROJECTS
    # =========================================================

    projects_sheet = workbook.create_sheet(
        "Economic Projects"
    )

    projects_sheet["A1"] = "ECONOMIC PROJECTS"
    projects_sheet["A1"].font = section_font

    project_headers = [
        "Title",
        "Project Type",
        "District",
        "Location",
        "Status",
        "Start Date",
        "Expected Completion",
        "Implementing Organization",
    ]

    for column, header in enumerate(
        project_headers,
        start=1
    ):
        cell = projects_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    projects = (
        EconomicProject.objects
        .filter(is_published=True)
        .order_by("district", "title")
    )

    row = 4

    for project in projects:

        projects_sheet.cell(
            row=row,
            column=1,
            value=project.title
        )

        projects_sheet.cell(
            row=row,
            column=2,
            value=project.get_project_type_display()
        )

        projects_sheet.cell(
            row=row,
            column=3,
            value=project.district
        )

        projects_sheet.cell(
            row=row,
            column=4,
            value=project.location
        )

        projects_sheet.cell(
            row=row,
            column=5,
            value=project.get_status_display()
        )

        projects_sheet.cell(
            row=row,
            column=6,
            value=project.start_date
        )

        projects_sheet.cell(
            row=row,
            column=7,
            value=project.expected_completion_date
        )

        projects_sheet.cell(
            row=row,
            column=8,
            value=project.implementing_organization
        )

        row += 1

    # =========================================================
    # 3. BUSINESS REGISTRATIONS
    # =========================================================

    business_sheet = workbook.create_sheet(
        "Business Registrations"
    )

    business_sheet["A1"] = "BUSINESS REGISTRATION REQUESTS"
    business_sheet["A1"].font = section_font

    business_headers = [
        "Reference",
        "Applicant",
        "Business Name",
        "Business Type",
        "District",
        "Status",
        "Created",
    ]

    for column, header in enumerate(
        business_headers,
        start=1
    ):
        cell = business_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    business_requests = (
        BusinessRegistrationRequest.objects
        .order_by("-created_at")
    )

    row = 4

    for item in business_requests:

        business_sheet.cell(
            row=row,
            column=1,
            value=item.reference_number
        )

        business_sheet.cell(
            row=row,
            column=2,
            value=item.applicant_name
        )

        business_sheet.cell(
            row=row,
            column=3,
            value=item.business_name
        )

        business_sheet.cell(
            row=row,
            column=4,
            value=item.get_business_type_display()
        )

        business_sheet.cell(
            row=row,
            column=5,
            value=item.district
        )

        business_sheet.cell(
            row=row,
            column=6,
            value=item.get_status_display()
        )

        business_sheet.cell(
            row=row,
            column=7,
            value=item.created_at
        )

        row += 1

    # =========================================================
    # 4. TRADE & MARKET REQUESTS
    # =========================================================

    trade_sheet = workbook.create_sheet(
        "Trade & Markets"
    )

    trade_sheet["A1"] = "TRADE & MARKET REQUESTS"
    trade_sheet["A1"].font = section_font

    trade_headers = [
        "Reference",
        "Citizen",
        "District",
        "Location",
        "Request Type",
        "Subject",
        "Status",
        "Created",
    ]

    for column, header in enumerate(
        trade_headers,
        start=1
    ):
        cell = trade_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    trade_requests = (
        TradeMarketRequest.objects
        .order_by("-created_at")
    )

    row = 4

    for item in trade_requests:

        trade_sheet.cell(
            row=row,
            column=1,
            value=item.reference_number
        )

        trade_sheet.cell(
            row=row,
            column=2,
            value=item.citizen_name
        )

        trade_sheet.cell(
            row=row,
            column=3,
            value=item.district
        )

        trade_sheet.cell(
            row=row,
            column=4,
            value=item.location
        )

        trade_sheet.cell(
            row=row,
            column=5,
            value=item.get_request_type_display()
        )

        trade_sheet.cell(
            row=row,
            column=6,
            value=item.subject
        )

        trade_sheet.cell(
            row=row,
            column=7,
            value=item.get_status_display()
        )

        trade_sheet.cell(
            row=row,
            column=8,
            value=item.created_at
        )

        row += 1

    # =========================================================
    # 5. COOPERATIVE REQUESTS
    # =========================================================

    cooperative_sheet = workbook.create_sheet(
        "Cooperatives"
    )

    cooperative_sheet["A1"] = "COOPERATIVE REQUESTS"
    cooperative_sheet["A1"].font = section_font

    cooperative_headers = [
        "Reference",
        "Citizen",
        "Cooperative Name",
        "District",
        "Location",
        "Request Type",
        "Subject",
        "Status",
        "Created",
    ]

    for column, header in enumerate(
        cooperative_headers,
        start=1
    ):
        cell = cooperative_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    cooperative_requests = (
        CooperativeRequest.objects
        .order_by("-created_at")
    )

    row = 4

    for item in cooperative_requests:

        cooperative_sheet.cell(
            row=row,
            column=1,
            value=item.reference_number
        )

        cooperative_sheet.cell(
            row=row,
            column=2,
            value=item.citizen_name
        )

        cooperative_sheet.cell(
            row=row,
            column=3,
            value=item.cooperative_name
        )

        cooperative_sheet.cell(
            row=row,
            column=4,
            value=item.district
        )

        cooperative_sheet.cell(
            row=row,
            column=5,
            value=item.location
        )

        cooperative_sheet.cell(
            row=row,
            column=6,
            value=item.get_request_type_display()
        )

        cooperative_sheet.cell(
            row=row,
            column=7,
            value=item.subject
        )

        cooperative_sheet.cell(
            row=row,
            column=8,
            value=item.get_status_display()
        )

        cooperative_sheet.cell(
            row=row,
            column=9,
            value=item.created_at
        )

        row += 1

    # =========================================================
    # 6. FUNDING REQUESTS
    # =========================================================

    funding_sheet = workbook.create_sheet(
        "Funding Requests"
    )

    funding_sheet["A1"] = "FUNDING & BUDGET REQUESTS"
    funding_sheet["A1"].font = section_font

    funding_headers = [
        "Reference",
        "Citizen",
        "District",
        "Request Type",
        "Subject",
        "Requested Amount",
        "Purpose",
        "Status",
        "Created",
    ]

    for column, header in enumerate(
        funding_headers,
        start=1
    ):
        cell = funding_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    funding_requests = (
        FundingBudgetRequest.objects
        .order_by("-created_at")
    )

    row = 4

    for item in funding_requests:

        funding_sheet.cell(
            row=row,
            column=1,
            value=item.reference_number
        )

        funding_sheet.cell(
            row=row,
            column=2,
            value=item.citizen_name
        )

        funding_sheet.cell(
            row=row,
            column=3,
            value=item.district
        )

        funding_sheet.cell(
            row=row,
            column=4,
            value=item.get_request_type_display()
        )

        funding_sheet.cell(
            row=row,
            column=5,
            value=item.subject
        )

        funding_sheet.cell(
            row=row,
            column=6,
            value=float(
                item.requested_amount or 0
            )
        )

        funding_sheet.cell(
            row=row,
            column=7,
            value=item.purpose_of_funding
        )

        funding_sheet.cell(
            row=row,
            column=8,
            value=item.get_status_display()
        )

        funding_sheet.cell(
            row=row,
            column=9,
            value=item.created_at
        )

        row += 1

    # =========================================================
    # 7. FINANCIAL RECORDS
    # =========================================================

    financial_sheet = workbook.create_sheet(
        "Financial Records"
    )

    financial_sheet["A1"] = "ECONOMIC FINANCIAL RECORDS"
    financial_sheet["A1"].font = section_font

    financial_headers = [
        "Title",
        "Financial Type",
        "District",
        "Organization",
        "Project",
        "Financial Year",
        "Allocated",
        "Approved",
        "Disbursed",
        "Spent",
        "Remaining",
        "Status",
    ]

    for column, header in enumerate(
        financial_headers,
        start=1
    ):
        cell = financial_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    financial_data = (
        EconomicFinancialRecord.objects
        .order_by(
            "financial_year",
            "district"
        )
    )

    row = 4

    for item in financial_data:

        financial_sheet.cell(
            row=row,
            column=1,
            value=item.title
        )

        financial_sheet.cell(
            row=row,
            column=2,
            value=item.get_financial_type_display()
        )

        financial_sheet.cell(
            row=row,
            column=3,
            value=item.district
        )

        financial_sheet.cell(
            row=row,
            column=4,
            value=item.organization
        )

        financial_sheet.cell(
            row=row,
            column=5,
            value=item.project_name
        )

        financial_sheet.cell(
            row=row,
            column=6,
            value=item.financial_year
        )

        financial_sheet.cell(
            row=row,
            column=7,
            value=float(
                item.allocated_amount or 0
            )
        )

        financial_sheet.cell(
            row=row,
            column=8,
            value=float(
                item.approved_amount or 0
            )
        )

        financial_sheet.cell(
            row=row,
            column=9,
            value=float(
                item.disbursed_amount or 0
            )
        )

        financial_sheet.cell(
            row=row,
            column=10,
            value=float(
                item.spent_amount or 0
            )
        )

        financial_sheet.cell(
            row=row,
            column=11,
            value=float(
                item.remaining_amount or 0
            )
        )

        financial_sheet.cell(
            row=row,
            column=12,
            value=item.get_status_display()
        )

        row += 1

    # =========================================================
    # 8. DISTRICT FINANCIAL BREAKDOWN
    # =========================================================

    district_sheet = workbook.create_sheet(
        "District Financials"
    )

    district_sheet["A1"] = (
        "DISTRICT FINANCIAL BREAKDOWN"
    )

    district_sheet["A1"].font = section_font

    district_headers = [
        "District",
        "Allocated",
        "Approved",
        "Disbursed",
        "Spent",
        "Remaining",
    ]

    for column, header in enumerate(
        district_headers,
        start=1
    ):
        cell = district_sheet.cell(
            row=3,
            column=column,
            value=header
        )
        cell.font = header_font

    district_totals = (
        EconomicFinancialRecord.objects
        .values("district")
        .annotate(
            allocated=Sum("allocated_amount"),
            approved=Sum("approved_amount"),
            disbursed=Sum("disbursed_amount"),
            spent=Sum("spent_amount"),
        )
        .order_by("district")
    )

    row = 4

    for item in district_totals:

        allocated = (
            item["allocated"] or 0
        )

        approved = (
            item["approved"] or 0
        )

        disbursed = (
            item["disbursed"] or 0
        )

        spent = (
            item["spent"] or 0
        )

        remaining = allocated - spent

        district_sheet.cell(
            row=row,
            column=1,
            value=item["district"]
        )

        district_sheet.cell(
            row=row,
            column=2,
            value=float(allocated)
        )

        district_sheet.cell(
            row=row,
            column=3,
            value=float(approved)
        )

        district_sheet.cell(
            row=row,
            column=4,
            value=float(disbursed)
        )

        district_sheet.cell(
            row=row,
            column=5,
            value=float(spent)
        )

        district_sheet.cell(
            row=row,
            column=6,
            value=float(remaining)
        )

        row += 1

    # =========================================================
    # 9. FORMAT ALL WORKSHEETS
    # =========================================================

    for sheet in workbook.worksheets:

        # Freeze header row
        sheet.freeze_panes = "A4"

        # Center headers
        for cell in sheet[3]:
            cell.alignment = center_alignment

        # Automatic column width
        for column_cells in sheet.columns:

            max_length = 0

            column_letter = get_column_letter(
                column_cells[0].column
            )

            for cell in column_cells:

                if cell.value is not None:

                    value_length = len(
                        str(cell.value)
                    )

                    if value_length > max_length:
                        max_length = value_length

            sheet.column_dimensions[
                column_letter
            ].width = min(
                max(max_length + 2, 12),
                40
            )

    # =========================================================
    # 10. NUMBER FORMATTING
    # =========================================================

    financial_columns = {
        "Executive Summary": ["B"],
        "Funding Requests": ["F"],
        "Financial Records": [
            "G",
            "H",
            "I",
            "J",
            "K",
        ],
        "District Financials": [
            "B",
            "C",
            "D",
            "E",
            "F",
        ],
    }

    for sheet_name, columns in financial_columns.items():

        sheet = workbook[sheet_name]

        for column in columns:

            for cell in sheet[column]:

                if isinstance(
                    cell.value,
                    (int, float)
                ):
                    cell.number_format = (
                        '#,##0.00'
                    )

    # =========================================================
    # 11. PREPARE DOWNLOAD RESPONSE
    # =========================================================

    response = HttpResponse(
        content_type=(
            "application/vnd.openxmlformats-"
            "officedocument.spreadsheetml.sheet"
        )
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; '
        'filename="SmartCity_Uganda_Economic_Report.xlsx"'
    )

    workbook.save(response)

    return response
def economic_financial_excel_import(request):
    """
    Import EconomicFinancialRecord data from an Excel file.

    This view is intended for authorized management use.
    Authentication and role restrictions will be integrated
    later with the Administrator Dashboard.
    """

    if request.method == "POST":

        form = EconomicFinancialExcelImportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            excel_file = form.cleaned_data["excel_file"]

            # -------------------------------------------------
            # Open uploaded workbook
            # -------------------------------------------------

            try:
                from openpyxl import load_workbook

                workbook = load_workbook(
                    excel_file,
                    read_only=True,
                    data_only=True
                )

            except Exception:
                messages.error(
                    request,
                    "The uploaded Excel file could not be opened."
                )

                return redirect(
                    "economic_development:economic_financial_excel_import"
                )

            # -------------------------------------------------
            # Check worksheet
            # -------------------------------------------------

            if "Financial Records" not in workbook.sheetnames:

                messages.error(
                    request,
                    "The Excel file does not contain the required "
                    "'Financial Records' worksheet."
                )

                workbook.close()

                return redirect(
                    "economic_development:economic_financial_excel_import"
                )

            sheet = workbook["Financial Records"]

            # -------------------------------------------------
            # Expected headers
            # -------------------------------------------------

            expected_headers = [
                "Title",
                "Financial Type",
                "District",
                "Organization",
                "Project",
                "Financial Year",
                "Allocated",
                "Approved",
                "Disbursed",
                "Spent",
                "Remaining",
                "Status",
            ]

            header_values = [
                cell.value
                for cell in sheet[3]
            ]

            # -------------------------------------------------
            # Validate headers
            # -------------------------------------------------

            if header_values[:len(expected_headers)] != expected_headers:

                messages.error(
                    request,
                    "The Financial Records worksheet has an "
                    "invalid column structure."
                )

                workbook.close()

                return redirect(
                    "economic_development:economic_financial_excel_import"
                )

            # -------------------------------------------------
            # Process records
            # -------------------------------------------------

            imported_count = 0
            skipped_count = 0
            errors = []

            for row_number, row in enumerate(
                sheet.iter_rows(
                    min_row=4,
                    values_only=True
                ),
                start=4
            ):

                # ---------------------------------------------
                # Skip completely empty rows
                # ---------------------------------------------

                if not any(
                    value is not None
                    for value in row
                ):
                    continue

                try:

                    title = str(
                        row[0] or ""
                    ).strip()

                    financial_type = str(
                        row[1] or ""
                    ).strip()

                    district = str(
                        row[2] or ""
                    ).strip()

                    organization = str(
                        row[3] or ""
                    ).strip()

                    project_name = str(
                        row[4] or ""
                    ).strip()

                    financial_year = str(
                        row[5] or ""
                    ).strip()

                    allocated = row[6] or 0
                    approved = row[7] or 0
                    disbursed = row[8] or 0
                    spent = row[9] or 0

                    status_display = str(
                        row[11] or ""
                    ).strip()

                    # -----------------------------------------
                    # Required fields
                    # -----------------------------------------

                    if not title:
                        raise ValueError(
                            "Title is required."
                        )

                    if not financial_type:
                        raise ValueError(
                            "Financial Type is required."
                        )

                    if not district:
                        raise ValueError(
                            "District is required."
                        )

                    if not financial_year:
                        raise ValueError(
                            "Financial Year is required."
                        )

                    # -----------------------------------------
                    # Convert financial type display value
                    # to database value
                    # -----------------------------------------

                    financial_type_map = dict(
                        EconomicFinancialRecord.FINANCIAL_TYPES
                    )

                    financial_type_reverse = {
                        label: value
                        for value, label
                        in financial_type_map.items()
                    }

                    financial_type_value = (
                        financial_type_reverse.get(
                            financial_type,
                            financial_type
                        )
                    )

                    # -----------------------------------------
                    # Convert status display value
                    # to database value
                    # -----------------------------------------

                    status_map = dict(
                        EconomicFinancialRecord.STATUS_CHOICES
                    )

                    status_reverse = {
                        label: value
                        for value, label
                        in status_map.items()
                    }

                    status_value = (
                        status_reverse.get(
                            status_display,
                            status_display
                        )
                    )

                    # -----------------------------------------
                    # Validate choices
                    # -----------------------------------------

                    valid_financial_types = dict(
                        EconomicFinancialRecord.FINANCIAL_TYPES
                    )

                    if financial_type_value not in valid_financial_types:

                        raise ValueError(
                            f"Invalid Financial Type: "
                            f"{financial_type}"
                        )

                    valid_statuses = dict(
                        EconomicFinancialRecord.STATUS_CHOICES
                    )

                    if status_value not in valid_statuses:

                        raise ValueError(
                            f"Invalid Status: "
                            f"{status_display}"
                        )

                    # -----------------------------------------
                    # Convert amounts
                    # -----------------------------------------

                    allocated = float(allocated)
                    approved = float(approved)
                    disbursed = float(disbursed)
                    spent = float(spent)

                    # -----------------------------------------
                    # Financial validation
                    # -----------------------------------------

                    if allocated < 0:
                        raise ValueError(
                            "Allocated amount cannot be negative."
                        )

                    if approved < 0:
                        raise ValueError(
                            "Approved amount cannot be negative."
                        )

                    if disbursed < 0:
                        raise ValueError(
                            "Disbursed amount cannot be negative."
                        )

                    if spent < 0:
                        raise ValueError(
                            "Spent amount cannot be negative."
                        )

                    if approved > allocated:
                        raise ValueError(
                            "Approved amount cannot exceed "
                            "allocated amount."
                        )

                    if disbursed > approved:
                        raise ValueError(
                            "Disbursed amount cannot exceed "
                            "approved amount."
                        )

                    if spent > disbursed:
                        raise ValueError(
                            "Spent amount cannot exceed "
                            "disbursed amount."
                        )

                    # -----------------------------------------
                    # Create financial record
                    # -----------------------------------------

                    EconomicFinancialRecord.objects.create(
                        title=title,
                        financial_type=financial_type_value,
                        district=district,
                        organization=organization,
                        project_name=project_name,
                        financial_year=financial_year,
                        allocated_amount=allocated,
                        approved_amount=approved,
                        disbursed_amount=disbursed,
                        spent_amount=spent,
                        status=status_value,
                    )

                    imported_count += 1

                except Exception as error:

                    skipped_count += 1

                    errors.append(
                        f"Row {row_number}: {error}"
                    )

            workbook.close()

            # -------------------------------------------------
            # Success message
            # -------------------------------------------------

            if imported_count:

                messages.success(
                    request,
                    f"{imported_count} financial record(s) "
                    f"were imported successfully."
                )

            # -------------------------------------------------
            # Error messages
            # -------------------------------------------------

            for error in errors[:10]:

                messages.error(
                    request,
                    error
                )

            if skipped_count > 10:

                messages.error(
                    request,
                    f"{skipped_count - 10} additional "
                    f"row error(s) were not displayed."
                )

            return redirect(
                "economic_development:economic_financial_excel_import"
            )

    else:

        form = EconomicFinancialExcelImportForm()

    return render(
        request,
        "economic_development/economic_financial_excel_import.html",
        {
            "form": form,
        }
    )