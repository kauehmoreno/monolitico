# -- coding: utf-8 --
import requests
import json
import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from materia.models import Materia
from django.conf import settings

@receiver(post_save, sender=Materia)
def materia_save_actions(sender, **kwargs):
    instance = kwargs.get('instance')
    host = '{}/insert/'.format(settings.MICROSERVICO_HOST_INTEGRATION)
    try:
        r = requests.post(
            host,
            data = instance.to_dict()
        )
    except Exception as e:
        msg = 'Não foi possível enviar os dados à applicacao microservico {}'
        logging.error(msg.format(e))



@receiver(post_delete, sender=Materia)
def materia_delete_actions(sender, **kwargs):
    instance = kwargs.get('instance')
    host = '{}/delete/'.format(settings.MICROSERVICO_HOST_INTEGRATION)

    uuid = str(instance._id)

    try:
        r = requests.post(
            host,
            data = json.dumps({'uuid': uuid})
        )
    except Exception as e:
        msg = 'Ocorreu um erro ao enviar objeto à aplicacao microservico: {}'
        logging.error(msg.format(e))

