numeros = [10,20,30,40,50,60]

for numero in numeros: 

    print(numero)

frase_motivadora='Al que madruga,encuentra todo cerrado'
contador=0

for caracter in frase_motivadora:
    # print(caracter)
    if caracter == 'n':
        contador = contador +1
print('Hay {} veces repetida las letra N' .format(contador) )

for valor in range(10):
    # empiza desde el numero 0 hasta <10 e incrementa de 1 en 1
    print (valor)

for valor in range(3,7):
    #el primer parametro sera el numero en el cual va a empezar y el segundo hasta que numero debe llegar incrementandose de 1 en 1
    print(valor)

for valor in range(4,7,2):
    # el primer parametro sera el numero en el cual va a empezar y el segundo hasta que numero debe llegar, y el tercero sera de cuanto en cuanto debe alterar el contador
    print (valor)


# ejercicio

numeros = [10,30,12,17,24,67]

#Cuantos de esos digitos son numeros pares y cuantos son multiplos de 3

contador_pares= 0
contador_multiplo3 = 0
for numero in numeros:
    if numero % 2 ==0:
        contador_pares+=1
    
    if numero %3 == 0:
        contador_multiplo3 +=1

print ("Hay {} numeros pares y hay {} multiplos de 3".format(contador_pares,contador_multiplo3))

# supongamos que los 10000 son los usuarios de un sistema y queremos encontrar al usuario con un determinado nombre (y ese usuarrio es el numero 600)

for valor in range(0,10000):
    print (valor)
    if(valor==600):
        print ("El usuario fue encontrado")
        # break => sirve para finalizar de manera prematura un bucle(for,while)
        break

for valor in range (0,20):
    if valor ==5:
        print ("el usuario fue encontrado")
        # continue => sirve para que el codigo que viene no se ejecute
        continue
    print (valor)

for valor in range (0,20):
    # TODO :implementar la logica
    # pass => no hara nada pero evitara que nos lance error python 
    pass