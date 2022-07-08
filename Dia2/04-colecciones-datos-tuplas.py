#TUPLAS 
#Colecciones de datos pero no editables

profesores = ('Eduardo' , 'Osmar')

# print(profesores[0])

data = (1,True,'Junio',14.5,[1,2,3,4])

print(data[1:4])

#Se puede eliminar toda la variable pero no se puede eliminar parte del contendio de la Tupla
del data

notas = (10,15,15,18,10,5,7,14)

#Count => Sirve para contar las veces que se repite cierto valor

print(notas.count(10))
print(notas.count(20))
print(notas.count('Onomatopeya'))

#Index=> si existe ese valor en la tupla me retornara la posicion en la que se encuentra, sino existe me emitira un error

print(notas.index(15))
