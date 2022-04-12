from django.contrib.auth import get_user_model
from rest_framework import serializers
from empleado.models import Empleado, Ingreso

User = get_user_model()


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = "__all__"


class EmpleadoSerializer(serializers.ModelSerializer):
    #detalle = IngresoSerializer(required=True)

    class Meta:
        model = Empleado
        fields = "__all__"

    def create(self, validated_data):
        detalle_data = validated_data.pop('ingresos_empleado')
        pj = Ingreso.objects.create(**detalle_data)
        validated_data.update({'detalle': pj})
        Empleado = Empleado.objects.create(**validated_data)

        return Empleado
