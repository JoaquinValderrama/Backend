curso = 'Backend'
print (curso)
dia = 16
#cuando dos valores son textos hace una concatenacion
print ("El curso es: " + curso)
print ("el curso es",curso)

#si queremos usar un texto y un numero no se puede usar la sumatoria ya que al ser de tipos de datos diferentes python no sabra si concatenar o una suma
# print ("el curso es "+curso+" y el dia es " +dia) ❌

print ("El curso es " + curso + " y el dia es",dia)

print ("El curso es {} y el dia es {}".format(curso, dia))

print ("El curso es {1} y el dia es {0}".format(curso, dia))
