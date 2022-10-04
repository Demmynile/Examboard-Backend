"""payportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from portal.views import PortaltViewSet
from portal.api.bece_views import BeceViewSet,CustomAuthToken,PayPublicService,getPserviceInfo,getBeceInfo,PublicServiceViewSet,PayBece,getShoppedPin,Jss3ViewSet,getJss3Info,PayJss,UpdatePayBece,PayBecePrivate,MCViewSet,PayJSSPrivate,PayBeceAdmin,PayJssAdmin
from payment.views import PaymentViewSet
# from portal.views import BeceViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'portals', PortaltViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'bece' ,  BeceViewSet)
router.register(r'bece', BeceViewSet) # upload bece data
router.register(r'jss', Jss3ViewSet) # upload jss data
router.register(r'bece', BeceViewSet) # upload bece data
router.register(r'jss', Jss3ViewSet) # upload jss data
router.register(r'mcollege', MCViewSet) # model college payment
router.register(r'pservice', PublicServiceViewSet) # public service payment upload from admin
router.register(r'adminlogin', PublicServiceViewSet) # admin login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('beceid/<str:pk>/', getBeceInfo, name ="getBeceinformation"),# getbeceinfo
    path('becepayment/<str:pk>/', PayBece, name ="getBeceinformation"),# pay for bece exams form
    path('paybeceprivate/<str:pk>/',PayBecePrivate, name ="getBeceinformation"),# pay for bece exams form
    path('updatequota/<str:pk>/', UpdatePayBece, name ="getBeceinformation"),#increase number of students
    path('jssid/<str:pk>/', getJss3Info, name ="getJss3information"),# getjssinfo
    path('mcpin/<str:pk>/', getShoppedPin, name ="getJss3information"),# getshopped pin 
    path('jsspayment/<str:pk>/', PayJss, name ="getBeceinformation"),# pay for jss exams form
    path('jssprivatepay/<str:pk>/', PayJSSPrivate, name ="getBeceinformation"),# pay for jss exams form
    path('jssadminpayment/<str:pk>/', PayJssAdmin, name ="adjustjss info"),# admin adjust for jss
    path('pservice/<str:pk>/', getPserviceInfo, name ="get ps info"),# get pservice info
    path('beceadminpayment/<str:pk>/', PayBeceAdmin, name ="adjustbece info"),# admin adjust for bece
    path('paypservie/<str:pk>/', PayPublicService, name ="adjustbece info"),# pay for public service
    # path('login/',CustomAuthToken, name='auth-token'),
]
