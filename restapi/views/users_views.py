from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import CreateModelMixin

from django.contrib.auth import get_user_model

from .users_serializers import SignUpSerializer


class SignUpUserView(CreateModelMixin, GenericViewSet):
    """Регистрация нового пользователя."""

    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = SignUpSerializer
