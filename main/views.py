from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)

    return Response(products_serializer.data)

@api_view(['GET'])
def product(request, id):
    product = Product.objects.get(id=id)
    product_serializer = ProductSerializer(product)

    return Response(product_serializer.data)