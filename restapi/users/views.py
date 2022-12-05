from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import SignUpSerializer, ChangeUserPasswordSerializer


class SignUpUserView(CreateAPIView):
    """Регистрация нового пользователя."""

    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user': 'created'}, status=status.HTTP_200_OK)


class ChangePasswordUserView(UpdateAPIView):
    """Изменение пароля пользователя."""

    permission_classes = [IsAuthenticated]
    serializer_class = ChangeUserPasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'pass': 'changed'}, status=status.HTTP_200_OK)


