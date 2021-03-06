# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo da mat\xe9ria')),
                ('subtitulo', models.CharField(blank=True, max_length=255, verbose_name='Subtitulo')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='cover', verbose_name='Imagem Cover')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('data_modificacao', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('data_publicacao', models.DateTimeField(verbose_name='Publicado em')),
                ('slug', models.SlugField(max_length=255, verbose_name='Permalink da mat\xe9ria')),
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id da mat\xe9ria')),
            ],
            options={
                'ordering': ['data_publicacao'],
                'verbose_name': 'Mat\xe9ria',
                'verbose_name_plural': 'Mat\xe9rias',
            },
        ),
    ]
