from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class categorias(models.Model):
    nombre = models.CharField('Nombre de la categoria',max_length=50)
    created = models.DateField('Fecha de creacion',auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion',auto_now=True)
    

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def __str__(self):
        return self.nombre

class empresasCliente(models.Model):
    empresa = models.CharField('Nombrre de la empresa',max_length=50)
    created = models.DateField('Fecha de registro',auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion',auto_now=True)

    class Meta:
        verbose_name='Empresa cliente'
        verbose_name_plural='empresas clientes'
    
    def __str__(self):
        return self.empresa

class proyecto(models.Model):
    titulo = models.CharField('Nombre del proyecto', max_length=50)
    contenido = models.TextField('Descripcion del protyecto', max_length=400)
    descripcionTrabajo = models.TextField('Descripcion del protyecto',null=True, blank=True, max_length=40000)
    imagen = models.ImageField('Imagen para mostrar', upload_to='Portafolio', null=True, blank=True)
    empresaCliente =models.ForeignKey(empresasCliente, on_delete= models.CASCADE)
    categorias = models.ManyToManyField(categorias, related_name='categorias')
    created = models.DateField('Fecha de registro', auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion', auto_now=True)

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
    
    def __str__(self):
        return self.titulo

class galeria(models.Model):
    proyectoPertenece = models.ForeignKey(proyecto, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre de la imagen',max_length=10, null=True, blank=True)
    imagen = models.ImageField('Imagen de galeria', upload_to='Galerias')
    created = models.DateField('Fecha de creacion',auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion',auto_now=True)

    class Meta:
        verbose_name='Galeria'
        verbose_name_plural='Galerias'
    
    def __str__(self):
        return self.nombre