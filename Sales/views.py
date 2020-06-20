from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from django.db.models import Q
from .pagination import (
    ProductCategoryListOffsetPagination,
    ProductCategoryPagePagination,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .models import Product, Category
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductCategorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


# Create your views here.
# Handles Creation and List i.e GET, POST, OPTION
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'


class ProductCategoryList(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'product-category-list'
    filter_backends = [SearchFilter]
    search_fields = ['name', 'unique_color']
    # If I want to state the Limit the number of items to be displayed  and the offset
    # pagination_class = ProductCategoryListOffsetPagination
    # Arrange based on the number of page to be considered
    pagination_class = ProductCategoryPagePagination

    # Altering some of the model field in the hardcore way from here
    #def perform_create(self, serializer):
        #serializer.save(unique_color="WE WIN")


class ProductUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'


class ProductCategoryUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'category-detail'


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

"""

"""class SalesList(APIView):

    def get(self, request, format=None):
        an_apiview = [
            "URLs for APIVIEWs are mapped manually",
            "God is always good to me",
            "I love the man of galilee"
        ]
        return Response({"hello": "Message", "apiView": an_apiview})
        
 """
