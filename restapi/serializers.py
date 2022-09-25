from rest_framework import serializers
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

    class Meta:

        model = Product
        fields = ('id', 'title', 'thumbnail', 'category', 'technique',
            'author', 'description',)


class IdListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ('id',)


