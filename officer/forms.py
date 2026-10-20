
from django import forms

from .models import CitizenRequest, RequestReply, RequestStatusHistory


class OfficerReplyForm(forms.ModelForm):
    class Meta:
        model = RequestReply
        fields = ["message", "attachment"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "class": "form-control form-control-sm",
                    "rows": 3,
                    "placeholder": "Write a reply to the citizen...",
                }
            ),
            "attachment": forms.ClearableFileInput(
                attrs={"class": "form-control form-control-sm"}
            ),
        }

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if not message:
            raise forms.ValidationError("Please enter a reply.")
        return message


class OfficerRequestStatusForm(forms.ModelForm):
    class Meta:
        model = RequestStatusHistory
        fields = ["new_status", "note"]
        widgets = {
            "new_status": forms.Select(
                attrs={"class": "form-select form-select-sm"}
            ),
            "note": forms.Textarea(
                attrs={
                    "class": "form-control form-control-sm",
                    "rows": 2,
                    "placeholder": "Add a note about this update...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_status"].choices = CitizenRequest.Status.choices
        self.fields["note"].required = False
