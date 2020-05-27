# Ejercicio Herencia POO
# Archivo 3

from vehiculo import vehiculo

class acuatico(vehiculo):
    def __init__(self):
        print('= CAPTURA DE DATOS CLASE ACUÁTICA =')
        super().__init__()
        self.flotabilidad = input('Digite la flotabilidad de la embarcación: ')
        self.helice = input('Digite la cantidad de hélices de la embarcación: ')

    def imprimirHer(self):
        super().imprimir()
        print('Flotabilidad:' + self.flotabilidad)
        print('Cantidad de hélices:' + self.helice)



