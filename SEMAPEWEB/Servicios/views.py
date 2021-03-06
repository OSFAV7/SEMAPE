from django.shortcuts import get_object_or_404, render
from Servicios.models import Servicio, Espesificaciondetalle, EspesificacionServicio, BloqueServicio
from django.views.generic import ListView

# Create your views here.
class Service(ListView):
    template_name= 'Servicios/servicios.html'

    def get_queryset(self):

        self.Bloquedeservicio= BloqueServicio.objects.filter(area = self.kwargs['area_id'])
        self.servicioslista=[]
        for lista in self.Bloquedeservicio:
            id=lista.id
            hacerlista=Servicio.objects.filter(bloque= id)
            for lista in hacerlista:
                self.servicioslista.append(lista)
        return self.Bloquedeservicio, self.servicioslista

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['servicioLLAMA']= self.servicioslista
        context['nombreBloque']= self.Bloquedeservicio
        return context

class SpecificService(ListView):
    template_name='Servicios/detallesServicio.html'

    def get_queryset(self):
        self.servicioEspesifico= get_object_or_404(Servicio, id=self.kwargs['servicio_id'])
        self.employee_list = [cosa for cosa in self.servicioEspesifico.servicioEspesificacion.all()]
        self.employee_ids = [emp.id for emp in self.employee_list]
        self.espeficacionlista=[]
        for ids in self.employee_ids:
            servicioEspesificacion=EspesificacionServicio.objects.filter( id=ids)
            servicio_ids = [ser.id for ser in servicioEspesificacion]
            for detalle in servicio_ids:
                especificaciones= Espesificaciondetalle.objects.filter(espesificacion= detalle)
                self.espeficacionlista.append( especificaciones)
        #self.especificaciones= Espesificaciondetalle.objects.filter(espesificacion= self.servicioEspesificacion)
        return  self.servicioEspesifico, self.espeficacionlista #, self.especificaciones


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicioEspesifico'] = self.servicioEspesifico
        context['servicioEspesificacion'] = self.espeficacionlista
       #context['listaEspesificaciones'] = self.especificaciones

        return context

