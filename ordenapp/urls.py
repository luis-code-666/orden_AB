from django.urls import path

from . import views

urlpatterns = [
    path('', views.miOrdenDelDia, name="orden_dia" ),
    path('imagen/', views.imagenOrdenDia, name="imagen_orden_dia" ),
]
