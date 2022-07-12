#Pilares
#1. Abstraccion
#2. Encapsulamiento
#3. Herencia
#4. Polimorfismo

class Vehiculo:
    def __init__ (self, marca,modelo):
        self.marca = marca
        self.modelo = modelo
        #Si queremos indicar que un atributo de la clase va a ser privado, no va a poder ser accedido desde fuera de la clase, tendremos que colocar doble guion bajo adelante del atributo
        self.__serie = marca+modelo

    def mostrarSerie(self):
        print (self.__serie)
        
auto = Vehiculo('Kia','Picanto')
camion = Vehiculo('Volvo','F30')

print(auto.marca)
auto.mostrarSerie()