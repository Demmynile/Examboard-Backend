from pickle import OBJ
from turtle import title
from unittest import result
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from portal.models import Portals
from payment.models import Payment
from portal.serializers import PortalSerializer
from django.http import HttpResponse
from django.db import transaction
from rest_framework.decorators import action
from django.core import serializers
import random

import uuid
from django.db import transaction


# Create your views here.


class PortaltViewSet(viewsets.ModelViewSet):
    queryset = Portals.objects.all()
    serializer_class = PortalSerializer

    @action(detail=False, methods=["GET"])
    def getByPhoneNumber(self, request):
        phone = request.query_params.get("phone", None)
        query = Portals.objects.filter(phone=phone)
        result = serializers.serialize('json', query)
        return HttpResponse(result, content_type='application/json')

    # @action(detail=False, methods=["POST"])
    # def get_object(self, querysets=None):
    #   obj = super(PortaltViewSet, self).get_object(querysets=querysets)
    #   self.generate_pin(obj)
    #   return obj

    @action(detail=False, methods=["GET"])
    def getByEmail(self, request):
        email = request.query_params.get("email", None)
        query = Portals.objects.filter(email=email)
        result = serializers.serialize('json', query)
        return HttpResponse(result, content_type='application/json')


class PortaltViewSets(viewsets.ModelViewSet):
    queryset = Portals.objects.all()
    serializer_class = PortalSerializer

    # def create(self, request, *args, **kwargs):
    #   serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    #   serializer.is_valid(raise_exception=True)
    #   self.perform_create(serializer)
    #   headers = self.get_success_headers(serializer.data)
    #   return HttpResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    @action(detail=False, methods=['PATCH'])
    def updatepin(self, *args, **kwargs):
        portal_ids_dict = {}
        portal_bulk_update_list = []
        with transaction.atomic():
            for key, value in portal_ids_dict.items():
                port = Portals.objects.get(id=key)
                port.pinum = value
                portal_bulk_update_list.append(port)
               #  pinx= Portals.objects.filter(id=key).update(pinum=value)
                pinx = Portals.objects.bulk_update(
                    portal_bulk_update_list, ['pinum'])
                return HttpResponse(pinx, content_type='application/json')

    @action(detail=False, methods=["PUT"])
    def generate_pin(self, request):
        records = []
        # # generatedpin=
        # # pinx=request.data.get('id')
        # # pinum = generatedpin
        # for record , value in Portals.objects.all():
        #   value = "LAG"+ uuid.uuid4().hex.upper()
        #   port = Portals.objects.get(id=record)
        # #   port=int(request.data.get('id'))
        #   port.pinum=value
        #   records.append(port)
        # # query  = Payment.objects.bulk_create(bulk_list)
        # # result = serializers.serialize('json', query)
        # query = Portals.objects.bulk_update(records, ['pinum'])
        porty = Portals.objects.all()
        for portals in porty:
            portals.pinum = "LAG" + uuid.uuid4().hex.upper()
            query = Portals.objects.bulk_update(porty,  ['pinum'])
            return HttpResponse(query, content_type='application/json')

    # def partial_update(self, request, *args, **kwargs):
    #   serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    #   serializer.is_valid(raise_exception=True)
    #   self.partial_update(serializer)
    #   headers = self.get_success_headers(serializer.data)
    #   return HttpResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # # @action(detail=False, methods=["GET"])
    # def getByName(self, request):
    #     name = request.query_params.get("Name", None)
    #     query = Portals.objects.filter(Name=name)
    #     result = serializers.serialize('json', query)
    #     return HttpResponse(result, content_type='application/json')

    # @action(detail=False, methods=["GET"])
    # def getByInvoice(self, request):
    #     invoice = request.query_params.get("InvoiceNumber", None)
    #     query = Portals.objects.filter(InvoiceNumber=invoice)
    #     result = serializers.serialize('json', query)
    #     return HttpResponse(result, content_type='application/json')

    # @action(detail=False, methods=['POST'])
    # def savePin(self,request):
    #     # generate a new pin with this function
    #     # Check if id is a list
    #     if isinstance(request.data['id'], list):
    #       ids = request.data.pop('id')
    #       models = []
    #       for id in ids:
    #         # validate each model with one seat at a time
    #         request.data['id'] = id
    #         serializer = PortalSerializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         models.append(serializer)

        # generated_pin = ''.join(random.SystemRandom().choice(
        #     [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(10))
        # print(generated_pin)
        # Save it only after all seats are valid.
        # To avoid situations when one seat has wrong id
        # And you already save previous
        # saved_models = [model.save() for model in models]
        # result_serializer = PortalSerializer(saved_models, many=True)
        # Return list of tickets
        # return HttpResponse(result_serializer.data)

        # id = request.data.get("id")

        # x = Portals.objects.get(id=id)
        # x.pinum = generated_pin
        # x.save()
        # return HttpResponse(x.pinum, content_type='application/json')

    # @action(detail=False, methods=['POST'])
    # def get_serializer(self, *args, **kwargs):
    #    if "data" in kwargs:
    #     data = kwargs["data"]

    #     # check if many is required
    #     if isinstance(data, list):
    #         kwargs["many"] = True

    #     return HttpResponse(data, content_type='application/json')
