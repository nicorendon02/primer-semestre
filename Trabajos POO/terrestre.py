# Ejercicio Herencia POO
# Archivo 2

from vehiculo import vehiculo

class terrestre(vehiculo):
    def __init__(self):
        print('= CAPTURA DE DATOS CLASE TERRESTRE =')
        super().__init__()
        self.ruedas = int(input('Digite la cantidad de ruedas: '))

    def imprimirHer(self):
        super().imprimir()
        print('Cantidad de ruedas:' + str(self.ruedas))

class bicicleta(terrestre):
    def __init__(self):
        terrestre.__init__()
        print('= CAPTURA DE DATOS BICICLETA =')
        self.canCad = int(input('Digite cantidad de cadenas: '))
        self.canPed = int(input('Digite cantidad de pedales: '))

    def imprimirHerBici(self):
        terrestre.imprimirHer()
        print('Cadenas: ' + str(self.canCad))
        print('Pedales: ' + str(self.canPed))


class patineta(terrestre):
    def __init__(self):
        terrestre.__init__()
        print('= CAPTURA DE DATOS PATINETA =')
        self.canEjes = int(input('Digite cantidad de ejes: '))
        self.capLij = int(input('Digite cantidad capas de lija: '))

    def imprimirHerPat(self):
        terrestre.imprimirHer()
        print('Ejes: ' + str(self.canEjes))
        print('Capas: ' + str(self.capLij))


class automovil(terrestre):
    def __init__(self):
        terrestre.__init__()
        print('= CAPTURA DE DATOS AUTOMÓVIL =')
        self.canPuertas = int(input('Digite cantidad de puertas: '))
        self.CanPar = int(input('Digite cantidad de parachoques: '))

    def imprimirHerAuto(self):
        terrestre.imprimirHer()
        print('Puertas: ' + str(self.canPuertas))
        print('Parachoques: ' + str(self.CanPar))


class motocicleta(terrestre):
    def __init__(self):
        terrestre.__init__()
        print('= CAPTURA DE DATOS MOTOCICLETA =')
        self.canFarDel = int(input('Digite cantidad de faros delanteros: '))
        self.tamSill = input('Digite tamaño de sillín en cm: '))

    def imprimirHerMot(self):
        terrestre.imprimirHer()
        print('Faros delanteros: ' + str(self.canFarDel))
        print('Sillín: ' + self.tamSill + 'cm.')






