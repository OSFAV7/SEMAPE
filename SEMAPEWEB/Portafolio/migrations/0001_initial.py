# Generated by Django 3.2.5 on 2021-07-13 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='empresasCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField(max_length=1000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Portafolio')),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
                ('categorias', models.ManyToManyField(to='Portafolio.categorias')),
                ('empresaCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portafolio.empresascliente')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
    ]
