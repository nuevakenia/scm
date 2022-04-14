"""externo URL Configuration

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
from django.urls import include, path
from django.urls.conf import re_path
from django.views.generic import TemplateView

from enrolamiento.views import (Inicio,Enrolamiento,Enrolamientos,Empleado_modificar)

app_name = 'externo'


urlpatterns = [
    # Externo
    path('admin/', admin.site.urls),
    path('inicio/', view=Inicio.as_view(), name="inicio"),
    path('enrolamiento/', view=Enrolamiento.as_view(), name="enrolamiento"),
    path('enrolamientos/', view=Enrolamientos.as_view(), name="enrolamientos"),
    path('empleado/modificar/<int:pk>/', view=Empleado_modificar.as_view(), name="empleado"),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += []