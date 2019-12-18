from django.forms import ModelForm
from django import forms

from ..models import Client

class ClientFormModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'lastname',
            'address',
            'phone',
            'cellphone'
            
        ]