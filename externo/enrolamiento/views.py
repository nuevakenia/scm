from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.


class Inicio(TemplateView):

    template_name = "inicio.html"

    def get(self, request):

        return render(request, "inicio.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "inicio.html")

class Enrolamiento(TemplateView):

    template_name = "inicio.html"

    def get(self, request):

        return render(request, "inicio.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "inicio.html")

class Enrolamiento(TemplateView):

    template_name = "enrolamiento.html"
    
    def get(self, request):

        return render(request, "enrolamiento.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "enrolamiento.html")