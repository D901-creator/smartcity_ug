from django.contrib import admin

from .models import (
    RevenueService,
    Bill,
    Payment,
)


@admin.register(RevenueService)
class RevenueServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "service_type",
        "organisation",
        "active",
        "created_at",
    )

    list_filter = (
        "service_type",
        "active",
    )

    search_fields = (
        "name",
        "organisation",
    )


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    list_display = (
        "bill_number",
        "citizen",
        "revenue_service",
        "amount_due",
        "amount_paid",
        "status",
        "due_date",
        "created_at",
    )

    list_filter = (
        "status",
        "revenue_service",
    )

    search_fields = (
        "bill_number",
        "reference_number",
        "citizen__username",
    )

    readonly_fields = (
        "bill_number",
        "created_at",
        "updated_at",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "payment_number",
        "citizen",
        "bill",
        "amount",
        "payment_method",
        "provider",
        "status",
        "transaction_reference",
        "paid_at",
        "created_at",
    )

    list_filter = (
        "payment_method",
        "status",
        "provider",
    )

    search_fields = (
        "payment_number",
        "transaction_reference",
        "payment_reference",
        "citizen__username",
        "bill__bill_number",
    )

    readonly_fields = (
        "payment_number",
        "created_at",
        "updated_at",
    )