"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app import views as app_v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/index/', app_v.index),
    # path('app/setcookies/<str:company>', app_v.setcookies),
    # path('app/getcookies/', app_v.getcookies),
    # path('app/setsaltcookies/<str:language>', app_v.setsaltcookies),
    # path('app/getsaltcookies/',app_v.getsaltcookies),
    path('app/home/',app_v.home),
    path('app/login/',app_v.login),
    #path('app/setSessions/<str:username>',app_v.setSessions),
    #path('app/getSessions/',app_v.getSessions),
    path('app/gotoLogin/',app_v.gotoLogin),
    path('app/logout',app_v.logout),



]
