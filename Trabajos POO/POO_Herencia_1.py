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

# Ejercicio Herencia POO
# Archivo 2

class terrestre(vehiculo):
    def __init__(self):
        print('= CLASE TERRESTRE =')
        super().__init__()
        self.ruedas = int(input('Digite la cantidad de ruedas: '))

    def imprimirHer(self):
        super().imprimir()
        print('Cantidad de ruedas:' + str(self.ruedas))

class bicicleta(terrestre):
    def __init__(self):
        super().__init__()
        terrestre().__init__()
        print('= CAPTURA DE DATOS BICICLETA =')
        self.canCad = int(input('Digite cantidad de cadenas: '))
        self.canPed = int(input('Digite cantidad de pedales: '))

    def imprimirHerBici(self):
        super().imprimir()
        terrestre().imprimirHer()
        print('Cadenas: ' + str(self.canCad))
        print('Pedales: ' + str(self.canPed))


class patineta(terrestre):
    def __init__(self):
        super().__init__()
        terrestre().__init__()
        print('= CAPTURA DE DATOS PATINETA =')
        self.canEjes = int(input('Digite cantidad de ejes: '))
        self.capLij = int(input('Digite cantidad capas de lija: '))

    def imprimirHerPat(self):
        super().imprimir()
        terrestre().imprimirHer()
        print('Ejes: ' + str(self.canEjes))
        print('Capas: ' + str(self.capLij))


class automovil(terrestre):
    def __init__(self):
        super().__init__()
        terrestre().__init__()
        print('= CAPTURA DE DATOS AUTOMÓVIL =')
        self.canPuertas = int(input('Digite cantidad de puertas: '))
        self.CanPar = int(input('Digite cantidad de parachoques: '))

    def imprimirHerAuto(self):
        super().imprimir()
        terrestre().imprimirHer()
        print('Puertas: ' + str(self.canPuertas))
        print('Parachoques: ' + str(self.CanPar))


class motocicleta(terrestre):
    def __init__(self):
        super().__init__()
        terrestre().__init__()
        print('= CAPTURA DE DATOS MOTOCICLETA =')
        self.canFarDel = int(input('Digite cantidad de faros delanteros: '))
        self.tamSill = input('Digite tamaño de sillín en cm: ')

    def imprimirHerMot(self):
        super().imprimir()
        terrestre().imprimirHer()
        print('Faros delanteros: ' + str(self.canFarDel))
        print('Sillín: ' + self.tamSill + 'cm.')

# Ejercicio Herencia POO
# Archivo 3

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

class yate(acuatico):
    def __init__(self):
        super().__init__()
        acuatico().__init__()
        print('= CAPTURA DE DATOS YATE =')
        self.tamTim = input('Digite tamaño timón en cm: ')

    def imprimirHerYate(self):
        super().imprimir()
        acuatico().imprimirHer()
        print('Timón: ' + self.tamTim + 'cm.')

class trasatlantico(acuatico):
    def __init__(self):
        super().__init__()
        acuatico().__init__()
        print('= CAPTURA DE DATOS TRASATLÁNTICO =')
        self.botSal = int(input('Digite cantidad de botes salvavidas: '))

    def imprimirHerTras(self):
        super().imprimir()
        acuatico().imprimirHer()
        print('Botes salvavidas: ' + str(self.botSal))

# Ejercicio Herencia POO
# Archivo 4

#===================================
# instancia de objetos en clases heredadas...
# objetos terrestres
print('= Objeto bicicleta =')
print('======================')
obj_bicicleta = bicicleta()

print('= Objeto patineta =')
print('======================')
obj_patineta = patineta()

print('= Objeto automóvil =')
print('======================')
obj_automovil = automovil()

print('= Objeto motocicleta =')
print('======================')
obj_motocicleta = motocicleta()

# objetos acuáticos
print('= Objeto Yate =')
print('======================')
obj_yate = yate()

print('= Objeto trasatlántico =')
print('======================')
obj_trasatlantico = trasatlantico()

#===================================
#imprimir objs heredados
# Envío de mensajes
print('= Objeto bicicleta =')
print('======================')
obj_bicicleta.imprimirHerBici()

print('= Objeto patineta =')
print('======================')
obj_patineta.imprimirHerPat()

print('= Objeto automóvil =')
print('======================')
obj_automovil.imprimirHerAuto()

print('= Objeto motocicleta =')
print('======================')
obj_motocicleta.imprimirHerMot()

print('= Objeto Yate =')
print('======================')
obj_yate.imprimirHerYate()

print('= Objeto trasatlántico =')
print('======================')
obj_trasatlantico.imprimirHerTras()
