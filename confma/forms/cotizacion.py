from django import forms

from ..models import Cotizacion
from ..static_methods import ClothWithOutCotizacion


class CotizacionFormModel(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = [
            'cloth',
            'value_cloth',
            'value_work',
            'value_threads',
            'value_buttons',
            'value_necks',
            'value_embroidery',
            'value_prints',
        ]

        widgets = {

            'cloth': forms.Select(
                attrs={'class ': 'form-control bg-dark text-white'}),
        }

    def __init__(self, *args, **kwargs):
        super(CotizacionFormModel, self).__init__(*args, **kwargs)
        self.fields['cloth'].queryset = ClothWithOutCotizacion()
