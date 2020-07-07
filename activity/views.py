from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import ActivityUserSerializer
from rest_framework import status
from rest_framework.response import Response

from activity.services.all_activity_service import AllActivityService

# Create your views here.

def index(request):
    return HttpResponse("Hello, world")


class ActivityUserView(APIView):
    """
    Post the data User and Activity(with time duration)
    """
    def post(self, request, format=None):
        serializer = ActivityUserSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityView(APIView):
    """
    Get all the Activity Data
    """
    def get(self, request, format=None):
        AllActivityService_obj = AllActivityService()
        all_activity_data = AllActivityService_obj.get_all_activity()
        return Response(all_activity_data, status=status.HTTP_200_OK)