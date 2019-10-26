from django.forms import ModelForm , TextInput
from django import forms

from ..models import Cotizacion

FASHION_CHOICE = [
    ('General' , 'general'),
    ('A medida' , 'a medida')
]

class CotizacionFormModel(forms.ModelForm):

    class Meta:
        model = Cotizacion
        fields = [
            'value_cloth',
            'value_work',
            'value_threads',
            'value_buttons',
            'value_necks',
            'value_embroidery',
            'value_prints',
            'fashion',
            ]
            
        widgets = {
            'value_cloth'       : forms.NumberInput(attrs = {'placeholder' : 'Valor de la tela , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'value_work'        : forms.NumberInput(attrs = {'placeholder' : 'Valor del Trabajo  , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'value_threads'     : forms.NumberInput(attrs = {'placeholder' : 'Valor de los Hilos  , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'value_buttons'     : forms.NumberInput(attrs = {'placeholder' : 'Valor de los botones  , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'value_necks'       : forms.NumberInput(attrs = {'placeholder' : 'Valor de los cuello  , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'value_embroidery'  : forms.NumberInput(attrs = {'placeholder' : 'Valor del bordado  , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'value_prints'      : forms.NumberInput(attrs = {'placeholder' : 'Valor del estanpado  , Ejemplo : 150.00' , 'class' : 'form-control'}),
            'fashion'           : forms.Select(choices = FASHION_CHOICE , attrs ={'class' : 'form-control'}),
            
        }