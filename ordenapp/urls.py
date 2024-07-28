from django.urls import path

from . import views

urlpatterns = [
    path('', views.miOrdenDelDia, name="orden_dia" )
]
