from tokenize import String
import datetime
from datetime import date
from urllib import response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import query
from django.forms import DateField
from django.utils.dateparse import parse_date
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from django.core.mail import send_mail
from django.core import serializers as core_serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ViewSet
from portal.models import BECE,JSS3,ModelCollege,PublicScretariat
from portal.serializers import BeceSerializer,CreateListMixin,PBSerializer,BeceSerializers,BeceSerializerd,Jss3Serializer,Jss3Serializerd,MCSerializer
from django.http import HttpResponse
import uuid
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# @api_view(['POST'])
# def PSExam( request):
  
#     # venues = Task.objects.get(pk=db_id)
#     # pk = self.kwargs.get('pk')
#     # Product.vendors = Vendor.objects.get(id)
#     # print(Product.vendors)
    
#     # print(vendors)
    
#     # print(vendors)
    
#     data = request.data
   
#     # vendors = request.data.vendorsy7u.id
#     product = PublicScretariat.objects.create(
#     Payeremail  = request.data.get('Payeremail')
#     CurrentSchoolName = request.data.get('CurrentSchoolName')
#     trnsref = request.data.get('trnsref')
#     PayerName = request.data.get('PayerName')
#     ExamCost = request.data.get('ExamCost')
#     Payerphone = request.data.get('Payerphone')
#     LgaId = request.data.get('LgaId')
#     SchoolId = request.data.get('SchoolId')
#     ChoiceSchoolName = request.data.get('ChoiceSchoolName')
#     pinum = (request.data.get('pinnum'))
#     NumberOfCandidates  = int(request.data.get('NumberOfCandidates'))
#     )

#     serializer = PBSerializer(product, many=False)
#     return Response(serializer.data)
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        # product=serializer.validated_data['product']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'username': user.username,
            # 'product':product.user.username,
        })
class MCViewSet(viewsets.ModelViewSet):

    queryset = ModelCollege.objects.all()
    serializer_class = MCSerializer
    # lookup_field = 'transactionRef'

    @action(detail=False, methods=["POST"])
    def generate_pin(self, request):
          Payeremail  = request.data.get('Payeremail')
          CurrentSchoolName = request.data.get('CurrentSchoolName')
          trnsref = request.data.get('trnsref')
          PayerName = request.data.get('PayerName')
          ExamCost = request.data.get('ExamCost')
          Payerphone = request.data.get('Payerphone')
          LgaId = request.data.get('LgaId')
          SchoolId = request.data.get('SchoolId')
          ChoiceSchoolName = request.data.get('ChoiceSchoolName')
          pinum = (request.data.get('pinnum'))
          NumberOfCandidates  = int(request.data.get('NumberOfCandidates'))
          ExamCost = NumberOfCandidates * 4
          bulk_list = list()
        
          x = uuid.uuid4().hex.upper()
          b=0
          genid=x[15:20]
         
          for _ in range(NumberOfCandidates):
            trnsref=genid
            pinum = uuid.uuid4().hex.upper()[15:20]
            bulk_list.append(
                ModelCollege( PayerName = PayerName, SchoolId=SchoolId, LgaId =  LgaId, ChoiceSchoolName =ChoiceSchoolName , Payeremail=Payeremail,Payerphone=Payerphone, trnsref = trnsref,  ExamCost = ExamCost, pinum = pinum , CurrentSchoolName=CurrentSchoolName ))

          

          query = ModelCollege.objects.bulk_create(bulk_list)
          result = core_serializers.serialize('json', query)
        # result = serializers.serialize('json', query)
          return HttpResponse(result, content_type='application/json')

class BeceViewSet(CreateListMixin,viewsets.ModelViewSet):

    queryset = BECE.objects.all()
    serializer_class = BeceSerializers
    lookup_field = 'uniquecode'

class PublicServiceViewSet(CreateListMixin,viewsets.ModelViewSet):

    queryset = PublicScretariat.objects.all()
    serializer_class = PBSerializer
    lookup_field = 'OracleNumber'

class Jss3ViewSet(CreateListMixin,viewsets.ModelViewSet):

    queryset = JSS3.objects.all()
    serializer_class = Jss3Serializer
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

