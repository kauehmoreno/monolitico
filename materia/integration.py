# -#- coding:utf-8 -*-
from __future__ import unicode_literals
from materia.models import Materia


class  DbBridge(object):

    @classmethod
    def all(cls, resoure_class=None):
        if resoure_class is None:
            raise AttributeError(
                    'Resource class must be provied otherwise it wont be '
                    'possible to queryset Object'
            )
        materias = resoure_class.objects.all().order_by('-data_publicacao')
        for materia in materias:
            yield materia.to_dict()

    @classmethod
    def filter(cls, **kwargs):
        slug = kwargs.get('slug')
        resource_class = kwargs.get('resource_class')
        uuid = kwargs.get('uuid')
        try:
            return resource_class.objects.get(slug=slug, _id=uuid).to_dict()
        except Exception as e:
            raise e

