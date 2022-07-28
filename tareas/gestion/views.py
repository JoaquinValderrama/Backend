from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from .serializer import pruebaSerializer
# Create your views here.

@api_view (http_method_names=['GET','POST'])
def inicio(request:Request):
    # El request me dara toda la informacion del usuario que me hara la peticion
    print(request)
    return Response(data={
        "message" : "Endpoint de un decorador"
    })

class ListarTareas(ListAPIView):
    # En cualquiera de las clases genericas se necesita declarar los atributos
    queryset =[{
        'nombre' : 'Joaquin',
        'apellido' : 'Valderrama'
    },{
        'nombre' : 'Angela',
        'apellido' : 'Valeriano'
    }]

# Serializador es un DTO (DATA TRANSFER OBEJCT)
    serializer_class = pruebaSerializer