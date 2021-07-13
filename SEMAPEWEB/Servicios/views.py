from django.shortcuts import render
from Servicios.models import Servicio


# Create your views here.
def service(request):
    servicios_llamada= Servicio.objects.all()
    return render(request, 'Servicios/servicios.html',{"servicioLLAMA":servicios_llamada})
