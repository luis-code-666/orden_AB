from django.contrib import admin
from .models import OrdenDia

class OrdenDiaAdmin(admin.ModelAdmin):
    model = OrdenDia
    list_display = ['name','photo']
    search_fields = ['name']
admin.site.register(OrdenDia,OrdenDiaAdmin)

