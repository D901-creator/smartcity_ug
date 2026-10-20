from django import forms
from .models import FarmerProfile, Farm
from .models import Crop, CropProduction, LivestockRecord
from django import forms
from .models import ( MarketMatch,  AgriculturalProject, AgriculturalProgram,
    FarmerProfile, IrrigationProject,
    Farm,
    Crop,
    CropProduction,
    LivestockRecord,
    MarketListing,
    BuyerRequest,
    AgriculturalInput,
    ExtensionService,
     DiseaseReport,
     Fisher,
FishingActivity,
AquacultureFarm,
FishProcessingFacility,
FishMarketListing,
)

class FarmerProfileForm(forms.ModelForm):

    class Meta:
        model = FarmerProfile

        fields = [
            "farmer_name",
            "phone_number",
            "district",
            "subcounty",
            "village",
            "farmer_type",
            "farm_size_acres",
            "crops",
            "livestock",
        ]

        widgets = {
            "farmer_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter farmer's full name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+256 7XX XXX XXX",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "subcounty": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Subcounty",
                }
            ),

            "village": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Village",
                }
            ),

            "farmer_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "farm_size_acres": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Farm size in acres",
                    "step": "0.01",
                }
            ),

            "crops": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Maize, beans, coffee",
                    "rows": 3,
                }
            ),

            "livestock": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Cattle, goats, poultry",
                    "rows": 3,
                }
            ),
        }


class FarmForm(forms.ModelForm):

    class Meta:
        model = Farm

        fields = [
            "farmer",
            "farm_name",
            "district",
            "location",
            "size_acres",
            "soil_type",
            "irrigation_available",
            "ownership_type",
        ]

        widgets = {
            "farmer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "farm_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Farm name",
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
                    "placeholder": "Village / location",
                }
            ),

            "size_acres": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "soil_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Loam",
                }
            ),

            "irrigation_available": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "ownership_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
class CropForm(forms.ModelForm):

    class Meta:
        model = Crop

        fields = [
            "name",
            "category",
            "description",
            "growing_period_days",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Maize",
                }
            ),

            "category": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Cereals",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Describe the crop",
                }
            ),

            "growing_period_days": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: 120",
                }
            ),
        }


class CropProductionForm(forms.ModelForm):

    class Meta:
        model = CropProduction

        fields = [
            "farmer",
            "farm",
            "crop",
            "season",
            "planting_date",
            "expected_harvest_date",
            "expected_quantity",
            "actual_quantity",
            "unit",
            "status",
        ]

        widgets = {
            "farmer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "farm": forms.Select(
                attrs={"class": "form-select"}
            ),

            "crop": forms.Select(
                attrs={"class": "form-select"}
            ),

            "season": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Season 2026A",
                }
            ),

            "planting_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "expected_harvest_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "expected_quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "actual_quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "unit": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "kg, tonnes, bags...",
                }
            ),

            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }


class LivestockRecordForm(forms.ModelForm):

    class Meta:
        model = LivestockRecord

        fields = [
            "farmer",
            "livestock_type",
            "breed",
            "number_of_animals",
            "location",
            "health_status",
        ]

        widgets = {
            "farmer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "livestock_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Cattle",
                }
            ),

            "breed": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Ankole",
                }
            ),

            "number_of_animals": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Farm location",
                }
            ),

            "health_status": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Healthy",
                }
            ),
        }
class MarketListingForm(forms.ModelForm):
    class Meta:
        model = MarketListing
        fields = [
            "farmer",
            "product_name",
            "category",
            "quantity",
            "unit",
            "price_per_unit",
            "district",
            "description",
            "status",
        ]
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Describe the agricultural product..."
            }),
        }


class BuyerRequestForm(forms.ModelForm):
    class Meta:
        model = BuyerRequest
        fields = [
            "buyer_name",
            "phone_number",
            "product_required",
            "quantity_required",
            "unit",
            "district",
            "maximum_price",
            "description",
            "status",
        ]
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Describe what you are looking for..."
            }),
        }
        
class MarketMatchResponseForm(forms.ModelForm):
    class Meta:
        model = MarketMatch

        fields = [
            "buyer_message",
            "farmer_message",
            "agreed_quantity",
            "agreed_price",
            "transaction_notes",
            "status",
        ]

        widgets = {
            "buyer_message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Message to the farmer..."
                }
            ),

            "farmer_message": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Message to the buyer..."
                }
            ),

            "transaction_notes": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Add transaction notes..."
                }
            ),

            "agreed_quantity": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "Agreed quantity"
                }
            ),

            "agreed_price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "Agreed price per unit"
                }
            ),
        } 
class AgriculturalInputForm(forms.ModelForm):
    class Meta:
        model = AgriculturalInput

        fields = [
            "name",
            "input_type",
            "supplier",
            "district",
            "description",
            "price",
            "is_available",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Describe the agricultural input..."
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "Enter price in UGX"
                }
            ),
        }
        
class ExtensionServiceForm(forms.ModelForm):
    class Meta:
        model = ExtensionService

        fields = [
            "title",
            "description",
            "officer_name",
            "district",
            "service_type",
            "scheduled_date",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Describe the extension service..."
                }
            ),

            "scheduled_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }
