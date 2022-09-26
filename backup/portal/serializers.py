
from .models import Portals
from rest_framework import serializers


class PortalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portals
        fields = '__all__'

# class ThingSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(ThingSerializer, self).__init__(many=many, *args, **kwargs)

#     class Meta:
#         model = Portals
#         fields ='__all__'
