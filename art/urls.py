from django.urls import include, path, re_path
from django.views.generic import TemplateView

from art.views import IndexView, DetailView, ContactFormView

app_name = 'art'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path('(?P<filter>[-a-zA-Z0-9_]+)/(?P<pk>[0-9]+)/\\Z', IndexView.as_view(), name='filter'),
#    path('<slug:sort>/<int:pk>/', IndexView.as_view(), name='filter'),
#    path('cat/<int:pk>/', IndexView.as_view(), name='category'),
#    path('tec/<int:pk>/', IndexView.as_view(), name='technique'),
    re_path('(?P<pk>[0-9]+)/\\Z', DetailView.as_view(), name='detail'),
    re_path(
        '(?P<pk>[0-9]+)/del/(?P<dc>[0-9]+)\\Z', DetailView.as_view(),
        name='delete-comment'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('thanks/', TemplateView.as_view(
                        template_name='art/thanks.html'), name='thanks'),
]
