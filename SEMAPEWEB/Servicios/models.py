from django.db import models

# Create your models here.



class EspesificacionServicio(models.Model):
    titulo = models.CharField('Nombre del servicio', max_length=50)
    cajadetexto=models.BooleanField('Llevara caja e texto?', null=True)
    created = models.DateField('Fecha de registro', auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion', auto_now=True)

    class Meta:
        verbose_name='espesificacion servicio'
        verbose_name_plural='espesificaciones de servicio'
    
    def __str__(self):
        return self.titulo

class Espesificaciondetalle(models.Model):
    espesificacion=models.ForeignKey( EspesificacionServicio, on_delete= models.CASCADE)
    detalle = models.CharField('detalle', max_length=50)
    created = models.DateField('Fecha de registro', auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion', auto_now=True)

    class Meta:
        verbose_name='espesificacion detalles'
        verbose_name_plural='espesificaciones detalles'
    
    def __str__(self):
        return self.detalle

class Servicio(models.Model):
    titulo = models.CharField('Nombre del servicio', max_length=50)
    contenido = models.TextField('Descripcion el servicio', max_length=1000)
    servicioEspesificacion=models.ManyToManyField(EspesificacionServicio)
    imagen = models.ImageField('Imagen para mostar', upload_to='servicios')
    created = models.DateField('Fecha de registro', auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion', auto_now=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo




