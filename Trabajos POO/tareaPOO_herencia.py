# Ejercicio Herencia POO

class vehiculo:
    def _init_(self):
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

class terrestre(vehiculo):
    def _init_(self):
        print('= CAPTURA DE DATOS CLASE TERRESTRE =')
        super()._init_()
        self.ruedas = int(input('Digite la cantidad de ruedas: '))

    def imprimirHer(self):
        super().imprimir()
        print('Cantidad de ruedas:' + str(self.ruedas))


class acuatico(vehiculo):
    def _init_(self):
        print('= CAPTURA DE DATOS CLASE ACUÁTICA =')
        super()._init_()
        self.flotabilidad = input('Digite la flotabilidad de la embarcación: ')
        self.helice = input('Digite la cantidad de hélices de la embarcación: ')

    def imprimirHer(self):
        super().imprimir()
        print('Flotabilidad:' + self.flotabilidad)
        print('Cantidad de hélices:' + self.helice)

#===================================
# instancia de objetos en clases heredadas...
# objetos terrestres
print('= Objeto bicicleta =')
print('======================')
obj_bicicleta = terrestre()

print('= Objeto patineta =')
print('======================')
obj_patineta = terrestre()

print('= Objeto automóvil =')
print('======================')
obj_automovil = terrestre()

print('= Objeto motocicleta =')
print('======================')
obj_motocicleta = terrestre()

# objetos acuáticos
print('= Objeto Yate =')
print('======================')
obj_yate = acuatico()

print('= Objeto trasatlántico =')
print('======================')
obj_trasatlantico = acuatico()

#===================================
#imprimir objs heredados
# Envío de mensajes
print('= Objeto bicicleta =')
print('======================')
obj_bicicleta.imprimirHer()

print('= Objeto patineta =')
print('======================')
obj_patineta.imprimirHer()

print('= Objeto automóvil =')
print('======================')
obj_automovil.imprimirHer()

print('= Objeto motocicleta =')
print('======================')
obj_motocicleta.imprimirHer()

print('= Objeto Yate =')
print('======================')
obj_yate.imprimirHer()

print('= Objeto trasatlántico =')
print('======================')
obj_trasatlantico.imprimirHer()