from django import forms
from crud.models import company

class cpnform(forms.ModelForm):
    class Meta:
        model=company
        fields="__all__"