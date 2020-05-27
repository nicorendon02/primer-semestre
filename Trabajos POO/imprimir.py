# Ejercicio Herencia POO
# Archivo 4

from vehiculo import vehiculo
from terrestre import terrestre
from acuatico import acuatico

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