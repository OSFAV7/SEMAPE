# Generated by Django 3.2.5 on 2021-07-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0004_auto_20210713_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='update',
            field=models.DateField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='empresascliente',
            name='update',
            field=models.DateField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='update',
            field=models.DateField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
    ]
