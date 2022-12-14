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
        return super(BECE,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #         self.uniquecode = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    # def save(self, *args, **kwargs):
    #     self.update()
        
    #     return super(BECE,self).save(*args,**kwargs)

    def updates(self):
        # self.TotalPrice= self.StudentNumber * 4
        # self.SchoolId = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
        self.ExamCost = self.NumberOfCandidates * 4
        x = uuid.uuid4().hex.upper()
        b=0
        genid=x[15:20]
        # uniquecode=genid
        print(genid)
        print(genid)
        if(self.SchoolType == '1'):
            self.uniquecode = genid
            print(self.uniquecode)
        elif(self.SchoolType == '0'):
            self.uniquecode = b

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
class BECE(models.Model):
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
    RequestId = models.CharField(max_length=100, null=True, blank=True)
    InvoiceNumber = models.CharField(max_length=100, null=True, blank=True)
    SchoolName = models.CharField(max_length=100, null=True, blank=True)
    PayerName = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    NumberOfCandidates = models.IntegerField(null=True, blank=True)
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
    TownCity = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    currentOffice = models.CharField(max_length=100, null=True, blank=True)
    Mda = models.CharField(max_length=100, null=True, blank=True)
    pinum = models.CharField(max_length=500, null=True, blank=True)
    trnsref = models.CharField(max_length=100, null=True, blank=True)
    uniquecode = models.CharField(max_length=100, null=True, blank=True)
    quota= models.CharField(max_length=100, null=True, blank=True)
    quota2 = models.CharField(max_length=100, null=True, blank=True)
    
 
    # def save(self, *args, **kwargs):
    #     self.update()
    #     return super(BECE,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #         self.uniquecode = self.LgaId+''+ self.SchoolId+''+self.SchoolTypeId
    # def save(self, *args, **kwargs):
    #     self.update()
        
    #     return super(BECE,self).save(*args,**kwargs)

    # def update(self):
    #     # self.TotalPrice= self.StudentNumber * 4
    #     x = uuid.uuid4().hex.upper()
    #     b=0
    #     genid=x[15:20]
    #     # uniquecode=genid
    #     print(genid)
    #     print(genid)
    #     if(self.SchoolType == 'PUBLIC'):
    #         self.uniquecode = genid
    #         print(self.uniquecode)
    #     elif(self.SchoolType == 'PRIVATE'):
    #         self.uniquecode = b

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


