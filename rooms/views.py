from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from profile_api.models import UserProfile
from .models import Room
from .models import RoomCategory
from .models import Customer
from .models import Invoice
from .serializers import RoomSerializer
from .serializers import RoomCategorySerializer, RoomCategoryUpdateSerializer, RoomCategoryCreateSerializer
from .serializers import CustomerSerializer
from .serializers import InvoiceSerializer
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    )


# Create your views here.
# GET, POST, and OPTIONS
class RoomCategoryList(generics.ListCreateAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields= ['name','unique_color']
    name = 'roomcategory-list'



# PUT
class RoomCategoryUpdate(generics.RetrieveUpdateAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategoryUpdateSerializer
    name = 'roomcategory-update'


# POST
class RoomCategoryCreate(generics.CreateAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategoryCreateSerializer
    name= 'roomcategory-create'


# GET, PUT, PATCH, DELETE, and OPTIONS
class RoomCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    name = 'roomcategory-detail'


# GET, POST, and OPTIONS
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    name = 'room-list'

    def perform_create(self, serializer):
        serializer.save(creator= UserProfile.objects.first())


# GET, PUT, PATCH, DELETE, and OPTIONS
class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    name = 'room-detail'


# GET, POST, and OPTIONS
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'


# GET, PUT, PATCH, DELETE, and OPTIONS
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-detail'


# GET, POST, and OPTIONS
class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    name = 'invoice-list'


# GET, PUT, PATCH, DELETE, and OPTIONS
class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    name = 'invoice-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'room-categories': reverse(RoomCategoryList.name, request=request),
            'rooms': reverse(RoomList.name, request=request),
            'customers': reverse(CustomerList.name, request=request),
            'invoices': reverse(InvoiceList.name, request=request)

        })
