#Conjunto (set)
#Coleccion de datos desordenada (no lleva orden en los indices) es editable

meses = {'Enero','Febrero','Marzo','Abril'}
print(meses)
print('Enero' in meses)
print('Agosot' in meses)

#Se ppuede agregar nuevos elementos

meses.add('Mayo')
meses.add('Junio')

print(meses)

# Se puede agregar un conjutno de nuevos elementos

meses.update(['Julio','Agosot', 'Septiembre','Junio','Julio'])
print(meses)

#El metodo Discard o remove elimina todos los valores que coincidan con ese elemento

meses.discard('Junio')
print(meses)

meses.remove('Julio')
print(meses)