from django.contrib import admin

# Register your models here.

from .models import Servicio, EspesificacionServicio, Espesificaciondetalle, BloqueServicio, AreaServicio, DetallesArea

class areadeservicio(admin.ModelAdmin):
    search_fields= ['area']
    list_display = ['area', 'update']
    readonly_fields= ('created','update')

class detalledearea(admin.ModelAdmin):
    search_fields= ['detalle', 'area__area']
    list_display = ['detalle', 'area', 'realisable', 'update']
    readonly_fields= ('created','update')


class bloquedeservicio(admin.ModelAdmin):
    search_fields= ['titulo']
    list_display = ['titulo', 'area', 'update']
    readonly_fields= ('created','update')

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
    search_fields= ['detalle', 'espesificacion__titulo']
    list_display = ['espesificacion','detalle', 'update']
    readonly_fields= ('created','update')

admin.site.register(Servicio, servioadmin)
admin.site.register(EspesificacionServicio, servioEspesificasionadmin)
admin.site.register( Espesificaciondetalle, espesificacionDetalleadmin)
admin.site.register(BloqueServicio, bloquedeservicio)
admin.site.register(AreaServicio, areadeservicio)
admin.site.register(DetallesArea, detalledearea)