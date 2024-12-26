"""Prologicielsucces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Qrcodes.views import telecharger_attestation,creer_attestation,liste_attestations,index


urlpatterns = [
    path('', index, name='index'),
    path('creer/', creer_attestation, name='creer_attestation'),
    path('liste/', liste_attestations, name='liste_attestations'),
    path('telecharger/<int:attestation_id>/', telecharger_attestation, name='telecharger_attestation'),
    path("admin/", admin.site.urls),
]
