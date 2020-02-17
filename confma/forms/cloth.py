from django import forms

from ..models import Cloth

FASHION_CHOICE = [
    ('General', 'General'),
    ('A Medida', 'A Medida')
]


class ClothFormModel(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = [
            'name',
            'color',
            'size',
            'fashion',
            'image'
        ]

        widgets = {
            'size': forms.Select(attrs={'class ': 'form-control bg-dark text-white mb-3'}),
            'fashion': forms.Select(choices=FASHION_CHOICE, attrs={'class': 'form-control bg-dark text-white mb-3'}),
        }
