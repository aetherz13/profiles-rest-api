from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Return a list of APIView features"""

        an_apiview = [
        'uses http methods as func (get post patch put delete)',
        'it is similiar to a traditional django view',
        'gives u the most control over ur logic',
        'it mapped mannually to urls'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
        
# Create your views here.
