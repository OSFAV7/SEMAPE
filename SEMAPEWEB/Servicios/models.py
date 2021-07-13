from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField('Nombre del servicio', max_length=50)
    contenido = models.TextField('Descripcion el servicio', max_length=1000)
    imagen = models.ImageField('Imagen para mostar', upload_to='servicios')
    created = models.DateField('Fecha de registro', auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion', auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo
