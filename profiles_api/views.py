from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


from profiles_api import serializers
from profiles_api import models
from profiles_api import permission

class HelloApiView(APIView):
    """Test APIViews"""


    serializer_class = serializers.HelloSerilaizer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP metthods as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',


            'Gives you the most control over yours application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request, pk=None):
        """Delete an object """
        return Response({'method':'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    
    serializer_class = serializers.HelloSerilaizer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            'USes action (list, create ,retrive, update, partial_update,destroy)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})
    
    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
    

    def retrive(self, request, pk=None):
        """Handle getting an object"""
        return Response ({'http_method': 'GET'})

    def update(self,request, pk=None):
        """Handle updating an object"""
        return Response ({'http_method': 'PUT'})

    
    def partial_update(self,request, pk=None):
        """Handle updating part of an object"""
        return Response ({'http_method': 'PATCH'}
        )

    
    def destroy(self,request, pk=None):
        """Handle removing an object"""
        return Response ({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):

    """Handle Creating and updating Profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
