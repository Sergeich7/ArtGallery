from rest_framework import serializers

from art.models import Category, Product, Technique, Author


class CategorySerializer(serializers.ModelSerializer):
    category_products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = Category
        fields = ('id', 'title', 'category_products')


class TechniqueSerializer(serializers.ModelSerializer):
    technique_products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = Technique
        fields = ('id', 'title', 'technique_products')


class AuthorSerializer(serializers.ModelSerializer):
    author_products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = Author
        fields = ('id', '__str__', 'last_name', 'author_products')


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.__str__')
    category = serializers.ReadOnlyField(source='category.title')
    technique = serializers.ReadOnlyField(source='technique.title')
    thumb = serializers.CharField(source='thumbnail')

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'thumb', 'category', 'technique',
            'author', 'description',)


class IdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',)
