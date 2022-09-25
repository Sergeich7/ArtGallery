from rest_framework.response import Response
from rest_framework.decorators import api_view


from art.models import Category, Product, Technique, Author
from .serializers import CategorySerializer, ProductSerializer
from .serializers import TechniqueSerializer, AuthorSerializer
from .serializers import IdListSerializer

@api_view(['GET'])
def api_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_category_detail(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['GET'])
def api_techniques(request):
    if request.method == 'GET':
        categories = Technique.objects.all()
        serializer = TechniqueSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_technique_detail(request, pk):
    if request.method == 'GET':
        category = Technique.objects.get(pk=pk)
        serializer = TechniqueSerializer(category)
        return Response(serializer.data)

@api_view(['GET'])
def api_authors(request):
    if request.method == 'GET':
        categories = Author.objects.all()
        serializer = AuthorSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_author_detail(request, pk):
    if request.method == 'GET':
        category = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(category)
        return Response(serializer.data)

@api_view(['GET'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()[:20]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_product_detail(request, pk):
    if request.method == 'GET':
        category = Product.objects.get(pk=pk)
        serializer = ProductSerializer(category)
        return Response(serializer.data)

@api_view(['GET'])
def api_id_list_products(request, **kwargs):
    if request.method == 'GET':
        products = Product.objects.all()
        for key, value in kwargs.items():
            if 'fn' in key:
                products = products.filter(
                    **{value: kwargs.get(key.replace("fn", "pk"))})
        serializer = IdListSerializer(products, many=True)
        return Response(serializer.data)

