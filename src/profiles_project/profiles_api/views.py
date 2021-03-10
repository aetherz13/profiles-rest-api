from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status
from rest_framework import viewsets
class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer



    def get(self,request,format=None):
        """Return a list of APIView features"""

        an_apiview = [
        'uses http methods as func (get post patch put delete)',
        'it is similiar to a traditional django view',
        'gives u the most control over ur logic',
        'it mapped mannually to urls'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handles updating an object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request , only update fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API VIEWSET"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset = [

        'uses actions(list,create,retrieve,update,partial_update)',
        'automatically maps to urls using routers',
        'provides more functionality with less code'

        ]
        return Response({'message':'Hello','a viewset':a_viewset})

    def create(self,request):
        """create a hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """handles getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """handles updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handles removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """handles creating reading and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()





















# Create your views here.
