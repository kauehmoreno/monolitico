# -#- coding:utf-8 -*-
from __future__ import unicode_literals
import json
from django.contrib import admin
from django.db import models
from uuid import uuid4
from django.core.urlresolvers import reverse

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
    corpo = models.TextField('Corpo da matéria', blank=True)

    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'
        ordering= ['data_publicacao']

    def __str__(self):
        return 'Materia: {}'.format(self.slug)

    def permalink(self):
        return reverse(
            'single_article',
            kwargs={
                'uuid':self._id,
                'slug': self.slug
            }
        )


    def to_dict(self):
        return dict(zip(
            [
                'titulo', 'data_publicacao', 'data_criacao', 'data_modificacao',
                'subtitulo', 'cover', 'uuid', 'corpo', 'slug'
            ],
            [
                self.titulo, self.data_publicacao.strftime('%Y-%m-%d %H:%M:%S'),
                self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
                self.data_modificacao.strftime('%Y-%m-%d %H:%M:%S'),
                self.subtitulo if self.subtitulo else '', self.cover.name,
                str(self._id), self.corpo if self.corpo else '', self.slug
            ]
        ))

    def to_dict_home(self):
        return dict(zip(
            [
                'id','titulo', 'subtitulo', 'corpo','slug', 'cover',
                'data_publicacao'
            ],
            [
                self._id, self.titulo, self.subtitulo, self.corpo, self.slug,
                self.cover, self.data_publicacao
            ]
        ))

def integrate_all(modeladmin, request, queryset):
    for materia in queryset:
        materia.save()

integrate_all.short_description = 'Integração com Microserviço'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
    search_fields = ('titulo', 'subtitulo', 'data_criacao', 'slug')
    actions = [integrate_all]
