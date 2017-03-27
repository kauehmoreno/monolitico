# -- coding: utf-8 --

from django.shortcuts import render
from django.views import generic
from materia.integration import DbBridge
from materia.models import Materia

class MainPageView(generic.ListView):

    template_name = 'materia/home.html'
    context_object_name = 'materias'
    #paginate_by = 20


    def get_queryset(self):
        return DbBridge.all(Materia)



