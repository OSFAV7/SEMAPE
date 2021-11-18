from django.urls import path
from Servicios.views import Service, SpecificService

urlpatterns = [
    path('/<int:area_id>/',Service.as_view(), name='servicios'),
    path('servicioDetalle/<int:servicio_id>/',SpecificService.as_view(), name='espesificacionServicio'),

]
