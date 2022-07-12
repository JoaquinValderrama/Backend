from camelcase import CamelCase

camelcase = CamelCase()

parrafo = 'Hola amigos veamos si esta libreria funciona'

resultado = camelcase.hump(parrafo)
print(resultado)