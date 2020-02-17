from django import forms

from ..models import CotizacionClient, Client, Cotizacion


class CotizacionClientForm(forms.ModelForm):
    class Meta:
        model = CotizacionClient
        fields = [
            "cotizacion",
            "client",
            "total"
        ]

        widgets = {
            'client': forms.Select(attrs={'class ': 'form-control bg-dark text-white mb-3'}),
        }

    def __init__(self, *args, **kwargs):
        super(CotizacionClientForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(state=1)
        self.fields['cotizacion'].queryset = Cotizacion.objects.filter(state=1)
