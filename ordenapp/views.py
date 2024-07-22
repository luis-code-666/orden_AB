
from django.views import generic
from django.urls import reverse_lazy
from .forms import OrdenDiaForm

class MiOrdenDelDia(generic.FormView):
    template_name = "orden/orden.html"    
    form_class = OrdenDiaForm
    success_url = reverse_lazy("orden_dia")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    