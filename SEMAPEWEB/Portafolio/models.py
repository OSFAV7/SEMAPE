from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class categorias(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    update  = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def _str_(self):
        return self.nombre

class empresasCliente(models.Model):
    empresa = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    update  = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='empresa'
        verbose_name_plural='empresas'
    
    def _str_(self):
        return self.nombre

class proyecto(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='Portafolio', null=True, blank=True)
    empresaCliente =models.ForeignKey(empresasCliente, on_delete= models.CASCADE)
    categorias = models.ManyToManyField(categorias)
    created = models.DateField(auto_now_add=True)
    update  = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
    
    def _str_(self):
        return self.titulo
