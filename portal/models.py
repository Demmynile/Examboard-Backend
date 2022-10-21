import email
from pyexpat import model
from re import S
from tokenize import Number
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from api.documents.models import Document, OtherDocument
# from api.industry.models import Industry
# from api.user.models import Supplier
# from api.user.models import ProcurementManager
import uuid
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from .utils import Util
# from django_filters import FilterSet , DateFromToRangeFilter
# from computed_property import ComputedTextField

# class User(AbstractUser):
#     is_buyer = models.BooleanField(default=False, null=True, blank=True)
#     is_vendor = models.BooleanField(default=False, null=True, blank=True)
#     email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
#     uuid = models.CharField(max_length=500, blank=True)
#     digiNumber = models.CharField(max_length=100, null=True, blank=True)
#     Vendaddress = models.CharField(max_length=500, null=True, blank=True)
#     shopName = models.CharField(max_length=500, null=True, blank=True)
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     Country = models.CharField(max_length=225, null=True, blank=True)
#     State = models.CharField(max_length=225, null=True, blank=True)
#     City = models.CharField(max_length=225, null=True, blank=True)
#     notify = models.IntegerField(null=True, blank=True, default=0)
#     phone = models.CharField(max_length=20, null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True)
#     last_login = models.DateTimeField(null=True)
#     is_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     def _str_(self):
#         return f"{self.username}"
    # def save(self,*args,**kwargs):
    #    send_mail(
    #     'Vendor Registration',
    #     'Vendor Registration Successfull.',
    #     'aakindele@sterlingtech.com.ng',
    #     [self.email],
    #     fail_silently=False,
    #    )
       
    #    return super(User,self).save(*args,**kwargs)
