from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticated

from .models import NetworkList, AddSubList, NewExposure
from .serializers import ( 
                          NetworkSerializer, 
                          AddSubListSerializer, 
                          NewExpoSerializer
)


# Create your views here.
class NetworkViewsets(viewsets.ModelViewSet):
    """View for Network List"""
    serializer_class = NetworkSerializer
    queryset = NetworkList.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'subnet_name',)


class AddSubViewsets(viewsets.ModelViewSet):
    """View for Network List"""
    serializer_class = AddSubListSerializer
    queryset = AddSubList.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'acc_subnet_name',)
    
    
class NewExpoViewsets(viewsets.ModelViewSet):
    """View for Network List"""
    serializer_class = NewExpoSerializer
    queryset = NewExposure.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'new_sub_name',)