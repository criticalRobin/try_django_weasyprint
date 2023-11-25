from django import forms
from .models import ChangeForm


class ChangeFormForm(forms.ModelForm):
    class Meta:
        model = ChangeForm
        fields = ["project", "change", "description"]
        labels = {
            "project": "Proyecto",
            "change": "Cambio",
            "description": "Descripción",
        }
