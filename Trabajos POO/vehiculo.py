# Ejercicio Herencia POO
# Archivo 1

class vehiculo:
    def __init__(self):
        self.nombre = input('Digite nombre de vehículo: ')
        self.marca = input('Digite la marca del vehículo: ')
        self.velocidad = int(input('Digite la velocidad del vehículo: '))
        self.color = input('Digite el color del vehículo: ')
        self.canPas = input('Digite la cantidad máxima de pasajeros: ')

    def imprimir(self):
        print('Nombre vehículo: ' + self.nombre)
        print('Marca: ' + self.marca)
        print('Velocidad: ' + str(self.velocidad))
        print('Color: ' + self.color)
        print('Cantidad pasajeros: ' + self.canPas)







