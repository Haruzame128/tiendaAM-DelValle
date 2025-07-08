from django.urls import path

from .views import inicio, productos, usuarios, escuelas, productos_listado, productos_mostrar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'), # type: ignore
    path('usuarios/', usuarios, name='usuarios'), # type: ignore
    path('escuelas/', escuelas, name='escuelas'), # type: ignore
    path('productos/listado', productos_listado, name='productosListado'), # type: ignore
    path('productos-mostrar', productos_mostrar, name='productosMostrar'), # type: ignore
]
