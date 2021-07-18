from django.urls import path
from Portafolio.views import Folder, Categorias
from . import views

urlpatterns = [
    path('',Folder.as_view(), name='portafolio'),
    path('categoria/<int:proyecto_id>/',Categorias.as_view(), name='categorias'),

]
