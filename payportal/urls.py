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
from portal.api.bece_views import BeceViewSet,getBeceInfo,PayBece
from payment.views import PaymentViewSet
from portal.views import BeceViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'portals', PortaltViewSet)
router.register(r'payment', PaymentViewSet)
<<<<<<< HEAD
router.register(r'bece' ,  BeceViewSet)
=======
router.register(r'bece', BeceViewSet) # upload bece data
>>>>>>> e9f00e480e1d8f22010101808481f224d05ee742


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('beceid/<str:pk>/', getBeceInfo, name ="getBeceinformation"),# getbeceinfo
    path('becepayment/<str:pk>/', PayBece, name ="getBeceinformation"),# pay for bece exams form
]
