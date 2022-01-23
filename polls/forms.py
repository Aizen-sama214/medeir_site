from django import forms

from .models import Import

class ImportForm(forms.ModelForm):
    class Meta:
        model = Import
        fields = "__all__"