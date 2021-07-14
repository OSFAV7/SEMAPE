from django.urls import path

from Index.views import Home, Contac

urlpatterns = [
    path('',Home.as_view(), name='inicio'),
    path('contact',Contac.as_view(), name='contacto'),
]
