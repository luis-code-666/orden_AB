
from django.db import models

class OrdenDia(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    photo = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="foto")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # Devuelve una cadena de texto, como el nombre del archivo o un identificador
        return self.name
    
    class Meta:
        db_table = "orden"
        ordering = ['-created_at']



