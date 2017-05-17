from django.contrib import admin
from materia.models import Materia, ArticleAdmin

admin.site.register(Materia, ArticleAdmin)
