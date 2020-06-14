from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status

from .models import Product, Category
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.

""" index view to the Sales API

This shows the list of all Sales made
Did not use JSONResponse to allow us work with other 
data that are not necessarily JSON 

"""

"""
This is a decorator that help restrict the function product_list to GET and POST request
If a request like DELETE is sent, the appropriate response is given without dishing out 
sensitive information
"""


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        list_of_product = Product.objects.all()
        serialized_products = ProductSerializer(list_of_product, many=True)
        return Response(serialized_products.data)

    elif request.method == 'POST':
        new_product_serialized = ProductSerializer(data=request.data)
        if new_product_serialized.is_valid():
            new_product_serialized.save()
            return Response(new_product_serialized.data, status = status.HTTP_201_CREATED)
        else:
            return Response(new_product_serialized.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialized_product = ProductSerializer(product)
        return Response(serialized_product.data, status = status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serialized_product = ProductSerializer(product)
        if serialized_product.is_valid():
            serialized_product.save()
            return Response(serialized_product.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serialized_product.errors, status = status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status = status.HTTP_200_OK)




"""class SalesList(APIView):

    def get(self, request, format=None):
        an_apiview = [
            "URLs for APIVIEWs are mapped manually",
            "God is always good to me",
            "I love the man of galilee"
        ]
        return Response({"hello": "Message", "apiView": an_apiview})
        
 """
