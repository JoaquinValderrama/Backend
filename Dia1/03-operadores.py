#Operadores Aritmeticos 

from cgi import print_form


edad_juan = 40
edad_maria = 34

#Suma 
print(edad_juan+edad_maria)

#resta
print(edad_juan-edad_maria)

#multiplicacion
print(edad_juan*edad_maria)

#division 
print(edad_juan/edad_maria)

#modulo
print(edad_juan%edad_maria)

#cociente 
print(edad_juan//edad_maria)

#---------------------------------------------

#Operadores de Comparacion

edad_Luis = 15
edad_martha = 30

#> Mayor que 
print(edad_Luis > edad_martha)

# < Menor que 
print(edad_Luis < edad_martha)

# == Igual que 
print(edad_Luis == edad_martha)

# != Diferente de
print(edad_Luis != edad_martha)

# >= Mayor o igual que 
print(edad_Luis >= edad_martha)

# <= Menor o igual que
print(edad_Luis <= edad_martha)

#Operadores logicos 

edad_luis = 25
edad_martha = 30

# and Y > basta con que una de las condiciones sean F para que todo sea F
print (edad_luis>18 and edad edad_luis>edad_martha)

#or O > basta con que una sea V para que todo sea V
print(edad_luis >18 or edad_luis>edad_martha)

#not No > invierte el resultado
print (not edad_luis >50) 

#------------------------------------------------------------------------------

#Operadores de Asignacion

# = Asignacion
edad = 50

# += incremento
edad+=1 #edad++

# -= decremento
edad-=1

# *= multiplicador
edad*=1

# /= division
edad /=2

