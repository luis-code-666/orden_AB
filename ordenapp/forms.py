from .models import OrdenDia
from django import forms

class OrdenDiaForm(forms.ModelForm):
    class Meta:
        model = OrdenDia
        # fields = '__all__'
        # fields = ('name', 'img_zapato')
        fields = ['name', 'photo']
        labels = {
            'name': 'Nombre de la Imagen',
            'photo': 'Imagen'
        }