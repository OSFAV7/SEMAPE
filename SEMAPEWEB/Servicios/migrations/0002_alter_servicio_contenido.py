# Generated by Django 3.2.5 on 2021-07-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.TextField(max_length=1000),
        ),
    ]
