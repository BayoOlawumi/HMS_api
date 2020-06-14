from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        """A keyword argument kwargs is where  you provide a name to the
        variable as you pass it into the function."""
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def UserProfileList(request):
    if (request.method == 'GET'):
        AllUserProfile = UserProfile.objects.all()
        AllUserProfile_Serialized = UserProfileSerializer(AllUserProfile, many=True)
        return JSONResponse(AllUserProfile_Serialized.data)
    elif (request.method == 'POST'):
        parsedData = JSONParser().parse(request)
        UserProfileParsed = UserProfileSerializer(data=parsedData)
        if (UserProfileParsed.is_valid()):
            UserProfileParsed.save()
            return JSONResponse(UserProfileParsed.data,
                                status=status.HTTP_201_CREATED
                                )
        else:
            return JSONResponse(UserProfileParsed.errors,
                                status=status.HTTP_400_BAD_REQUEST
                                )


@csrf_exempt
def UserProfileDetail(request, pk):
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if (request.method == "GET"):
        user_serialized = UserProfileSerializer(user_profile)
        return JSONResponse(user_serialized.data)
    elif (request.method == "PUT"):
        user_parsed = JSONParser().parse(request)
        user_serialized = UserProfileSerializer(user_profile, data=user_parsed)
        if (user_serialized.is_valid()):
            user_serialized.save()
            return JSONResponse(user_serialized.data)
        else:
            return JSONResponse(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_profile.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    """Using APIView"""


class ProfileUser(APIView):
    """Testing API views"""

    def get(self, request, format=None):
        an_apiview = [
            "URLs for APIVIEWs are mapped manually",
            "God is always good to me",
            "I love the man of galilee"
        ]
        return Response({"hello": "Message", "apiView": an_apiview})
