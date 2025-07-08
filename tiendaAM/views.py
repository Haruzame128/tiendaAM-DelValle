from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UsuarioForm, ProductoForm, EscuelaForm
from .models import Producto, Usuario, Escuela

def inicio(request):
    return render(request, 'tiendaAM/inicio.html')

def productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = Producto(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
                tipo_producto=form.cleaned_data['tipo_producto']
            )
            nuevo_producto.save()
            form = ProductoForm()
            return redirect('inicio') # Redirige a la página de inicio después de guardar el producto
    else:  
        form = ProductoForm()
        return render(request, 'tiendaAM/productos.html', {'form': form})
    
def usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            nuevo_usuario.save()
            form = UsuarioForm()
            return redirect('inicio') # Redirige a la página de inicio después de guardar el usuario
    else:  
        form = UsuarioForm()
        return render(request, 'tiendaAM/usuarios.html', {'form': form})
    
def escuelas(request):
    if request.method == 'POST':
        form = EscuelaForm(request.POST)
        if form.is_valid():
            nueva_escuela = Escuela(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                ubicacion=form.cleaned_data['ubicacion']
            )
            nueva_escuela.save()
            form = EscuelaForm()
            return redirect('inicio') # Redirige a la página de inicio después de guardar la escuela
    else:  
        form = EscuelaForm()
        return render(request, 'tiendaAM/escuelas.html', {'form': form})

def productos_listado(request):
    if request.method == 'GET':
        nombre_producto = request.GET.get('nombre', '')
        productos = Producto.objects.filter(nombre__icontains=nombre_producto)
        return render(request, 'tiendaAM/productos_listado.html', {'productos': productos, 'nombre_producto': nombre_producto})
    else:
        return HttpResponse("Método no permitido", status=405)
    
def productos_mostrar(request):
    productos = Producto.objects.all()
    return render(request, 'tiendaAM/productos_listado.html', {'productos': productos})
   