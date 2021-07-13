from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    QuerySet= request.GET.get("busqueda")
    if QuerySet:
        print('buqueda realisada')

    return render(request, 'Index/inicio.html')


def contac(request):
    return render(request, 'Index/contacto.html')