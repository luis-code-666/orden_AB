from .models import OrdenDia
from django import forms

class OrdenDiaForm(forms.Form):
    photo = forms.ImageField(label="Foto", required=False)
    
    def save(self):
        OrdenDia.objects.create(
        photo=self.cleaned_data['photo'],
        )