from django.urls import path
from .views import inicio,ListarTareas,TareasView

# Seran todas las rutas que pueden ser accedidas a esta aplicacion 
urlpatterns = [
    path('inicio',inicio),
    path('prueba',ListarTareas.as_view()),
    path('tareas',TareasView.as_view())
] 