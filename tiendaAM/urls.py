from django.urls import path

from .views import saludo, inicio

urlpatterns = [
    path('saludo/', saludo, name='saludo'),
    path('inicio/', inicio, name='inicio'),
]
