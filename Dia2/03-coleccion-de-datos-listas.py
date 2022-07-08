# LISTAS

from ast import alias


alumnos = ['Javier', 'Alejandro', 'Alexandra','Jenny','Eduardo']

otra = [1,10,'hola',True,5.2,None]

# Son colleciones de datos ordenandas (posiciones) , las posiciones siempre empiezan en 0

print(alumnos[0])

# Si queremos acceder a una posicion que no existe en nuestra lista esta nos emitira un error, a diferencia de JS que me muestra 'Undefined'

variados = [10,[1,2,3]]
print (variados[1][1])

# Cuando usamos 2 puntos ":" al momento de definir la posicion de una lista entonces le estaremos indicando que queremos una sublista de esa lista siendo el primer valor la posicion inicial y el segundo valor hasta que posicion tiene que llegar
print(alumnos[1:3])

#destructuracion de una lista(extraer los elementos internos de lista)
print(alumnos[:])

#Cuando usamos posiciones negativas en una lista entonces la invierte, es decir, ahora la posicion -1 sera el ultimo elemento de la lista y asi sucesivamente
print(alumnos[-1])
print(alumnos[-2])

for alumno in alumnos:
    if alumno == 'Eduardo':
        print('Si esta')
        break

#Sentido de pertenencia => podemos consultar si un valor determinado existe en la lista

print ('Eduardo' in alumnos)
print (10 in alumnos)

#Lista son colecciones de datos EDITABLES
alumnos[0] = 'Martin'
print(alumnos)

#append => Sirve para agregar un valor a la lista final
alumnos.append('Ivanov')
print(alumnos)

#extend => combinar las dos listas en una sola
alumnos.extend(['Luis','Lily','Jordan'])
print(alumnos)

#otra forma de combinar es 'concatenando' las listas
alumnos += ['Yordy','Javier','Ruben']
print(alumnos)

#Eliminar elemento de una lista
#Eliminando por el metodo DEL
del alumnos[1]
print (alumnos)

del alumnos[1:3]
print(alumnos)

#Eliminando por el metodo POP
#este metodo, elimina el contenido de esa posicion, pero se puede almacenar el contenido en otra variable

alumno_eliminado = alumnos.pop(2)
print(alumnos)
print(alumno_eliminado)

#Eliminando por el metodo CLEAR
#Vaciara toda la lista, dejandolo en blanco

alumnos.clear()
print(alumnos)