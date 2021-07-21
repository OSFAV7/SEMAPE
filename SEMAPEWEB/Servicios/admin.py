from django.contrib import admin

# Register your models here.

from .models import Servicio, EspesificacionServicio, Espesificaciondetalle

class servioadmin(admin.ModelAdmin):
    search_fields= ['titulo']
    list_display = ['titulo', 'update']
    readonly_fields= ('created','update')
    filter_horizontal = ('servicioEspesificacion',) 

class servioEspesificasionadmin(admin.ModelAdmin):
    search_fields= ['titulo']
    list_display = ['titulo', 'update']
    readonly_fields= ('created','update')

class espesificacionDetalleadmin(admin.ModelAdmin):
    search_fields= ['espesificacion']
    list_display = ['espesificacion','detalle', 'update']
    readonly_fields= ('created','update')

admin.site.register(Servicio, servioadmin)
admin.site.register(EspesificacionServicio, servioEspesificasionadmin)
admin.site.register( Espesificaciondetalle, espesificacionDetalleadmin)