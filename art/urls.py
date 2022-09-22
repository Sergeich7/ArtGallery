from django.urls import include, path, re_path

from art.views import ClearTextView, IndexView, DetailView, ContactFormView

app_name = 'art'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cat/<int:pk>/', IndexView.as_view(), name='category'),
    re_path('(?P<pk>[0-9]+)/\\Z', DetailView.as_view(), name='detail'),
    re_path(
        '(?P<pk>[0-9]+)/del/(?P<dc>[0-9]+)\\Z', DetailView.as_view(),
        name='delete-comment'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('thanks/', ClearTextView.as_view(
                        template_name='art/thanks.html'), name='thanks'),
]
