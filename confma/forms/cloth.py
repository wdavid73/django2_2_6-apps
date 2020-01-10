from django.forms import ModelForm , TextInput
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import  Cloth

FASHION_CHOICE = [
    ('General' , 'General'),
    ('A Medida' , 'A Medida')
]

class ClothFormModel(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = [
            'name',
            'color',
            'size',
            'fashion'
         ]

        widgets = {
            'name'      : forms.TextInput(
                attrs={'class ' : 'form-control bg-dark text-white mb-3' , 'placeholder' : 'Ingrese un Nombre para identificar a la Prenda'}),
            'color'     : forms.TextInput(
                attrs={'class ' : 'form-control bg-dark text-white mb-3', 'placeholder' : 'Ingrese el Color de la prenda'}),
            'size'      : forms.Select( attrs={'class ' : 'form-control bg-dark text-white mb-3'}),
            'fashion'   : forms.Select( choices = FASHION_CHOICE,attrs ={ 'class' : 'form-control bg-dark text-white mb-3'}),
        }

        labels = {
            "name"  : _("Prenda"),
            "size"  : _("Talla"),
            "color" : _("Color"),
            "fashion" : _("Moda"),
        }