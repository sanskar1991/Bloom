from rest_framework import serializers

from .models import NetworkList, AddSubList, NewExposure


class NetworkSerializer(serializers.ModelSerializer):
    """Serializer for NetworkList model"""
    
    class Meta:
        model = NetworkList
        fields = ('id', 'subnet_name' ,'subnet_value')
        

class AddSubListSerializer(serializers.ModelSerializer):
    """Serializer for AddSubList model"""
    
    class Meta:
        model = AddSubList
        fields =('id', 'acc_subnet_name', 'acc_subnet_value')
    

class NewExpoSerializer(serializers.ModelSerializer):
    """Serializer for NewExposure model"""
    
    class Meta: 
        model = NewExposure
        fields =('id', 'new_sub_name', 'new_sub_value')