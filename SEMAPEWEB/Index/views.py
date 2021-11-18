from django.db.models.query import QuerySet, ValuesIterable
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from Portafolio.models import proyecto
from Servicios.models import DetallesArea, AreaServicio


# Create your views here.
class Home(ListView):
    template_name= 'Index/index.html'

    def get_queryset(self):
        self.areasdeservicio= AreaServicio.objects.all()
        self.detallesarea= DetallesArea.objects.all()
        self.proyectosllamada= proyecto.objects.filter(destacado=True)
        return self.proyectosllamada, self.areasdeservicio, self.detallesarea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectosgaleria'] = self.proyectosllamada
        context['areas'] = self.areasdeservicio
        context['detalles'] = self.detallesarea
        return context
    

 #   QuerySet= request.GET.get("busqueda")
  #  if QuerySet:
  #      print('buqueda realisada')

class Contac(TemplateView):
    template_name='Index/contacto.html'
    