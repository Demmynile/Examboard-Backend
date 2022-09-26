
from .models import Portals,BECE,JSS3
import uuid
from rest_framework import serializers


class PortalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portals
        fields = '__all__'

class BeceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BECE
        fields = [ 'adminemail','SchoolTypeId','Payeremail','SchoolName','SchoolType','quota','uniquecode','LgaId','PayerName','quota2','LgaName']
class BeceSerializerd(serializers.ModelSerializer):

    class Meta:
        model = BECE
        fields =  '__all__'
class Jss3Serializerd(serializers.ModelSerializer):

    class Meta:
        model = JSS3
        fields =  '__all__'

class Jss3Serializer(serializers.ModelSerializer):

   class Meta:
        model = JSS3
        fields = [ 'ClosingDate','StartingDate','SchoolTypeId','SchoolName','SchoolType','SchoolId','quota','uniquecode','LgaId','LgaName']
class BeceSerializers(serializers.ModelSerializer):

    class Meta:
        model = BECE
        fields = [ 'ClosingDate','StartingDate','SchoolTypeId','SchoolName','SchoolType','SchoolId','quota','uniquecode','LgaId','LgaName']

class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)
# class ThingSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(ThingSerializer, self).__init__(many=many, *args, **kwargs)

#     class Meta:
#         model = Portals
#         fields ='__all__'
