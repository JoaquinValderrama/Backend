from wsgiref import validate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .serializer import pruebaSerializer,TareaSerializer
from rest_framework import status
from .models import Tarea
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
# Serializaer_class => lo que va a convertir la informacion que llega desde el cliente y tbn la informacion que retornaremos hacia el cliente
    serializer_class = pruebaSerializer

# Admite un GET y un POST
class TareasView(ListCreateAPIView):
    queryset  = Tarea.objects.all() # Select *from Tarea
    serializer_class = TareaSerializer

    def get(self, request):
        #Cuando se modifica el metodo por algun comportamiento diferente DRF ahora obedecera a este comportamiento, ahi se podra dejar de utilizar los atributos queryset y serializer_class
        #primero obtengo las tareas
        tareas = self.get_queryset()
        #luego la paso al serializador para convertirlas a tipos de datos genericos
        tareaSerializada = self.serializer_class(tareas, many=True)
        return Response (data={
            'message' : 'Las tareas son:',
            'content' : tareaSerializada.data
        })


    def post(self,request:Request):
        body = request.data
        instancia_Serializador = self.serializer_class(data=body)
        validacion =  instancia_Serializador.is_valid(raise_exception=True) #me retornara true si es valida, sino es valida emitira un error
        
        if validacion ==True:
            #save => guarda la informacion en la bd
            instancia_Serializador.save()

            return Response(data = instancia_Serializador.data,status=status.HTTP_201_CREATED)