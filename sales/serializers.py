from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    SlugRelatedField,
)
import re
from .models import Product, Category

"""This is the serializer for Category Table
    
"""


class ProductCategorySerializer(HyperlinkedModelSerializer):
    products = HyperlinkedRelatedField(
        view_name='product-detail',
        many=True,
        read_only=True,

    )
    num_unique_color = SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'url',
            'products',
            'unique_color',
            'num_unique_color',
        )

    def get_num_unique_color(self, obj):
        return int(re.findall(r'\d+', obj.unique_color)[0])


""" Serializer for Product category


"""


class ProductSerializer(HyperlinkedModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'url',
                  'price',
                  'category',
                  'no_available',
                  'no_of_intake'
                  )

