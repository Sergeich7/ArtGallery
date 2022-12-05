from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.generics import ListAPIView

from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model

from .serializers import CategorySerializer, ProductSerializer
from .serializers import TechniqueSerializer, AuthorSerializer
from .serializers import IdListSerializer, SignUpSerializer

from art.models import Category, Product, Technique, Author

from rest_framework.permissions import AllowAny, IsAuthenticated


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


class IdListProductsView(ListAPIView):
    serializer_class = IdListSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        for key, value in self.kwargs.items():
            if 'fn' in key:
                qs = qs.filter(
                    **{value: self.kwargs.get(key.replace("fn", "pk"))})
        return qs


class SignUpUserView(CreateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = SignUpSerializer
