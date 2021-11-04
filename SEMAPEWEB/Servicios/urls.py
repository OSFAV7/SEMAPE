from django.urls import path
from Servicios.views import Service, SpecificService

urlpatterns = [
    path('',Service.as_view(), name='servicios'),
    path('servicioDetalle/<int:servicio_id>/',SpecificService.as_view(), name='espesificacionServicio'),

]
