# Programacion Orientada a objetos (POO)
# Una clase sera como una plantilla que va a ser para empezar a definir los atributos y metodos de ese determinado objeto

class Persona:
    #atributos
    estatura = 100
    colorOjos = 'Cafe'
    colorCabello = 'Negro'
    fechaNacimiento = '2000-01-01'

    def saludar(self):
        print('Hola buenos dias')


#Cuando nosotros creamos una copia de una plantilla se le dice 'instanciar' o crear una referencia de una clase

personaEduardo = Persona()
print(personaEduardo.colorCabello)

personaMaria = Persona()
personaMaria.colorOjos = 'Verde'
print(personaMaria.colorOjos)

#Constructor 
#Self => es la referencia de la instancia que hemos creado en una relacion a su posicion de memoria, con esto no modificaremos a las demas instancias cuando cambiemos algun atributo o comportamiento de una instancia 
#Self debe ser declarado como primer parametro de TODO metodo de una clase Obligatoriamente

class Mascota:
    def __init__(self, nombre, especie,raza,sexo):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.sexo = sexo

    def info(self):
        print(self.nombre)
        print(self.especie)
        print(self.raza)
        print(self.sexo)

mascotaPerro = Mascota('Moroch', 'Perro', 'Salchicha', 'Femeninino')
mascotaGato = Mascota('Michifus', 'Gato' , 'Siames', 'Masculino')

print(mascotaGato.nombre)
print(mascotaPerro.nombre)
