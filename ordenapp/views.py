from django.shortcuts import render
from django.views import generic
from .forms import OrdenDiaForm

class MiOrdenDelDia(generic.FormView):
    tempate_name = "orden/orden.html"    
    form_class = OrdenDiaForm