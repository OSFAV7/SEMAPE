from django.db import models

class banerscarousel(models.Model):
    titulo = models.CharField('Nombre del contenido', max_length=50)
    contenido = models.TextField('Descripcion del del contenido', max_length=400)
    imagen = models.ImageField('Imagen para mostrar', upload_to='Carousel', null=True, blank=True)
    created = models.DateField('Fecha de registro', auto_now_add=True)
    update  = models.DateField('Fecha de actualizacion', auto_now=True)

    class Meta:
        verbose_name='Baner_carousel'
        verbose_name_plural='Baner_carouseles'
    
    def __str__(self):
        return self.titulo

# Create your models here.
