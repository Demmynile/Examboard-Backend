from tokenize import String
from urllib import response
from django.db.models import query
from django.forms import DateField
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from django.core.mail import send_mail
from django.core import serializers as core_serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ViewSet
from portal.models import BECE
from portal.serializers import BeceSerializer,CreateListMixin,BeceSerializers,BeceSerializerd
from django.http import HttpResponse
import uuid
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser



class BeceViewSet(CreateListMixin,viewsets.ModelViewSet):

    queryset = BECE.objects.all()
    serializer_class = BeceSerializers
    lookup_field = 'uniquecode'

    # @action(detail=False, methods=["POST"])
    # def Upload(self, request):
    #     ClosingDate  = parse_date(request.data.get('ClosingDate'))
    #     StartingDate = parse_date(request.data.get('StartingDate'))
    #     SchoolTypeId  = request.data.get('SchoolTypeId')
    #     RequestId = request.data.get('RequestId')
    #     InvoiceNumber  = request.data.get('InvoiceNumber')
    #     SchoolName = request.data.get('SchoolName')
    #     SchoolType = request.data.get('SchoolType')
    #     quota = request.data.get('quota')
    #     ExamCost = request.data.get('ExamCost')
    #     uniquecode = request.data.get('uniquecode')
    #     LgaId = request.data.get('LgaId')
    #     SchoolId = request.data.get('SchoolId')
    #     # pinNo = (request.data.get('pinNo'))
    #     NumberOfCandidates  = int(request.data.get('NumberOfCandidates'))
    #     SchoolId = LgaId+''+SchoolTypeId +''+ SchoolId
    #     ExamCost = NumberOfCandidates * 4
    #     bulk_list = list()
    #     x = uuid.uuid4().hex.upper()
    #     b=0
    #     genid=x[15:20]
    #     uniquecode=genid
    #     print(genid)
    #     if SchoolType =='1':
    #         uniquecode = genid
    #         print(uniquecode)
    #     elif SchoolType =='0':
    #         uniquecode = b
    #     # for _ in range(bulknumber):
    #     #     pinNo = "LAG" + uuid.uuid4().hex.upper()
    #     #     transactionRef = "LAGEDU" + uty
    #     bulk_list.append(
    #             BECE(ClosingDate=ClosingDate, StartingDate=StartingDate, SchoolTypeId =SchoolTypeId , RequestId=RequestId, InvoiceNumber=InvoiceNumber, SchoolName=SchoolName , SchoolType=SchoolType, 
    #              quota = quota , uniquecode=uniquecode, LgaId=LgaId,  ExamCost=  ExamCost, SchoolId = SchoolId  ,  NumberOfCandidates = NumberOfCandidates ))

    #         # email_body = examName + "-" + pinNo
    #         # data = {"email_body": email_body, "to_email": email,
    #         #         "email_subject": "Acquisition of the Invoice Number"}

    #         # # send the email
    #         # Util.send_email(data)

    #     query = BECE.objects.bulk_create(bulk_list)
    #     print (query)
    #     result = core_serializers.serialize('json', query)
    #     # result = serializers.serialize('json', query)
    #     return HttpResponse(result, content_type='application/json')

@api_view(['GET'])
# @permission_classes([IsAuthenticated&IsVendorUser])
def getBeceInfo(request,pk):
    bece = BECE.objects.filter(SchoolId=pk)
    serializer = BeceSerializerd(bece, many=True)
    return Response(serializer.data)
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayBece(request, pk):
    data = request.data
    bece = BECE.objects.get(SchoolId=pk)
    bece.quota = data['quota']
    bece.quota2 = data['quota2']

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    bece.adminemail = data['adminemail']
    bece.SchoolName = data['SchoolName']
    bece.LgaName = data['LgaName']


    bece.SchoolType = data['SchoolType']
    bece.Payeremail = data['Payeremail']
    bece.PayerName = data['PayerName']
    if(bece.quota2 <= bece.quota):
        bece.pinum = genid
        bece.save()
        serializer = BeceSerializer(bece, many=False)
        return Response(serializer.data)
       
    elif(bece.quota2 > bece.quota):

        send_mail(
        [bece.SchoolName],
        'attend to this school  above who is trying to enter more than what was allocated',
        'aakindele@sterlingtech.com.ng',
        [bece.adminemail],
        fail_silently=False,
       )
        return Response({'detail': 'you cant pay more than this quota'},
                 status=status.HTTP_400_BAD_REQUEST)

   

