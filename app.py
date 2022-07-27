from flask import Flask
from config import conexion
from models.participantes import Participante
#environ => me devuelve todas las variables de entorno en forma de un diccionario
from os import environ
from dotenv import load_dotenv
#carga todas las variables declaradas en el archivo .env como si fuesen variables, de entorno para que puedan ser accedidas desde el metodo 'environ'
from flask_restful import Api
from controlers.participante import ParticipanteController
from flask_cors import CORS

load_dotenv()
app = Flask (__name__)
api = Api (app)
CORS(app)
#URI dialect://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
#sqlalchemy hace un seguimiento a las modificaciones que haremos a la bd pero actualmente tiene un valor predeterminado PERO en futuuras versionestendremos que OBLIGATORIAMENTE iindicar si queremos hacer el seguimiento o no
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#se inicializa mi conexion de mi sqlachemy con la base de datos PERO todavia no me he conectado
conexion.init_app(app)
#se ejecuta la conexion y se creara las tablas, PERO si no hay ninguna tabla a crear entonces no lanzara error de credenciales invalidas
# si ya se creo la tabla entonces no debe volver  a intentar crear las tablas ya que me da un error
# conexion.create_all(app=app)


@app.route ('/',methods=['GET'])
def inicio():
    return{
        'message': 'Bienvenidos a Api de Concursos'
    }
#Definicion de  rutas usando Flask Restful
api.add_resource(ParticipanteController,'/participantes')
if __name__ == '__main__':
    app.run(debug=True)