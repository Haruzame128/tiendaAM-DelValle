from django.contrib import admin

# Register your models here.

from .models import Usuario, Producto, Escuela

register_models = [Usuario, Producto, Escuela]

admin.site.register(register_models)