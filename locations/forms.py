
from django import forms
from .models import Region, District, City, Municipality


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter region name",
            }),
        }


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        
        fields = ["name", "region", "latitude", "longitude"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter district name",
            }),
            "region": forms.Select(attrs={"class": "form-select"}),
        
            "latitude": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.000001",
                "placeholder": "District latitude",
            }),
            "longitude": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.000001",
                "placeholder": "District longitude",
            }),

        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "district"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter city name",
            }),
            "district": forms.Select(attrs={"class": "form-select"}),
        }


class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ["name", "district"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter municipality name",
            }),
            "district": forms.Select(attrs={"class": "form-select"}),
        }