class AgriculturalProjectForm(forms.ModelForm):
    class Meta:
        model = AgriculturalProject
        fields = [
            "name",
            "description",
            "district",
            "implementing_organization",
            "target_beneficiaries",
            "budget",
            "start_date",
            "end_date",
            "status",
        ]
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Describe the agricultural project..."
            }),
            "target_beneficiaries": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Describe the people or groups benefiting..."
            }),
            "budget": forms.NumberInput(attrs={
                "step": "0.01",
                "placeholder": "Enter project budget in UGX"
            }),
            "start_date": forms.DateInput(attrs={
                "type": "date"
            }),
            "end_date": forms.DateInput(attrs={
                "type": "date"
            }),
        }


class AgriculturalProgramForm(forms.ModelForm):
    class Meta:
        model = AgriculturalProgram
        fields = [
            "name",
            "description",
            "target_group",
            "district",
            "application_open",
        ]
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Describe the agricultural programme..."
            }),
            "target_group": forms.TextInput(attrs={
                "placeholder": "e.g. Smallholder farmers, youth, women, cooperatives"
            }),
            "application_open": forms.DateInput(attrs={
                "type": "date"
            }),
        }
class DiseaseReportForm(forms.ModelForm):
    class Meta:
        model = DiseaseReport
        fields = [
            "crop_or_animal",
            "symptoms",
            "district",
            "location",
            "urgency",
        ]
        widgets = {
            "crop_or_animal": forms.TextInput(attrs={
                "placeholder": "e.g. Maize, Coffee, Cattle"
            }),
            "symptoms": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Describe the symptoms you observed..."
            }),
            "location": forms.TextInput(attrs={
                "placeholder": "Village, parish, farm or other location"
            }),
        }
class IrrigationProjectForm(forms.ModelForm):
    class Meta:
        model = IrrigationProject
        fields = [
            "name",
            "district",
            "location",
            "beneficiaries",
            "hectares_supported",
            "status",
            "description",
        ]
        widgets = {
            "location": forms.TextInput(attrs={
                "placeholder": "Village, parish, sub-county or project location"
            }),
            "beneficiaries": forms.NumberInput(attrs={
                "min": "0",
                "placeholder": "Number of beneficiaries"
            }),
            "hectares_supported": forms.NumberInput(attrs={
                "step": "0.01",
                "min": "0",
                "placeholder": "Hectares supported"
            }),
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Describe the irrigation project..."
            }),
        }
        
        # ============================================================
# PHASE 3 — FISHING & FISHERIES FORMS
# ============================================================


class FisherForm(forms.ModelForm):

    class Meta:
        model = Fisher

        fields = [
            "name",
            "phone_number",
            "fisher_type",
            "district",
            "location",
            "fishing_community",
            "registration_number",
            "number_of_boats",
            "active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter fisher or group name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),

            "fisher_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Village, landing site or location",
                }
            ),

            "fishing_community": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter fishing community",
                }
            ),

            "registration_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter registration number",
                }
            ),

            "number_of_boats": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                }
            ),

            "active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class FishingActivityForm(forms.ModelForm):

    class Meta:
        model = FishingActivity

        fields = [
            "fisher",
            "water_body",
            "fishing_area",
            "fishing_method",
            "fishing_date",
            "species",
            "quantity",
            "unit",
            "notes",
        ]

        widgets = {
            "fisher": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "water_body": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Lake, river or other water body",
                }
            ),

            "fishing_area": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Fishing area or landing site",
                }
            ),

            "fishing_method": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "fishing_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "species": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Fish species",
                }
            ),

            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "unit": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "kg, tonnes, baskets, etc.",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Additional information",
                }
            ),
        }


class AquacultureFarmForm(forms.ModelForm):

    class Meta:
        model = AquacultureFarm

        fields = [
            "owner_name",
            "phone_number",
            "farm_name",
            "farm_type",
            "district",
            "location",
            "number_of_units",
            "fish_species",
            "production_capacity",
            "capacity_unit",
            "active",
        ]

        widgets = {
            "owner_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Farm owner or responsible person",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),

            "farm_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter fish farm name",
                }
            ),

            "farm_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Village, town or location",
                }
            ),

            "number_of_units": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                }
            ),

            "fish_species": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example Nile tilapia, catfish",
                }
            ),

            "production_capacity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "capacity_unit": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "kg, tonnes, etc.",
                }
            ),

            "active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class FishProcessingFacilityForm(forms.ModelForm):

    class Meta:
        model = FishProcessingFacility

        fields = [
            "name",
            "facility_type",
            "owner_or_organization",
            "district",
            "location",
            "phone_number",
            "processing_capacity",
            "capacity_unit",
            "services",
            "active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Processing facility name",
                }
            ),

            "facility_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "owner_or_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Owner or organization",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Facility location",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),

            "processing_capacity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "capacity_unit": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "kg, tonnes, etc.",
                }
            ),

            "services": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": (
                        "For example: drying, smoking, "
                        "cold storage, packaging"
                    ),
                }
            ),

            "active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class FishMarketListingForm(forms.ModelForm):

    class Meta:
        model = FishMarketListing

        fields = [
            "seller_name",
            "phone_number",
            "fish_species",
            "product_description",
            "quantity",
            "unit",
            "price_per_unit",
            "district",
            "location",
            "status",
        ]

        widgets = {
            "seller_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seller or producer name",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),

            "fish_species": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example Nile perch, tilapia",
                }
            ),

            "product_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe the fish product",
                }
            ),

            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "unit": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "kg, tonnes, baskets, etc.",
                }
            ),

            "price_per_unit": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Town, landing site or location",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }