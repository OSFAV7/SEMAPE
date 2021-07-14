from django.db.models.query import QuerySet, ValuesIterable
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name= 'Index/inicio.html'
    

 #   QuerySet= request.GET.get("busqueda")
  #  if QuerySet:
  #      print('buqueda realisada')

class Contac(TemplateView):
    template_name='Index/contacto.html'
    
