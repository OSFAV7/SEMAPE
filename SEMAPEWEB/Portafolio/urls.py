from django.urls import path

from . import views

urlpatterns = [
    path('',views.folder, name='portafolio'),
    path('categoria/<int:categoria_id>/',views.categoria, name='categorias'),

]
