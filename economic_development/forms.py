from django import forms

from .models import (FinancialPlanningInformation,BusinessRegistrationInformation,TradeMarketInformation,
    TradeMarketRequest, CooperativeInformation,FundingBudgetInformation,
    CooperativeRequest,EconomicProject,FundingBudgetRequest,
    BusinessRegistrationRequest,)

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
class FinancialPlanningInformationForm(forms.ModelForm):

    class Meta:
        model = FinancialPlanningInformation

        fields = [
            "title",
            "information_type",
            "district",
            "summary",
            "description",
            "requirements",
            "planning_process",
            "important_information",
            "contact_information",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter financial planning information title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Short summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Detailed information",
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Requirements, where applicable",
                }
            ),

            "planning_process": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Explain the planning process",
                }
            ),

            "important_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Important information for citizens",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Contact information",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
        
class BusinessRegistrationInformationForm(forms.ModelForm):

    class Meta:
        model = BusinessRegistrationInformation

        fields = [
            "title",
            "information_type",
            "district",
            "summary",
            "description",
            "requirements",
            "registration_process",
            "fees_information",
            "contact_information",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Business registration information title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Short summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Detailed information",
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Business registration requirements",
                }
            ),

            "registration_process": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Registration procedure",
                }
            ),

            "fees_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Fees information",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Contact information",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class BusinessRegistrationRequestForm(forms.ModelForm):

    class Meta:
        model = BusinessRegistrationRequest

        fields = [
            "applicant_name",
            "phone_number",
            "email",
            "district",
            "business_name",
            "business_type",
            "business_location",
            "business_description",
            "proposed_activities",
            "supporting_information",
            "supporting_document",
        ]

        widgets = {
            "applicant_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "business_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Proposed business name",
                }
            ),

            "business_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "business_location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Business location",
                }
            ),

            "business_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe the business",
                }
            ),

            "proposed_activities": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe the proposed business activities",
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Additional information",
                }
            ),

            "supporting_document": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        
class TradeMarketInformationForm(forms.ModelForm):

    class Meta:
        model = TradeMarketInformation

        fields = [
            "title",
            "information_type",
            "district",
            "location",
            "summary",
            "description",
            "requirements",
            "process_information",
            "contact_information",
            "is_featured",
            "is_published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Trade or market information title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Market or trade location",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Short summary",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Detailed information",
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Requirements",
                }
            ),

            "process_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Process or procedure information",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Contact information",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class TradeMarketRequestForm(forms.ModelForm):

    class Meta:
        model = TradeMarketRequest

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "request_type",
            "subject",
            "description",
            "supporting_information",
            "attachment",
        ]

        widgets = {

            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District or city",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Market or trade location",
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Request subject",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Describe your trade or market request",
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Additional information",
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        
class CooperativeInformationForm(forms.ModelForm):

    class Meta:
        model = CooperativeInformation

        fields = [
            "title",
            "information_type",
            "district",
            "location",
            "summary",
            "description",
            "requirements",
            "application_process",
            "support_information",
            "contact_information",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "support_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }


class CooperativeRequestForm(forms.ModelForm):

    class Meta:
        model = CooperativeRequest

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "cooperative_name",
            "request_type",
            "subject",
            "description",
            "supporting_information",
            "attachment",
        ]

        widgets = {
            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name"
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "your@email.com"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District / City"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Town / Municipality / Area"
                }
            ),

            "cooperative_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Cooperative name if applicable"
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Subject of your request"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your request"
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Any additional information"
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }
class EconomicProjectForm(forms.ModelForm):

    class Meta:
        model = EconomicProject

        fields = [
            "title",
            "project_type",
            "district",
            "location",
            "summary",
            "description",
            "objectives",
            "expected_benefits",
            "implementing_organization",
            "partners",
            "contact_information",
            "start_date",
            "expected_completion_date",
            "status",
            "image",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "project_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "objectives": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),

            "expected_benefits": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),

            "implementing_organization": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "partners": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "expected_completion_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }
        
class FundingBudgetInformationForm(forms.ModelForm):

    class Meta:
        model = FundingBudgetInformation

        fields = [
            "title",
            "information_type",
            "district",
            "organization",
            "summary",
            "description",
            "eligibility",
            "requirements",
            "application_process",
            "funding_amount_information",
            "deadline",
            "contact_information",
            "website",
            "is_featured",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Funding opportunity title",
                }
            ),

            "information_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Funding organization",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),

            "eligibility": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "requirements": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "application_process": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "funding_amount_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Example: Up to UGX 50,000,000",
                }
            ),

            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "contact_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.org",
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class FundingBudgetRequestForm(forms.ModelForm):

    class Meta:
        model = FundingBudgetRequest

        fields = [
            "citizen_name",
            "phone_number",
            "email",
            "district",
            "location",
            "request_type",
            "subject",
            "description",
            "requested_amount",
            "purpose_of_funding",
            "supporting_information",
            "attachment",
        ]

        widgets = {

            "citizen_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Full name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Town / City / Community",
                }
            ),

            "request_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Subject of your request",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe what you need funding or financial assistance for.",
                }
            ),

            "requested_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Amount in UGX",
                    "step": "0.01",
                }
            ),

            "purpose_of_funding": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Explain how the funding will be used.",
                }
            ),

            "supporting_information": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "attachment": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        
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
    
class EconomicFinancialExcelImportForm(forms.Form):
    excel_file = forms.FileField(
        label="Excel Financial Report",
        help_text="Upload a valid Smart City Uganda financial Excel file."
    )

    def clean_excel_file(self):
        excel_file = self.cleaned_data["excel_file"]

        if not excel_file.name.lower().endswith(".xlsx"):
            raise forms.ValidationError(
                "Please upload an Excel .xlsx file."
            )

        if excel_file.size > 10 * 1024 * 1024:
            raise forms.ValidationError(
                "The Excel file must not exceed 10 MB."
            )

        return excel_file