@api_view(['GET'])
# @permission_classes([IsAuthenticated&IsVendorUser])
def getPserviceInfo(request,pk):
    bece = PublicScretariat.objects.filter( OracleNumber=pk)
    serializer = PBSerializer(bece, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated&IsVendorUser])
def getJss3Info(request,pk):
    jss = JSS3.objects.filter(SchoolId=pk)
    serializer = Jss3Serializerd(jss, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayBecePrivate(request, pk):
    data = request.data
    bece = BECE.objects.get(SchoolId=pk)
    # bece.quota = data['quota']
    # bece.quota2 = data['quota2']

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    # bece.adminemail = data['adminemail']
    # bece.SchoolName = data['SchoolName']
    # bece.LgaName = data['LgaName']


    # bece.SchoolType = data['SchoolType']
    # bece.Payeremail = data['Payeremail']
    # bece.PayerName = data['PayerName']
    bece.pinum = genid
    
    # if(bece.quota2 <= bece.quota):
        # bece.pinum = genid
    bece.save()
    serializer = BeceSerializer(bece, many=False)


@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayPublicService(request, pk):
    data = request.data
    ps= PublicScretariat.objects.get(OracleNumber=pk)
    # bece.quota = data['quota']
    # bece.quota2 = data['quota2']

    
    x = uuid.uuid4().hex.upper()
    genid=x[15:20]
    print(genid)
    ps.pinum = data["pinum"]
    # print(ps.pinum)
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    # bece.adminemail = data['adminemail']
    # bece.SchoolName = data['SchoolName']
    # bece.LgaName = data['LgaName']


    # bece.SchoolType = data['SchoolType']
    # bece.Payeremail = data['Payeremail']
    # bece.PayerName = data['PayerName']
    
    
    ps.OracleNumber = data['OracleNumber']
    # ps.pinum = "09876"
    
    ps.adminemail = data['adminemail']
    ps.ExamType= data['ExamType']
    ps.candidateemail = data['candidateemail']


    ps.ClosingDate =  parse_date(data['ClosingDate'])
   
    ps.candidatephone = data['candidatephone']
    ps.CandidateName = data['CandidateName']
    ps.currentOffice = data['currentOffice']
    ps.Mda = data['Mda']
    # ps.pinum = genid
    
    # if(bece.quota2 <= bece.quota):
        # bece.pinum = genid
    ps.save()
    serializer = PBSerializer(ps, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayJSSPrivate(request, pk):
    data = request.data
    jss= JSS3.objects.get(SchoolId=pk)
    # bece.quota = data['quota']
    # bece.quota2 = data['quota2']

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    # bece.adminemail = data['adminemail']
    # bece.SchoolName = data['SchoolName']
    # bece.LgaName = data['LgaName']


    # bece.SchoolType = data['SchoolType']
    # bece.Payeremail = data['Payeremail']
    # bece.PayerName = data['PayerName']
    jss.pinum = genid
    
    # if(bece.quota2 <= bece.quota):
        # bece.pinum = genid
    jss.save()
    serializer = BeceSerializer(jss, many=False)
    return Response(serializer.data)
       
    # elif(bece.quota2 > bece.quota):

    #     send_mail(
    #     [bece.SchoolName],
    #     'attend to this school  above who is trying to enter more than what was allocated',
    #     'aakindele@sterlingtech.com.ng',
    #     [bece.adminemail],
    #     fail_silently=False,
    #    )
    #     return Response({'detail': 'you cant pay more than this quota'},
    #              status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayBece(request, pk):
    data = request.data
    bece = BECE.objects.get(SchoolId=pk)
    bece.quota = data['quota']
    bece.quota2 = data['quota2']
    bece.ClosingDate = parse_date(data['ClosingDate'])

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    bece.NumberOfCandidates = data['NumberOfCandidates']
    
    bece.adminemail = data['adminemail']
    bece.SchoolName = data['SchoolName']
    bece.LgaName = data['LgaName']


    bece.SchoolType = data['SchoolType']
    bece.Payeremail = data['Payeremail']
    bece.PayerName = data['PayerName']
      
    if(bece.quota2 > bece.quota) :
        print(datetime.date.today())

        send_mail(
        [bece.SchoolName],
        'attend to this school  above who is trying to enter more than what was allocated',
        'obalogun@sterlingtech.com.ng',
        [bece.adminemail],
        fail_silently=False,
       )
        return Response({'detail': 'you cant pay more than this quota'},status=status.HTTP_400_BAD_REQUEST)
        #  return Response({"status": "success","data":serializer.data,'viewed': product.viewed}, status=status.HTTP_200_OK)

    if date.today()  > bece.ClosingDate :
        print(datetime.date.today())

        send_mail(
        [bece.SchoolName],
        'attend to this school  above who is paying late for an exam',
        'obalogun@sterlingtech.com.ng',
        [bece.adminemail],
        fail_silently=False,
       )
        return Response({'detail': 'you are too late please pay your charges '},status=status.HTTP_400_BAD_REQUEST)

    if(bece.quota2 <= bece.quota) and (bece.SchoolType!='1') :
        bece.pinum = b
        bece.save()
        serializer = BeceSerializer(bece, many=False)
        return Response(serializer.data)
    if(bece.quota2 <= bece.quota) and (bece.SchoolType== '1') :
        bece.pinum = genid
        bece.save()
        serializer = BeceSerializer(bece, many=False)
        return Response(serializer.data)
    
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayBeceAdmin(request, pk):
    data = request.data
    bece = BECE.objects.get(SchoolId=pk)
    bece.quota = data['quota']
    bece.quota2 = data['quota2']
    bece.ClosingDate = parse_date(data['ClosingDate'])

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    bece.NumberOfCandidates = data['NumberOfCandidates']
    
    bece.adminemail = data['adminemail']
    bece.SchoolName = data['SchoolName']
    bece.LgaName = data['LgaName']


    bece.SchoolType = data['SchoolType']
    bece.Payeremail = data['Payeremail']
    bece.PayerName = data['PayerName']
      
    # if(bece.quota2 > bece.quota) :
    #     print(datetime.date.today())

    #     send_mail(
    #     [bece.SchoolName],
    #     'attend to this school  above who is trying to enter more than what was allocated',
    #     'obalogun@sterlingtech.com.ng',
    #     [bece.adminemail],
    #     fail_silently=False,
    #    )
    #     return Response({'detail': 'you cant pay more than this quota'},status=status.HTTP_400_BAD_REQUEST)
    #     #  return Response({"status": "success","data":serializer.data,'viewed': product.viewed}, status=status.HTTP_200_OK)

    # if date.today()  > bece.ClosingDate :
    #     print(datetime.date.today())

    #     send_mail(
    #     [bece.SchoolName],
    #     'attend to this school  above who is paying late for an exam',
    #     'obalogun@sterlingtech.com.ng',
    #     [bece.adminemail],
    #     fail_silently=False,
    #    )
    #     return Response({'detail': 'you are too late please pay your charges '},status=status.HTTP_400_BAD_REQUEST)

    # if(bece.quota2 <= bece.quota) and (bece.SchoolType!='1') :
    #     bece.pinum = b
    #     bece.save()
    #     serializer = BeceSerializer(bece, many=False)
    #     return Response(serializer.data)
    # if(bece.quota2 <= bece.quota) and (bece.SchoolType== '1') :
    #     bece.pinum = genid
    bece.save()
    serializer = BeceSerializer(bece, many=False)
    return Response(serializer.data)
     


@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def UpdatePayBece(request, pk):
    data = request.data
    bece = BECE.objects.get(pinum=pk)
    bece.quota = data['quota']
    bece.quota2 = data['quota2']

    # x = uuid.uuid4().hex.upper()
    # b=0
    # genid=x[15:20]
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    bece.adminemail = data['adminemail']
    bece.SchoolName = data['SchoolName']
    bece.LgaName = data['LgaName']
    bece.NumberOfCandidates +=data['NumberOfCandidates']


    bece.SchoolType = data['SchoolType']
    bece.Payeremail = data['Payeremail']
    bece.PayerName = data['PayerName']
    # if(bece.quota2 <= bece.quota):
        # bece.pinum = genid
    bece.save()
    serializer = BeceSerializer(bece, many=False)
    return Response(serializer.data)
       
    # elif(bece.quota2 > bece.quota):

    #     send_mail(
    #     [bece.SchoolName],
    #     'attend to this school  above who is trying to enter more than what was allocated',
    #     'obalogun@sterlingtech.com.ng',
    #     [bece.adminemail],
    #     fail_silently=False,
    #    )
    #     return Response({'detail': 'you cant pay more than this quota'},
    
#              status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated&IsVendorUser])
def getShoppedPin(request,pk):
 
    modelc = ModelCollege.objects.filter(trnsref=pk)
    serializer = MCSerializer(modelc, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayJss(request, pk):
    data = request.data
    jss = JSS3.objects.get(SchoolId=pk)
    jss.quota = data['quota']
    jss.quota2 = data['quota2']

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    jss.adminemail = data['adminemail']
    jss.SchoolName = data['SchoolName']
    jss.LgaName = data['LgaName']


    jss.SchoolType = data['SchoolType']
    jss.Payeremail = data['Payeremail']
    jss.PayerName = data['PayerName']
    
    if(jss.quota2 > jss.quota) :
        print(datetime.date.today())

        send_mail(
        [jss.SchoolName],
        'attend to this school  above who is trying to enter more than what was allocated',
        'obalogun@sterlingtech.com.ng',
        [jss.adminemail],
        fail_silently=False,
       )
        return Response({'detail': 'you cant pay more than this quota'},
                 status=status.HTTP_400_BAD_REQUEST)

    if date.today()  > jss.ClosingDate :
        print(datetime.date.today())

        send_mail(
        [jss.SchoolName],
        'attend to this school  above who is trying to enter more than what was allocated',
         'obalogun@sterlingtech.com.ng',
        [jss.adminemail],
        fail_silently=False,
       )
        return Response({'detail': 'you are too late please pay your charges '},
                 status=status.HTTP_400_BAD_REQUEST)
    if(jss.quota2 <= jss.quota) and (jss.SchoolType!='1') :
        jss.pinum = b
        jss.save()
        serializer = BeceSerializer(jss, many=False)
        return Response(serializer.data)
    if(jss.quota2 <= jss.quota) and (jss.SchoolType== '1') :
        jss.pinum = genid
        jss.save()
        serializer = BeceSerializer(jss, many=False)
        return Response(serializer.data)
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def PayJssAdmin(request, pk):
    data = request.data
    jss = JSS3.objects.get(SchoolId=pk)
    jss.quota = data['quota']
    jss.quota2 = data['quota2']

    x = uuid.uuid4().hex.upper()
    b=0
    genid=x[15:20]
    
    
    # bece.NumberOfCandidates = data['NumberOfCandidates']
    
    jss.adminemail = data['adminemail']
    jss.SchoolName = data['SchoolName']
    jss.LgaName = data['LgaName']


    jss.SchoolType = data['SchoolType']
    jss.Payeremail = data['Payeremail']
    jss.PayerName = data['PayerName']
    
    # if(jss.quota2 > jss.quota) :
    #     print(datetime.date.today())

    #     send_mail(
    #     [jss.SchoolName],
    #     'attend to this school  above who is trying to enter more than what was allocated',
    #     'obalogun@sterlingtech.com.ng',
    #     [jss.adminemail],
    #     fail_silently=False,
    #    )
    #     return Response({'detail': 'you cant pay more than this quota'},
    #              status=status.HTTP_400_BAD_REQUEST)

    # if date.today()  > jss.ClosingDate :
    #     print(datetime.date.today())

    #     send_mail(
    #     [jss.SchoolName],
    #     'attend to this school  above who is trying to enter more than what was allocated',
    #      'obalogun@sterlingtech.com.ng',
    #     [jss.adminemail],
    #     fail_silently=False,
    #    )
    #     return Response({'detail': 'you are too late please pay your charges '},
    #              status=status.HTTP_400_BAD_REQUEST)
    # if(jss.quota2 <= jss.quota) and (jss.SchoolType!='1') :
    #     jss.pinum = b
    #     jss.save()
    #     serializer = BeceSerializer(jss, many=False)
    #     return Response(serializer.data)
    # if(jss.quota2 <= jss.quota) and (jss.SchoolType== '1') :
    #     jss.pinum = genid
    jss.save()
    serializer = BeceSerializer(jss, many=False)
    return Response(serializer.data)
     

