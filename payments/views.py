from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone

from .forms import (
    PaymentAmountForm,
    MobileMoneyPaymentForm,
    CardPaymentForm,
    BankPaymentForm,
    PaywayPaymentForm,
    CashPaymentForm,
)

from .models import (
    Bill,
    Payment,
)


@login_required
def payment_home(request):

    bills = Bill.objects.filter(
        citizen=request.user
    ).order_by(
        "-created_at"
    )

    unpaid_bills = bills.filter(
        status__in=[
            "unpaid",
            "partial",
            "overdue",
        ]
    )

    recent_payments = Payment.objects.filter(
        citizen=request.user
    ).order_by(
        "-created_at"
    )[:5]

    context = {
        "bills": bills,
        "unpaid_bills": unpaid_bills,
        "recent_payments": recent_payments,
    }

    return render(
        request,
        "payments/home.html",
        context,
    )


@login_required
def my_bills(request):

    bills = Bill.objects.filter(
        citizen=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "payments/bills.html",
        {
            "bills": bills,
        },
    )


@login_required
def bill_detail(request, bill_id):

    bill = get_object_or_404(
        Bill,
        id=bill_id,
        citizen=request.user,
    )

    return render(
        request,
        "payments/bill_detail.html",
        {
            "bill": bill,
        },
    )


@login_required
def start_payment(request, bill_id):

    bill = get_object_or_404(
        Bill,
        id=bill_id,
        citizen=request.user,
    )

    if bill.balance <= 0:
        messages.info(
            request,
            "This bill has already been fully paid.",
        )

        return redirect(
            "payments:bill_detail",
            bill_id=bill.id,
        )

    if request.method == "POST":

        form = PaymentAmountForm(
            request.POST,
            bill=bill,
        )

        if form.is_valid():

            payment = form.save(
                commit=False
            )

            payment.citizen = request.user
            payment.bill = bill
            payment.status = "pending"

            payment.save()

            return redirect(
                "payments:select_payment_method",
                payment_id=payment.id,
            )

    else:

        form = PaymentAmountForm(
            initial={
                "amount": bill.balance,
            },
            bill=bill,
        )

    return render(
        request,
        "payments/payment_amount.html",
        {
            "bill": bill,
            "form": form,
        },
    )


@login_required
def select_payment_method(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        method = request.POST.get(
            "payment_method"
        )

        allowed_methods = {
            choice[0]
            for choice in Payment.PAYMENT_METHODS
        }

        if method not in allowed_methods:

            messages.error(
                request,
                "Please select a valid payment method.",
            )

            return redirect(
                "payments:select_payment_method",
                payment_id=payment.id,
            )

        payment.payment_method = method
        payment.status = "processing"
        payment.save(
            update_fields=[
                "payment_method",
                "status",
            ]
        )

        if method == "mobile_money":
            return redirect(
                "payments:mobile_money_payment",
                payment_id=payment.id,
            )

        if method == "card":
            return redirect(
                "payments:card_payment",
                payment_id=payment.id,
            )

        if method == "bank":
            return redirect(
                "payments:bank_payment",
                payment_id=payment.id,
            )

        if method == "payway":
            return redirect(
                "payments:payway_payment",
                payment_id=payment.id,
            )

        return redirect(
            "payments:cash_payment",
            payment_id=payment.id,
        )

    return render(
        request,
        "payments/payment_method.html",
        {
            "payment": payment,
        },
    )


@login_required
def mobile_money_payment(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        form = MobileMoneyPaymentForm(
            request.POST,
            instance=payment,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "payments:mobile_money_dial",
                payment_id=payment.id,
            )

    else:

        form = MobileMoneyPaymentForm(
            instance=payment,
        )

    return render(
        request,
        "payments/mobile_money.html",
        {
            "payment": payment,
            "form": form,
        },
    )


@login_required
def mobile_money_dial(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        payment.transaction_reference = (
            f"MM-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        )

        payment.status = "approved"
        payment.paid_at = timezone.now()

        with transaction.atomic():

            payment.save()

            bill = payment.bill

            bill.amount_paid += payment.amount

            bill.save()

        return redirect(
            "payments:payment_success",
            payment_id=payment.id,
        )

    return render(
        request,
        "payments/mobile_money_dial.html",
        {
            "payment": payment,
        },
    )


@login_required
def card_payment(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        form = CardPaymentForm(
            request.POST
        )

        if form.is_valid():

            payment.transaction_reference = (
                f"CARD-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )

            payment.status = "approved"
            payment.paid_at = timezone.now()

            with transaction.atomic():

                payment.save()

                bill = payment.bill
                bill.amount_paid += payment.amount
                bill.save()

            return redirect(
                "payments:payment_success",
                payment_id=payment.id,
            )

    else:

        form = CardPaymentForm()

    return render(
        request,
        "payments/card_payment.html",
        {
            "payment": payment,
            "form": form,
        },
    )


@login_required
def bank_payment(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        form = BankPaymentForm(
            request.POST
        )

        if form.is_valid():

            payment.transaction_reference = (
                f"BANK-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )

            payment.status = "approved"
            payment.paid_at = timezone.now()

            with transaction.atomic():

                payment.save()

                bill = payment.bill
                bill.amount_paid += payment.amount
                bill.save()

            return redirect(
                "payments:payment_success",
                payment_id=payment.id,
            )

    else:

        form = BankPaymentForm()

    return render(
        request,
        "payments/bank_payment.html",
        {
            "payment": payment,
            "form": form,
        },
    )


@login_required
def payway_payment(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        form = PaywayPaymentForm(
            request.POST
        )

        if form.is_valid():

            payment.transaction_reference = (
                f"PAYWAY-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )

            payment.status = "approved"
            payment.paid_at = timezone.now()

            with transaction.atomic():

                payment.save()

                bill = payment.bill
                bill.amount_paid += payment.amount
                bill.save()

            return redirect(
                "payments:payment_success",
                payment_id=payment.id,
            )

    else:

        form = PaywayPaymentForm()

    return render(
        request,
        "payments/payway_payment.html",
        {
            "payment": payment,
            "form": form,
        },
    )


@login_required
def cash_payment(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    if request.method == "POST":

        form = CashPaymentForm(
            request.POST
        )

        if form.is_valid():

            payment.transaction_reference = (
                f"CASH-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )

            payment.status = "pending"

            payment.save()

            messages.success(
                request,
                "Cash payment request recorded. Complete payment at the selected government payment centre.",
            )

            return redirect(
                "payments:payment_history"
            )

    else:

        form = CashPaymentForm()

    return render(
        request,
        "payments/cash_payment.html",
        {
            "payment": payment,
            "form": form,
        },
    )


@login_required
def payment_success(
    request,
    payment_id,
):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        citizen=request.user,
    )

    return render(
        request,
        "payments/payment_success.html",
        {
            "payment": payment,
        },
    )


@login_required
def payment_history(request):

    payments = Payment.objects.filter(
        citizen=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "payments/history.html",
        {
            "payments": payments,
        },
    )