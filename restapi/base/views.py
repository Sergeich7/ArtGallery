from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer, ProductSerializer
from .serializers import TechniqueSerializer, AuthorSerializer
from .serializers import IdListSerializer

from art.models import Category, Product, Technique, Author


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TechniqueViewSet(ReadOnlyModelViewSet):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#class IdListProductsView(ListAPIView):
#    serializer_class = IdListSerializer
#
#    def get_queryset(self):
#        qs = Product.objects.all()
#        for key, value in self.kwargs.items():
#            if 'fn' in key:
#                qs = qs.filter(
#                    **{value: self.kwargs.get(key.replace("fn", "pk"))})
#        return qs


class ListIdProductsView(ListAPIView):
    serializer_class = IdListSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        # author=1/category=4/technique=5
        for p in self.kwargs.get('filter', '/').split('/'):
            try:
                (key, value) = p.split('=')
            except ValueError:
                pass
            else:
                if key in ['author', 'category', 'technique']:
                    qs = qs.filter(**{key: value})
        return qs
