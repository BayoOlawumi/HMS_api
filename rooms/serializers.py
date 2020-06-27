from .models import Room
from rest_framework import serializers
from .models import RoomCategory
from .models import Customer
from .models import Invoice

'''Room Category Serializers'''


class RoomCategorySerializer(serializers.HyperlinkedModelSerializer):
    # Displays all the rooms in the category
    """rooms = serializers.HyperlinkedRelatedField(
        # rooms is the name used for the related field while creating the mode room
        many=True,
        read_only=True,
        view_name='room-detail',
    )
    """
    rooms = serializers.SlugRelatedField(
        # rooms is the name used for the related field while creating the mode room
        many=True,
        read_only=True,
        slug_field='number',
    )

    class Meta:
        model = RoomCategory
        fields = (
            'pk',
            'url',
            'name',
            'unique_color',
            'rooms',
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
            'unique_color',
        )


'''Room Serializer'''


class RoomSerializer(serializers.ModelSerializer):
    # Displays the category of the Room
    category = serializers.SlugRelatedField(slug_field='name', queryset=RoomCategory.objects.all())
    creator = serializers.ReadOnlyField(source='creator.name')

    class Meta:
        model = Room
        fields = (
            'number',
            'category',
            'status',
            'condition',
            'creator',
        )


'''Customer Serializer'''


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    invoices = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='invoice-detail',
        read_only=True,
    )

    class Meta:
        model = Customer
        fields = (
            'fullname',
            'address',
            'phone_number',
            'email_address',
            'invoices',
        )


'''Invoices Serializer'''


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    # Displays the Customer with the Invoice
    customer = serializers.HyperlinkedRelatedField(many=False, view_name='customer-detail', read_only=True)
    # Displays the Room with the Invoice, showing only the number
    # room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='number')

    # Display all the details for the related drone
    room = RoomSerializer()

    class Meta:
        model = Invoice
        fields = (
            'url',
            'date_issued',
            'amount',
            'details',
            'room',
            'customer',
        )