class Portals(models.Model):

    # is_technical = models.BooleanField(default=False, null = True, blank= True)
    email = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    REQUIRED_FIELDS = []
    EventsType = (
        ('0', 'B.E.C.E'),
        ('1', 'JUNIOR SCHOOL'),
        ('2', 'M.C'),
        ('3', 'P.S')
    )
    tstType = (

        ('0', 'demola'),
        ('1', 'balogun'),
        ('2', 'surajudeen'),

    )
    combineType = (
        ('0', 'red'),
        ('1', 'yellow'),
        ('2', 'green'),
    )
    phone = models.CharField(max_length=100, null=True, blank=True)
    LedNumber = models.CharField(max_length=100, null=True, blank=True)
    LedDistrict = models.CharField(max_length=100, null=True, blank=True)
    RequestId = models.CharField(max_length=100, null=True, blank=True)
    InvoiceNumber = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    StudentNumber = models.IntegerField(null=True, blank=True)
    SchoolName = models.CharField(max_length=200, null=True, blank=True)
    session_token = models.CharField(
    max_length=10, default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    ExamType = models.CharField(
    max_length=100, choices=EventsType, null=True, default=0, blank=True)
    CandidateName = models.CharField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    AddressNo = models.CharField(max_length=100, null=True, blank=True)
    Street = models.CharField(max_length=100, null=True, blank=True)
    TownCity = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    testType = models.CharField(
        max_length=100, default=0, choices=tstType, null=True, blank=True)
    combine = models.CharField(
        max_length=100, default=0, choices=combineType, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=100, null=True, blank=True)
    staffID = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    pinum = models.CharField(max_length=100, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    
 
class Payments(models.Model):

    # is_technical = models.BooleanField(default=False, null = True, blank= True)
    email = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    REQUIRED_FIELDS = []
    EventsType = (
        ('Name Coorection', 'Correction Of Names'),
        ('TEDAC', 'TEDAC'),
        ('Change Of Status', 'Change Of Status'),
        ('Collection Of Certificates', 'Collection Of Certificates'),
        ('Reactivation Of School Codes', 'Reactivation Of School Codes'),
        ( 'B.E.C.E Result', 'B.E.C.E Result')
    )
    phone = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    PayerID = models.CharField(max_length=100, null=True, blank=True)
    LassraNumber = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    StudentNumber = models.IntegerField(null=True, blank=True)
    SchoolName = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    PaymentType = models.CharField(
    max_length=100, choices=EventsType, null=True, default=0, blank=True)
    Street = models.CharField(max_length=100, null=True, blank=True)
    Payeremail = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    TownCity = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=100, null=True, blank=True)
    staffID = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    pinum = models.CharField(max_length=100, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.updates()
        return super(Payments,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #         self.uniquecode = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    # def save(self, *args, **kwargs):
    #     self.update()
        
    #     return super(BECE,self).save(*args,**kwargs)

    def updates(self):
        # self.TotalPrice= self.StudentNumber * 4
       
        x = uuid.uuid4().hex.upper()
        genid=x[16:21]
        self.trnsref=genid
        b=0
        
     

    # DisplayFields = ['id','ExamType','LedNumber','InvoiceNumber','SchoolName','StudentNumber','pricing']

    # @property
   

    # def save(self, *args, **kwargs):
    #     self.update()
    #     super().save(*args, **kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #     if(self.ExamType == '0'):
    #         self.TotalPrice = self.StudentNumber * 4
    #     elif(self.ExamType == '1'):
    #         self.TotalPrice = self.StudentNumber * 3
    #     # elif(self.ExamType == '2'):
    #     #     self.TotalPrice = self.StudentNumber * 5
    #     elif(self.ExamType == '3'):
    #         self.TotalPrice = self.StudentNumber * 2

        # email body composition
        # email_body = self.InvoiceNumber
        # data = {"email_body": email_body, "to_email": self.email,
        #         "email_subject": "Acquisition of the Invoice Number"}

        # send the email
        # Util.send_email(data)

        # super(Portals, self).save(*args, **kwargs) # Call the "real" save() method
        # return self.TotalPrice
class BECE(models.Model):
    EventsType = (
        ('0', 'PRIVATE'),
        ('1', 'PUBLIC')
    )
    EventsType2 = (
        ('PAID', 'True'),
        ('NOT PAID', 'False')
    )
    # is_technical = models.BooleanField(default=False, null = True, blank= True)
    Payeremail = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    Payerphone = models.CharField(max_length=100, null=True, blank=True)
    SchoolId= models.CharField(max_length=100, null=True, blank=True)
    SchoolTypeId = models.CharField(max_length=100, null=True, blank=True)
    schoolIds = models.CharField(max_length=100, null=True, blank=True)
    InvoiceNumber = models.CharField(max_length=100, null=True, blank=True)
    SchoolName = models.CharField(max_length=100, null=True, blank=True)
    PayerName = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    CodePrice = models.IntegerField(null=True, blank=True)
    NumberOfCandidates = models.IntegerField(null=True, blank=True,default=0)
    SchoolName = models.CharField(max_length=200, null=True, blank=True)
    session_token = models.CharField(
    max_length=10, default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField( null=True, blank=True)
    StartingDate = models.DateField(null=True, blank=True)
    ClosingDate = models.DateField( null=True, blank=True)
    ExamName =  models.CharField(max_length=100, null=True, blank=True)
    LgaId = models.CharField(max_length=500, null=True, blank=True)
    LgaName = models.CharField(max_length=500, null=True, blank=True)
    ExamCost =  models.CharField(max_length=500, null=True, blank=True)
    SchoolType = models.CharField(max_length=100, choices=EventsType, null=True, blank=True)
    Street = models.CharField(max_length=100, null=True, blank=True)
    adminemail = models.CharField(max_length=500, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=100,choices=EventsType2 ,null=True, blank=True)
    pinum = models.CharField(max_length=500, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    uniquecode = models.CharField(max_length=100, null=True, blank=True)
    quota= models.CharField(max_length=100, null=True, blank=True)
    quota2 = models.CharField(max_length=100, null=True, blank=True)
    
 
    def save(self, *args, **kwargs):
        self.updates()
        return super(BECE,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #         self.uniquecode = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    # def save(self, *args, **kwargs):
    #     self.update()
        
    #     return super(BECE,self).save(*args,**kwargs)

    def updates(self):
        # self.TotalPrice= self.StudentNumber * 4
        self.SchoolId = self.LgaId+''+self.SchoolTypeId
        self.ExamCost = self.NumberOfCandidates * 4
        x = uuid.uuid4().hex.upper()
        b=0
        
        if(self.SchoolType == '1'):
            self.ExamCost = 0
            print(self.uniquecode)
       

    # DisplayFields = ['id','ExamType','LedNumber','InvoiceNumber','SchoolName','StudentNumber','pricing']

    # @property
class ModelCollege(models.Model):
    # EventsType = (
    #     ('0', 'PRIVATE'),
    #     ('1', 'PUBLIC')
    # )
    # is_technical = models.BooleanField(default=False, null = True, blank= True)
    Payeremail = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    Payerphone = models.CharField(max_length=100, null=True, blank=True)
    SchoolId= models.CharField(max_length=100, null=True, blank=True)
    CurrentSchoolName = models.CharField(max_length=100, null=True, blank=True)
    PayerName = models.CharField(max_length=100, null=True, blank=True)
    NumberOfCandidates = models.IntegerField(null=True, blank=True,default=0)
    ChoiceSchoolName = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField( null=True, blank=True)
    StartingDate = models.DateField(null=True, blank=True)
    ClosingDate = models.DateField( null=True, blank=True)
    ExamName =  models.CharField(max_length=100, null=True, blank=True)
    LgaId = models.CharField(max_length=500, null=True, blank=True)
    LgaName = models.CharField(max_length=500, null=True, blank=True)
    ExamCost =  models.CharField(max_length=500, null=True, blank=True)
    # SchoolType = models.CharField(max_length=100, choices=EventsType, null=True, blank=True)
    # Street = models.CharField(max_length=100, null=True, blank=True)
    adminemail = models.CharField(max_length=500, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=700, null=True, blank=True)
    pinum = models.CharField(max_length=500, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    uniquecode = models.CharField(max_length=100, null=True, blank=True)
    # quota= models.CharField(max_length=100, null=True, blank=True)
    # quota2 = models.CharField(max_length=100, null=True, blank=True)
    
 
  
class PublicScretariat(models.Model):
    EventsType = (
        ('1', 'Compulsory'),
        ('2', 'C.O 2'),
        ('3', 'C.A'),
        ('4', 'Trade Test'),
    )
    is_technical = models.BooleanField(default=False, null = True, blank= True)
    candidateemail = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    candidatephone = models.CharField(max_length=100, null=True, blank=True)
    SchoolId= models.CharField(max_length=100, null=True, blank=True)
    CurrentSchoolName = models.CharField(max_length=100, null=True, blank=True)
    CandidateName = models.CharField(max_length=100, null=True, blank=True)
    NumberOfCandidates = models.IntegerField(null=True, blank=True,default=0)
    ChoiceSchoolName = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField( null=True, blank=True)
    StartingDate = models.DateField(null=True, blank=True)
    ClosingDate = models.DateField( null=True, blank=True)
    ExamName =  models.CharField(max_length=100, null=True, blank=True)
    OracleNumber = models.CharField(max_length=500, null=True, blank=True)
    LgaName = models.CharField(max_length=500, null=True, blank=True)
    ExamCost =  models.CharField(max_length=500, null=True, blank=True)
    ExamType = models.CharField(max_length=100, choices=EventsType, null=True, blank=True)
    # Street = models.CharField(max_length=100, null=True, blank=True)
    adminemail = models.CharField(max_length=500, null=True, blank=True)
    candidateAdress= models.CharField(max_length=100, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=700, null=True, blank=True)
    pinum = models.CharField(max_length=500, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    uniquecode = models.CharField(max_length=100, null=True, blank=True)
    # quota= models.CharField(max_length=100, null=True, blank=True)
    # quota2 = models.CharField(max_length=100, null=True, blank=True)
    
 
    def save(self, *args, **kwargs):
        self.updates()
        return super(PublicScretariat,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #         self.uniquecode = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    # def save(self, *args, **kwargs):
    #     self.update()
        
    #     return super(BECE,self).save(*args,**kwargs)

    def updates(self):
        # self.TotalPrice= self.StudentNumber * 4
        # self.SchoolId = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
        # self.ExamCost = self.NumberOfCandidates * 4
        x = uuid.uuid4().hex.upper()
        b=0
        genix=x[15:20]
        genid=x[16:21]
        # self.OracleNumber=genix
        self.pinum=genid
        # uniquecode=genid
        # print(genix)
        # print(genix)
        
        if(self.ExamType == '1'):
            self.ExamCost = 2 * 4
            print(self.uniquecode)
        elif(self.ExamType == '2'):
             self.ExamCost = 1 * 2
        elif(self.ExamType == '3'):
             self.ExamCost = 3 * 3
        elif(self.ExamType == '4'):
             self.ExamCost = 2 * 5


        # email body composition
        # email_body = self.InvoiceNumber
        # data = {"email_body": email_body, "to_email": self.email,
        #         "email_subject": "Acquisition of the Invoice Number"}

        # send the email
        # Util.send_email(data)

        # super(Portals, self).save(*args, **kwargs) # Call the "real" save() method
        # return self.TotalPrice
class JSS3(models.Model):
    EventsType = (
        ('0', 'PRIVATE'),
        ('1', 'PUBLIC')
    )
    # is_technical = models.BooleanField(default=False, null = True, blank= True)
    Payeremail = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    Payerphone = models.CharField(max_length=100, null=True, blank=True)
    SchoolId= models.CharField(max_length=100, null=True, blank=True)
    SchoolTypeId = models.CharField(max_length=100, null=True, blank=True)
    schoolIds = models.CharField(max_length=100, null=True, blank=True)
    InvoiceNumber = models.CharField(max_length=100, null=True, blank=True)
    SchoolName = models.CharField(max_length=100, null=True, blank=True)
    PayerName = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    NumberOfCandidates = models.IntegerField(null=True, blank=True,default=0)
    SchoolName = models.CharField(max_length=200, null=True, blank=True)
    session_token = models.CharField(
    max_length=10, default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField( null=True, blank=True)
    StartingDate = models.DateField(null=True, blank=True)
    ClosingDate = models.DateField( null=True, blank=True)
    ExamName =  models.CharField(max_length=100, null=True, blank=True)
    LgaId = models.CharField(max_length=500, null=True, blank=True)
    LgaName = models.CharField(max_length=500, null=True, blank=True)
    ExamCost =  models.CharField(max_length=500, null=True, blank=True)
    SchoolType = models.CharField(max_length=100, choices=EventsType, null=True, blank=True)
    Street = models.CharField(max_length=100, null=True, blank=True)
    adminemail = models.CharField(max_length=500, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=100, null=True, blank=True)
    pinum = models.CharField(max_length=500, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    uniquecode = models.CharField(max_length=100, null=True, blank=True)
    quota= models.CharField(max_length=100, null=True, blank=True)
    quota2 = models.CharField(max_length=100, null=True, blank=True)
    
 
    def save(self, *args, **kwargs):
        self.updates()
        return super(JSS3,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #         self.uniquecode = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    # def save(self, *args, **kwargs):
    #     self.update()
        
    #     return super(BECE,self).save(*args,**kwargs)

    # def updates(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #     # self.SchoolId = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    #     self.ExamCost = self.NumberOfCandidates * 3
    #     x = uuid.uuid4().hex.upper()
    #     b=0
    #     genid=x[15:20]
    #     # uniquecode=genid
    #     print(genid)
    #     print(genid)
    #     if(self.SchoolType == '1'):
    #         self.uniquecode = genid
    #         print(self.uniquecode)
    #     elif(self.SchoolType == '0'):
    #         self.uniquecode = b
    def updates(self):
        # self.TotalPrice= self.StudentNumber * 4
        self.SchoolId = self.LgaId+''+self.SchoolTypeId
        self.ExamCost = self.NumberOfCandidates * 4
        x = uuid.uuid4().hex.upper()
        b=0
        
        if(self.SchoolType == '1'):
            self.ExamCost = 0
            print(self.uniquecode)

    # DisplayFields = ['id','ExamType','LedNumber','InvoiceNumber','SchoolName','StudentNumber','pricing']

    # @property
   

    

        # email body composition
        # email_body = self.InvoiceNumber
        # data = {"email_body": email_body, "to_email": self.email,
        #         "email_subject": "Acquisition of the Invoice Number"}

        # send the email
        # Util.send_email(data)

        # super(Portals, self).save(*args, **kwargs) # Call the "real" save() method
        # return self.TotalPrice
