from django.contrib import admin
from .models import categorias, empresasCliente, proyecto

# Register your models here.
class categoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

class empresaClienteAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

class proyectoAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(categorias, categoriasAdmin)
admin.site.register(empresasCliente, empresaClienteAdmin)
admin.site.register(proyecto, proyectoAdmin)