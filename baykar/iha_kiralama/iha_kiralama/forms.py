from django import forms 
from iha_kiralama.models import IHA

class IhaForms(forms.ModelForm):
    class Meta:
        model=IHA
        fields="__all__"