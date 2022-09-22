from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('art.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
]

