# -- coding: utf-8 --
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from materia.models import Materia

@receiver(post_save, sender=Materia)
def materia_actions(sender, **kwargs):
    #TODO irá notificar a rota da aplicação de microserviço
    pass


