from django.urls import path

from . import views


app_name = "payments"


urlpatterns = [

    path(
        "",
        views.payment_home,
        name="home",
    ),

    path(
        "bills/",
        views.my_bills,
        name="my_bills",
    ),

    path(
        "bill/<int:bill_id>/",
        views.bill_detail,
        name="bill_detail",
    ),

    path(
        "bill/<int:bill_id>/pay/",
        views.start_payment,
        name="start_payment",
    ),

    path(
        "payment/<int:payment_id>/method/",
        views.select_payment_method,
        name="select_payment_method",
    ),

    path(
        "payment/<int:payment_id>/mobile-money/",
        views.mobile_money_payment,
        name="mobile_money_payment",
    ),

    path(
        "payment/<int:payment_id>/mobile-money/dial/",
        views.mobile_money_dial,
        name="mobile_money_dial",
    ),

    path(
        "payment/<int:payment_id>/card/",
        views.card_payment,
        name="card_payment",
    ),

    path(
        "payment/<int:payment_id>/bank/",
        views.bank_payment,
        name="bank_payment",
    ),

    path(
        "payment/<int:payment_id>/payway/",
        views.payway_payment,
        name="payway_payment",
    ),

    path(
        "payment/<int:payment_id>/cash/",
        views.cash_payment,
        name="cash_payment",
    ),

    path(
        "payment/<int:payment_id>/success/",
        views.payment_success,
        name="payment_success",
    ),

    path(
        "history/",
        views.payment_history,
        name="history",
    ),
]