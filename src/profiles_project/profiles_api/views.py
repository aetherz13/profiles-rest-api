from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

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
# Create your views here.
