from django.forms import ModelForm , TextInput
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Cotizacion , Cloth

FASHION_CHOICE = [
    ('General' , 'General'),
    ('A medida' , 'A Medida')
]

CLOTH_CHOICE = []
cc = []
def cloths(cc):
    if (Cloth.objects.all == None):
        return cc
    else:
        for clo in Cloth.objects.all():
            cc.append((clo.id , clo.name))
        return cc

CLOTH_CHOICE = cloths(cc)


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
            'fashion'
         ]

        #cloth = forms.ChoiceField(widget = forms.Select(attrs={'class' : 'form-control'})),
        widgets = {

            'cloth'            : forms.Select(
                choices = CLOTH_CHOICE,
                attrs={'class ' : 'form-control bg-dark text-white mb-3'}),

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
            "cloth"             : _("Seleccione una Prenda"),
            "value_cloth"       : _("Valor de la Tela"),
            "value_work"        : _("Valor del Trabajo"),
            "value_threads"     : _("Valor de los Hilos"),
            "value_buttons"     : _("Valor de los Botones"),
            "value_necks"       : _("Valor de los cuellos"),
            "value_embroidery"  : _("Valor del bordado"),
            "value_print"       : _("Valor del estampado"),
            "fashion"           : _("Selecciones una Moda:"),
        }