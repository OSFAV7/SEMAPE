from django.shortcuts import render
from Portafolio.models import proyecto, categorias

# Create your views here.
def folder(request):
    proyectos_llamada= proyecto.objects.all()
    categoriallamada= categorias.objects.all()
    return render(request, 'Portafolio/portafolio.html', {'proyectosLLAMA': proyectos_llamada , 'categoriaLLAMA':categoriallamada})

def categoria(request, categoria_id):
    categoria= categorias.objects.get(id=categoria_id)
    proyectos_llamada= proyecto.objects.filter(categorias= categoria)
    return render(request, 'Portafolio/categorias.html',{'proyectosLLAMA': proyectos_llamada,'categoria':categoria})