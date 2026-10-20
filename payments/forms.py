from django import forms

from .models import (
    Bill,
    Payment,
)


class PaymentAmountForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = [
            "amount",
        ]

        widgets = {
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "step": "1",
                    "placeholder": "Enter amount",
                }
            ),
        }

    def __init__(self, *args, bill=None, **kwargs):

        super().__init__(*args, **kwargs)

        self.bill = bill

    def clean_amount(self):

        amount = self.cleaned_data["amount"]

        if amount <= 0:
            raise forms.ValidationError(
                "Enter an amount greater than zero."
            )

        if self.bill and amount > self.bill.balance:
            raise forms.ValidationError(
                "Amount cannot be greater than the outstanding bill balance."
            )

        return amount


class MobileMoneyPaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = [
            "provider",
            "phone_number",
        ]

        widgets = {

            "provider": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 077XXXXXXX",
                }
            ),
        }

    PROVIDERS = [
        ("MTN Mobile Money", "MTN Mobile Money"),
        ("Airtel Money", "Airtel Money"),
    ]

    provider = forms.ChoiceField(
        choices=PROVIDERS,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    def clean_phone_number(self):

        phone = self.cleaned_data["phone_number"].strip()

        if len(phone) < 9:
            raise forms.ValidationError(
                "Enter a valid Uganda mobile number."
            )

        return phone


class CardPaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = []

    card_name = forms.CharField(
        label="Cardholder Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    card_number = forms.CharField(
        label="Card Number",
        max_length=19,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Card number",
            }
        ),
    )

    expiry = forms.CharField(
        label="Expiry Date",
        max_length=5,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "MM/YY",
            }
        ),
    )

    cvv = forms.CharField(
        label="CVV",
        max_length=4,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class BankPaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = []

    bank_name = forms.CharField(
        label="Bank",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class PaywayPaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = []

    phone_number = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }
        ),
    )


class CashPaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = []

    payment_centre = forms.CharField(
        label="Government Payment Centre",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Payment centre",
            }
        ),
    )