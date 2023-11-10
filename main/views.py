from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product
# Create your views here.

@api_view(['GET'])
def apiOverview (request):
    api_urls ={
        'list': '/product_list/',
        'detail view': '/product-detail/<int:id>',
        'create': '/product-create/',
        'update': '/product-update/<int:id>',
        'delete': '/product-delete/<int:id>',
    }

    return Response(api_urls)


#get all information i have added from the admin panel
@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

#show single product
@api_view(['GET'])
def viewproduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many = False)
    return Response(serializer.data)

#create product
@api_view(['POST'])
def createproduct(request):
    serializer = ProductSerializer(data = request.data)

    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)

#update product
@api_view(['POST'])
def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete product
@api_view(['GET'])
def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response('Items deleted successfully')