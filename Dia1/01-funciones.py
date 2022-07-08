#Una funcion es un bloque de codgio que no se ejecutara automaticamente hasta que sea llamado 

from ast import operator
from traceback import print_tb


def saludar():
    print('Buenas Tardes :D')

saludar()

def saludarConNombre(nombre):
    print(nombre)

saludarConNombre('Jose')

def saludoCordial (nombre):
    '''Funcion que recibe un nombre y te saluda cordialmente preguntadndote como te va'''
    print("Hola, {}, Como te va?".format(nombre))

saludoCordial ('Eduardo')

def calcularIGV(valor):
    '''Funcion que recibe el valor y te devuelve el valor incluido su IGV'''
    valorIncluidoIGV = valor * 1.18
    return valorIncluidoIGV


precio = 100

precioConIGV = calcularIGV(100)
print(precioConIGV)


def calcularSalarioMinimo (profesion,experiencia):
    salarioMinimo = 1050
    if profesion =='Desarrollador':
        if experiencia == 'Basica':
            salarioMinimo = 3000
        elif experiencia == 'Media':
            salarioMinimo = 4000
        elif experiencia == 'Avanzada':
            salarioMinimo = 7000
    elif profesion == 'Marketing':
        if experiencia == 'Basica':
            salarioMinimo = 2500
        elif experiencia == 'Media':
            salarioMinimo = 4150
        elif experiencia == 'Avanzada':
            salarioMinimo = 6820
    
    return salarioMinimo

profesion,experiencia = 'Desarrollador' , 'Media'
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

profesion,experiencia = 'Desarrollador' , 'Basica'
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

profesion,experiencia = 'Marketing' , 'Media'
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)


electrodomesticos = []

def registrarElectrodomesticos(nombre,precio,almacen='Las Malvinas'):
    electrodomesticos.append({'Nombre':nombre ,'precio':precio,'almacen' : almacen})

registrarElectrodomesticos('Licuadora 12v', 115.00)
registrarElectrodomesticos('Freidora de aire', 100,'Cercado')
registrarElectrodomesticos('Secador de cabello', 140)

print(electrodomesticos)

def contadorElectrodomesticosPorAlmacen():
    '''Cuenta cuantos electrodomesticos hay en cada almacen'''
    #usar un for para iterar los electrodomesticos

    malvinas = 0
    cercado = 0
    otro = 0

    for electrodomestico in electrodomesticos:
        if electrodomestico['almacen'] == 'Las Malvinas':
            malvinas+=1
        elif electrodomestico['almacen'] == 'Cercado':
            cercado +=1
        else:
            otro+=1
    #luego de iterar los electrodomesticos, indicar cuantos hay
    
    print('En las Malvinas hay {}, en cercado hay {}, y en otros hay {} electrodomesticos'.format(malvinas,cercado,otro))

contadorElectrodomesticosPorAlmacen()

#Si en una funcion queremos revibir un numero indeterminado de valores
#args > arguments

def recibirAlumnos(clase, *alumnos):
    #cuando un parametro tiene el * ak comienzo significa que ese parametro recibira n valores y lo convertira a una tupla
    print(alumnos)

    #para convertir de una tupla a lista
    alumnos_lista = list(alumnos)
    print(type(alumnos_lista))
