
class terrestre(vehiculo):
    def __init__(self):
        print('= CAPTURA DE DATOS CLASE TERRESTRE =')
        super().__init__()
        self.ruedas = int(input('Digite la cantidad de ruedas: '))

    def imprimirHer(self):
        super().imprimir()
        print('Cantidad de ruedas:' + str(self.ruedas))


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
