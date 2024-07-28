from django.urls import path
from .views import MiOrdenDelDia


urlpatterns = [
    path('', MiOrdenDelDia, name="orden_dia" )
]
