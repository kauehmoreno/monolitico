# -#- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from uuid import uuid4

#TODO create signal to build slug automatically
class Materia(models.Model):

    titulo = models.CharField('Titulo da matéria', max_length=100, blank=False)
    subtitulo = models.CharField('Subtitulo', max_length=255, blank=True)
    cover = models.ImageField('Imagem Cover', upload_to='cover', blank=True, null=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_modificacao = models.DateTimeField('Modificado em', auto_now=True)
    data_publicacao = models.DateTimeField('Publicado em')
    slug = models.SlugField('Permalink da matéria', max_length=255)
    _id = models.UUIDField(
        'Id da matéria',
        primary_key=True,
        default=uuid4,
        editable=False
    )

    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'
        ordering= ['data_publicacao']

    def __str__(self):
        return 'Materia: {}'.format(self.slug)

    def permalink(self):
        pass
