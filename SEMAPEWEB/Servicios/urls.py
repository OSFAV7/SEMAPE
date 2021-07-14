from django.urls import path
from Servicios.views import Service

urlpatterns = [
    path('',Service.as_view(), name='servicios'),

]
