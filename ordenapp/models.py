
from django.db import models
from django.utils.html import mark_safe

class OrdenDia(models.Model):
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")

    def __str__(self):
        # Devuelve una cadena de texto, como el nombre del archivo o un identificador
        return f"Orden del día {self.id}" if self.photo else "Sin Foto"

    def photo_tag(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="350" height="350" />')
        return "No Image"

    photo_tag.short_description = 'Foto'

