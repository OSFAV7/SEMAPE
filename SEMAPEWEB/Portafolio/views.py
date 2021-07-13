from django.shortcuts import render
from Portafolio.models import proyecto

# Create your views here.
def folder(request):
    proyectos_llamada= proyecto.objects.all()
    return render(request, 'Portafolio/portafolio.html', {'proyectosLLAMA': proyectos_llamada })