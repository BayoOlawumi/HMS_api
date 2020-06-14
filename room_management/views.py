from django.http import HttpResponse
from django.shortcuts import render
from .models import Roomclass
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RoomclassSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
class room_managementView(APIView):
    """Testing API View"""
    def get(self,request,format=None):
        """Response given when a GET request is made"""
        val=Roomclass.objects.all()
        return Response(RoomclassSerializer(val, many=True).data)
    def post(self,request):
        """Response to POST action"""
        serialized_data=RoomclassSerializer(data=request.data)
        #user_parsed = JSONParser().parse(serialized_data)
        if(serialized_data.is_valid()):
            #user_parsed.save()
            serialized_data.save()
            name=serialized_data.data.get('name')
            message="Hello {0}".format(name)
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        """Response to PUT action"""
        try:
            room_class = Roomclass.objects.get(pk=pk)
        except room_class.DoesNotExist():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        roomclass_serialized=RoomclassSerializer(room_class,data=room_class)
        if(roomclass_serialized.is_valid()):
            roomclass_serialized.save()
            return Response(roomclass_serialized.data)
        else:
            return Response(roomclass_serialized.errors,status=status.HTTP_400_BAD_REQUEST)

