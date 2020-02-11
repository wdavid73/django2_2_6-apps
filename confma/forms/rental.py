from django.forms import ModelForm, TextInput
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget
from ..models import Alquiler, Client


class RentalForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = [
            'date_return',
            'price',
            'cloth',
            'client'
        ]

        widgets = {
            'date_return': forms.DateInput(
                attrs={'class': 'form-control bg-dark text-white mb-3',
                       'placeholder': 'Ingrese la fecha de devolucion   YYYY-MM-DD'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control bg-dark text-white mb-3'}),
            'cloth': forms.Select(
                attrs={'class ': 'form-control bg-dark text-white mb-3'}),
            'client': forms.Select(
                attrs={'class ': 'form-control bg-dark text-white mb-3'}),
        }

        labels = {
            'date_return': _("Fecha de Devolucion (YYYY-MM-DD) "),
            'price': _("Valor del Alquier"),
            'cloth': _("Prenda a Alquilar"),
            'client': _("Cliente")
        }

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(state=1)
