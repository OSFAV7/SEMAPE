from django.shortcuts import get_object_or_404, render
from Portafolio.models import proyecto, categorias
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
        self.categoria= get_object_or_404(categorias, id=self.kwargs['categoria_id'])
        self.proyectoLLama= proyecto.objects.filter(categorias =self.categoria)
        return  self.proyectoLLama, self.categoria


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        context['listaProyecto'] = self.proyectoLLama
        return context

