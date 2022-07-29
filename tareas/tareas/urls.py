from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Aplicacion de gestion de tareas",
      default_version='v1',
      description="Api de gestion de tareas para empresa de servicios",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="joaquin.valderrama.e@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('gestion/',include('gestion.urls')),
    path('autorizacion/',include('autorizacion.urls'))
]
