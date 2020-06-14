from rest_framework import serializers
from .models import Product, Category



"""This is the serializer for Category Table
    
"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
                    'id',
                    'name',
                    'unique_color'
                )


""" Serializer for Product category


"""


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'no_available',
                  'no_of_intake'
                  )
