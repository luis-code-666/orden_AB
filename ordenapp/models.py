from django.db import models

class OrdenDia(models.Model):
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")

    def __str__(self):
        return self.photo
