from django.contrib import admin
from .models import OrdenDia

class OrdenDiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'photo_tag')

admin.site.register(OrdenDia, OrdenDiaAdmin)