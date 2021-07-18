from django.shortcuts import get_object_or_404, render
from Portafolio.models import proyecto, categorias, galeria
from django.views.generic import TemplateView, ListView


class Folder(ListView):
    template_name= 'Portafolio/portafolio.html'

    def get_queryset(self):
        self.proyectosllamada=proyecto.objects.all()
        self.categoriallamada= categorias.objects.all()
        return self.proyectosllamada, self.categoriallamada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectosLLAMA'] = self.proyectosllamada
        context['categoriaLLAMA'] = self.categoriallamada
        return context



class Categorias(ListView):
    template_name='Portafolio/categorias.html'

    def get_queryset(self):
        self.proyectoEspesifico= get_object_or_404(proyecto, id=self.kwargs['proyecto_id'])
        self.proyectoGaleria= galeria.objects.filter(proyectoPertenece =self.proyectoEspesifico)
        return  self.proyectoEspesifico, self.proyectoGaleria


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto'] = self.proyectoEspesifico
        context['listaProyecto'] = self.proyectoGaleria
        return context

