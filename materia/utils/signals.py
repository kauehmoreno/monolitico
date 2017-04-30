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

    def context_sender(context=None):
        host = '{}/insert/'.format(settings.MICROSERVICO_HOST_INTEGRATION)

        requests.post(
            host,
            data = json.dumps(context.to_dict())
        )

    def file_sender(context=None):
        if context.cover.name:
            requests.post(
                '{}/api/file_upload/'.format(settings.MICROSERVICO_BASE_HOST),
                files=({'file': open(context.cover.path)})
            )

    instance = kwargs.get('instance')
    try:
        context_sender(context=instance)
    except Exception as e:
        msg = 'Não foi possível enviar os dados à applicacao microservico {}'
        logging.error(msg.format(e))
    else:
        try:
            file_sender(context=instance)
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

