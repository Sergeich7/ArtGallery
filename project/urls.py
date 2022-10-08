from django.contrib import admin
from django.urls import include, path

from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
#from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include('restapi.urls')),
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('art.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve))) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
