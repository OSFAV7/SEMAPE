from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Index/inicio.html')


def folder(request):

    return render(request, 'Index/portafolio.html')

def contac(request):
    return render(request, 'Index/contacto.html')