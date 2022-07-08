# While
numero = 10 

# Es un bucle que se realiza de manera automatica hasta que la condiion o condiciones dejan de ser verdaderass

while numero >0:
    print("Numero postivo")
    print(numero)
    numero -=1

# Solicitar 5 digitos para la loteria pero estos no pueden ser mayor que 100 ni numeros negativos

contador = 0

while contador <5:
    numero = int(input ("Ingresa el numero de la loteria: "))
    if not(numero>100 or numero <0):
        contador +=1
        continue
    print("Numero ingresador es invalido, vuelve a intentar")