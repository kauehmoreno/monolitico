# -- coding: utf-8 --
from django.conf.urls import url
from .views import MainPageView, SingleArticleView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='home'),
    url(
        r'materia/(?P<uuid>[^/]+)/(?P<slug>[\w-]+).html$',
        SingleArticleView.as_view(),
        name='single_article'
    )
]
