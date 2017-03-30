# -- coding: utf-8 --
import requests
import json
import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from materia.models import Materia

@receiver(post_save, sender=Materia)
def materia_save_actions(sender, **kwargs):
    instance = kwargs.get('instance')
    try:
        r = requests.post('http://localhost:8888/api/v1/insert/', data = instance.to_dict())
    except Exception as e:
        msg = 'Não foi possível enviar os dados à applicacao microservico {}'
        logging.error(msg.format(e))




