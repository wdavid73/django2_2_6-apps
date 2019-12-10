from django.forms import ModelForm , TextInput
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import  Cloth

class ClothFormModel(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = [
            'name',
            'color',
            'size'
         ]

        widgets = {
            'name'  : forms.TextInput(attrs={'class ' : 'form-control bg-dark text-white mb-3'}),
            'size'  : forms.Select(attrs={'class ' : 'form-control bg-dark text-white mb-3'}),
            'color' : forms.TextInput(attrs={'class ' : 'form-control bg-dark text-white mb-3'}),
        }

        labels = {
            "name"  : _("Prenda"),
            "size"  : _("Talla"),
            "color" : _("Color"),
        }