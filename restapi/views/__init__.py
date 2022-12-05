from .api_views import CategoriesViewSet, TechniqueViewSet, AuthorViewSet
from .api_views import ProductViewSet, IdListProductsView
from .users_views import SignUpUserView

__all__ = [
    'CategoriesViewSet', 'TechniqueViewSet', 'ProductViewSet', 'AuthorViewSet',
    'SignUpUserView', 'IdListProductsView',
    ]
