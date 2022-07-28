from django.urls import path
from .views import inicio,ListarTareas

# Seran todas las rutas que pueden ser accedidas a esta aplicacion 
urlpatterns = [
    path('inicio',inicio),
    path('prueba',ListarTareas.as_view())
] 