from django import forms

from ..models import Client, Alquiler


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


class FindForm(forms.ModelForm):
    class Meta:
        model = Alquiler  # uso del modelo de alquiler como pivote para acceder al modelo client desde este form
        fields = [
            'client'
        ]

        widgets = {
            'client': forms.Select(attrs={'class ': 'form-control bg-dark text-white mb-3'}),
        }

    def __init__(self, *args, **kwargs):
        super(FindForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(state=1)


class AllClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['id']
