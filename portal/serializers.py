
from .models import Portals,BECE
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
class BeceSerializers(serializers.ModelSerializer):

    class Meta:
        model = BECE
        fields = [ 'ClosingDate','StartingDate','SchoolTypeId','SchoolName','SchoolType','SchoolId','quota','uniquecode','LgaId','LgaName']
    # def save(self, **kwargs):
    #     bece=BECE(
    #         ClosingDate="2022-09-90",
    #         StartingDate=self.validated_data['StartingDate'],
    #         # SchoolTypeId=self.validated_data['SchoolTypeId'],
    #         SchoolName="kkkkk",
    #         SchoolType="oepepep",
    #         quota=self.validated_data['quota'],
    #         # LgaId=self.validated_data['LgaId'],
    #         # SchoolId=self.validated_data['SchoolId'],
    #         LgaName =self.validated_data['LgaName '],
    #         # altPhone=self.validated_data['altPhone'],          
    #     )
    #     SchoolId=self.validated_data['SchoolId']
    #     LgaId=self.validated_data['LgaId']
    #     SchoolTypeId=self.validated_data['SchoolTypeId']
    #     bece.SchoolId= SchoolId+''+LgaId+''+SchoolTypeId
    #     SchoolType=self.validated_data['SchoolType']
    #     # x = uuid.uuid4().hex.upper()
    #     # b=0
    #     # genid=x[15:20]
    #     # # uniquecode=genid
    #     # print(genid)
    #     # print(genid)
    #     # print(SchoolType)
    #     # # if SchoolType == '1':
    #     # bece.uniquecode = genid
    #     x = uuid.uuid4().hex.upper()
    #     genid=x[10:20]
    #     bece.uniquecode="DIGI" + genid
    #     # elif SchoolType == '0':
    #     #     bece.uniquecode = b

    #     bece.save()
    #     return bece
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
