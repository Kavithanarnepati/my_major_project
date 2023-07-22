"""InternetBandwidth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from users import views as u1
from admins import views as a1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',u1.index1,name='index1'),
  
    path("userRegister", u1.UserRegister, name="userRegister"),
    path('userlogin',u1.UserLoginCheck,name='userlogin'),
    path('userbase',u1.userbase,name='userbase'),
    path('usrViewData/', u1.usrViewData, name='usrViewData'),
    path('usrEDAData/', u1.usrEDAData, name='usrEDAData'),
    path('usrMachineLearning/', u1.usrMachineLearning, name='usrMachineLearning'),
    path('usrPredictForm/', u1.usrPredictForm, name='usrPredictForm'),
    
    
    path('adminlogin',a1.adminlog,name='adminlogin'),
    path('AdminHome',a1.AdminHome,name='AdminHome'),
    path("ViewRegisteredUsers", a1.ViewRegisteredUsers, name="ViewRegisteredUsers"),
    path("AdminActivaUsers/", a1.AdminActivaUsers, name="AdminActivaUsers"),
    path("mlresults/", a1.mlresults, name='mlresults'),
]
