from __future__ import unicode_literals

from django.apps import AppConfig


class MateriaConfig(AppConfig):
    name = 'materia'

    def ready(self):
        import materia.utils.signals
