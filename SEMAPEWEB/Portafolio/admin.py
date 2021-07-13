from django.contrib import admin
from .models import categorias, empresasCliente, proyecto

# Register your models here.
class categoriasAdmin(admin.ModelAdmin):
    search_fields= ['nombre']
    list_display = ['nombre', 'update']
    readonly_fields=('created','update')

class empresaClienteAdmin(admin.ModelAdmin):
    search_fields= ['empresa']
    list_display = ['empresa', 'update']
    readonly_fields=('created','update')

class proyectoAdmin(admin.ModelAdmin):
    search_fields= ['titulo']
    list_display = ['titulo', 'update']
    readonly_fields=('created','update')

admin.site.register(categorias, categoriasAdmin)
admin.site.register(empresasCliente, empresaClienteAdmin)
admin.site.register(proyecto, proyectoAdmin)