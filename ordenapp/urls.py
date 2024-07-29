from django.urls import path

from . import views

urlpatterns = [
    path('', views.imagenOrdenDia, name="imagen_orden_dia" ),
    path('imagenAdmin/', views.miOrdenDelDia, name="orden_dia" ),
]
