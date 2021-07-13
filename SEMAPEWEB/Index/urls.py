from django.urls import path

from Index import views

urlpatterns = [
    path('',views.home, name='inicio'),
    path('contact',views.contac, name='contacto'),
]
