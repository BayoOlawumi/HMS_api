from .models import Room
from rest_framework import serializers
from .models import RoomCategory
from .models import Customer
from .models import Invoice

'''Room Category Serializers'''


class RoomCategorySerializer(serializers.ModelSerializer):
    # Displays all the rooms in the category
    '''rooms = serializers.HyperlinkedRelatedField(
        # rooms is the name used for the related field while creating the mode room
        many=True,
        read_only=True,
        view_name='room-category'
    )'''

    class Meta:
        model = RoomCategory
        fields = (
            'pk',
            'name',
            'unique_color'
        )


class RoomCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = (
            'name',
            'unique_color',
        )

class RoomCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = (
            'name',
        )


'''Room Serializer'''


class RoomSerializer(serializers.ModelSerializer):
    # Displays the category of the Room
    room_category = serializers.SlugRelatedField(slug_field='name', queryset=RoomCategory.objects.all())

    class Meta:
        model = Room
        fields = (
            'url',
            'room_category',
            'number',
            'status',
            'condition',
        )


'''Customer Serializer'''


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    invoices = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="customer-invoices"
    )

    class Meta:
        model = Customer
        fields = (
            'url',
            'fullname',
            'address',
            'phone_number',
            'email_address',
            'invoices'
        )


'''Invoices Serializer'''


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    # Displays the Customer with the Invoice
    customer = serializers.SlugRelatedField(queryset=Customer.objects.all(), slug_field='fullname')
    # Displays the Room with the Invoice
    room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='status')

    class Meta:
        model = Invoice
        fields = (
            'url',
            'pk',
            'date_issued',
            'amount',
            'details',
            'room',
            'customer',
        )
