from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView

from .base import CategoryViewSet, TechniqueViewSet
from .base import AuthorViewSet, ProductViewSet, ListIdProductsView

from .users import SignUpUserView, ChangePasswordUserView
from .users import EditUserView, DeleteUserView

from .views import APIRootView

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'cats', CategoryViewSet)
router.register(r'techs', TechniqueViewSet)
router.register(r'auths', AuthorViewSet)
router.register(r'prods', ProductViewSet)

urlpatterns = [
    path('', APIRootView.as_view(), name='index'),

    # Регистрация, аутентификация и изменение пользователя
    path('users/signup/', SignUpUserView.as_view(), name='users-signup'),
    path('users/edit/', EditUserView.as_view(), name='users-edit'),
    path('users/delete/', DeleteUserView.as_view(), name='users-delete'),
    path('users/changepassword/', ChangePasswordUserView.as_view(), name='users-changepassword'),
    path('users/', include('rest_framework.urls', namespace='rest_framework')),

    # Выборка из базы продуктов по различным параметрам
    # http://127.0.0.1:8000/api/list - все продукты
    # http://127.0.0.1:8000/api/list/category=2/ - все продукты 2ой категории
    # http://127.0.0.1:8000/api/list/category=2/technique=4/ - все продукты 2ой категории и 4ой техники
    # http://127.0.0.1:8000/api/list/category=2/technique=1/ - все продукты 2ой категории и 1ой техники
    # http://127.0.0.1:8000/api/list/author=1/category=4/technique=5/ - все продукты 1го автора 2ой категории и 1ой техники
    path('list/<path:filter>', ListIdProductsView.as_view(), name='products-id-list'),

    # Выборка из базы - таблица целиком или детали
    # http://127.0.0.1:8000/api/cats/
    # http://127.0.0.1:8000/api/techs/
    # http://127.0.0.1:8000/api/auths/
    # http://127.0.0.1:8000/api/prods/
    # http://127.0.0.1:8000/api/cats/1/
    # http://127.0.0.1:8000/api/techs/1/
    # http://127.0.0.1:8000/api/auths/1/
    # http://127.0.0.1:8000/api/prods/1/
    path('', include(router.urls)),

    # API документация
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
