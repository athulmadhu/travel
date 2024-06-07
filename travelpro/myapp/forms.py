from django import forms
from .models import contactdb

class contactform(forms.ModelForm):
    class Meta:
        model=contactdb
        fields="__all__"
        widget={}