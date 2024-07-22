
from django.views import generic
from .forms import OrdenDiaForm

class MiOrdenDelDia(generic.FormView):
    template_name = "orden/orden.html"    
    form_class = OrdenDiaForm