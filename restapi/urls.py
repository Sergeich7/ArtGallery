from django.urls import path

from .views import api_categories, api_techniques, api_products, api_authors
from .views import api_category_detail, api_technique_detail, api_product_detail, api_author_detail, api_id_list_products

# http://127.0.0.1:8000/api/cats/
# http://127.0.0.1:8000/api/techs/
# http://127.0.0.1:8000/api/auths/
# http://127.0.0.1:8000/api/prods/
#
# http://127.0.0.1:8000/api/cats/1/
# http://127.0.0.1:8000/api/techs/1/
# http://127.0.0.1:8000/api/auths/1/
# http://127.0.0.1:8000/api/prods/1/
#
# http://127.0.0.1:8000/api/filter/author/1/category/2/technique/4/

urlpatterns = [

    path('cats/<int:pk>/', api_category_detail),
    path('techs/<int:pk>/', api_technique_detail),
    path('auths/<int:pk>/', api_author_detail),
    path('prods/<int:pk>/', api_product_detail),

    path('cats/', api_categories),
    path('techs/', api_techniques),
    path('auths/', api_authors),
    path('prods/', api_products),

    # фильтры. можно комбинировать до 3х. порядок не важен
    # cat/2/ - все продукты 2ой категории
    # cat/2/tech/4/ - все продукты 2ой категории и 4ой техники
    # cat/2/tech/4/ - все продукты 2ой категории и 1ой техники
    # auth/1/cat/2/tech/4/ - все продукты 1uj автора 2ой категории и 1ой техники
    path('filter/<slug:fn1>/<int:pk1>/<slug:fn2>/<int:pk2>/<slug:fn3>/<int:pk3>/', api_id_list_products),
    path('filter/<slug:fn1>/<int:pk1>/<slug:fn2>/<int:pk2>/', api_id_list_products),
    path('filter/<slug:fn1>/<int:pk1>/', api_id_list_products),
    path('filter/', api_id_list_products),

]

