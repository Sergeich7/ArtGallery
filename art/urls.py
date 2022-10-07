from django.urls import include, path, re_path
from django.views.generic import TemplateView

from art.views import IndexView, DetailView, ContactFormView

app_name = 'art'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('thanks/', TemplateView.as_view(
                        template_name='art/thanks.html'), name='thanks'),

    # фильтр по категориям и техникам (id или slug)
    # /cat/1/ /cat/vazy/ /tec/2/ /tec/dekupazh/
    re_path('(?P<filter>[a-z]+)/(?P<pk>[0-9]+)/\\Z', IndexView.as_view(), name='filter'),
    re_path('(?P<filter>[a-z]+)/(?P<slug>[-a-z]+)/\\Z', IndexView.as_view(), name='filter'),

    # детали работы по pk
    re_path('(?P<pk>[0-9]+)/\\Z', DetailView.as_view(), name='detail'),
    re_path(
        '(?P<pk>[0-9]+)/del/(?P<dc>[0-9]+)\\Z', DetailView.as_view(),
        name='delete-comment'),

    # детали работы по slug
    re_path('(?P<slug>[-a-zA-Z0-9_]+)/\\Z', DetailView.as_view(), name='detail'),
    re_path(
        '(?P<slug>[-a-zA-Z0-9_]+)/del/(?P<dc>[0-9]+)\\Z', DetailView.as_view(),
        name='delete-comment'),
]
