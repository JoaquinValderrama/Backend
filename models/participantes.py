from email.policy import default
from inspect import CO_ASYNC_GENERATOR
from click import password_option
from config import conexion
from sqlalchemy import Column,types

class Participante(conexion.Model):
    #ahora esta clase tendra un comportamiento en forma de una tabla en la bd
    #(todos los atributos que declare sea propios de la bd se creara como columnas)
    
    #conexion.Column() = Column()
    
    #Si no se pone el parametro 'name' este sera el mismo que el nombre del atributo
    id = Column(type_= types.Integer, autoincrement= True,primary_key=True)
    nombre = Column(type_=types.String(50),nullable=False)
    apellido = Column(type_=types.String(50),nullable=False)
    telefono =  Column(type_=types.String(10))
    password = Column(type_=types.Text)
    zona = Column(type_=types.Enum('SUPER_VIP','VIP','GENERAL'),default='GENERAL',nullable=False)
    # comentario = Column(type_=types.Text)
    # correo = Column(type_=types.String(45),nullabe=False)

# se modificara el nombre de la tabla actual a nivel de base de datos para que no se llame igual que la clase(en singular y con la primera mayuscula)
#  __tablename__ = 'participantes'