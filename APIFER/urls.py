"""APIFER URL Configuration

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
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Acceso.as_view(),name="acceso"),
    path('Inicio/',Inicio.as_view(), name="inicio"),
    path('forms/',Forms.as_view(), name="Forms"),
    path('ubicacion/',Ubicacion.as_view(), name="ubicacion"),
    path('tables/',Tables.as_view(), name="Tables"),
    path('galeria/',Galeria.as_view(), name="galeria"),
    path('completo/',Completo.as_view(), name="completo"),
    # path('registro/',Registro.as_view(), name="registro"),
    path('acceso/', Acceso.as_view(), name='acceso'),
    path('carrito/', Carrito.as_view(), name='carrito')
]
