# Ejercicio 1 - Herencia múltiple

#clase super
#===============================================
class vehiculo:
    def __init__(self):
        self.marca = input('Digite la marca: ')
        self.color = input('Digite el color: ')
        self.velocidad = input('Digite velocidad: ')
        self.canPas = input('Digite cantidad máxima pasajeros: ')

    def imprimir(self):
        print('Marca: ' + self.marca)
        print('Color: ' + self.color)
        print('Velocidad: ' + self.velocidad)
        print('Cant. Pasajeros: ' + self.canPas)

#subclase terrestre
#===============================================

class terrestre(vehiculo):
    def __init__(self):
        super().__init__()
        self.canRuedas = input ('Digite la cantidad de ruedas: ')

    def imprimirHer(self):
        super().imprimir()
        print('Cantidad ruedas: ' + self.canRuedas)

#subclase acuatico
#===============================================

class acuatico(vehiculo):
    def __init__(self):
        super().__init__()
        self.canHel = int(input('Digite la cantidad de hélices: '))
        self.flotabilidad = int(input('Digite índice de flotabilidad: '))

    def imprimirHer(self):
        super().imprimir()
        print('Cantidad hélices: ' + str(self.canHel))
        print('Flotabilidad: ' + str(self.flotabilidad))

#===============================================

class bici(terrestre):
    def __init__(self):
        super().__init__()
        self.canCad = int(input('Digite cantidad de cadenas: '))
        self.canPed = int(input('Digite cantidad de pedales: '))

    def imprimirHerBici(self):
        super().imprimirHer()
        print('Cadenas: ' + str(self.canCad))
        print('Pedales: ' + str(self.canPed))

class patineta(terrestre):
    def __init__(self):
        super().__init__()
        self.canEjes = int(input('Digite cantidad de ejes: '))
        self.capLij = int(input('Digite cantidad capas de lija: '))

    def imprimirHerPat(self):
        super().imprimirHer()
        print('Ejes: ' + str(self.canEjes))
        print('Capas: ' + str(self.capLij))

class moto(terrestre):
    def __init__(self):
        super().__init__()
        self.canFarDel = int(input('Digite cantidad de faros delanteros: '))
        self.tamSill = int(input('Digite tamaño de sillín en cm: '))

    def imprimirHerMoto(self):
        super().imprimirHer()
        print('Faros delanteros: ' + str(self.canFarDel))
        print('Tamaño sillín: ' + str(self.tamSill) + 'cm.')

class carro(terrestre):
    def __init__(self):
        super().__init__()
        self.canPuertas = int(input('Digite cantidad de puertas: '))
        self.CanPara = int(input('Digite cantidad de parachoques: '))

    def imprimirHerCarro(self):
        super().imprimirHer()
        print('Puertas: ' + str(self.canPuertas))
        print('Parachoques: ' + str(self.CanPara))

#===============================================

class yate(acuatico):
    def __init__(self):
        super().__init__()
        self.tamPopa = int(input('Digite tamaño popa en cm: '))

    def imprimirHerYate(self):
        super().imprimirHer()
        print('Popa: ' + str(self.tamPopa) + 'cm.')

class trasatlantico(acuatico):
    def __init__(self):
        super().__init__()
        self.canSal = int(input('Digite cantidad de botes salvavidas: '))

    def imprimirHerTras(self):
        super().imprimirHer()
        print('Botes salvavidas: ' + str(self.canSal))

#===============================================
# Generar instancias...
print('=================')
print('OBJETO BICI')
obj_bici = bici()

print('=================')
print('OBJETO PATINETA')
obj_pat = patineta()

print('=================')
print('OBJETO CARRO')
obj_carro = carro()

print('=================')
print('OBJETO MOTO')
obj_moto = moto()

print('=================')
print('OBJETO YATE')
obj_yate = yate()

print('=================')
print('OBJETO TRASATLÁNTICO')
obj_trasatlantico = trasatlantico()

#===============================================
# Envío de mensajes....
print('=================')
print('IMPRESIONES BICI')
obj_bici.imprimirHerBici()

print('=================')
print('IMPRESIONES PATINETA')
obj_pat.imprimirHerPat()

print('=================')
print('IMPRESIONES CARRO')
obj_carro.imprimirHerCarro()

print('=================')
print('IMPRESIONES MOTO')
obj_moto.imprimirHerMoto()

print('=================')
print('IMPRESIONES YATE')
obj_yate.imprimirHerYate()

print('=================')
print('IMPRESIONES TRASATLANTICO')
obj_trasatlantico.imprimirHerTras()

# fin del programa... ========














