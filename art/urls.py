from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from art.views import IndexView, DetailView, ContactFormView
from .sitemaps import ArtSiteMaps

app_name = 'art'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),

    path('thanks/', TemplateView.as_view(
                        template_name='art/thanks.html'), name='thanks'),

    path('instruction/', TemplateView.as_view(
                        template_name='art/instruction.html'), name='instruction'),

    # фильтр по категориям и техникам (id или slug)
    # /cat/1/ /cat/vazy/ /tec/2/ /tec/dekupazh/
    re_path('(?P<filter>[a-z]+)/(?P<pk>[0-9]+)/\\Z', IndexView.as_view(), name='filter'),
    re_path('(?P<filter>[a-z]+)/(?P<slug>[-a-z0-9_]+)/\\Z', IndexView.as_view(), name='filter'),

    # детали работы по pk
    re_path('(?P<pk>[0-9]+)/\\Z', DetailView.as_view(), name='detail'),
    re_path(
        '(?P<pk>[0-9]+)/del/(?P<dc>[0-9]+)\\Z',
        DetailView.as_view(),
        name='delete-comment'),

    re_path(
        'sitemap.xml/{0,1}', sitemap, {'sitemaps': ArtSiteMaps}, name='sitemaps'),

    # детали работы по slug
    re_path(
        '(?P<slug>[-a-zA-Z0-9_!sitemap.xml]+)/\\Z',
        DetailView.as_view(),
        name='detail'),
    re_path(
        '(?P<slug>[-a-zA-Z0-9_!sitemap.xml]+)/del/(?P<dc>[0-9]+)\\Z',
        DetailView.as_view(),
        name='delete-comment'),

]
