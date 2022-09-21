from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from django.core import serializers as core_serializers
from rest_framework.viewsets import ViewSet
from payment.serializers import PaymentSerializer
from payment.models import Payment
from django.http import HttpResponse
import uuid
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from portal.utils import Util


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'transactionRef'

    @action(detail=False, methods=["POST"])
    def generate_pin(self, request):
        ExamType = request.data.get('ExamType')
        transactionRef = request.data.get('transactionRef')
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        amount = request.data.get('amount')
        id = request.data.get('id')
        pinNo = (request.data.get('pinNo'))
        bulknumber = int(request.data.get('bulknumber'))
        bulk_list = list()
        x = uuid.uuid4()
        pinn = x.time_low
        uty = hex(int(pinn))[2:]
        if(ExamType == '1'):
            amount = bulknumber * 4
            examName = 'M C'
        elif(ExamType == '2'):
            amount = bulknumber * 3
            examName = 'P S'
        for _ in range(bulknumber):
            pinNo = "LAG" + uuid.uuid4().hex.upper()
            transactionRef = "LAGEDU" + uty
            bulk_list.append(
                Payment(transactionRef=transactionRef, ExamType=ExamType, pinNo=pinNo, amount=amount, name=name, email=email, phone=phone, bulknumber=bulknumber))

            email_body = examName + "-" + pinNo
            data = {"email_body": email_body, "to_email": email,
                    "email_subject": "Acquisition of the Invoice Number"}

            # send the email
            Util.send_email(data)

        query = Payment.objects.bulk_create(bulk_list)
        result = core_serializers.serialize('json', query)
        # result = serializers.serialize('json', query)
        return HttpResponse(result, content_type='application/json')

    @action(detail=False, methods=["GET"])
    def getByTransId(self, request,):
        transactionRef = request.query_params.get("transactionRef", None)
        numberref = Payment.objects.filter(transactionRef=transactionRef)
        result = core_serializers.serialize('json', numberref)
        return HttpResponse(result, content_type='application/json')
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
