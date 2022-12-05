from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from art.models import Category, Product, Technique, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class TechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technique
        fields = ('id', 'title')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', '__str__', 'last_name',)


class ProductSerializer(serializers.ModelSerializer):
    thumb = serializers.CharField(source='thumbnail.picture')

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'thumb', 'category', 'technique',
            'author', 'description',)


class IdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',)


UserModel = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

