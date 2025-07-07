from django.shortcuts import render

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola, mundo!")

def inicio(request):
    return render(request, 'tiendaAM/inicio.html')
