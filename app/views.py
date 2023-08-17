from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import Rapido


# Create your views here.

def home(request):
    # return render(request, "home.html")
    rapido = Rapido.objects.all()
    return render(request, "consulta.html", {"rapido": rapido})


def ingreso(request):
    return render(request, "home.html")

def edicion(request, id):
#return render(request, "home.html")
    rapido = Rapido.objects.get(id=id)
    return render(request, "editar.html", {"rapido": rapido})



def registrar(request):
    nombre_establecimiento1 = request.POST['nombre_establecimiento'],
    rapido = Rapido.objects.create(
        nombre_establecimiento=request.POST['nombre_establecimiento'],
        direccion=request.POST['direccion'],
        cp=request.POST['cp'],
        localidad=request.POST['localidad'],
        provincia=request.POST['provincia'],
        persona_contacto=request.POST['persona_contacto'],
        telefono_contacto=request.POST['telefono_contacto'],
        email=request.POST['email'],
        sector_actividad=request.POST['sector_actividad'],
        tipo_terminal=request.POST['tipo_terminal'],
        comision=request.POST['comision'],
        retorno=request.POST['retorno'],
        fondo_inicial=request.POST['fondo_inicial'],
        aportacion_fondo=request.POST['aportacion_fondo'],
        metodo_reposicion=request.POST['metodo_reposicion'])
    # rapido.save()
    mensaje = "El Registro fue creado con Exito...!"
    messages.success(request, f'Registro {nombre_establecimiento1} creado')

    return render(request, 'consulta.html', {
        'form': UserCreationForm,
        'mensaje': mensaje
    })
