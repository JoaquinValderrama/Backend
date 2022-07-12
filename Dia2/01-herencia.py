#Herencia
#En python el polimorfismo es la definicion del mismo metodo en diferentes clases pero con un comportamiento diferente
class Usuario: 
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def info(self):
        return {
            'nombre' : self.nombre,
            'apellido' : self.apellido
        }
class Alumno(Usuario):
    def __init__(self,nombre,apellido,anio,seccion):
        self.anio = anio
        self.seccion = seccion

        #Super => Metodo que sirve para utlizar los metodos y atributos de la clase o clases que estmaos heredando
        super().__init__(nombre,apellido)

    def info(self):
        infoUsuario = super().info()
        data = {
            'anio': self.anio,
            'seccion' : self.seccion
        }

        return {**data,**infoUsuario}

alumnoEduardo = Alumno('Eduardo' , 'de Rivero ','Sexto','A')
UsuarioRaul = Usuario('Raul', 'Mendoza')

informacion= alumnoEduardo.info()
print(informacion)
print(UsuarioRaul.info())
