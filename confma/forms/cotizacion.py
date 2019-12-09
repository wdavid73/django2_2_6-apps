from django.forms import ModelForm , TextInput
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Cotizacion

FASHION_CHOICE = [
    ('General' , 'general'),
    ('A medida' , 'a medida')
]

class CotizacionFormModel(forms.ModelForm):

    class Meta:
        model = Cotizacion
        fields = [
            'nickname',
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
            'nickname'         : forms.TextInput(
                attrs = {
                    'placeholder' : 'Nombre de la Cotizacion , Ejemplo : Cotizacion Base' , 
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_cloth'      : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor de la tela , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_work'       : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor del Trabajo , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_threads'    : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor de los Hilos  , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_buttons'    : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor de los botones  , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_necks'      : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor de los cuello , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_embroidery' : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor del bordado  , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'value_prints'     : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Valor del estanpado  , Ejemplo : 150.00',
                    'class' : 'form-control bg-dark text-white mb-3'}),

            'fashion'          : forms.Select(choices = FASHION_CHOICE,
                attrs ={
                    'class' : 'form-control bg-dark text-white mb-3'}),
            
        }

        labels = {
            "nickmae"           : _("Nombre para la Cotizacion"),
            "value_cloth"       : _("Valor de la Tela"),
            "value_work"        : _("Valor del Trabajo"),
            "value_threads"     : _("Valor de los Hilos"),
            "value_buttons"     : _("Valor de los Botones"),
            "value_necks"       : _("Valor de los cuellos"),
            "value_embroidery"  : _("Valor del bordado"),
            "value_print"       : _("Valor del estampado"),
            "fashion"           : _("Selecciones una Moda:"),
        }