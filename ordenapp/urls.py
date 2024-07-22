from django.urls import path
from .views import MiOrdenDelDia


urlpatterns = [
    path('orden/', MiOrdenDelDia.as_view(), name="orden_dia" )
]
