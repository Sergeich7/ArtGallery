from django.urls import include, path
from rest_framework import routers

from .base import CategoriesViewSet, TechniqueViewSet
from .base import AuthorViewSet, ProductViewSet, IdListProductsView

from .users import SignUpUserView, ChangePasswordUserView

router = routers.SimpleRouter()

router.register(r'cats', CategoriesViewSet)
router.register(r'techs', TechniqueViewSet)
router.register(r'auths', AuthorViewSet)
router.register(r'prods', ProductViewSet)

urlpatterns = [

    # Регистрация, аутентификация и изменение пользователя
    path('users/signup/', SignUpUserView.as_view()),
    path('users/changepassword/', ChangePasswordUserView.as_view()),
    path('users/', include('rest_framework.urls')),

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

    # Выборка из базы подуктов по различным параметрам
    # http://127.0.0.1:8000/api/filter/category/2/ - все продукты 2ой категории
    # http://127.0.0.1:8000/api/filter/category/2/technique/4/ - все продукты 2ой категории и 4ой техники
    # http://127.0.0.1:8000/api/filter/category/2/technique/1/ - все продукты 2ой категории и 1ой техники
    # http://127.0.0.1:8000/api/filter/author/1/category/4/technique/5/ - все продукты 1uj автора 2ой категории и 1ой техники
    # http://127.0.0.1:8000/api/filter/author/1/category/4/technique/5/
    path('filter/<slug:fn1>/<int:pk1>/<slug:fn2>/<int:pk2>/<slug:fn3>/<int:pk3>/', IdListProductsView.as_view()),
    path('filter/<slug:fn1>/<int:pk1>/<slug:fn2>/<int:pk2>/', IdListProductsView.as_view()),
    path('filter/<slug:fn1>/<int:pk1>/', IdListProductsView.as_view()),
    path('filter/', IdListProductsView.as_view()),

]

