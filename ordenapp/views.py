
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import OrdenDiaForm
from .models import OrdenDia

# Create your views here.
def miOrdenDelDia(request):
    if request.method == 'POST':
        form = OrdenDiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('La imagen fue registrada con exito'))
            return redirect('orden_dia')
        else:
            messages.error(request, 'Error, no se pudo registrar la imagen.')
            return redirect("orden_dia")
    else:
        form = OrdenDiaForm()
        data = {
            'form': form,
            'orden': list_imagenes(request)
        }
    return render(request, 'orden/orden.html', data)


def list_imagenes(request):
    return OrdenDia.objects.all()


"""
def list_imagenes(request):
    zapatos = Zapato.objects.all()
    return render(request, 'list.html', {'zapatos': zapatos})
"""    