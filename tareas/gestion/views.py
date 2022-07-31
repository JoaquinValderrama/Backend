from wsgiref import validate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,ListCreateAPIView

# from tareas.autorizacion.models import Usuario
from .serializer import pruebaSerializer,TareaSerializer
from rest_framework import status
from .models import Tarea
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    def get(self, request:Request):
        #Cuando se modifica el metodo por algun comportamiento diferente DRF ahora obedecera a este comportamiento, ahi se podra dejar de utilizar los atributos queryset y serializer_class
        #primero obtengo las tareas
        UsuarioId=request.user.id
        tareas = Tarea.objects.filter(UsuarioId = UsuarioId).all()
        #luego la paso al serializador para convertirlas a tipos de datos genericos
        tareaSerializada = self.serializer_class(tareas, many=True)
        return Response (data={
            'message' : 'Las tareas son:',
            'content' : tareaSerializada.data
        })


    def post(self,request:Request):
        body = request.data
        # request.user => devolvera toda la instancia del usuario que esta en la token (basandose en su ID)si no hay un usuario entonces sera un AnonymousUser
        print(request.user)
        body['UsuarioId']  = request.user.id # modifico el body entrante y le agrego el ID del usuario que actualmente esta haciendo la peticion
        instancia_Serializador = self.serializer_class(data=body)
        validacion =  instancia_Serializador.is_valid(raise_exception=True) #me retornara true si es valida, sino es valida emitira un error
        
        if validacion ==True:
            #save => guarda la informacion en la bd
            instancia_Serializador.save()

            return Response(data = instancia_Serializador.data,status=status.HTTP_201_CREATED)