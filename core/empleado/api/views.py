from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from django.views.generic import CreateView, DetailView, UpdateView
from empleado.models import Empleado, Ingreso
# from users.models import User
from .serializers import UserSerializer, EmpleadoSerializer, IngresoSerializer


class EmpleadoViewSet(ListModelMixin, GenericViewSet):

    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()


class DetalleEmpleadoViewSet(ListModelMixin, GenericViewSet):
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        #user = self.request.user
        queryset = Empleado.objects.prefetch_related('ingresos_empleado').filter()
        #print("User: ", user.id)
        return queryset

class ModificarEmpleadoViewSet(ListModelMixin, GenericViewSet):
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        #user = self.request.user
        queryset = Empleado.objects.prefetch_related('ingresos_empleado').filter()
        #print("User: ", user.id)
        return queryset

class EliminarEmpleadoViewSet(ListModelMixin, GenericViewSet):
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        #user = self.request.user
        queryset = Empleado.objects.prefetch_related('ingresos_empleado').filter()
        #print("User: ", user.id)
        return queryset

class ListarEmpleadoViewSet(ListModelMixin, GenericViewSet):
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        #user = self.request.user
        queryset = Empleado.objects.prefetch_related('ingresos_empleado').filter()
        #print("User: ", user.id)
        return queryset


class EmpleadoCreateAPIView(generics.CreateAPIView):
    serializer_class = EmpleadoSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Empleado.objects.filter(user=user.id)
        print("User: ", user.id)
        return queryset

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empleado creado exitosamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngresoCreateAPIView(generics.CreateAPIView):
 
    serializer_class = IngresoSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ingreso.objects.select_related('ingresos_empleado').filter(user=user.id)
        print("User: ", user.id)
        return queryset


