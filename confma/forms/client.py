from django import forms

from ..models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'lastname',
            'address',
            'phone',
            'cellphone'
        ]


class AllClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['id']
