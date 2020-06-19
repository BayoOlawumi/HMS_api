from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)
from .models import Product, Category

"""This is the serializer for Category Table
    
"""


class ProductCategorySerializer(ModelSerializer):
    """url = HyperlinkedIdentityField(
        view_name='sales:cat-list',
        )
    """
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'unique_color'
        )


""" Serializer for Product category


"""


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'no_available',
                  'no_of_intake'
                  )
