# -- coding: utf-8 --
import logging
from django.views import generic
from materia.integration import DbBridge
from materia.models import Materia
from django.http import Http404


class MainPageView(generic.ListView):

    template_name = 'materia/home.html'
    context_object_name = 'materias'

    def get_queryset(self):
        return DbBridge.all(Materia)


class SingleArticleView(generic.TemplateView):

    template_name = 'materia/single_article.html'

    def get_context_data(self, **kwargs):
        context = super(SingleArticleView, self).get_context_data(**kwargs)
        try:
            context['materia'] = DbBridge.filter(
                slug=kwargs.get('slug'),
                resource_class=Materia,
                uuid=kwargs.get('uuid')
            )
            return context
        except Materia.DoesNotExist as e:
            logging.error(
                'Materia não encontrada - {} - uuid: {} slug:{}'.format(
                    e,
                    kwargs.get('uuid'),
                    kwargs.get('slug')
                )
            )
            raise Http404('Não foi possível encontrar está matéria')
