from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class RevenueService(models.Model):
    """
    Government revenue or tax service that a citizen can be charged for.
    """

    SERVICE_TYPES = [
        ("tax", "Tax"),
        ("fee", "Government Fee"),
        ("licence", "Licence"),
        ("permit", "Permit"),
        ("property", "Property / Land Fee"),
        ("business", "Business Fee"),
        ("utility", "Utility Bill"),
        ("other", "Other Revenue"),
    ]

    name = models.CharField(max_length=200)

    service_type = models.CharField(
        max_length=30,
        choices=SERVICE_TYPES,
        default="fee",
    )

    organisation = models.CharField(
        max_length=200,
        default="Government of Uganda",
    )

    description = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    """
    A bill issued to a citizen.
    """

    BILL_STATUS = [
        ("unpaid", "Unpaid"),
        ("partial", "Partially Paid"),
        ("paid", "Paid"),
        ("cancelled", "Cancelled"),
        ("overdue", "Overdue"),
    ]

    bill_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
    )

    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="smartcity_bills",
    )

    revenue_service = models.ForeignKey(
        RevenueService,
        on_delete=models.PROTECT,
        related_name="bills",
    )

    organisation = models.CharField(
        max_length=200,
        default="Government of Uganda",
    )

    description = models.TextField(blank=True)

    amount_due = models.DecimalField(
        max_digits=14,
        decimal_places=2,
    )

    amount_paid = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )

    due_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=BILL_STATUS,
        default="unpaid",
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.bill_number:
            self.bill_number = (
                f"SCB-{uuid.uuid4().hex[:10].upper()}"
            )

        if self.amount_paid >= self.amount_due:
            self.status = "paid"

        elif self.amount_paid > 0:
            self.status = "partial"

        elif self.due_date and self.due_date < timezone.now().date():
            self.status = "overdue"

        else:
            self.status = "unpaid"

        super().save(*args, **kwargs)

    @property
    def balance(self):
        return max(
            self.amount_due - self.amount_paid,
            0,
        )

    def __str__(self):
        return self.bill_number


class Payment(models.Model):
    """
    Payment transaction recorded by Smart City Uganda.
    """

    PAYMENT_METHODS = [
        ("mobile_money", "Mobile Money"),
        ("card", "Debit / Credit Card"),
        ("bank", "Bank Payment"),
        ("payway", "Payway"),
        ("cash", "Cash / Government Payment Centre"),
    ]

    PAYMENT_STATUS = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("approved", "Approved"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    ]

    payment_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
    )

    citizen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="smartcity_payments",
    )

    bill = models.ForeignKey(
        Bill,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHODS,
    )

    provider = models.CharField(
        max_length=100,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True,
    )

    transaction_reference = models.CharField(
        max_length=150,
        blank=True,
    )

    payment_reference = models.CharField(
        max_length=150,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="pending",
    )

    failure_reason = models.TextField(
        blank=True,
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs):

        if not self.payment_number:
            self.payment_number = (
                f"SCP-{uuid.uuid4().hex[:10].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.payment_number