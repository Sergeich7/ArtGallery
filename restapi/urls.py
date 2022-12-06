from django.urls import include, path
from rest_framework import routers

from .base import CategoriesViewSet, TechniqueViewSet
from .base import AuthorViewSet, ProductViewSet, ListIdProductsView
#from .base import IdListProductsView

from .users import SignUpUserView, ChangePasswordUserView
from .users import EditUserView, DeleteUserView

#from .views import api_root
from .views import APIRootView

urlpatterns = [
    path('', APIRootView.as_view(), name='index'),
#    path('', api_root, name='api-root'),

    # Регистрация, аутентификация и изменение пользователя
    path('users/signup/', SignUpUserView.as_view(), name='users-signup'),
    path('users/edit/', EditUserView.as_view(), name='users-edit'),
    path('users/delete/', DeleteUserView.as_view(), name='users-delete'),
    path('users/changepassword/', ChangePasswordUserView.as_view(), name='users-changepassword'),
    path('users/', include('rest_framework.urls', namespace='rest_framework')),

    # Выборка из базы продуктов по различным параметрам - другой формат
    # http://127.0.0.1:8000/api/list - все продукты
    # http://127.0.0.1:8000/api/list/category=2/ - все продукты 2ой категории
    # http://127.0.0.1:8000/api/list/category=2/technique=4/ - все продукты 2ой категории и 4ой техники
    # http://127.0.0.1:8000/api/list/category=2/technique=1/ - все продукты 2ой категории и 1ой техники
    # http://127.0.0.1:8000/api/list/author=1/category=4/technique=5/ - все продукты 1го автора 2ой категории и 1ой техники
    path('list<path:filter>', ListIdProductsView.as_view(), name='products-id-list'),

    # Выборка из базы - таблица целиком или детали
    # http://127.0.0.1:8000/api/cats/
    # http://127.0.0.1:8000/api/techs/
    # http://127.0.0.1:8000/api/auths/
    # http://127.0.0.1:8000/api/prods/
    # http://127.0.0.1:8000/api/cats/1/
    # http://127.0.0.1:8000/api/techs/1/
    # http://127.0.0.1:8000/api/auths/1/
    # http://127.0.0.1:8000/api/prods/1/

    path('cats/', CategoriesViewSet.as_view({'get': 'list', }), name='categories-list'),
    path('cats/<int:pk>/', CategoriesViewSet.as_view({'get': 'retrieve', }), name='categories-detail'),

    path('techs/', TechniqueViewSet.as_view({'get': 'list', }), name='technique-list'),
    path('techs/<int:pk>/', TechniqueViewSet.as_view({'get': 'retrieve', }), name='technique-detail'),

    path('auths/', AuthorViewSet.as_view({'get': 'list', }), name='author-list'),
    path('auths/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve', }), name='author-detail'),

    path('prods/', ProductViewSet.as_view({'get': 'list', }), name='product-list'),
    path('prods/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', }), name='product-detail'),

]

