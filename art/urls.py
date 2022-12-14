from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from art.views import IndexView, DetailProdView, ContactFormView, FavoritesCMD
from art.views import session_to_json

from .sitemaps import ArtSiteMaps

app_name = 'art'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('favorites/', IndexView.as_view(), name='favorites'),
    # add/pk/ remove/pk/ clear/0/ 
    path('favorites/<slug:cmd>/<int:pk>/', FavoritesCMD.as_view(), name='favorites-cmd'),

    path('contacts/', ContactFormView.as_view(), name='contacts'),

    path(
        'thanks/',
        TemplateView.as_view(template_name='art/email_success.html'),
        name='thanks'),

    path('buy/<str:pk>', session_to_json, name='buy'),
    path(
        'payment_success/',
        TemplateView.as_view(template_name='art/payment_success.html'),
        name='payment_success'),
    path(
        'payment_cancel/',
        TemplateView.as_view(template_name='art/payment_cancel.html'),
        name='payment_cancel'),

    path(
        'instruction/',
        TemplateView.as_view(template_name='art/instruction.html'),
        name='instruction'),

    # фильтр по категориям, техникам или авторам
    re_path(
        '(?P<filter>[a-z]+)/(?P<slug>[-a-z0-9_]+)/\\Z',
        IndexView.as_view(),
        name='filter'),

    re_path(
        'sitemap.xml/{0,1}', sitemap, {'sitemaps': ArtSiteMaps},
        name='sitemaps'),

    # детали работы
    re_path(
        '(?P<slug>[-a-zA-Z0-9_!sitemap.xml]+)/\\Z',
        DetailProdView.as_view(),
        name='detail'),

    re_path(
        '(?P<slug>[-a-zA-Z0-9_!sitemap.xml]+)/del/(?P<dc>[0-9]+)\\Z',
        DetailProdView.as_view(),
        name='delete-comment'),
]
