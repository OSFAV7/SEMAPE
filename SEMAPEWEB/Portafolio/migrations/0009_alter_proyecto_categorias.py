# Generated by Django 3.2.5 on 2021-07-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0008_auto_20210715_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='categorias',
            field=models.ManyToManyField(related_name='categorias', to='Portafolio.categorias'),
        ),
    ]