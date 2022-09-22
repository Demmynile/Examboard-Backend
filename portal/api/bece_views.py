from tokenize import String
from django.db.models import query
from django.forms import DateField
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from django.core import serializers as core_serializers
from rest_framework.viewsets import ViewSet
from portal.models import BECE
from portal.serializers import BeceSerializer
from django.http import HttpResponse
import uuid
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser



class BeceViewSet(viewsets.ModelViewSet):

    queryset = BECE.objects.all()
    serializer_class = BeceSerializer
    lookup_field = 'transactionRef'

    @action(detail=False, methods=["POST"])
    def Upload(self, request):
        ClosingDate  = parse_date(request.data.get('ClosingDate'))
        StartingDate = parse_date(request.data.get('StartingDate'))
        SchoolTypeId  = request.data.get('SchoolTypeId')
        RequestId = request.data.get('RequestId')
        InvoiceNumber  = request.data.get('InvoiceNumber')
        SchoolName = request.data.get('SchoolName')
        SchoolType = request.data.get('SchoolType')
        quota = request.data.get('quota')
        ExamCost = request.data.get('ExamCost')
        uniquecode = request.data.get('uniquecode')
        LgaId = request.data.get('LgaId')
        SchoolId = request.data.get('SchoolId')
        # pinNo = (request.data.get('pinNo'))
        NumberOfCandidates  = int(request.data.get('NumberOfCandidates'))
        SchoolId = LgaId+''+SchoolTypeId +''+ SchoolId
        ExamCost = NumberOfCandidates * 4
        bulk_list = list()
        x = uuid.uuid4().hex.upper()
        b=0
        genid=x[15:20]
        uniquecode=genid
        print(genid)
        if SchoolType =='1':
            uniquecode = genid
            print(uniquecode)
        elif SchoolType =='0':
            uniquecode = b
        # for _ in range(bulknumber):
        #     pinNo = "LAG" + uuid.uuid4().hex.upper()
        #     transactionRef = "LAGEDU" + uty
        bulk_list.append(
                BECE(ClosingDate=ClosingDate, StartingDate=StartingDate, SchoolTypeId =SchoolTypeId , RequestId=RequestId, InvoiceNumber=InvoiceNumber, SchoolName=SchoolName , SchoolType=SchoolType, 
                 quota = quota , uniquecode=uniquecode, LgaId=LgaId,  ExamCost=  ExamCost, SchoolId = SchoolId  ,  NumberOfCandidates = NumberOfCandidates ))

            # email_body = examName + "-" + pinNo
            # data = {"email_body": email_body, "to_email": email,
            #         "email_subject": "Acquisition of the Invoice Number"}

            # # send the email
            # Util.send_email(data)

        query = BECE.objects.bulk_create(bulk_list)
        result = core_serializers.serialize('json', query)
        # result = serializers.serialize('json', query)
        return HttpResponse(result, content_type='application/json')

    # @action(detail=False, methods=["GET"])
    # def getByTransId(self, request,):
    #     transactionRef = request.query_params.get("transactionRef", None)
    #     numberref = Payment.objects.filter(transactionRef=transactionRef)
    #     result = core_serializers.serialize('json', numberref)
    #     return HttpResponse(result, content_type='application/json')
    # def get_queryset(self):
    #     transactionRef = self.kwargs['transactionRef']
    #     return Payment.objects.filter(transactionRef=transactionRef)
    # def get_object(self):
    #     return super().get_object()
    # def retrieve(self, request, transactionRef=None):
    #     queryset = Payment.objects.all()
    #     user = get_object_or_404(queryset, transactionRef=transactionRef)
    #     serializer = PaymentSerializer(Payment)
    #     return Response(serializer.data , content_type='application/json')

    # def get_queryset(self):
    #     queryset = Payment.objects.filter(transactionRef=self.kwargs['transactionRef'])
    #     return HttpResponse(query, content_type='application/json')
