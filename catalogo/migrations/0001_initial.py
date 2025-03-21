# Generated by Django 5.1.7 on 2025-03-16 05:29

import catalogo.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus_Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviacion', models.CharField(max_length=50, verbose_name='Abreviación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('color', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='El color debe estar en formato HEX, por ejemplo: #RRGGBB', regex='^#(?:[0-9a-fA-F]{3}){1,2}$')], verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Estatus de unidad',
                'verbose_name_plural': 'Estatus de unidades',
            },
        ),
        migrations.CreateModel(
            name='Lineas_Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=catalogo.models.custom_upload_logo_to, validators=[catalogo.models.validate_image_mime], verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Linea',
                'verbose_name_plural': 'Lineas',
            },
        ),
    ]
