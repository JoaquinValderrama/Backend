from pkgutil import ImpImporter
from flask_restful import Resource ,request
from config import conexion
from models.participantes import Participante
from dtos.participante_dto import ParticipanteRequestDTO, ParticipanteResponseDTO

#los tipos de datos que se pueden retornar son Strings, Int, Boolean, Arreglos y Diccionarios

class ParticipanteController(Resource):
    #esta clase se comportara como si fuese un controlador, es decir que si deifinimos un metodo llamado get
    def get(self):
        resultado = conexion.session.query(Participante).all()
        # manu = True => indico que estoy pasando una lista de instancias, por lo que el dto va a tener que iterar esa lista y transformarla en diccionario
        participantesSerializados = ParticipanteResponseDTO().dump(resultado, many = True)
        print(resultado[0].nombre)
        participantes = []
        
        for participante in resultado:
            participantes.append({
             'id':participante.id,
             'nombre':participante.nombre   
            })
        return {
            'message':'Ingreso al get',
            'content' : participantes,
            'content2' : participantesSerializados
        }
    
    def post(self):
        print(request.get_json())
        data = request.get_json()
        try:
            dataSerializada = ParticipanteRequestDTO().load(data)
            print (dataSerializada)
            
            #**dataSerializada => convertimos ese diccionario en parametros
            # {'nombre' : 'fabio'} => nombre = 'fabio'
            nuevoParticipante = Participante(**dataSerializada)
            # Empezamos una nueva transaccion 
            conexion.session.add(nuevoParticipante)
            #una vez que queremos guardar de manera permaennte los cambios (insercion o actualizacion o eliminacion ) de los registros haremos un commit
            conexion.session.commit()
            return{
                'message':'Ingresaste al post'
            }
        except Exception as e:
            #Si fallas entonces entraras al except
            #para deshacer los cambios de la transaccion hacemos uso del rollback
            conexion.session.rollback()
            return {
                'message' : 'Error al ingresar el participante',
                'content' : e.args
            }

        #Cuando se retorna una tupla la primera posicion sera el body y la segunda posicion sera el estado de respuesta
        #return ((1,2,3),200)