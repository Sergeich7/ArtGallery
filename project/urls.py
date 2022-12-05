from django.contrib import admin
from django.urls import include, path

from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

from django.views.generic.base import TemplateView, RedirectView

from django.conf.urls.static import static

from django.conf import settings
#from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL
#from django.contrib.staticfiles.storage import staticfiles_storage


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('static/<path:path>', never_cache(serve)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path('api/', include('restapi.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"),
    ),
    path('', include('art.urls')),
]
