from django.urls import path

from . import views


app_name = "economic_development"


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    # 15.1 Financial Planning
    path(
        "financial-planning/",
        views.financial_planning,
        name="financial_planning"
    ),

    path(
        "financial-planning/<int:information_id>/",
        views.financial_planning_detail,
        name="financial_planning_detail"
    ),

    # 15.2 Business Registration
    path(
        "business-registration/",
        views.business_registration,
        name="business_registration"
    ),

    path(
        "business-registration/<int:information_id>/",
        views.business_registration_detail,
        name="business_registration_detail"
    ),

    path(
        "business-registration/apply/",
        views.business_registration_apply,
        name="business_registration_apply"
    ),

    path(
        "business-registration/success/<int:request_id>/",
        views.business_registration_success,
        name="business_registration_success"
    ),
# 15.3 Trade & Markets

path(
    "trade-markets/",
    views.trade_markets,
    name="trade_markets"
),

path(
    "trade-markets/<int:information_id>/",
    views.trade_market_detail,
    name="trade_market_detail"
),

path(
    "trade-markets/request/",
    views.trade_market_request_create,
    name="trade_market_request_create"
),

path(
    "trade-markets/request/success/<int:request_id>/",
    views.trade_market_request_success,
    name="trade_market_request_success"
),
path(
    "cooperatives/",
    views.cooperatives,
    name="cooperatives"
),

path(
    "cooperatives/<int:information_id>/",
    views.cooperative_detail,
    name="cooperative_detail"
),

path(
    "cooperatives/request/",
    views.cooperative_request_create,
    name="cooperative_request_create"
),

path(
    "cooperatives/request/success/<int:request_id>/",
    views.cooperative_request_success,
    name="cooperative_request_success"
),
path(
    "projects/",
    views.economic_projects,
    name="economic_projects"
),

path(
    "projects/<int:project_id>/",
    views.economic_project_detail,
    name="economic_project_detail"
),
path(
    "funding-budget/",
    views.funding_budget,
    name="funding_budget"
),

path(
    "funding-budget/<int:information_id>/",
    views.funding_budget_detail,
    name="funding_budget_detail"
),

path(
    "funding-budget/request/",
    views.funding_budget_request_create,
    name="funding_budget_request_create"
),

path(
    "funding-budget/request/success/<int:request_id>/",
    views.funding_budget_request_success,
    name="funding_budget_request_success"
),
path(
    "reports/",
    views.economic_reports,
    name="economic_reports"
),

path(
    "reports/excel/",
    views.economic_reports_excel,
    name="economic_reports_excel"
),

path(
    "reports/excel/import/",
    views.economic_financial_excel_import,
    name="economic_financial_excel_import",
),
]