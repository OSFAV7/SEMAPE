from django.contrib import admin

# Register your models here.

from .models import Servicio

class servioadmin(admin.ModelAdmin):
    readonly_fields= ('created','update')

admin.site.register(Servicio, servioadmin)