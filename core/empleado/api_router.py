from django.urls import path, include
from django.contrib.auth.models import User
from django.urls.conf import re_path
from rest_framework import routers, serializers, viewsets
from empleado.api.views import (EmpleadoCreateAPIView,
 ListarEmpleadoViewSet, DetalleEmpleadoViewSet,
 ModificarEmpleadoViewSet,IngresoCreateAPIView,EliminarEmpleadoViewSet,ListarIngresosViewSet) 

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
# DASHBOARD ListarIngresosViewSet
router.register("empleado", ListarEmpleadoViewSet, basename='Empleados')
router.register("empleado/detalle", DetalleEmpleadoViewSet, basename='empleados_detalle')
router.register("empleado/modificar", ModificarEmpleadoViewSet, basename='empleados_modificar')
router.register("empleado/eliminar", EliminarEmpleadoViewSet, basename='empleados_eliminar')
#router.register("Empleados/crear", EmpleadoCreateAPIView, basename='Empleados_crear')
#router.register("Empleados/detalle", EmpleadoDetailAPIView, basename='Empleados_detalle')
router.register("ingresos", ListarIngresosViewSet, basename='ingresos')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('empleado/crear', EmpleadoCreateAPIView.as_view(), name="empleados_crear"),
    path('ingreso/crear', IngresoCreateAPIView.as_view(), name="ingresos_crear"),
    #path('empleado/detalle', EmpleadoDetailAPIView.as_view(), name="Empleados_detalle")
]

