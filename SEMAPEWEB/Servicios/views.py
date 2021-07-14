
from Servicios.models import Servicio
from django.views.generic import TemplateView, ListView

# Create your views here.
class Service(ListView):
    template_name= 'Servicios/servicios.html'
    context_object_name="servicioLLAMA"
    queryset= Servicio.objects.all()