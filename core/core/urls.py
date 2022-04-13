
from django.contrib import admin
from django.urls import include, path
from django.urls.conf import re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from empleado.views import Inicio

app_name = 'core'

urlpatterns = [
    # Core
    path('admin/', admin.site.urls),
    path('inicio/', view=Inicio.as_view(), name="inicio_view"),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include("empleado.api_router")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += []
