from django.urls import include, path
from rest_framework import routers

from .views import CategoriesViewSet, TechniqueViewSet, SignUpUserView
from .views import AuthorViewSet, ProductViewSet, IdListProductsView

router = routers.SimpleRouter()

# http://127.0.0.1:8000/api/cats/
# http://127.0.0.1:8000/api/techs/
# http://127.0.0.1:8000/api/auths/
# http://127.0.0.1:8000/api/prods/
# http://127.0.0.1:8000/api/cats/1/
# http://127.0.0.1:8000/api/techs/1/
# http://127.0.0.1:8000/api/auths/1/
# http://127.0.0.1:8000/api/prods/1/

router.register(r'cats', CategoriesViewSet)
router.register(r'techs', TechniqueViewSet)
router.register(r'auths', AuthorViewSet)
router.register(r'prods', ProductViewSet)
router.register(r'users/create', SignUpUserView)

# http://127.0.0.1:8000/api/filter/author/1/category/4/technique/5/

urlpatterns = [

    path('users/', include('rest_framework.urls')),
    path('', include(router.urls)),
    # фильтры. можно комбинировать до 3х. порядок не важен
    # filter/cat/2/ - все продукты 2ой категории
    # filter/cat/2/tech/4/ - все продукты 2ой категории и 4ой техники
    # filter/cat/2/tech/4/ - все продукты 2ой категории и 1ой техники
    # filter/auth/1/cat/4/tech/5/ - все продукты 1uj автора 2ой категории и 1ой техники
    path('filter/<slug:fn1>/<int:pk1>/<slug:fn2>/<int:pk2>/<slug:fn3>/<int:pk3>/', IdListProductsView.as_view()),
    path('filter/<slug:fn1>/<int:pk1>/<slug:fn2>/<int:pk2>/', IdListProductsView.as_view()),
    path('filter/<slug:fn1>/<int:pk1>/', IdListProductsView.as_view()),
    path('filter/', IdListProductsView.as_view()),

]

